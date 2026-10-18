# Sistema de Estacionamiento - Grupo 4

Primera version funcional correspondiente al Sprint 2.

El lenguaje principal del sistema es **Python**. La informacion se guarda temporalmente en archivos CSV y la interfaz grafica se realizo con Tkinter.

## Ejecutar la interfaz

```powershell
python interfaz.py
```

## Ejecutar por consola

```powershell
python main.py
```

## Ejecutar las pruebas

```powershell
python -m unittest discover pruebas -v
```

## Archivos principales

- `archivos.py`: lectura y escritura de CSV.
- `usuarios_vehiculos.py`: registro de usuarios y vehiculos.
- `espacios.py`: consulta y cambio de estado de espacios.
- `reservas.py`: creacion y cancelacion de reservas.
- `ingresos.py`: entrada y asignacion de espacio.
- `tarifas.py`: calculo de cobro.
- `salidas_pagos.py`: salida, liberacion del espacio y pago.
- `reportes.py`: consultas y resumen por fecha.
- `interfaz.py`: ventana sencilla hecha con Tkinter.
- `pruebas/`: pruebas unitarias y una prueba de integracion.

## Reparto de trabajo

- **Ermi:** reservaciones, tarifas, reportes e interfaz.
- **Nicolas:** espacios, ingreso, apoyo en integracion y revision.
- **Noe:** usuarios, vehiculos, salida/pago y pruebas de integracion.

## Sobre C++

`motor_tarifas.cpp` se conserva como un prototipo sencillo del calculo de tarifas. La version funcional presentada en este Sprint trabaja principalmente en Python, lo cual cumple con la indicacion de desarrollar la solucion utilizando C++ o Python.
