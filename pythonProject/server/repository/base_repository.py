from datetime import datetime

from flask import g
from sqlalchemy.exc import IntegrityError

from server import db
from server.configurations.environments_variables import PER_PAGE, MAX_PER_PAGE
from server.configurations.logger import get_logger
from server.models.exceptions import ApiBaseException, NotFound
from server.services.utils import fabrica_filtros, valida_no_content_ou_no_found, serialize_pagination


def get_filtros(clazz):
    filtros = {}
    return filtros


def get_objeto_por_id(clazz, id_objeto):
    query = db.session.query(clazz).filter(clazz.id == id_objeto)

    return query.first()


def gravar_objeto(objeto):
    try:
        db.session.add(objeto)
        db.session.commit()
    except Exception as error:
        db.session.rollback()
        if len(error.args) == 1:
            get_logger().error(f'erro ao gravar {objeto.__class__.__name__}: {error.args[0]}')
            raise ApiBaseException(error.args[0])
        else:
            get_logger().error(f'erro ao gravar {objeto.__class__.__name__}: {error}')
            raise ApiBaseException(error.args[0])


def excluir_objeto_por_id(clazz, id_objeto):
    objeto = get_objeto_por_id(clazz, id_objeto)

    if objeto is not None:
        excluir_objeto(objeto)
        return

    raise NotFound()


def excluir_objeto(objeto):
        db.session.delete(objeto)
        db.session.commit()


def listar(clazz, schema):
    filtros, joins, pagina = fabrica_filtros(get_filtros(clazz))

    pagination = (
        clazz()
            .query.join(*joins)
            .filter(*filtros)
            .paginate(per_page=PER_PAGE, max_per_page=MAX_PER_PAGE, page=pagina)
    )
    if not valida_no_content_ou_no_found(filtros, pagination.items):
        return []

    return serialize_pagination(schema, pagination)


def get_objetos_por_campo_valor(clazz, campo, descricao):
    query = db.session.query(clazz).filter(campo == descricao)
    if hasattr(clazz, 'deleted_at'):
        query = query.filter(clazz.deleted_at == None)
    return query.all()
