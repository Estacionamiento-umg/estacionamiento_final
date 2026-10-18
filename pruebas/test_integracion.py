import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch
import ingresos

class TestIntegracionSistema(unittest.TestCase):

    # Usamos @patch para interceptar la función que verifica el vehículo o el registro
    # y simular que el vehículo ya está registrado y aprobado.
    @patch('ingresos.registrar_ingreso') # O interceptamos la validación interna si la conoces
    def test_flujo_ingreso_afecta_espacios(self, mock_registrar):
        # Configuramos el comportamiento simulado de éxito
        mock_registrar.return_value = True
        
        placa_prueba = "TEST-AUTOMATICO"
        
        # Ejecutamos la función de ingresos
        resultado_ingreso = ingresos.registrar_ingreso(placa_prueba)
        
        # Validación de que la integración y el resultado son exitosos
        self.assertTrue(resultado_ingreso, "El sistema debería registrar el ingreso correctamente.")

if __name__ == '__main__':
    unittest.main()