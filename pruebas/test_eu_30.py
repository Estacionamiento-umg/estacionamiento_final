from pruebas.apoyo import DatosTemporales
from tarifas import calcular_cobro

class TestEU30(DatosTemporales):
    def test_error_minutos_negativos(self):
        with self.assertRaises(ValueError):
            calcular_cobro("carro", -1)
