from log.log import LoggerApp
from db.config import Session
from gestion.graficos import oro_por_cliente, ventas_por_mes
from db.models.models import Venta
from db.factory.factory import inicializar_datos
from services.services import (
    registrar_venta, registrar_cliente, mostrar_clientes,
    tasaciones_pendientes, ventas_cliente, ventas_mes,
    cliente_mas_ventas, clientes_inactivos
)

logger = LoggerApp()
db_session = Session()

def menu_principal():
    activo = True
    while activo:
        print("--------------- MENU PRINCIPAL ---------------\n")
        print("1) Alta de cliente")
        print("2) Mostrar clientes")
        print("3) Mostrar ventas")
        print("4) Registrar venta de oro")
        print("5) Ventas por mes")
        print("6) Ventas por cliente")
        print("7) Tasaciones pendientes")
        print("8) Cliente con mayor número de ventas")
        print("9) Clientes inactivos últimos 3 meses")
        print("10) Cargar datos iniciales")
        print("11) Gráfico oro por cliente")
        print("12) Gráfico ventas por mes")
        print("13) Salir\n")

        try:
            opcion = int(input("Selecciona una opción:\n"))
        except ValueError:
            print("Entrada inválida, debes introducir un número.\n")
            logger.error("Entrada no numérica en menú principal")
            opcion = -1

        if opcion == 1:
            logger.info("Seleccionada opción: Alta cliente")
            nombre = input("Nombre:\n")
            apellidos = input("Apellidos:\n")
            fecha_nacimiento = input("Fecha nacimiento (YYYY-MM-DD):\n")
            dni = input("DNI:\n")
            email = input("Email:\n")
            nacionalidad = input("Nacionalidad:\n")
            telefono = input("Teléfono:\n")
            direccion = input("Dirección:\n")

            if registrar_cliente(nombre, apellidos, fecha_nacimiento, dni, email, nacionalidad, telefono, direccion):
                print("Cliente registrado correctamente.\n")
            else:
                print("El cliente ya existe.\n")

        elif opcion == 2:
            logger.info("Seleccionada opción: Mostrar clientes")
            for c in mostrar_clientes():
                print(f"{c.id} | {c.nombre} {c.apellidos} | DNI: {c.dni} | Email: {c.email}")
            print()

        elif opcion == 3:
            logger.info("Seleccionada opción: Mostrar ventas")
            for v in db_session.query(Venta).all():
                print(f"{v.id} | Cliente {v.id_cliente} | Tasación {v.id_tasacion} | {v.gramos} g | {v.precio_total_eur} € | Estado {v.id_estado}")
            print()

        elif opcion == 4:
            logger.info("Seleccionada opción: Registrar venta")
            cliente_id = int(input("ID cliente:\n"))
            gramos = float(input("Cantidad oro (g):\n"))
            observaciones = input("Observaciones:\n")
            if registrar_venta(cliente_id, gramos, observaciones):
                print("Venta registrada.\n")
            else:
                print("Error al registrar la venta.\n")

        elif opcion == 5:
            anio = int(input("Año:\n"))
            mes = int(input("Mes (1-12):\n"))
            for v in ventas_mes(anio, mes):
                print(f"{v.id} | Cliente {v.id_cliente} | {v.gramos} g | {v.precio_total_eur} € | Fecha {v.fecha}")
            print()

        elif opcion == 6:
            cliente_id = int(input("ID cliente:\n"))
            for v in ventas_cliente(cliente_id):
                print(f"{v.id} | {v.gramos} g | {v.precio_total_eur} € | Fecha {v.fecha}")
            print()

        elif opcion == 7:
            for v in tasaciones_pendientes():
                print(f"{v.id} | Cliente {v.id_cliente} | Estado {v.estado.nombre} | Fecha {v.fecha}")
            print()

        elif opcion == 8:
            top = cliente_mas_ventas()
            if top:
                cliente, total = top
                print(f"Cliente con más ventas: {cliente.nombre} {cliente.apellidos} ({total} ventas)")
            else:
                print("No hay ventas registradas.\n")

        elif opcion == 9:
            inactivos = clientes_inactivos()
            if inactivos:
                print("Clientes inactivos últimos 3 meses:")
                for c in inactivos:
                    print(f"{c.id} | {c.nombre} {c.apellidos}")
            else:
                print("No hay clientes inactivos.\n")

        elif opcion == 10:
            inicializar_datos()
            print("Datos iniciales cargados.\n")

        elif opcion == 11:
            oro_por_cliente()
            logger.info("Seleccionada opción: Gráfico oro por cliente")

        elif opcion == 12:
            ventas_por_mes()
            logger.info("Seleccionada opción: Gráfico ventas por mes")

        elif opcion == 13:
            logger.info("Fin del programa desde menú principal")
            print("Programa finalizado")
            activo = False

        else:
            if opcion != -1:
                print("Opción inválida.\n")
                logger.error(f"Opción inválida: {opcion}")
