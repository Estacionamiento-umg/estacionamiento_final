from pruebas.apoyo import DatosTemporales
from tarifas import calcular_cobro

class TestEU27(DatosTemporales):
    def test_tarifas(self):
        self.assertEqual(calcular_cobro("carro", 120), 20.0)
        self.assertEqual(calcular_cobro("carro", 121), 25.0)
