from fastapi import APIRouter
from services.usuario_service import buscar_usuarios, persistir_usuario, buscar_usuario_por_id, editar_usuario, eliminar_usuario_bd
from models.Usuario_model import Usuario

router_usuarios = APIRouter(prefix='/usuarios',
                            tags=["Usuarios."])


@router_usuarios.get('/obtener',
                     summary='Informacion de usuarios.')
def obtener_usuarios():
    return buscar_usuarios()


@router_usuarios.get('/obtener/{usuario_id}',
                     summary='Obtiene usuario por el id.')
def obtener_usuario_por_id(usuario_id: int):
    return buscar_usuario_por_id(usuario_id)


@router_usuarios.post('/guardar',
                      summary='Guardar nuevo usuario.')
def guardar_usuario(usuario: Usuario):
    return persistir_usuario(usuario)


@router_usuarios.put('/actualizar/{usuario_id}',
                     summary='Actualiza un usuario.')
def actualizar_usuario(usuario: Usuario, usuario_id: int):
    return editar_usuario(usuario, usuario_id)


@router_usuarios.put('/eliminar/{usuario_id}',
                     summary='Realiza una baja logica del usuario en base de datos.')
def eliminar_usuario(usuario_id: int):
    return eliminar_usuario_bd


