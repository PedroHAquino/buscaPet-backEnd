from server import logger, NotFound, db
from server.models.adm import Admin, AdminSchema
from server.models.instituicao import Instituicao, InstituicaoSchema
from server.repository import base_repository
from server.services import utils


def post_instituicao(instituicao_dto):
    logger.info(f"Cadastro de nova instituição")
    instituicao = utils.converte_dto_para_objeto(Instituicao, instituicao_dto)
    base_repository.gravar_objeto(instituicao)
    return utils.serialize_entidade(instituicao, InstituicaoSchema)


def post_adm_instituicao(admin_dto):
    logger.info(f"Cadastrar adm")
    admin = utils.converte_dto_para_objeto(Admin, admin_dto)
    base_repository.gravar_objeto(admin)
    return utils.serialize_entidade(admin, AdminSchema)


def get_all_instituicao():
    logger.info(f"Inicio - Listar Instituicao")
    return base_repository.listar(Instituicao, InstituicaoSchema)


def get_all_adm_instituicao():
    logger.info(f"Inicio - Listar Administrador")
    return base_repository.listar(Admin, AdminSchema)


def put_instituicao(id, instituicao_dto):
    logger.info(f"Inicio: - atualizar cliente por id \n {id}")
    try:
        instituicao = base_repository.get_objeto_por_id(Instituicao, id)

        if instituicao is not None:
            utils.converte_dto_para_objeto(Instituicao, instituicao_dto, instituicao)
            base_repository.gravar_objeto(instituicao)

            return utils.serialize_entidade(instituicao, InstituicaoSchema)

        raise NotFound()

    except Exception as ex:
        logger.error(f"Erro ao atualizar cliente \n {ex}")
        db.session.rollback()
        raise ex


def put_adm_instituicao(id, instituicao_dto):
    logger.info(f"Inicio - atualizar Administrador por id \n {id}")
    try:
        adm = base_repository.get_objeto_por_id(Admin, id)

        if adm is not None:
            utils.converte_dto_para_objeto(Admin, instituicao_dto, adm)
            base_repository.gravar_objeto(adm)

            return utils.serialize_entidade(adm, AdminSchema)

        raise NotFound()

    except Exception as ex:
        logger.error(f"Erro ao atualizar Administrador \n {ex}")
        db.session.rollback()
        raise ex


def cancelar_adm(id):
    logger.info(f"Inicio - Cancelar Administrador")
    try:
        adm = base_repository.get_objeto_por_id(Admin, id)

        if adm is not None:
            adm.status = "CANCELADO"
            base_repository.gravar_objeto(adm)

            return utils.serialize_entidade(adm, AdminSchema)

        raise NotFound

    except Exception as ex:
        logger.error(f"Erro ao cancelar Administrador \n {ex}")
        db.session.rollback()
        raise ex
