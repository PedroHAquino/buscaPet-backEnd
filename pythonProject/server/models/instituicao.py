from datetime import datetime

from sqlalchemy import Column, Integer, Date, Text, DateTime

from server import db, ma


class Instituicao(db.Model):
    __tablename__ = "instituicao"

    id = Column(Integer, primary_key=True)
    cnpj = Column(Text)
    nome = Column(Text)
    dt_criacao = Column(Date)
    telefone = Column(Text)
    email = Column(Text)
    descricao = Column(Text)
    endereco = Column(Text)
    senha = Column(Text)

    create_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class InstituicaoSchema(ma.ModelSchema):
    class Meta:
        fields = (
            "id",
            "cnpj",
            "nome",
            "dt_criacao",
            "telefone",
            "email",
            "descricao",
            "endereco",
            "senha",
        )
