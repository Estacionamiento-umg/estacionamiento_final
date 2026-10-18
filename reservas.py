from datetime import datetime
import archivos
from usuarios_vehiculos import buscar_usuario, buscar_vehiculo
from espacios import buscar_espacio

FORMATO = "%Y-%m-%d %H:%M"


def convertir_fecha(texto):
    try:
        return datetime.strptime(texto, FORMATO)
    except ValueError:
        raise ValueError("Use el formato de fecha AAAA-MM-DD HH:MM.")


def hay_traslape(codigo_espacio, inicio, fin):
    reservas = archivos.leer("reservas")

    for reserva in reservas:
        if reserva["espacio"] == codigo_espacio and reserva["estado"] == "confirmada":
            inicio_existente = convertir_fecha(reserva["inicio"])
            fin_existente = convertir_fecha(reserva["fin"])

            # Hay choque si los dos horarios se cruzan.
            if inicio < fin_existente and fin > inicio_existente:
                return True

    return False


def crear_reserva(id_usuario, placa, espacio, inicio, fin):
    if buscar_usuario(id_usuario) is None:
        raise ValueError("El usuario no existe.")

    vehiculo = buscar_vehiculo(placa)

    if vehiculo is None:
        raise ValueError("El vehiculo no existe.")

    if vehiculo["id_usuario"] != str(id_usuario):
        raise ValueError("El vehiculo no corresponde al usuario.")

    espacio_info = buscar_espacio(espacio)

    if espacio_info is None:
        raise ValueError("El espacio no existe.")

    if espacio_info["tipo"] != vehiculo["tipo"]:
        raise ValueError("El espacio no corresponde al tipo de vehiculo.")

    inicio_dt = convertir_fecha(inicio)
    fin_dt = convertir_fecha(fin)

    if inicio_dt >= fin_dt:
        raise ValueError("La fecha inicial debe ser anterior a la final.")

    if hay_traslape(espacio_info["codigo"], inicio_dt, fin_dt):
        raise ValueError("Ya existe otra reserva en ese horario.")

    reservas = archivos.leer("reservas")

    reserva = {
        "id_reserva": archivos.siguiente_id(reservas, "id_reserva"),
        "id_usuario": str(id_usuario),
        "placa": placa.upper().replace(" ", ""),
        "espacio": espacio_info["codigo"],
        "inicio": inicio,
        "fin": fin,
        "estado": "confirmada",
    }

    reservas.append(reserva)
    archivos.escribir("reservas", reservas)
    return reserva


def cancelar_reserva(id_reserva):
    reservas = archivos.leer("reservas")

    for reserva in reservas:
        if reserva["id_reserva"] == str(id_reserva):
            reserva["estado"] = "cancelada"
            archivos.escribir("reservas", reservas)
            return reserva

    raise ValueError("La reserva no existe.")
