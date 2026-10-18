from pruebas.apoyo import DatosTemporales
from usuarios_vehiculos import registrar_usuario, registrar_vehiculo
from reservas import crear_reserva, cancelar_reserva

class TestEU25(DatosTemporales):
    def test_reserva(self):
        usuario = registrar_usuario("Ermi", "5555-1111")
        registrar_vehiculo(usuario["id_usuario"], "P111AAA", "carro")
        reserva = crear_reserva(
            usuario["id_usuario"], "P111AAA", "A01",
            "2031-02-01 09:00", "2031-02-01 10:00"
        )
        cancelada = cancelar_reserva(reserva["id_reserva"])
        self.assertEqual(cancelada["estado"], "cancelada")
