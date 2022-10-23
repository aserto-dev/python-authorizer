//go:build mage
// +build mage

package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"path"
	"path/filepath"
	"strings"

	"github.com/aserto-dev/mage-loot/buf"
	"github.com/aserto-dev/mage-loot/common"
	"github.com/aserto-dev/mage-loot/deps"
	"github.com/aserto-dev/mage-loot/fsutil"
	"github.com/aserto-dev/mage-loot/mage"
	"github.com/magefile/mage/sh"
)

const (
	googleApiBufImage   = "buf.build/googleapis/googleapis"
	grpcGatewayBufImage = "buf.build/grpc-ecosystem/grpc-gateway"
	asertoBufImage      = "buf.build/aserto-dev/authorizer"
)

func init() {
	os.Setenv("GO_VERSION", "1.17")
	os.Setenv("GOPRIVATE", "github.com/aserto-dev")
}

func All() error {
	Deps()
	err := Clean()
	if err != nil {
		return err
	}
	err = Generate()
	if err != nil {
		return err
	}
	return Build()

}

// install required dependencies.
func Deps() {
	deps.GetAllDeps()
}

func Generate() error {
	bufImage := asertoBufImage

	tag, err := buf.GetLatestTag(asertoBufImage)
	if err != nil {
		fmt.Println("Could not retrieve tags, using latest")
	} else {
		bufImage = fmt.Sprintf("%s:%s", bufImage, tag.Name)
	}

	return gen(bufImage, bufImage)
}

// Generates from a dev build.
func GenerateDev() error {
	err := BuildDev()
	if err != nil {
		return err
	}

	bufImage := filepath.Join(getProtoRepo(), "bin", "authorizer.bin#format=bin")
	fileSources := filepath.Join(getProtoRepo(), "proto#format=dir")

	return gen(bufImage, fileSources)
}

// Builds the aserto proto image
func BuildDev() error {
	return mage.RunDirs(path.Join(getProtoRepo(), "magefiles"), getProtoRepo(), mage.AddArg("build"))
}

func getProtoRepo() string {
	protoRepo := os.Getenv("PROTO_REPO")
	if protoRepo == "" {
		protoRepo = "../pb-authorizer"
	}
	return protoRepo
}

//Generate the code

func gen(bufImage, fileSources string) error {
	files, err := getClientFiles(fileSources)
	if err != nil {
		return err
	}

	for bufImage, clientFiles := range files {
		err = buf.Run(
			buf.AddArg("generate"),
			buf.AddArg("--template"),
			buf.AddArg(filepath.Join("buf", "buf.gen.yaml")),
			buf.AddArg(bufImage),
			buf.AddPaths(clientFiles),
		)
		if err != nil {
			return err
		}
	}

	return genInitFiles()
}

func getClientFiles(fileSources string) (map[string][]string, error) {
	var clientFiles = make(map[string][]string)

	bufExportDir, err := ioutil.TempDir("", "bufimage")
	if err != nil {
		return clientFiles, err
	}
	bufExportDir = filepath.Join(bufExportDir, "")

	defer os.RemoveAll(bufExportDir)
	err = buf.Run(
		buf.AddArg("export"),
		buf.AddArg(fileSources),
		buf.AddArg("-o"),
		buf.AddArg(bufExportDir),
	)
	if err != nil {
		return clientFiles, err
	}

	authorizerPatterns := []string{
		filepath.Join(bufExportDir, "aserto", "authorizer", "**", "*.proto"),
	}

	googleApiPatterns := []string{
		filepath.Join(bufExportDir, "google", "api", "**", "*.proto"),
	}

	grpcGatewayPatterns := []string{
		filepath.Join(bufExportDir, "protoc-gen-openapiv2", "options", "**", "*.proto"),
	}

	for _, pattern := range authorizerPatterns {
		files, err := fsutil.Glob(pattern, "")
		if err != nil {
			return clientFiles, err
		}
		for _, file := range files {
			clientFiles[asertoBufImage] = append(clientFiles[asertoBufImage], strings.TrimPrefix(file, bufExportDir+string(filepath.Separator)))
		}
	}

	for _, pattern := range googleApiPatterns {
		files, err := fsutil.Glob(pattern, "")
		if err != nil {
			return clientFiles, err
		}
		for _, file := range files {
			clientFiles[googleApiBufImage] = append(clientFiles[googleApiBufImage], strings.TrimPrefix(file, bufExportDir+string(filepath.Separator)))
		}
	}

	for _, pattern := range grpcGatewayPatterns {
		files, err := fsutil.Glob(pattern, "")
		if err != nil {
			return clientFiles, err
		}
		for _, file := range files {
			clientFiles[grpcGatewayBufImage] = append(clientFiles[grpcGatewayBufImage], strings.TrimPrefix(file, bufExportDir+string(filepath.Separator)))
		}
	}

	return clientFiles, nil
}

func genInitFiles() error {
	return sh.RunV("python3", "./init_gen.py", "src/aserto")
}

func Bump(next string) error {
	nextVersion, err := common.NextVersion(next)
	if err != nil {
		return err
	}
	fmt.Println("Bumping version to", nextVersion)

	input, err := ioutil.ReadFile("pyproject.toml")
	if err != nil {
		return err
	}

	lines := strings.Split(string(input), "\n")

	for i, line := range lines {
		if strings.Contains(line, "version = \"") {
			lines[i] = "version = \"" + nextVersion + "\""
		}
	}
	output := strings.Join(lines, "\n")

	return ioutil.WriteFile("pyproject.toml", []byte(output), 0644)
}

func Build() error {
	err := os.RemoveAll("dist")
	if err != nil {
		return err
	}

	return sh.RunV("poetry", "build")
}

func Push() error {
	return sh.RunV("poetry", "publish")
}

func Release() error {
	err := Build()
	if err != nil {
		return err
	}

	return Push()
}

// Clean generated files
func Clean() error {
	return os.RemoveAll("src")
}

func deleteDirContentWithException(dir, exceptionFileName string) error {
	entries, err := os.ReadDir(dir)
	if err != nil {
		return err
	}

	for _, entry := range entries {
		if entry.IsDir() {
			err := deleteDirContentWithException(filepath.Join(dir, entry.Name()), exceptionFileName)
			if err != nil {
				return err
			}
			continue
		}
		if entry.Name() == exceptionFileName {
			continue
		}
		err = os.RemoveAll(filepath.Join(dir, entry.Name()))
		if err != nil {
			return err
		}

	}

	return nil
}
