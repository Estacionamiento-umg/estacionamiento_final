from pruebas.apoyo import DatosTemporales
from reportes import reporte_por_fecha

class TestEU29(DatosTemporales):
    def test_reporte_sin_movimientos(self):
        reporte = reporte_por_fecha("2099-01-01")
        self.assertEqual(reporte["cantidad_entradas"], 0)
        self.assertEqual(reporte["cantidad_pagos"], 0)
        self.assertEqual(reporte["ingresos"], 0)
