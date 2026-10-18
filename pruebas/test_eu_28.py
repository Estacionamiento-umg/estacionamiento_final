from pruebas.apoyo import DatosTemporales
from usuarios_vehiculos import registrar_usuario, registrar_vehiculo
from ingresos import registrar_ingreso
from salidas_pagos import registrar_salida

class TestEU28(DatosTemporales):
    def test_salida_y_pago(self):
        usuario = registrar_usuario("Noe", "5555-3333")
        registrar_vehiculo(usuario["id_usuario"], "P555CCC", "carro")
        registrar_ingreso("P555CCC", "2031-02-01 08:00")
        salida = registrar_salida("P555CCC", "2031-02-01 10:01")
        self.assertEqual(salida["total"], 25.0)
