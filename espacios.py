import archivos


def listar_espacios():
    return archivos.leer("espacios")


def buscar_espacio(codigo):
    codigo = codigo.upper().strip()
    espacios = listar_espacios()

    for espacio in espacios:
        if espacio["codigo"] == codigo:
            return espacio

    return None


def obtener_espacio_libre(tipo):
    espacios = listar_espacios()

    for espacio in espacios:
        if espacio["tipo"] == tipo and espacio["estado"] == "libre":
            return espacio

    return None


def cambiar_estado(codigo, nuevo_estado):
    if nuevo_estado not in ("libre", "ocupado"):
        raise ValueError("Estado de espacio no valido.")

    espacios = listar_espacios()

    for espacio in espacios:
        if espacio["codigo"] == codigo.upper():
            espacio["estado"] = nuevo_estado
            archivos.escribir("espacios", espacios)
            return espacio

    raise ValueError("El espacio no existe.")
