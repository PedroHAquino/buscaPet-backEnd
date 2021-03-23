from server.services import instituicao_service


def post_instituicao(body):
    return instituicao_service.post_instituicao(body), 201


def get_all_instituicao():
    return instituicao_service.get_all_instituicao(), 200


def post_adm_instituicao(body):
    return instituicao_service.post_adm_instituicao(body), 201


def get_all_adm_instituicao():
    return instituicao_service.get_all_adm_instituicao(), 200


def put_instituicao(id, body):
    return instituicao_service.put_instituicao(id, body), 200


def put_adm_instituicao(id, body):
    return instituicao_service.put_instituicao(id, body), 200


def post_cancelar_adm(id, body=None):
    return instituicao_service.cancelar_adm(id), 201



