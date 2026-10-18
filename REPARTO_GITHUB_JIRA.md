# Reparto para Jira y GitHub

Este reparto permite que los tres integrantes tengan una contribucion real y facil de explicar.

## Ermi - EU-33 Corregir interfaz y mensajes

Rama sugerida:
`feature/eu33-interfaz`

Archivo principal:
`interfaz.py`

Commit sugerido:
`EU-33: simplificar interfaz y mensajes del sistema`

Que explica:
La interfaz usa Tkinter. Cada boton llama a una funcion que ya existe en los modulos.

## Noe - EU-32 Ejecutar pruebas de integracion

Rama sugerida:
`feature/eu32-pruebas-integracion`

Archivos principales:
- `usuarios_vehiculos.py`
- `pruebas/test_integracion.py`

Commit sugerido:
`EU-32: agregar validaciones y prueba de flujo completo`

Que explica:
La prueba registra usuario y vehiculo, hace un ingreso, registra la salida y comprueba el reporte.

## Nicolas - EU-31 Integrar modulos en develop

Rama sugerida:
`feature/eu31-integracion`

Archivos principales:
- `archivos.py`
- `espacios.py`
- `ingresos.py`

Commit sugerido:
`EU-31: ordenar manejo de archivos e integracion de ingreso`

Que explica:
Se reviso que el ingreso use usuarios, vehiculos, espacios y archivos CSV correctamente y que no permita doble ingreso.

## Orden de integracion

1. Cada integrante crea su rama desde `develop`.
2. Cada integrante copia/modifica solamente sus archivos.
3. Ejecuta pruebas.
4. Hace su commit con su propia cuenta.
5. Publica la rama.
6. Abre Pull Request hacia `develop`.
7. Otro integrante revisa y fusiona.
8. Al terminar las tres ramas, Nicolas puede marcar EU-31 como finalizada.
9. La fusion final `develop` -> `main` se hace al final de la entrega y corresponde a EU-36.
