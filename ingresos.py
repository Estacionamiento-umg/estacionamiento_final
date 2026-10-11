from datetime import datetime
import archivos
from usuarios_vehiculos import buscar_vehiculo
from espacios import obtener_espacio_libre, cambiar_estado

FORMATO = "%Y-%m-%d %H:%M"

def registrar_ingreso(placa, fecha_hora=None):
    vehiculo = buscar_vehiculo(placa)
    if vehiculo is None:
        raise ValueError("El vehiculo no esta registrado.")

    movimientos = archivos.leer("movimientos")
    for movimiento in movimientos:
        if movimiento["placa"] == vehiculo["placa"] and movimiento["salida"] == "":
            raise ValueError("El vehiculo ya esta dentro.")

    espacio = obtener_espacio_libre(vehiculo["tipo"])
    if espacio is None:
        raise ValueError("No hay espacios disponibles.")

    if fecha_hora is None:
        fecha_hora = datetime.now().strftime(FORMATO)

    movimiento = {
        "id_movimiento": archivos.siguiente_id(movimientos, "id_movimiento"),
        "placa": vehiculo["placa"],
        "espacio": espacio["codigo"],
        "entrada": fecha_hora,
        "salida": "",
        "total": "",
    }
    movimientos.append(movimiento)
    archivos.escribir("movimientos", movimientos)
    cambiar_estado(espacio["codigo"], "ocupado")
    return movimiento
