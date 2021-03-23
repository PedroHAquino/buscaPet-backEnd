from datetime import datetime

from sqlalchemy import Column, Integer, Date, Text, DateTime, ForeignKey

from server import db, ma


class Admin(db.Model):
    __tablename__ = "adm"

    id = Column(Integer, primary_key=True)
    cpf = Column(Text)
    nome = Column(Text)
    dt_nasc = Column(Date)
    telefone = Column(Text)
    email = Column(Text)
    senha = Column(Text)
    cargo = Column(Text)
    id_instituicao = Column('id_instituicao', Integer, ForeignKey("instituicao.id"))

    create_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class AdminSchema(ma.ModelSchema):
    class Meta:
        fields = (
            "id",
            "cpf",
            "nome",
            "dt_nasc",
            "telefone",
            "email",
            "senha",
            "cargo",
            "id_instituicao",
        )
