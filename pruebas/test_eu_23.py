from pruebas.apoyo import DatosTemporales
from usuarios_vehiculos import registrar_usuario, registrar_vehiculo, buscar_vehiculo

class TestEU23(DatosTemporales):
    def test_usuario_y_vehiculo(self):
        usuario = registrar_usuario("Noe", "5555-0000")
        vehiculo = registrar_vehiculo(usuario["id_usuario"], "P123ABC", "carro")
        self.assertEqual(buscar_vehiculo("P123ABC")["placa"], vehiculo["placa"])
