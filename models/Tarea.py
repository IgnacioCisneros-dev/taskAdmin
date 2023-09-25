import db
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship


class Tarea(db.Base):

    __tablename__ = 'tareas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    titulo = Column(String(50))
    descripcion = Column(String(255))
    fecha_creacion = Column(Date)
    comentarios = Column(String(255))
    estado = Column(String(15))
    fecha_termino = Column(Date)
    status = Column(Boolean)

    # Se hace la relacion con la tabla de usuarios.

    usuario = relationship("Usuario", back_populates="tareas")

    def __init__(self, id, usuario_id, titulo, descripcion, fecha_creacion, comentarios, estado, fecha_termino, status):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.comentarios = comentarios
        self.estado = estado
        self.fecha_termino = fecha_termino
        self.status = status
