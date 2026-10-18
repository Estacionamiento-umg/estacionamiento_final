import archivos

TIPOS_VALIDOS = ("carro", "moto", "camion", "otro")


def registrar_usuario(nombre, telefono):
    nombre = nombre.strip()
    telefono = telefono.strip()

    if nombre == "":
        raise ValueError("Debe escribir el nombre del usuario.")

    if telefono == "":
        raise ValueError("Debe escribir un telefono.")

    usuarios = archivos.leer("usuarios")

    usuario = {
        "id_usuario": archivos.siguiente_id(usuarios, "id_usuario"),
        "nombre": nombre,
        "telefono": telefono,
    }

    usuarios.append(usuario)
    archivos.escribir("usuarios", usuarios)
    return usuario


def buscar_usuario(id_usuario):
    usuarios = archivos.leer("usuarios")

    for usuario in usuarios:
        if usuario["id_usuario"] == str(id_usuario):
            return usuario

    return None


def registrar_vehiculo(id_usuario, placa, tipo):
    if buscar_usuario(id_usuario) is None:
        raise ValueError("El usuario no existe.")

    placa = placa.upper().replace(" ", "")
    tipo = tipo.lower().strip()

    if placa == "":
        raise ValueError("Debe escribir una placa.")

    if tipo not in TIPOS_VALIDOS:
        raise ValueError("Tipo de vehiculo no valido.")

    vehiculos = archivos.leer("vehiculos")

    # Revisamos una por una las placas para evitar duplicados.
    for vehiculo in vehiculos:
        if vehiculo["placa"] == placa:
            raise ValueError("La placa ya esta registrada.")

    vehiculo = {
        "placa": placa,
        "id_usuario": str(id_usuario),
        "tipo": tipo,
    }

    vehiculos.append(vehiculo)
    archivos.escribir("vehiculos", vehiculos)
    return vehiculo


def buscar_vehiculo(placa):
    placa = placa.upper().replace(" ", "")
    vehiculos = archivos.leer("vehiculos")

    for vehiculo in vehiculos:
        if vehiculo["placa"] == placa:
            return vehiculo

    return None
