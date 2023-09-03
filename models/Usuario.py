import db
from sqlalchemy import Column, Integer, String


class Usuario(db.Base):

    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement='auto')
    nombre = Column(String(80), nullable=False)
    correo = Column(String(80), nullable=False)
    contrasena = Column(String(80), nullable=False)

    def __init__(self, id, nombre, correo, contrasena):
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
