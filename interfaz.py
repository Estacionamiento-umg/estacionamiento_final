import tkinter as tk
from tkinter import messagebox, simpledialog

import archivos
from usuarios_vehiculos import registrar_usuario, registrar_vehiculo
from espacios import listar_espacios
from reservas import crear_reserva
from ingresos import registrar_ingreso
from salidas_pagos import registrar_salida
from reportes import reporte_por_fecha, vehiculos_dentro

# Esta interfaz es sencilla: cada boton llama a una funcion del sistema.
archivos.inicializar_datos()


def pedir_usuario():
    nombre = simpledialog.askstring("Usuario", "Nombre:")
    telefono = simpledialog.askstring("Usuario", "Telefono:")

    if nombre is None or telefono is None:
        return

    try:
        usuario = registrar_usuario(nombre, telefono)
        messagebox.showinfo("Registro", "Usuario registrado con ID: " + usuario["id_usuario"])
    except ValueError as error:
        messagebox.showerror("Error", str(error))


def pedir_vehiculo():
    id_usuario = simpledialog.askstring("Vehiculo", "ID del usuario:")
    placa = simpledialog.askstring("Vehiculo", "Placa:")
    tipo = simpledialog.askstring("Vehiculo", "Tipo: carro, moto, camion u otro:")

    if id_usuario is None or placa is None or tipo is None:
        return

    try:
        vehiculo = registrar_vehiculo(id_usuario, placa, tipo)
        messagebox.showinfo("Registro", "Vehiculo registrado: " + vehiculo["placa"])
    except ValueError as error:
        messagebox.showerror("Error", str(error))


def mostrar_espacios():
    espacios = listar_espacios()
    texto = "CODIGO   TIPO   ESTADO\n\n"

    for espacio in espacios:
        texto = texto + espacio["codigo"] + "   " + espacio["tipo"] + "   " + espacio["estado"] + "\n"

    messagebox.showinfo("Espacios", texto)


def pedir_reserva():
    id_usuario = simpledialog.askstring("Reserva", "ID del usuario:")
    placa = simpledialog.askstring("Reserva", "Placa:")
    espacio = simpledialog.askstring("Reserva", "Codigo del espacio:")
    inicio = simpledialog.askstring("Reserva", "Inicio (AAAA-MM-DD HH:MM):")
    fin = simpledialog.askstring("Reserva", "Fin (AAAA-MM-DD HH:MM):")

    if None in (id_usuario, placa, espacio, inicio, fin):
        return

    try:
        reserva = crear_reserva(id_usuario, placa, espacio, inicio, fin)
        messagebox.showinfo("Reserva", "Reserva creada con ID: " + reserva["id_reserva"])
    except ValueError as error:
        messagebox.showerror("Error", str(error))


def pedir_ingreso():
    placa = simpledialog.askstring("Ingreso", "Placa del vehiculo:")

    if placa is None:
        return

    try:
        movimiento = registrar_ingreso(placa)
        messagebox.showinfo("Ingreso", "Espacio asignado: " + movimiento["espacio"])
    except ValueError as error:
        messagebox.showerror("Error", str(error))


def pedir_salida():
    placa = simpledialog.askstring("Salida", "Placa del vehiculo:")

    if placa is None:
        return

    try:
        salida = registrar_salida(placa)
        mensaje = "Tiempo: " + str(salida["minutos"]) + " minutos\nTotal: Q" + str(salida["total"])
        messagebox.showinfo("Salida y pago", mensaje)
    except ValueError as error:
        messagebox.showerror("Error", str(error))


def pedir_reporte():
    fecha = simpledialog.askstring("Reporte", "Fecha (AAAA-MM-DD):")

    if fecha is None:
        return

    reporte = reporte_por_fecha(fecha)
    mensaje = (
        "Fecha: " + reporte["fecha"] +
        "\nEntradas: " + str(reporte["cantidad_entradas"]) +
        "\nPagos: " + str(reporte["cantidad_pagos"]) +
        "\nIngresos: Q" + str(reporte["ingresos"])
    )
    messagebox.showinfo("Reporte", mensaje)


def mostrar_vehiculos_dentro():
    movimientos = vehiculos_dentro()

    if len(movimientos) == 0:
        messagebox.showinfo("Vehiculos dentro", "No hay vehiculos dentro.")
        return

    texto = ""
    for movimiento in movimientos:
        texto = texto + movimiento["placa"] + " - espacio " + movimiento["espacio"] + "\n"

    messagebox.showinfo("Vehiculos dentro", texto)


ventana = tk.Tk()
ventana.title("Sistema de Estacionamiento - Grupo 4")
ventana.geometry("480x560")
ventana.resizable(False, False)

# Titulo de la ventana.
tk.Label(ventana, text="SISTEMA DE ESTACIONAMIENTO", font=("Arial", 17, "bold")).pack(pady=20)
tk.Label(ventana, text="Primera version funcional - Sprint 2", font=("Arial", 10)).pack(pady=3)

# Botones principales.
tk.Button(ventana, text="1. Registrar usuario", width=32, command=pedir_usuario).pack(pady=6)
tk.Button(ventana, text="2. Registrar vehiculo", width=32, command=pedir_vehiculo).pack(pady=6)
tk.Button(ventana, text="3. Ver espacios", width=32, command=mostrar_espacios).pack(pady=6)
tk.Button(ventana, text="4. Crear reserva", width=32, command=pedir_reserva).pack(pady=6)
tk.Button(ventana, text="5. Registrar ingreso", width=32, command=pedir_ingreso).pack(pady=6)
tk.Button(ventana, text="6. Registrar salida y pago", width=32, command=pedir_salida).pack(pady=6)
tk.Button(ventana, text="7. Reporte por fecha", width=32, command=pedir_reporte).pack(pady=6)
tk.Button(ventana, text="8. Vehiculos dentro", width=32, command=mostrar_vehiculos_dentro).pack(pady=6)
tk.Button(ventana, text="Salir", width=32, command=ventana.destroy).pack(pady=18)

ventana.mainloop()
