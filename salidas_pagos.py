from datetime import datetime
import archivos
from usuarios_vehiculos import buscar_vehiculo
from espacios import cambiar_estado
from tarifas import calcular_cobro

FORMATO = "%Y-%m-%d %H:%M"


def registrar_salida(placa, fecha_hora=None):
    vehiculo = buscar_vehiculo(placa)

    if vehiculo is None:
        raise ValueError("El vehiculo no esta registrado.")

    movimientos = archivos.leer("movimientos")
    movimiento_activo = None

    for movimiento in movimientos:
        if movimiento["placa"] == vehiculo["placa"] and movimiento["salida"] == "":
            movimiento_activo = movimiento
            break

    if movimiento_activo is None:
        raise ValueError("El vehiculo no tiene un ingreso activo.")

    if fecha_hora is None:
        fecha_hora = datetime.now().strftime(FORMATO)

    try:
        entrada = datetime.strptime(movimiento_activo["entrada"], FORMATO)
        salida = datetime.strptime(fecha_hora, FORMATO)
    except ValueError:
        raise ValueError("Use el formato de fecha AAAA-MM-DD HH:MM.")

    if salida < entrada:
        raise ValueError("La salida no puede ser anterior al ingreso.")

    minutos = int((salida - entrada).total_seconds() / 60)

    if minutos < 1:
        minutos = 1

    total = calcular_cobro(vehiculo["tipo"], minutos)

    movimiento_activo["salida"] = fecha_hora
    movimiento_activo["total"] = str(total)
    archivos.escribir("movimientos", movimientos)

    cambiar_estado(movimiento_activo["espacio"], "libre")

    pagos = archivos.leer("pagos")
    pago = {
        "id_pago": archivos.siguiente_id(pagos, "id_pago"),
        "id_movimiento": movimiento_activo["id_movimiento"],
        "placa": vehiculo["placa"],
        "monto": str(total),
        "fecha": fecha_hora,
    }

    pagos.append(pago)
    archivos.escribir("pagos", pagos)

    return {
        "placa": vehiculo["placa"],
        "espacio": movimiento_activo["espacio"],
        "minutos": minutos,
        "total": total,
    }
