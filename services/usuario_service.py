import db
from models.Usuario import Usuario as usario_bd
from models.Usuario_model import Usuario as usuario_model


def buscar_usuarios():
    usuarios = db.session.query(usario_bd).all()
    if usuarios:
        return usuarios
    else:
        return 'Sin usuarios para mostrar.'


def persistir_usuario(usuario: usuario_model):
    usuario_a_guardar = usario_bd(id=usuario.id,
                                nombre=usuario.nombre,
                                correo=usuario.correo,
                                contrasena=usuario.contrasena)

    db.session.add(usuario_a_guardar)
    db.session.commit()
    db.session.close()

    return 'Usuario guardado correctamente.'


def buscar_usuario_por_id(usuario_id: int):
    usuario = db.session.query(usario_bd).filter_by(id=usuario_id).first()
    if usuario:
        return usuario
    else:
        return 'No se encontro el usuario.'
