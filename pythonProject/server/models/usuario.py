from datetime import datetime

from sqlalchemy import Column, Integer, Date, Text, DateTime

from server import db, ma


class Usuario(db.Model):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True)
    cpf = Column(Text)
    nome = Column(Text)
    dt_nasc = Column(Date)
    telefone = Column(Text)
    email = Column(Text)
    senha = Column(Text)

    create_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class UsuarioSchema(ma.ModelSchema):
    class Meta:
        fields = (
            "id",
            "cpf",
            "nome",
            "dt_nasc",
            "telefone",
            "email",
            "senha",
        )
