from fastapi import APIRouter
from services.tarea_service import buscar_tareas, buscar_tarea_por_id, agregar_tarea, editar_tarea
from models.Tarea_model import Tarea as tarea_model

router_tareas = APIRouter(prefix='/tareas',
                          tags=["Tareas."])


@router_tareas.get('/obtener',
                   summary='Muestra las tareas existentes')
def obtener_tareas():
    try:
        return buscar_tareas()
    except Exception as e:
        print(f'Ocurrio un error inesperado, {e}')


@router_tareas.get('/obtener/{tarea_id}',
                   summary='Obtiene una tarea por el id.')
def obtener_tarea_por_id(tarea_id: int):
    try:
        return buscar_tarea_por_id(tarea_id=tarea_id)
    except Exception as e:
        print(f'Ocurio un error al buscar la tarea por el id {tarea_id}, {e}')


@router_tareas.post('/agregar_tarea/{usuario_id}',
                    summary='agrega nueva tarea y se guarda en base de datos.')
def guardar_tarea(tarea: tarea_model, usuario_id: int):
    try:
        agregar_tarea(tarea, usuario_id)
    except Exception as e:
        return print(f'Ocurrio un error desconocido, {e}')


@router_tareas.put('/actualizar_tarea/{tarea_id}',
                   summary="Actualiza una tarea.")
def actualizar_tarea(tarea: tarea_model, tarea_id: int):
    try:
        return editar_tarea(tarea, tarea_id)
    except Exception as e:
        return f'Ocurrio un error desconocido, {e}'


@router_tareas.put('/eliminar/{tarea_id}',
                     summary='Hace una eliminacion logica en base de datos de una tarea.')
def eliminar_tarea(tarea_id: int):
    try:
        return 'Falta la llamada al servicio para la eliminacion.'
    except Exception as e:
        return e