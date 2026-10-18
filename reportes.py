import archivos


def vehiculos_dentro():
    resultado = []
    movimientos = archivos.leer("movimientos")

    for movimiento in movimientos:
        if movimiento["salida"] == "":
            resultado.append(movimiento)

    return resultado


def reporte_por_fecha(fecha):
    movimientos = archivos.leer("movimientos")
    pagos = archivos.leer("pagos")

    cantidad_entradas = 0
    cantidad_pagos = 0
    ingresos = 0.0

    for movimiento in movimientos:
        if movimiento["entrada"].startswith(fecha):
            cantidad_entradas = cantidad_entradas + 1

    for pago in pagos:
        if pago["fecha"].startswith(fecha):
            cantidad_pagos = cantidad_pagos + 1
            ingresos = ingresos + float(pago["monto"])

    return {
        "fecha": fecha,
        "cantidad_entradas": cantidad_entradas,
        "cantidad_pagos": cantidad_pagos,
        "ingresos": round(ingresos, 2),
    }
