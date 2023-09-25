import db
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship


class Usuario(db.Base):

    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement='auto')
    nombre = Column(String(80), nullable=False)
    correo = Column(String(80), nullable=False)
    contrasena = Column(String(80), nullable=False)
    es_activo = Column(Boolean, default=False)

    tareas = relationship("Tarea", back_populates="usuario")

    def __init__(self, id, nombre, correo, contrasena, es_activo):
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.es_activo = es_activo
