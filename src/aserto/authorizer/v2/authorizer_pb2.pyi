"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import aserto.authorizer.v2.api.identity_context_pb2
import aserto.authorizer.v2.api.module_pb2
import aserto.authorizer.v2.api.policy_context_pb2
import aserto.authorizer.v2.api.policy_instance_pb2
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _PathSeparator:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PathSeparatorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PathSeparator.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PATH_SEPARATOR_UNKNOWN: _PathSeparator.ValueType  # 0
    """Value not set."""
    PATH_SEPARATOR_DOT: _PathSeparator.ValueType  # 1
    """Dot "." path separator"""
    PATH_SEPARATOR_SLASH: _PathSeparator.ValueType  # 2
    """Slash "/" path separtor"""

class PathSeparator(_PathSeparator, metaclass=_PathSeparatorEnumTypeWrapper): ...

PATH_SEPARATOR_UNKNOWN: PathSeparator.ValueType  # 0
"""Value not set."""
PATH_SEPARATOR_DOT: PathSeparator.ValueType  # 1
"""Dot "." path separator"""
PATH_SEPARATOR_SLASH: PathSeparator.ValueType  # 2
"""Slash "/" path separtor"""
global___PathSeparator = PathSeparator

class _TraceLevel:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _TraceLevelEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TraceLevel.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    TRACE_LEVEL_UNKNOWN: _TraceLevel.ValueType  # 0
    """Value not set."""
    TRACE_LEVEL_OFF: _TraceLevel.ValueType  # 1
    """ExplainOffV1   ExplainModeV1 = "off" """
    TRACE_LEVEL_FULL: _TraceLevel.ValueType  # 2
    """ExplainFullV1  ExplainModeV1 = "full" """
    TRACE_LEVEL_NOTES: _TraceLevel.ValueType  # 3
    """ExplainNotesV1 ExplainModeV1 = "notes" """
    TRACE_LEVEL_FAILS: _TraceLevel.ValueType  # 4
    """ExplainFailsV1 ExplainModeV1 = "fails" """

class TraceLevel(_TraceLevel, metaclass=_TraceLevelEnumTypeWrapper): ...

TRACE_LEVEL_UNKNOWN: TraceLevel.ValueType  # 0
"""Value not set."""
TRACE_LEVEL_OFF: TraceLevel.ValueType  # 1
"""ExplainOffV1   ExplainModeV1 = "off" """
TRACE_LEVEL_FULL: TraceLevel.ValueType  # 2
"""ExplainFullV1  ExplainModeV1 = "full" """
TRACE_LEVEL_NOTES: TraceLevel.ValueType  # 3
"""ExplainNotesV1 ExplainModeV1 = "notes" """
TRACE_LEVEL_FAILS: TraceLevel.ValueType  # 4
"""ExplainFailsV1 ExplainModeV1 = "fails" """
global___TraceLevel = TraceLevel

class InfoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___InfoRequest = InfoRequest

class InfoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VERSION_FIELD_NUMBER: builtins.int
    COMMIT_FIELD_NUMBER: builtins.int
    DATE_FIELD_NUMBER: builtins.int
    OS_FIELD_NUMBER: builtins.int
    ARCH_FIELD_NUMBER: builtins.int
    version: builtins.str
    commit: builtins.str
    date: builtins.str
    os: builtins.str
    arch: builtins.str
    def __init__(
        self,
        *,
        version: builtins.str = ...,
        commit: builtins.str = ...,
        date: builtins.str = ...,
        os: builtins.str = ...,
        arch: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["arch", b"arch", "commit", b"commit", "date", b"date", "os", b"os", "version", b"version"]) -> None: ...

global___InfoResponse = InfoResponse

class GetPolicyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    FIELD_MASK_FIELD_NUMBER: builtins.int
    POLICY_INSTANCE_FIELD_NUMBER: builtins.int
    id: builtins.str
    @property
    def field_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    @property
    def policy_instance(self) -> aserto.authorizer.v2.api.policy_instance_pb2.PolicyInstance: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        field_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        policy_instance: aserto.authorizer.v2.api.policy_instance_pb2.PolicyInstance | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_policy_instance", b"_policy_instance", "field_mask", b"field_mask", "policy_instance", b"policy_instance"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_policy_instance", b"_policy_instance", "field_mask", b"field_mask", "id", b"id", "policy_instance", b"policy_instance"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_policy_instance", b"_policy_instance"]) -> typing_extensions.Literal["policy_instance"] | None: ...

global___GetPolicyRequest = GetPolicyRequest

class GetPolicyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> aserto.authorizer.v2.api.module_pb2.Module: ...
    def __init__(
        self,
        *,
        result: aserto.authorizer.v2.api.module_pb2.Module | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["result", b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["result", b"result"]) -> None: ...

global___GetPolicyResponse = GetPolicyResponse

class ListPoliciesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FIELD_MASK_FIELD_NUMBER: builtins.int
    POLICY_INSTANCE_FIELD_NUMBER: builtins.int
    @property
    def field_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    @property
    def policy_instance(self) -> aserto.authorizer.v2.api.policy_instance_pb2.PolicyInstance: ...
    def __init__(
        self,
        *,
        field_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        policy_instance: aserto.authorizer.v2.api.policy_instance_pb2.PolicyInstance | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_policy_instance", b"_policy_instance", "field_mask", b"field_mask", "policy_instance", b"policy_instance"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_policy_instance", b"_policy_instance", "field_mask", b"field_mask", "policy_instance", b"policy_instance"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_policy_instance", b"_policy_instance"]) -> typing_extensions.Literal["policy_instance"] | None: ...

global___ListPoliciesRequest = ListPoliciesRequest

class ListPoliciesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[aserto.authorizer.v2.api.module_pb2.Module]: ...
    def __init__(
        self,
        *,
        result: collections.abc.Iterable[aserto.authorizer.v2.api.module_pb2.Module] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["result", b"result"]) -> None: ...

global___ListPoliciesResponse = ListPoliciesResponse

class DecisionTreeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POLICY_CONTEXT_FIELD_NUMBER: builtins.int
    IDENTITY_CONTEXT_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    RESOURCE_CONTEXT_FIELD_NUMBER: builtins.int
    POLICY_INSTANCE_FIELD_NUMBER: builtins.int
    @property
    def policy_context(self) -> aserto.authorizer.v2.api.policy_context_pb2.PolicyContext: ...
    @property
    def identity_context(self) -> aserto.authorizer.v2.api.identity_context_pb2.IdentityContext: ...
    @property
    def options(self) -> global___DecisionTreeOptions: ...
    @property
    def resource_context(self) -> google.protobuf.struct_pb2.Struct: ...
    @property
    def policy_instance(self) -> aserto.authorizer.v2.api.policy_instance_pb2.PolicyInstance: ...
    def __init__(
        self,
        *,
        policy_context: aserto.authorizer.v2.api.policy_context_pb2.PolicyContext | None = ...,
        identity_context: aserto.authorizer.v2.api.identity_context_pb2.IdentityContext | None = ...,
        options: global___DecisionTreeOptions | None = ...,
        resource_context: google.protobuf.struct_pb2.Struct | None = ...,
        policy_instance: aserto.authorizer.v2.api.policy_instance_pb2.PolicyInstance | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_policy_instance", b"_policy_instance", "identity_context", b"identity_context", "options", b"options", "policy_context", b"policy_context", "policy_instance", b"policy_instance", "resource_context", b"resource_context"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_policy_instance", b"_policy_instance", "identity_context", b"identity_context", "options", b"options", "policy_context", b"policy_context", "policy_instance", b"policy_instance", "resource_context", b"resource_context"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_policy_instance", b"_policy_instance"]) -> typing_extensions.Literal["policy_instance"] | None: ...

global___DecisionTreeRequest = DecisionTreeRequest

class DecisionTreeOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PATH_SEPARATOR_FIELD_NUMBER: builtins.int
    path_separator: global___PathSeparator.ValueType
    def __init__(
        self,
        *,
        path_separator: global___PathSeparator.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["path_separator", b"path_separator"]) -> None: ...

global___DecisionTreeOptions = DecisionTreeOptions

class DecisionTreeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PATH_ROOT_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    path_root: builtins.str
    @property
    def path(self) -> google.protobuf.struct_pb2.Struct: ...
    def __init__(
        self,
        *,
        path_root: builtins.str = ...,
        path: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["path", b"path"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["path", b"path", "path_root", b"path_root"]) -> None: ...

global___DecisionTreeResponse = DecisionTreeResponse

class IsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POLICY_CONTEXT_FIELD_NUMBER: builtins.int
    IDENTITY_CONTEXT_FIELD_NUMBER: builtins.int
    RESOURCE_CONTEXT_FIELD_NUMBER: builtins.int
    POLICY_INSTANCE_FIELD_NUMBER: builtins.int
    @property
    def policy_context(self) -> aserto.authorizer.v2.api.policy_context_pb2.PolicyContext: ...
    @property
    def identity_context(self) -> aserto.authorizer.v2.api.identity_context_pb2.IdentityContext: ...
    @property
    def resource_context(self) -> google.protobuf.struct_pb2.Struct: ...
    @property
    def policy_instance(self) -> aserto.authorizer.v2.api.policy_instance_pb2.PolicyInstance: ...
    def __init__(
        self,
        *,
        policy_context: aserto.authorizer.v2.api.policy_context_pb2.PolicyContext | None = ...,
        identity_context: aserto.authorizer.v2.api.identity_context_pb2.IdentityContext | None = ...,
        resource_context: google.protobuf.struct_pb2.Struct | None = ...,
        policy_instance: aserto.authorizer.v2.api.policy_instance_pb2.PolicyInstance | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_policy_instance", b"_policy_instance", "identity_context", b"identity_context", "policy_context", b"policy_context", "policy_instance", b"policy_instance", "resource_context", b"resource_context"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_policy_instance", b"_policy_instance", "identity_context", b"identity_context", "policy_context", b"policy_context", "policy_instance", b"policy_instance", "resource_context", b"resource_context"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_policy_instance", b"_policy_instance"]) -> typing_extensions.Literal["policy_instance"] | None: ...

global___IsRequest = IsRequest

class Decision(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DECISION_FIELD_NUMBER: builtins.int
    IS_FIELD_NUMBER: builtins.int
    decision: builtins.str
    def __init__(
        self,
        *,
        decision: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["decision", b"decision", "is", b"is"]) -> None: ...

global___Decision = Decision

class IsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DECISIONS_FIELD_NUMBER: builtins.int
    @property
    def decisions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Decision]: ...
    def __init__(
        self,
        *,
        decisions: collections.abc.Iterable[global___Decision] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["decisions", b"decisions"]) -> None: ...

global___IsResponse = IsResponse

class QueryOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    METRICS_FIELD_NUMBER: builtins.int
    INSTRUMENT_FIELD_NUMBER: builtins.int
    TRACE_FIELD_NUMBER: builtins.int
    TRACE_SUMMARY_FIELD_NUMBER: builtins.int
    metrics: builtins.bool
    """default false"""
    instrument: builtins.bool
    """default false"""
    trace: global___TraceLevel.ValueType
    """default ExplainOffV1"""
    trace_summary: builtins.bool
    """default false"""
    def __init__(
        self,
        *,
        metrics: builtins.bool = ...,
        instrument: builtins.bool = ...,
        trace: global___TraceLevel.ValueType = ...,
        trace_summary: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["instrument", b"instrument", "metrics", b"metrics", "trace", b"trace", "trace_summary", b"trace_summary"]) -> None: ...

global___QueryOptions = QueryOptions

class QueryRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    QUERY_FIELD_NUMBER: builtins.int
    INPUT_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    POLICY_CONTEXT_FIELD_NUMBER: builtins.int
    IDENTITY_CONTEXT_FIELD_NUMBER: builtins.int
    RESOURCE_CONTEXT_FIELD_NUMBER: builtins.int
    POLICY_INSTANCE_FIELD_NUMBER: builtins.int
    query: builtins.str
    input: builtins.str
    @property
    def options(self) -> global___QueryOptions: ...
    @property
    def policy_context(self) -> aserto.authorizer.v2.api.policy_context_pb2.PolicyContext: ...
    @property
    def identity_context(self) -> aserto.authorizer.v2.api.identity_context_pb2.IdentityContext: ...
    @property
    def resource_context(self) -> google.protobuf.struct_pb2.Struct: ...
    @property
    def policy_instance(self) -> aserto.authorizer.v2.api.policy_instance_pb2.PolicyInstance: ...
    def __init__(
        self,
        *,
        query: builtins.str = ...,
        input: builtins.str = ...,
        options: global___QueryOptions | None = ...,
        policy_context: aserto.authorizer.v2.api.policy_context_pb2.PolicyContext | None = ...,
        identity_context: aserto.authorizer.v2.api.identity_context_pb2.IdentityContext | None = ...,
        resource_context: google.protobuf.struct_pb2.Struct | None = ...,
        policy_instance: aserto.authorizer.v2.api.policy_instance_pb2.PolicyInstance | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_identity_context", b"_identity_context", "_options", b"_options", "_policy_context", b"_policy_context", "_policy_instance", b"_policy_instance", "_resource_context", b"_resource_context", "identity_context", b"identity_context", "options", b"options", "policy_context", b"policy_context", "policy_instance", b"policy_instance", "resource_context", b"resource_context"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_identity_context", b"_identity_context", "_options", b"_options", "_policy_context", b"_policy_context", "_policy_instance", b"_policy_instance", "_resource_context", b"_resource_context", "identity_context", b"identity_context", "input", b"input", "options", b"options", "policy_context", b"policy_context", "policy_instance", b"policy_instance", "query", b"query", "resource_context", b"resource_context"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_identity_context", b"_identity_context"]) -> typing_extensions.Literal["identity_context"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_options", b"_options"]) -> typing_extensions.Literal["options"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_policy_context", b"_policy_context"]) -> typing_extensions.Literal["policy_context"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_policy_instance", b"_policy_instance"]) -> typing_extensions.Literal["policy_instance"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_resource_context", b"_resource_context"]) -> typing_extensions.Literal["resource_context"] | None: ...

global___QueryRequest = QueryRequest

class CompileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    QUERY_FIELD_NUMBER: builtins.int
    INPUT_FIELD_NUMBER: builtins.int
    UNKNOWNS_FIELD_NUMBER: builtins.int
    DISABLE_INLINING_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    POLICY_CONTEXT_FIELD_NUMBER: builtins.int
    IDENTITY_CONTEXT_FIELD_NUMBER: builtins.int
    RESOURCE_CONTEXT_FIELD_NUMBER: builtins.int
    POLICY_INSTANCE_FIELD_NUMBER: builtins.int
    query: builtins.str
    input: builtins.str
    @property
    def unknowns(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def disable_inlining(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def options(self) -> global___QueryOptions: ...
    @property
    def policy_context(self) -> aserto.authorizer.v2.api.policy_context_pb2.PolicyContext: ...
    @property
    def identity_context(self) -> aserto.authorizer.v2.api.identity_context_pb2.IdentityContext: ...
    @property
    def resource_context(self) -> google.protobuf.struct_pb2.Struct: ...
    @property
    def policy_instance(self) -> aserto.authorizer.v2.api.policy_instance_pb2.PolicyInstance: ...
    def __init__(
        self,
        *,
        query: builtins.str = ...,
        input: builtins.str = ...,
        unknowns: collections.abc.Iterable[builtins.str] | None = ...,
        disable_inlining: collections.abc.Iterable[builtins.str] | None = ...,
        options: global___QueryOptions | None = ...,
        policy_context: aserto.authorizer.v2.api.policy_context_pb2.PolicyContext | None = ...,
        identity_context: aserto.authorizer.v2.api.identity_context_pb2.IdentityContext | None = ...,
        resource_context: google.protobuf.struct_pb2.Struct | None = ...,
        policy_instance: aserto.authorizer.v2.api.policy_instance_pb2.PolicyInstance | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_identity_context", b"_identity_context", "_options", b"_options", "_policy_context", b"_policy_context", "_policy_instance", b"_policy_instance", "_resource_context", b"_resource_context", "identity_context", b"identity_context", "options", b"options", "policy_context", b"policy_context", "policy_instance", b"policy_instance", "resource_context", b"resource_context"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_identity_context", b"_identity_context", "_options", b"_options", "_policy_context", b"_policy_context", "_policy_instance", b"_policy_instance", "_resource_context", b"_resource_context", "disable_inlining", b"disable_inlining", "identity_context", b"identity_context", "input", b"input", "options", b"options", "policy_context", b"policy_context", "policy_instance", b"policy_instance", "query", b"query", "resource_context", b"resource_context", "unknowns", b"unknowns"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_identity_context", b"_identity_context"]) -> typing_extensions.Literal["identity_context"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_options", b"_options"]) -> typing_extensions.Literal["options"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_policy_context", b"_policy_context"]) -> typing_extensions.Literal["policy_context"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_policy_instance", b"_policy_instance"]) -> typing_extensions.Literal["policy_instance"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_resource_context", b"_resource_context"]) -> typing_extensions.Literal["resource_context"] | None: ...

global___CompileRequest = CompileRequest

class CompileResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    METRICS_FIELD_NUMBER: builtins.int
    TRACE_FIELD_NUMBER: builtins.int
    TRACE_SUMMARY_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> google.protobuf.struct_pb2.Struct: ...
    @property
    def metrics(self) -> google.protobuf.struct_pb2.Struct: ...
    @property
    def trace(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.struct_pb2.Struct]: ...
    @property
    def trace_summary(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        result: google.protobuf.struct_pb2.Struct | None = ...,
        metrics: google.protobuf.struct_pb2.Struct | None = ...,
        trace: collections.abc.Iterable[google.protobuf.struct_pb2.Struct] | None = ...,
        trace_summary: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metrics", b"metrics", "result", b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["metrics", b"metrics", "result", b"result", "trace", b"trace", "trace_summary", b"trace_summary"]) -> None: ...

global___CompileResponse = CompileResponse

class QueryResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESPONSE_FIELD_NUMBER: builtins.int
    METRICS_FIELD_NUMBER: builtins.int
    TRACE_FIELD_NUMBER: builtins.int
    TRACE_SUMMARY_FIELD_NUMBER: builtins.int
    @property
    def response(self) -> google.protobuf.struct_pb2.Struct: ...
    @property
    def metrics(self) -> google.protobuf.struct_pb2.Struct: ...
    @property
    def trace(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.struct_pb2.Struct]: ...
    @property
    def trace_summary(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        response: google.protobuf.struct_pb2.Struct | None = ...,
        metrics: google.protobuf.struct_pb2.Struct | None = ...,
        trace: collections.abc.Iterable[google.protobuf.struct_pb2.Struct] | None = ...,
        trace_summary: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metrics", b"metrics", "response", b"response"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["metrics", b"metrics", "response", b"response", "trace", b"trace", "trace_summary", b"trace_summary"]) -> None: ...

global___QueryResponse = QueryResponse
