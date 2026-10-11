# Estacionamiento Final - Grupo 4

Version simplificada del sistema para que el equipo pueda entender y explicar el codigo.

## Integrantes y EU

- Ermi: EU-25 Reservas, EU-27 Tarifas, EU-29 Reportes
- Nicolas: EU-24 Espacios, EU-26 Ingresos, EU-30 Pruebas
- Noe: EU-23 Usuarios y vehiculos, EU-28 Salida y pago

## Ejecutar el programa

```powershell
python main.py
```

## Ejecutar todas las pruebas

```powershell
python -m unittest discover pruebas -v
```

## C++

El archivo `motor_tarifas.cpp` contiene el mismo calculo basico de tarifas en C++.

En Windows con g++:

```powershell
g++ motor_tarifas.cpp -o motor_tarifas.exe
.\motor_tarifas.exe carro 121
```

El resultado esperado es `25`.
