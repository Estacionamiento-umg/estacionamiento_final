# Guia de defensa - Sprint 2

## Explicacion general

"Esta es una primera version funcional del sistema de estacionamiento. La dividimos en modulos para que cada archivo tenga una responsabilidad. Usamos Python para la logica, CSV para guardar datos y Tkinter para una interfaz inicial."

## Preguntas basicas

**¿Por que varios archivos?**  
Para separar responsabilidades y poder repartir el trabajo entre los integrantes.

**¿Que hace archivos.py?**  
Lee y escribe los CSV. Evita repetir el mismo codigo de archivos en todos los modulos.

**¿Que es un diccionario?**  
Es una estructura de clave y valor. Por ejemplo una placa, el ID del dueño y el tipo de vehiculo.

**¿Que hace un for?**  
Recorre una lista. Lo usamos para buscar usuarios, vehiculos, espacios o movimientos.

**¿Que hace un if?**  
Toma una decision segun una condicion, por ejemplo si un espacio esta libre.

**¿Que hace try/except?**  
Permite controlar un error y mostrar un mensaje entendible en lugar de cerrar el programa.

**¿Por que CSV?**  
Porque es una forma sencilla de almacenar datos para este avance sin implementar todavia una base de datos.

**¿Que hace la interfaz?**  
Recibe datos del usuario y llama a las funciones de los modulos. La logica no esta repetida dentro de la interfaz.

**¿Que son las pruebas unitarias?**  
Comprueban una funcion especifica. La prueba de integracion comprueba varias funciones trabajando juntas.

## Ermi

Debe explicar principalmente:
- `reservas.py`: valida usuario, vehiculo, espacio y horarios.
- `tarifas.py`: tarifa base y horas extra.
- `reportes.py`: cuenta entradas, pagos e ingresos por fecha.
- `interfaz.py`: cada boton llama a una funcion del sistema.

## Nicolas

Debe explicar principalmente:
- `espacios.py`: busca espacios libres y cambia libre/ocupado.
- `ingresos.py`: valida la placa, evita doble ingreso y asigna un espacio.
- Integracion en `develop`: revisa que los modulos unidos sigan funcionando.

## Noe

Debe explicar principalmente:
- `usuarios_vehiculos.py`: registra usuarios y placas y evita duplicados.
- `salidas_pagos.py`: calcula tiempo, cobra, guarda pago y libera espacio.
- `pruebas/test_integracion.py`: prueba el flujo registro -> ingreso -> salida -> reporte.
