# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import main_pb2  as main__pb2
# import main_pb2 as main__pb2


class BotAPIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMessage = channel.unary_unary(
            '/BotAPI/GetMessage',
            request_serializer=main__pb2.MessageRequest.SerializeToString,
            response_deserializer=main__pb2.MessageResponse.FromString,
        )
        self.GetMenu = channel.unary_unary(
            '/BotAPI/GetMenu',
            request_serializer=main__pb2.MenuRequest.SerializeToString,
            response_deserializer=main__pb2.MenuResponse.FromString,
        )


class BotAPIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetMessage(self, request, context):
        """объявляем сервис BotMessage с методом GetMessage который будет использован на стороне сервера и будет ждать/принимать
        MessageRequest и отдавать MessageResponse
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMenu(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BotAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetMessage': grpc.unary_unary_rpc_method_handler(
            servicer.GetMessage,
            request_deserializer=main__pb2.MessageRequest.FromString,
            response_serializer=main__pb2.MessageResponse.SerializeToString,
        ),
        'GetMenu': grpc.unary_unary_rpc_method_handler(
            servicer.GetMenu,
            request_deserializer=main__pb2.MenuRequest.FromString,
            response_serializer=main__pb2.MenuResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'BotAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class BotAPI(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetMessage(request,
                   target,
                   options=(),
                   channel_credentials=None,
                   call_credentials=None,
                   insecure=False,
                   compression=None,
                   wait_for_ready=None,
                   timeout=None,
                   metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BotAPI/GetMessage',
                                             main__pb2.MessageRequest.SerializeToString,
                                             main__pb2.MessageResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMenu(request,
                target,
                options=(),
                channel_credentials=None,
                call_credentials=None,
                insecure=False,
                compression=None,
                wait_for_ready=None,
                timeout=None,
                metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BotAPI/GetMenu',
                                             main__pb2.MenuRequest.SerializeToString,
                                             main__pb2.MenuResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
