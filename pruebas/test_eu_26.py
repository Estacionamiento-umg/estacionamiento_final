from pruebas.apoyo import DatosTemporales
from usuarios_vehiculos import registrar_usuario, registrar_vehiculo
from ingresos import registrar_ingreso

class TestEU26(DatosTemporales):
    def test_ingreso(self):
        usuario = registrar_usuario("Nico", "5555-2222")
        registrar_vehiculo(usuario["id_usuario"], "M123BBB", "moto")
        movimiento = registrar_ingreso("M123BBB", "2031-02-01 08:00")
        self.assertEqual(movimiento["espacio"], "M01")
