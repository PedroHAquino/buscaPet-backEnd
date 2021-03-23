from datetime import datetime

from sqlalchemy import Column, Integer, Date, Text, DateTime, ForeignKey, Time

from server import db, ma


class Mural(db.Model):
    __tablename__ = "mural"

    """id = Column(Integer, primary_key=True)
    status = Column(Text)
    data_agendamento = Column(Date)
    horas_publicacao = Column(Time)
    id_instituicao = Column('id_instituicao', Integer, ForeignKey("instituicao.id"))
    id_adm = Column('id_adm', Integer, ForeignKey("adm.id"))
    id_usuario = Column('id_usuario', Integer, ForeignKey("usuario.id"))

    create_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)"""
    id = Column(Integer, primary_key=True)
    id_instituicao = Column('id_instituicao', Integer, ForeignKey("instituicao.id"))
    id_adm = Column('id_adm', Integer, ForeignKey("adm.id"))
    id_usuario = Column('id_usuario', Integer, ForeignKey("usuario.id"))

    create_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class MuralSchema(ma.ModelSchema):
    class Meta:
        fields = (
            "id",
            "id_instituicao",
            "id_adm",
            "id_usuario",
        )
