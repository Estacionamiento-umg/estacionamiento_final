import archivos

def listar_espacios():
    return archivos.leer("espacios")

def buscar_espacio(codigo):
    codigo = codigo.upper()
    for espacio in listar_espacios():
        if espacio["codigo"] == codigo:
            return espacio
    return None

def obtener_espacio_libre(tipo):
    for espacio in listar_espacios():
        if espacio["tipo"] == tipo and espacio["estado"] == "libre":
            return espacio
    return None

def cambiar_estado(codigo, nuevo_estado):
    espacios = listar_espacios()
    for espacio in espacios:
        if espacio["codigo"] == codigo.upper():
            espacio["estado"] = nuevo_estado
            archivos.escribir("espacios", espacios)
            return espacio
    raise ValueError("El espacio no existe.")
