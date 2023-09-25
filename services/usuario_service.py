import db
#from models.Usuario import Usuario as usuario_bd
from models.Usuario_model import Usuario as usuario_model
from models.models_bd import Usuario as usuario_bd


def buscar_usuarios():
    usuarios = db.session.query(usuario_bd).filter_by(es_activo=True).all()
    if usuarios:
        return usuarios
    else:
        return 'Sin usuarios para mostrar.'


def persistir_usuario(usuario: usuario_model):
    # Se crea un instancia de usuario para crear un nuevo
    # registro en base de datos.
    usuario_a_guardar = usuario_bd(id=usuario.id,
                                   nombre=usuario.nombre,
                                   correo=usuario.correo,
                                   contrasena=usuario.contrasena,
                                   es_activo=True)

    db.session.add(usuario_a_guardar)
    db.session.commit()
    db.session.close()

    return 'Usuario guardado correctamente.'


def buscar_usuario_por_id(usuario_id: int):
    usuario = db.session.query(usuario_bd).filter_by(id=usuario_id).first()
    if usuario:
        return usuario
    else:
        return 'No se encontro el usuario.'


def editar_usuario(usuario_edit: usuario_model, usuario_id: int):
    usuario = db.session.query(usuario_bd).filter_by(id=usuario_id).first()
    if usuario:
        # Se recupera el objeto de base de datos y se editan sus
        # propiedades para solo actualizar en base de datos

        usuario.id = usuario_edit.id
        usuario.nombre = usuario_edit.nombre
        usuario.correo = usuario_edit.correo
        usuario.contrasena = usuario_edit.contrasena

        db.session.commit()
        db.session.close()
        return 'Usuario actualizado exitosamente.'
    else:
        return 'No se encontro el usuario para actualizar.'


def eliminar_usuario_bd(usuario_id: int):
    usuario = db.session.query(usuario_bd).filter_by(
        id=usuario_id, es_activo=True).first()
    if usuario:

        usuario.id = usuario.id,
        usuario.nombre = usuario.nombre,
        usuario.correo = usuario.correo,
        usuario.contrasena = usuario.contrasena,
        usuario.es_activo = False

        db.session.commit()
        db.session.close()
        return 'Usuario eliminado exitosamente'
    else:
        return 'Usuario no encontrado.'
