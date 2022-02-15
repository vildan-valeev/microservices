import asyncio
import logging

import grpc

from pb import main_pb2_grpc as pb2_grpc
from pb import main_pb2 as pb2

# log = logging.getLogger(__name__)

text_to_response = 'response text'
list_response = [
    {
        'title': 'title 1',
        'callback': 'callback_1'
    },
    {
        'title': 'title 2',
        'callback': 'callback_2'
    }
]


class MessageGreeter(pb2_grpc.BotMessageServicer):
    """Сервер который будет слушать/ждать запросы"""

    def GetMessage(self, request, context):
        tag = request.tag
        print(tag)

        result = {'text': text_to_response}
        return pb2.MessageResponse(**result)


class MenuGreeter(pb2_grpc.BotMenuServicer):
    # serializer_class = ButtonsSerializer

    def GetMenu(self, request, context):
        tag = request.tag
        user_id = request.user_id
        print(f'{tag=} {user_id=}')
        return pb2.MenuResponse(list_response)


async def serve() -> None:
    server = grpc.aio.server()
    pb2_grpc.add_BotMessageServicer_to_server(MessageGreeter(), server)
    pb2_grpc.add_BotMenuServicer_to_server(MenuGreeter(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
