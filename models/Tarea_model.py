from pydantic import BaseModel


class Tarea(BaseModel):
    #usuario_id: int
    titulo: str
    descripcion: str
    fecha_creacion: str
    comentarios: str
    estado: str
    fecha_termino: str
    status: bool
