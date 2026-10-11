import archivos

def vehiculos_dentro():
    return [m for m in archivos.leer("movimientos") if m["salida"] == ""]

def reporte_por_fecha(fecha):
    movimientos = [
        m for m in archivos.leer("movimientos")
        if m["entrada"].startswith(fecha)
    ]

    pagos = [
        p for p in archivos.leer("pagos")
        if p["fecha"].startswith(fecha)
    ]

    ingresos = sum(float(p["monto"]) for p in pagos)

    return {
        "fecha": fecha,
        "cantidad_entradas": len(movimientos),
        "cantidad_pagos": len(pagos),
        "ingresos": round(ingresos, 2),
    }
