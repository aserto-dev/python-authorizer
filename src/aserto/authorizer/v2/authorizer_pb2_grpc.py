# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from aserto.authorizer.v2 import authorizer_pb2 as aserto_dot_authorizer_dot_v2_dot_authorizer__pb2


class AuthorizerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DecisionTree = channel.unary_unary(
                '/aserto.authorizer.v2.Authorizer/DecisionTree',
                request_serializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.DecisionTreeRequest.SerializeToString,
                response_deserializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.DecisionTreeResponse.FromString,
                _registered_method=True)
        self.Is = channel.unary_unary(
                '/aserto.authorizer.v2.Authorizer/Is',
                request_serializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.IsRequest.SerializeToString,
                response_deserializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.IsResponse.FromString,
                _registered_method=True)
        self.Query = channel.unary_unary(
                '/aserto.authorizer.v2.Authorizer/Query',
                request_serializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.QueryRequest.SerializeToString,
                response_deserializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.QueryResponse.FromString,
                _registered_method=True)
        self.Compile = channel.unary_unary(
                '/aserto.authorizer.v2.Authorizer/Compile',
                request_serializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.CompileRequest.SerializeToString,
                response_deserializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.CompileResponse.FromString,
                _registered_method=True)
        self.ListPolicies = channel.unary_unary(
                '/aserto.authorizer.v2.Authorizer/ListPolicies',
                request_serializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.ListPoliciesRequest.SerializeToString,
                response_deserializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.ListPoliciesResponse.FromString,
                _registered_method=True)
        self.GetPolicy = channel.unary_unary(
                '/aserto.authorizer.v2.Authorizer/GetPolicy',
                request_serializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.GetPolicyRequest.SerializeToString,
                response_deserializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.GetPolicyResponse.FromString,
                _registered_method=True)
        self.Info = channel.unary_unary(
                '/aserto.authorizer.v2.Authorizer/Info',
                request_serializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.InfoRequest.SerializeToString,
                response_deserializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.InfoResponse.FromString,
                _registered_method=True)


class AuthorizerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DecisionTree(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Is(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Query(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Compile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPolicies(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPolicy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Info(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthorizerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DecisionTree': grpc.unary_unary_rpc_method_handler(
                    servicer.DecisionTree,
                    request_deserializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.DecisionTreeRequest.FromString,
                    response_serializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.DecisionTreeResponse.SerializeToString,
            ),
            'Is': grpc.unary_unary_rpc_method_handler(
                    servicer.Is,
                    request_deserializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.IsRequest.FromString,
                    response_serializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.IsResponse.SerializeToString,
            ),
            'Query': grpc.unary_unary_rpc_method_handler(
                    servicer.Query,
                    request_deserializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.QueryRequest.FromString,
                    response_serializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.QueryResponse.SerializeToString,
            ),
            'Compile': grpc.unary_unary_rpc_method_handler(
                    servicer.Compile,
                    request_deserializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.CompileRequest.FromString,
                    response_serializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.CompileResponse.SerializeToString,
            ),
            'ListPolicies': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPolicies,
                    request_deserializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.ListPoliciesRequest.FromString,
                    response_serializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.ListPoliciesResponse.SerializeToString,
            ),
            'GetPolicy': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPolicy,
                    request_deserializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.GetPolicyRequest.FromString,
                    response_serializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.GetPolicyResponse.SerializeToString,
            ),
            'Info': grpc.unary_unary_rpc_method_handler(
                    servicer.Info,
                    request_deserializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.InfoRequest.FromString,
                    response_serializer=aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.InfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'aserto.authorizer.v2.Authorizer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('aserto.authorizer.v2.Authorizer', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Authorizer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DecisionTree(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/aserto.authorizer.v2.Authorizer/DecisionTree',
            aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.DecisionTreeRequest.SerializeToString,
            aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.DecisionTreeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Is(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/aserto.authorizer.v2.Authorizer/Is',
            aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.IsRequest.SerializeToString,
            aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.IsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/aserto.authorizer.v2.Authorizer/Query',
            aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.QueryRequest.SerializeToString,
            aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.QueryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Compile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/aserto.authorizer.v2.Authorizer/Compile',
            aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.CompileRequest.SerializeToString,
            aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.CompileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListPolicies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/aserto.authorizer.v2.Authorizer/ListPolicies',
            aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.ListPoliciesRequest.SerializeToString,
            aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.ListPoliciesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetPolicy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/aserto.authorizer.v2.Authorizer/GetPolicy',
            aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.GetPolicyRequest.SerializeToString,
            aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.GetPolicyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Info(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/aserto.authorizer.v2.Authorizer/Info',
            aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.InfoRequest.SerializeToString,
            aserto_dot_authorizer_dot_v2_dot_authorizer__pb2.InfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
