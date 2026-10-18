from pathlib import Path
import csv

# Carpeta donde se guardan los archivos CSV.
DATA_DIR = Path(__file__).parent / "data"

# Columnas que tiene cada archivo.
CAMPOS = {
    "usuarios": ["id_usuario", "nombre", "telefono"],
    "vehiculos": ["placa", "id_usuario", "tipo"],
    "espacios": ["codigo", "tipo", "estado"],
    "reservas": ["id_reserva", "id_usuario", "placa", "espacio", "inicio", "fin", "estado"],
    "movimientos": ["id_movimiento", "placa", "espacio", "entrada", "salida", "total"],
    "pagos": ["id_pago", "id_movimiento", "placa", "monto", "fecha"],
}

ESPACIOS_INICIALES = [
    {"codigo": "A01", "tipo": "carro", "estado": "libre"},
    {"codigo": "A02", "tipo": "carro", "estado": "libre"},
    {"codigo": "M01", "tipo": "moto", "estado": "libre"},
    {"codigo": "M02", "tipo": "moto", "estado": "libre"},
    {"codigo": "C01", "tipo": "camion", "estado": "libre"},
    {"codigo": "O01", "tipo": "otro", "estado": "libre"},
]


def inicializar_datos():
    """Crea los CSV la primera vez que se ejecuta el programa."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    for nombre in CAMPOS:
        ruta = DATA_DIR / (nombre + ".csv")

        if not ruta.exists():
            if nombre == "espacios":
                escribir(nombre, ESPACIOS_INICIALES)
            else:
                escribir(nombre, [])


def leer(nombre):
    """Lee un CSV y devuelve sus filas como una lista de diccionarios."""
    inicializar_datos()
    ruta = DATA_DIR / (nombre + ".csv")

    with ruta.open("r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)


def escribir(nombre, filas):
    """Guarda una lista de diccionarios dentro de un CSV."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    ruta = DATA_DIR / (nombre + ".csv")

    with ruta.open("w", encoding="utf-8-sig", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS[nombre])
        escritor.writeheader()
        escritor.writerows(filas)


def siguiente_id(filas, campo):
    """Obtiene el siguiente numero disponible para un ID."""
    mayor = 0

    for fila in filas:
        numero = int(fila[campo])
        if numero > mayor:
            mayor = numero

    return str(mayor + 1)
