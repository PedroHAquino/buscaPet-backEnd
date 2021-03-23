from server import logger
from server.services import postagem_service


def post_postagem(body):
    return postagem_service.post_postagem(body), 201


def get_all_postagem():
    return postagem_service.get_all_postagem(), 200


def put_postagem(id, body):
    return postagem_service.put_postagem(id, body), 200
