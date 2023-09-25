from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crear una instancia de la clase base declarativa
Base = declarative_base()

# Definir el modelo de la tabla 'usuarios'


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(80))
    correo = Column(String(80))
    contrasena = Column(String(80))
    es_activo = Column(Boolean)

    # Definir la relación con la tabla 'tareas'
    tareas = relationship('Tarea', back_populates='usuario')
    # Definir la relación con la tabla 'lista_tareas'
    listas = relationship('ListaTarea', back_populates='usuario')

# Definir el modelo de la tabla 'tareas'


class Tarea(Base):
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

    # Definir la relación inversa con la tabla 'usuarios'
    usuario = relationship('Usuario', back_populates='tareas')

# Definir el modelo de la tabla 'lista_tareas'


class ListaTarea(Base):
    __tablename__ = 'lista_tareas'

    id = Column(Integer, primary_key=True)
    nombre_tarea = Column(String(50))
    descripcion = Column(String(255))
    fecha_creacion = Column(Date)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    tarea_id = Column(Integer, ForeignKey('tareas.id'))

    # Definir la relación con la tabla 'usuarios'
    usuario = relationship('Usuario', back_populates='listas')
    # Definir la relación con la tabla 'tareas'
    tarea = relationship('Tarea')


