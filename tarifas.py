import math

TARIFAS = {
    "carro":  {"base": 20.0, "horas_incluidas": 2, "hora_extra": 5.0},
    "moto":   {"base": 10.0, "horas_incluidas": 2, "hora_extra": 3.0},
    "camion": {"base": 35.0, "horas_incluidas": 2, "hora_extra": 10.0},
    "otro":   {"base": 15.0, "horas_incluidas": 2, "hora_extra": 4.0},
}

def calcular_cobro(tipo, minutos):
    if tipo not in TARIFAS:
        raise ValueError("Tipo de vehiculo no valido.")
    if minutos < 0:
        raise ValueError("Los minutos no pueden ser negativos.")

    tarifa = TARIFAS[tipo]
    horas = minutos / 60
    total = tarifa["base"]

    if horas > tarifa["horas_incluidas"]:
        horas_extra = math.ceil(horas - tarifa["horas_incluidas"])
        total += horas_extra * tarifa["hora_extra"]

    return round(total, 2)

def detalle_cobro(tipo, minutos):
    tarifa = TARIFAS[tipo]
    return {
        "tipo": tipo,
        "minutos": minutos,
        "base": tarifa["base"],
        "horas_incluidas": tarifa["horas_incluidas"],
        "hora_extra": tarifa["hora_extra"],
        "total": calcular_cobro(tipo, minutos),
    }
