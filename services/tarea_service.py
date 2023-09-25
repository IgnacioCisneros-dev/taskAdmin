import db
from models.models_bd import Tarea as tarea_db
from models.Tarea_model import Tarea as tarea_model
from sqlalchemy.exc import SQLAlchemyError
from services.usuario_service import buscar_usuario_por_id
from models.Usuario_model import Usuario as usuario_model
from fastapi import HTTPException
from models.models_bd import Tarea


def buscar_tareas():
    """Funcion que consulta todas las tareas de la base de datos
       que esten activas.

    Returns:
        Tareas: Retorna una lista con las tareas existentes
    """

    try:
        tareas = db.session.query(tarea_db).filter_by(status=True).all()
        if tareas:
            return tareas
        else:
            return 'Sin tareas para mostrar.'
    except SQLAlchemyError as e:
        print(
            f'Ocurrio un error al consultar las tareas existentes en base de datos. {e}')
    finally:
        db.session.close()


def buscar_tarea_por_id(tarea_id: int):
    """Funcion que busca una tarea especifica por el id en base de datos

    Args:
        tarea_id (int): filtro (id) por el cual se busca la tarea

    Returns:
        Tarea: Retorna la tarea en caso de estar en BD
    """
    try:
        tarea = db.session.query(tarea_db).filter_by(id=tarea_id).first()
        if tarea is not None:
            return tarea
        else:
            return print('No se encontro la tarea con el identificador proporsionado.')
    except SQLAlchemyError as e:
        print(f'Ocurrio un error al buscar la tarea con el id {tarea_id}, {e}')
    finally:
        db.session.close()


def agregar_tarea(tarea: tarea_model, usuario_id: int):
    try:
        usuario = obtener_usuario_por_id(usuario_id)
        if usuario is not None:

            nueva_tarea = Tarea(**tarea.model_dump(), usuario_id=usuario_id)

            db.session.add(nueva_tarea)
            db.session.commit()

            tarea_dict = nueva_tarea.__dict__
            # Eliminar '_sa_instance_state' del diccionario
            tarea_dict.pop('_sa_instance_state', None)

            return tarea_dict
           # return tarea
        else:
            raise HTTPException(
                status_code=404, detail='No se pudo obtener el usuario para asignar la tarea.')
    except SQLAlchemyError as e:
        return print(f'Ocurrio un error al intentar persistir en base de datos, {e}')
    finally:
        db.session.close()


def obtener_usuario_por_id(usuario_id: int):
    usuario = buscar_usuario_por_id(usuario_id)
    if usuario:
        return usuario
    else:
        return None


def editar_tarea(tarea: tarea_model, tarea_id: int):
    """Funcion que actualiza un tarea ya existente en base de datos

    Args:
        tarea (tarea_model): Propiedades de la tarea a actualizar
        tarea_id (int): id de la tarea que se va a actualizar

    Raises:
        HTTPException: Exception

    Returns:
        String: Mensaje que indica que la actualizacion fue correcta o se produjo algun error
    """
    try:
        tarea_a_editar = db.session.query(Tarea).filter_by(id=tarea_id).first()

        if tarea_a_editar is None:
            raise HTTPException(
                status_code=404, detail='No se encontro la tarea para poder ser editada.')

        tarea_a_editar.titulo = tarea.titulo
        tarea_a_editar.descripcion = tarea.descripcion
        tarea_a_editar.fecha_creacion = tarea.fecha_creacion
        tarea_a_editar.comentarios = tarea.comentarios
        tarea_a_editar.estado = tarea.estado
        tarea_a_editar.fecha_termino = tarea.fecha_termino
        tarea_a_editar.status = tarea.status

        # Se persisten los cambios en base de datos
        db.session.commit()

        respuesta = 'Tarea actualizada exitosamente.'
        return respuesta

    except SQLAlchemyError as e:
        return print(f'Ocurrio un error al tratar de actualizar la tarea, {e}')

    finally:
        db.session.close()


def borrar_tarea_por_id(tarea_id: int):
    """Funcion que actualiza el status de una tarea a falso para hacer una baja logica

    Args:
        tarea_id (int): tarea_id por la cual se hace la busqueda

    Raises:
        HTTPException: _description_

    Returns:
        String: Mensaje en donde indica que la tarea fue eliminada.
    """
    try:
        tarea = db.session.query(Tarea).filter_by(id=tarea_id).first()

        if tarea is None:
            raise HTTPException(
                status_code=404, detail='No se encontro la tarea para poder ser eliminada.')

        tarea.status = False

        db.session.commit()

        return 'Tarea eliminada exitosamente.'

    except SQLAlchemyError as e:
        return f'Ocurrio un error al intentar eliminar la tarea, {e}'
    finally:
        db.session.close()
