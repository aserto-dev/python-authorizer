# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aserto/authorizer/v2/api/identity_context.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/aserto/authorizer/v2/api/identity_context.proto\x12\x18\x61serto.authorizer.v2.api\"i\n\x0fIdentityContext\x12\x1a\n\x08identity\x18\x01 \x01(\tR\x08identity\x12:\n\x04type\x18\x02 \x01(\x0e\x32&.aserto.authorizer.v2.api.IdentityTypeR\x04type*\x89\x01\n\x0cIdentityType\x12\x19\n\x15IDENTITY_TYPE_UNKNOWN\x10\x00\x12\x16\n\x12IDENTITY_TYPE_NONE\x10\x01\x12\x15\n\x11IDENTITY_TYPE_SUB\x10\x02\x12\x15\n\x11IDENTITY_TYPE_JWT\x10\x03\x12\x18\n\x14IDENTITY_TYPE_MANUAL\x10\x04\x42\xfa\x01\n\x1c\x63om.aserto.authorizer.v2.apiB\x14IdentityContextProtoP\x01Z@github.com/aserto-dev/go-authorizer/aserto/authorizer/v2/api;api\xa2\x02\x04\x41\x41VA\xaa\x02\x18\x41serto.Authorizer.V2.Api\xca\x02\x18\x41serto\\Authorizer\\V2\\Api\xe2\x02$Aserto\\Authorizer\\V2\\Api\\GPBMetadata\xea\x02\x1b\x41serto::Authorizer::V2::Apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aserto.authorizer.v2.api.identity_context_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.aserto.authorizer.v2.apiB\024IdentityContextProtoP\001Z@github.com/aserto-dev/go-authorizer/aserto/authorizer/v2/api;api\242\002\004AAVA\252\002\030Aserto.Authorizer.V2.Api\312\002\030Aserto\\Authorizer\\V2\\Api\342\002$Aserto\\Authorizer\\V2\\Api\\GPBMetadata\352\002\033Aserto::Authorizer::V2::Api'
  _globals['_IDENTITYTYPE']._serialized_start=185
  _globals['_IDENTITYTYPE']._serialized_end=322
  _globals['_IDENTITYCONTEXT']._serialized_start=77
  _globals['_IDENTITYCONTEXT']._serialized_end=182
# @@protoc_insertion_point(module_scope)
