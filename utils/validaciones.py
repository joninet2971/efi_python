from sqlalchemy.orm.exc import NoResultFound

def validarNombre(nombre, model, campo):
    try:
        existe = model.query.filter(campo == nombre).one_or_none()
        if existe:
            return False
        return True
    except NoResultFound:
        return True