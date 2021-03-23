from server import logger, NotFound, db
from server.models.mural import Mural, MuralSchema
from server.models.postagem import Postagem, PostagemSchema
from server.repository import base_repository
from server.services import utils


def post_postagem(postagem_dto):
    logger.info(f"Inicio - Fazer uma nova Postagem")
    postagem = utils.converte_dto_para_objeto(Postagem, postagem_dto)
    base_repository.gravar_objeto(postagem)
    return utils.serialize_entidade(postagem, PostagemSchema)


def get_all_postagem():
    logger.info(f"Inicio - Lista todas as publicaçoes do Mural")
    return base_repository.listar(Postagem, PostagemSchema)


def put_postagem(id, postagem_dto):
    logger.info(f"Inicio - Atualizar Postagem por id \n {id}")
    try:
        postagem = base_repository.get_objeto_por_id(Postagem, id)

        if postagem is not None:
            utils.converte_dto_para_objeto(Postagem, postagem_dto, postagem)
            base_repository.gravar_objeto(postagem)

            return utils.serialize_entidade(postagem, PostagemSchema)

        raise NotFound()

    except Exception as ex:
        logger(f"Erro ao atualizar Postagem \n {ex}")
        db.session.rollback()
        raise ex
