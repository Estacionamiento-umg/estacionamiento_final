import tempfile
from pathlib import Path
import unittest
import archivos

class DatosTemporales(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        archivos.DATA_DIR = Path(self.temp.name)
        archivos.inicializar_datos()

    def tearDown(self):
        self.temp.cleanup()
