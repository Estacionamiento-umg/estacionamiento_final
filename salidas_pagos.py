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
    movimiento = None

    for item in movimientos:
        if item["placa"] == vehiculo["placa"] and item["salida"] == "":
            movimiento = item
            break

    if movimiento is None:
        raise ValueError("El vehiculo no tiene un ingreso activo.")

    if fecha_hora is None:
        fecha_hora = datetime.now().strftime(FORMATO)

    entrada = datetime.strptime(movimiento["entrada"], FORMATO)
    salida = datetime.strptime(fecha_hora, FORMATO)

    if salida < entrada:
        raise ValueError("La salida no puede ser anterior al ingreso.")

    minutos = max(1, int((salida - entrada).total_seconds() / 60))
    total = calcular_cobro(vehiculo["tipo"], minutos)

    movimiento["salida"] = fecha_hora
    movimiento["total"] = str(total)
    archivos.escribir("movimientos", movimientos)
    cambiar_estado(movimiento["espacio"], "libre")

    pagos = archivos.leer("pagos")
    pago = {
        "id_pago": archivos.siguiente_id(pagos, "id_pago"),
        "id_movimiento": movimiento["id_movimiento"],
        "placa": vehiculo["placa"],
        "monto": str(total),
        "fecha": fecha_hora,
    }
    pagos.append(pago)
    archivos.escribir("pagos", pagos)

    return {
        "placa": vehiculo["placa"],
        "espacio": movimiento["espacio"],
        "minutos": minutos,
        "total": total,
    }
