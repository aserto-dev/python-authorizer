"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import aserto.authorizer.v2.api.identity_context_pb2
import aserto.authorizer.v2.api.policy_context_pb2
import aserto.authorizer.v2.api.policy_instance_pb2
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Decision(google.protobuf.message.Message):
    """represents a decision that an authorizer performed in the past"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class OutcomesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.bool
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.bool = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class AnnotationsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    POLICY_FIELD_NUMBER: builtins.int
    OUTCOMES_FIELD_NUMBER: builtins.int
    RESOURCE_FIELD_NUMBER: builtins.int
    ANNOTATIONS_FIELD_NUMBER: builtins.int
    TENANT_ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """unique id, replay a decision starting with this, also useful to de-dup"""
    path: builtins.str
    """Policy path used in decision"""
    tenant_id: builtins.str
    """id of the tenant that generated the decision"""
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """UTC time when the decision was made"""

    @property
    def user(self) -> global___DecisionUser:
        """info about user for whom the decision as made"""

    @property
    def policy(self) -> global___DecisionPolicy:
        """info about policy used for the decision"""

    @property
    def outcomes(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.bool]:
        """outcome of the decisions specified in the policy context"""

    @property
    def resource(self) -> google.protobuf.struct_pb2.Struct:
        """the resource context used in a decision"""

    @property
    def annotations(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """annotations that may be added to a decision"""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        path: builtins.str = ...,
        user: global___DecisionUser | None = ...,
        policy: global___DecisionPolicy | None = ...,
        outcomes: collections.abc.Mapping[builtins.str, builtins.bool] | None = ...,
        resource: google.protobuf.struct_pb2.Struct | None = ...,
        annotations: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        tenant_id: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_tenant_id", b"_tenant_id", "policy", b"policy", "resource", b"resource", "tenant_id", b"tenant_id", "timestamp", b"timestamp", "user", b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_tenant_id", b"_tenant_id", "annotations", b"annotations", "id", b"id", "outcomes", b"outcomes", "path", b"path", "policy", b"policy", "resource", b"resource", "tenant_id", b"tenant_id", "timestamp", b"timestamp", "user", b"user"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_tenant_id", b"_tenant_id"]) -> typing.Literal["tenant_id"] | None: ...

global___Decision = Decision

@typing.final
class DecisionUser(google.protobuf.message.Message):
    """information about a user on behalf of whom a decision was made"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTEXT_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    EMAIL_FIELD_NUMBER: builtins.int
    id: builtins.str
    """id of the user the identity resolved to"""
    email: builtins.str
    """convinience human-readable identifier"""
    @property
    def context(self) -> aserto.authorizer.v2.api.identity_context_pb2.IdentityContext:
        """identity context used in the decision"""

    def __init__(
        self,
        *,
        context: aserto.authorizer.v2.api.identity_context_pb2.IdentityContext | None = ...,
        id: builtins.str = ...,
        email: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["context", b"context"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["context", b"context", "email", b"email", "id", b"id"]) -> None: ...

global___DecisionUser = DecisionUser

@typing.final
class DecisionPolicy(google.protobuf.message.Message):
    """information about a policy used in a decision"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTEXT_FIELD_NUMBER: builtins.int
    REGISTRY_SERVICE_FIELD_NUMBER: builtins.int
    REGISTRY_IMAGE_FIELD_NUMBER: builtins.int
    REGISTRY_TAG_FIELD_NUMBER: builtins.int
    REGISTRY_DIGEST_FIELD_NUMBER: builtins.int
    POLICY_INSTANCE_FIELD_NUMBER: builtins.int
    registry_service: builtins.str
    """registry service where policy was retrieved from (e.g. opcr.io)"""
    registry_image: builtins.str
    """image of the policy in the registry, including org (e.g. acmecorp/peoplefinder-abac)"""
    registry_tag: builtins.str
    """tag of the policy image (e.g. 0.8.2 or latest)"""
    registry_digest: builtins.str
    """digest of the policy image"""
    @property
    def context(self) -> aserto.authorizer.v2.api.policy_context_pb2.PolicyContext:
        """policy context used in the decision"""

    @property
    def policy_instance(self) -> aserto.authorizer.v2.api.policy_instance_pb2.PolicyInstance:
        """policy instance used in decision"""

    def __init__(
        self,
        *,
        context: aserto.authorizer.v2.api.policy_context_pb2.PolicyContext | None = ...,
        registry_service: builtins.str = ...,
        registry_image: builtins.str = ...,
        registry_tag: builtins.str = ...,
        registry_digest: builtins.str = ...,
        policy_instance: aserto.authorizer.v2.api.policy_instance_pb2.PolicyInstance | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["context", b"context", "policy_instance", b"policy_instance"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["context", b"context", "policy_instance", b"policy_instance", "registry_digest", b"registry_digest", "registry_image", b"registry_image", "registry_service", b"registry_service", "registry_tag", b"registry_tag"]) -> None: ...

global___DecisionPolicy = DecisionPolicy
