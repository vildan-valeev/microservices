import logging
from typing import Optional

import grpc
from aiohttp import web
from google.protobuf.json_format import MessageToJson, MessageToDict

from pb import main_pb2_grpc as pb2_grpc
from pb import main_pb2 as pb2

app = web.Application()
routes = web.RouteTableDef()


# log = logging.getLogger(__name__)


class BotAPIClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.BotAPIStub(self.channel)

    def get_text_from_db(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.MessageRequest(tag=message)
        print(f'{message}')

        return self.stub.GetMessage(message)

    def get_menu_from_db(self, tag, user_id):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.MenuRequest(tag=tag, user_id=user_id)
        print(f'{message}')
        return self.stub.GetMenu(message)


async def get_text(tag: str, ) -> Optional[str]:
    client = BotAPIClient()
    result = client.get_text_from_db(tag)
    # print(f'{result.text}')
    return result.text


async def get_menu(tag: str, user_id: int) -> Optional[str]:
    client = BotAPIClient()
    result = client.get_menu_from_db(tag, user_id)
    # print(f'{result.text}')

    return MessageToDict(result)


@routes.get('/text/')
async def start(request):
    """Call pong"""
    # logging.info('pong')
    result = await get_text('tag')
    logging.info(result)
    return web.json_response({'text': result}, status=200)


@routes.get('/menu/')
async def start(request):
    """Call pong"""
    # logging.info('pong')
    result = await get_menu('tag', 123)
    # data = {'service_two': 'service_two'}
    logging.info(result)
    return web.json_response(result, status=200)


app.add_routes(routes)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    web.run_app(app, port=7000)
