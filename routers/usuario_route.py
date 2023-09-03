from fastapi import APIRouter
from services.usuario_service import buscar_usuarios, persistir_usuario, buscar_usuario_por_id
from models.Usuario_model import Usuario

router_usuarios = APIRouter(prefix='/usuarios',
                            tags=["Usuario."])


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
