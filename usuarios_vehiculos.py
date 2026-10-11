import archivos

TIPOS_VALIDOS = ("carro", "moto", "camion", "otro")

def registrar_usuario(nombre, telefono):
    usuarios = archivos.leer("usuarios")
    usuario = {
        "id_usuario": archivos.siguiente_id(usuarios, "id_usuario"),
        "nombre": nombre.strip(),
        "telefono": telefono.strip(),
    }
    usuarios.append(usuario)
    archivos.escribir("usuarios", usuarios)
    return usuario

def buscar_usuario(id_usuario):
    for usuario in archivos.leer("usuarios"):
        if usuario["id_usuario"] == str(id_usuario):
            return usuario
    return None

def registrar_vehiculo(id_usuario, placa, tipo):
    if buscar_usuario(id_usuario) is None:
        raise ValueError("El usuario no existe.")

    tipo = tipo.lower().strip()
    if tipo not in TIPOS_VALIDOS:
        raise ValueError("Tipo de vehiculo no valido.")

    placa = placa.upper().replace(" ", "")
    vehiculos = archivos.leer("vehiculos")

    if any(v["placa"] == placa for v in vehiculos):
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
    for vehiculo in archivos.leer("vehiculos"):
        if vehiculo["placa"] == placa:
            return vehiculo
    return None
