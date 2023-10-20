from bcrypt import hashpw, gensalt

# Requieres: https://pypi.org/project/bcrypt/
# To check a password do:
#   checkpw(password.encode(), hashpw)

def proteger_passwd(clave):
    """Devuelve una contraseña salteada con bcrytp."""

    return hashpw(clave.encode(), gensalt())
