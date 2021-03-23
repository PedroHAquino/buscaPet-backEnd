import datetime

import connexion
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from server.configurations import environments_variables
from server.configurations.logger import factory_logger
from server.models.exceptions import DataFail, generic_render, NotFound, NoContent, Unauthorized, BusinessFail, \
    ConflictFail

db = SQLAlchemy()
ma = Marshmallow()
logger = factory_logger()


def init_api():
    app = connexion.App(__name__, specification_dir="./swagger/")
    app.add_api("swagger.yaml",
                arguments={"host_with_port": f"{environments_variables.HOST}:{environments_variables.PORT}"})
    app.add_error_handler(DataFail, generic_render)
    app.add_error_handler(NotFound, generic_render)
    app.add_error_handler(NoContent, generic_render)
    app.add_error_handler(Unauthorized, generic_render)
    app.add_error_handler(BusinessFail, generic_render)
    app.add_error_handler(ConflictFail, generic_render)
    app.app.config["SQLALCHEMY_DATABASE_URI"] = environments_variables.PROJETO_DBCONN
    app.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.app.config['SECRET_KEY'] = '%C*F-JaNdRgUkXp2s5v8y/B?E(G+KbPe'
    app.app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=1)
    db.init_app(app.app)
    CORS(app.app)
    ma.init_app(app.app)
    return app
