from datetime import datetime

from sqlalchemy import Column, Integer, Date, Text, DateTime, ForeignKey, Time

from server import db, ma


class Postagem(db.Model):
    __tablename__ = "postagem"

    id = Column(Integer, primary_key=True)
    animal = Column(Text)
    cor = Column(Text)
    descricao = Column(Text)
    dt_desaparecimento = Column(Date)
    id_mural = Column('id_mural', Integer, ForeignKey("mural.id"))

    create_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class PostagemSchema(ma.ModelSchema):
    class Meta:
        fields = (
            "id",
            "animal",
            "cor",
            "descricao",
            "dt_desaparecimento",
            "id_mural",
        )
