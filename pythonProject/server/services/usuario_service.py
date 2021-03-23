from server import logger
from server.models.usuario import Usuario, UsuarioSchema
from server.repository import base_repository
from server.services import utils


def post_usuario(usuario_dto):
    logger.info(f"Cadastro de novo usuario")
    usuario = utils.converte_dto_para_objeto(Usuario, usuario_dto)
    base_repository.gravar_objeto(usuario)
    return utils.serialize_entidade(usuario, UsuarioSchema)


def get_all_usuario():
    logger.info(f"Listar Usuario")
    return base_repository.listar(Usuario, UsuarioSchema)


def post_mural_usuario():
    pass


def get_all_mural():
    pass

