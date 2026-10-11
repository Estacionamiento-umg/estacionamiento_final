from pathlib import Path
import csv

DATA_DIR = Path(__file__).parent / "data"

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
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for nombre, campos in CAMPOS.items():
        ruta = DATA_DIR / f"{nombre}.csv"
        if not ruta.exists():
            datos = ESPACIOS_INICIALES if nombre == "espacios" else []
            escribir(nombre, datos)

def leer(nombre):
    inicializar_datos()
    ruta = DATA_DIR / f"{nombre}.csv"
    with ruta.open("r", encoding="utf-8-sig", newline="") as archivo:
        return list(csv.DictReader(archivo))

def escribir(nombre, filas):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    ruta = DATA_DIR / f"{nombre}.csv"
    with ruta.open("w", encoding="utf-8-sig", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=CAMPOS[nombre])
        writer.writeheader()
        writer.writerows(filas)

def siguiente_id(filas, campo):
    if not filas:
        return "1"
    return str(max(int(fila[campo]) for fila in filas) + 1)
