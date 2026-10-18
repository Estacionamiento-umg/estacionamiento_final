import math

# Tarifa base para las primeras 2 horas y precio por cada hora extra iniciada.
TARIFAS = {
    "carro": {"base": 20.0, "hora_extra": 5.0},
    "moto": {"base": 10.0, "hora_extra": 3.0},
    "camion": {"base": 35.0, "hora_extra": 10.0},
    "otro": {"base": 15.0, "hora_extra": 4.0},
}

MINUTOS_INCLUIDOS = 120


def calcular_cobro(tipo, minutos):
    if tipo not in TARIFAS:
        raise ValueError("Tipo de vehiculo no valido.")

    if minutos < 0:
        raise ValueError("Los minutos no pueden ser negativos.")

    tarifa = TARIFAS[tipo]
    total = tarifa["base"]

    if minutos > MINUTOS_INCLUIDOS:
        minutos_extra = minutos - MINUTOS_INCLUIDOS
        horas_extra = math.ceil(minutos_extra / 60)
        total = total + (horas_extra * tarifa["hora_extra"])

    return round(total, 2)


def detalle_cobro(tipo, minutos):
    return {
        "tipo": tipo,
        "minutos": minutos,
        "base": TARIFAS[tipo]["base"],
        "hora_extra": TARIFAS[tipo]["hora_extra"],
        "total": calcular_cobro(tipo, minutos),
    }
