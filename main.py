import archivos
from usuarios_vehiculos import registrar_usuario, registrar_vehiculo
from espacios import listar_espacios
from reservas import crear_reserva
from ingresos import registrar_ingreso
from salidas_pagos import registrar_salida
from reportes import reporte_por_fecha, vehiculos_dentro

def mostrar_menu():
    print("\n=== SISTEMA DE ESTACIONAMIENTO ===")
    print("1. Registrar usuario")
    print("2. Registrar vehiculo")
    print("3. Ver espacios")
    print("4. Crear reserva")
    print("5. Registrar ingreso")
    print("6. Registrar salida y pago")
    print("7. Reporte por fecha")
    print("8. Vehiculos dentro")
    print("0. Salir")

def main():
    archivos.inicializar_datos()

    while True:
        mostrar_menu()
        opcion = input("Opcion: ").strip()

        try:
            if opcion == "1":
                nombre = input("Nombre: ")
                telefono = input("Telefono: ")
                print(registrar_usuario(nombre, telefono))

            elif opcion == "2":
                id_usuario = input("ID del usuario: ")
                placa = input("Placa: ")
                tipo = input("Tipo (carro/moto/camion/otro): ")
                print(registrar_vehiculo(id_usuario, placa, tipo))

            elif opcion == "3":
                for espacio in listar_espacios():
                    print(espacio)

            elif opcion == "4":
                id_usuario = input("ID usuario: ")
                placa = input("Placa: ")
                espacio = input("Espacio: ")
                inicio = input("Inicio (AAAA-MM-DD HH:MM): ")
                fin = input("Fin (AAAA-MM-DD HH:MM): ")
                print(crear_reserva(id_usuario, placa, espacio, inicio, fin))

            elif opcion == "5":
                placa = input("Placa: ")
                print(registrar_ingreso(placa))

            elif opcion == "6":
                placa = input("Placa: ")
                print(registrar_salida(placa))

            elif opcion == "7":
                fecha = input("Fecha (AAAA-MM-DD): ")
                print(reporte_por_fecha(fecha))

            elif opcion == "8":
                for movimiento in vehiculos_dentro():
                    print(movimiento)

            elif opcion == "0":
                print("Programa finalizado.")
                break

            else:
                print("Opcion no valida.")

        except ValueError as error:
            print("Error:", error)

if __name__ == "__main__":
    main()
