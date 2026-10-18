from pruebas.apoyo import DatosTemporales
from usuarios_vehiculos import registrar_usuario, registrar_vehiculo
from ingresos import registrar_ingreso
from salidas_pagos import registrar_salida
from espacios import buscar_espacio
from reportes import reporte_por_fecha


class TestIntegracion(DatosTemporales):
    def test_flujo_completo_vehiculo(self):
        # 1. Registrar usuario y vehiculo.
        usuario = registrar_usuario("Prueba", "5555-1111")
        registrar_vehiculo(usuario["id_usuario"], "P100AAA", "carro")

        # 2. Registrar ingreso. El primer espacio de carro debe ser A01.
        ingreso = registrar_ingreso("P100AAA", "2031-05-10 08:00")
        self.assertEqual(ingreso["espacio"], "A01")
        self.assertEqual(buscar_espacio("A01")["estado"], "ocupado")

        # 3. Salir despues de 121 minutos. Debe cobrar una hora extra.
        salida = registrar_salida("P100AAA", "2031-05-10 10:01")
        self.assertEqual(salida["total"], 25.0)
        self.assertEqual(buscar_espacio("A01")["estado"], "libre")

        # 4. Revisar que el reporte incluya el movimiento y el pago.
        reporte = reporte_por_fecha("2031-05-10")
        self.assertEqual(reporte["cantidad_entradas"], 1)
        self.assertEqual(reporte["cantidad_pagos"], 1)
        self.assertEqual(reporte["ingresos"], 25.0)
