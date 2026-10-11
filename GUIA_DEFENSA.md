# Guia rapida para defender el codigo

## Idea general
El programa guarda la informacion en archivos CSV. Se uso esta forma porque es sencilla para un proyecto universitario y permite practicar lectura y escritura de archivos sin usar una base de datos.

## Preguntas posibles

**¿Que hace main.py?**  
Muestra un menu y llama a las funciones de los otros archivos.

**¿Por que separaron el proyecto en varios archivos?**  
Para que cada archivo tenga una responsabilidad y sea mas facil trabajar en equipo.

**¿Que hace archivos.py?**  
Lee, escribe e inicializa los CSV.

**¿Que es un diccionario?**  
Una estructura con pares clave-valor, por ejemplo `{"placa": "P123ABC", "tipo": "carro"}`.

**¿Que hace un for?**  
Recorre elementos de una lista para buscar usuarios, vehiculos, espacios o reservas.

**¿Que hace un if?**  
Permite tomar decisiones, por ejemplo verificar si un espacio esta libre.

**¿Para que sirve ValueError?**  
Para indicar que un dato no es valido sin que el programa falle de forma confusa.

**¿Como funciona una reserva?**  
Se valida usuario, vehiculo, espacio, fechas y que no exista otra reserva en el mismo horario. Luego se guarda en CSV.

**¿Como se calcula el cobro?**  
Cada tipo de vehiculo tiene una tarifa base que incluye 2 horas. Si se pasa ese tiempo, se cobra una cantidad por cada hora extra iniciada.

**¿Por que hay C++?**  
Porque el proyecto pide combinar Python y C++. `motor_tarifas.cpp` muestra el calculo de tarifas en C++.

**¿Que son las pruebas unitarias?**  
Son pequeños programas que verifican automaticamente que una funcion haga lo esperado.

## Que explica cada integrante

### Ermi
- reservas.py
- tarifas.py
- reportes.py
- test_eu_25.py, test_eu_27.py, test_eu_29.py

### Nicolas
- espacios.py
- ingresos.py
- test_eu_24.py, test_eu_26.py, test_eu_30.py

### Noe
- usuarios_vehiculos.py
- salidas_pagos.py
- test_eu_23.py, test_eu_28.py
