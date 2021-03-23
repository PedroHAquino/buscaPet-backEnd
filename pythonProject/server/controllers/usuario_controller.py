from server.services import usuario_service


def post_usuario(body):
    return usuario_service.post_usuario(body), 201


def get_all_usuario():
    return usuario_service.get_all_usuario(), 200


def get_all_mural():
    return usuario_service.get_all_usuario(), 200


def put_usuario(id, body):
    pass
