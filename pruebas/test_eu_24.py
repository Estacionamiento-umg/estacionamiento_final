from pruebas.apoyo import DatosTemporales
from espacios import obtener_espacio_libre, cambiar_estado, buscar_espacio

class TestEU24(DatosTemporales):
    def test_espacios(self):
        espacio = obtener_espacio_libre("carro")
        self.assertIsNotNone(espacio)
        cambiar_estado(espacio["codigo"], "ocupado")
        self.assertEqual(buscar_espacio(espacio["codigo"])["estado"], "ocupado")
