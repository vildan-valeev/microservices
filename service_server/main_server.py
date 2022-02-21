import asyncio
import logging
from collections import OrderedDict

import grpc

from pb import main_pb2_grpc as pb2_grpc
from pb import main_pb2 as pb2

# log = logging.getLogger(__name__)

text_to_response = 'response text'
# list_response = [
#     {
#         'title': 'title 1',
#         'callback': 'callback_1'
#     },
#     {
#         'title': 'title 2',
#         'callback': 'callback_2'
#     }
# ]

list_response = [OrderedDict([('title', 'Старт'), ('callback', 'start')]),
                 OrderedDict([('title', 'Добавить объявление'), ('callback', 'add')]),
                 OrderedDict([('title', 'Профиль'), ('callback', 'profile')])]


class BotAPIGreeter(pb2_grpc.BotAPIServicer):
    """Сервер который будет слушать/ждать запросы"""

    def GetMessage(self, request, context):
        tag = request.tag
        print('Запрос текста', tag)

        result = {'text': text_to_response}
        return pb2.MessageResponse(**result)

    def GetMenu(self, request, context):
        tag = request.tag
        user_id = request.user_id
        print('Запрос меню', tag, user_id)

        result = {'results': list_response}
        return pb2.MenuResponse(**result)


async def serve() -> None:
    server = grpc.aio.server()
    pb2_grpc.add_BotAPIServicer_to_server(BotAPIGreeter(), server)

    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
