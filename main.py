from gestion.gestion import Gestion
from db.graficos.graficos import Graficos
from utils.exportador import ExportadorPDF
from log.log import Log

log = Log()

def mostrarMenu():
    print("=== Menu Principal ===")
    print("1) Exportar informe de usuarios a CSV")
    print("2) Exportar informe de tasaciones a CSV")
    print("3) Exportar informe de ventas a CSV")
    print("4) Exportar informe de estados a CSV")
    print("5) Exportar informe de precio del oro a CSV")
    print("6) Exportar PDF completo")
    print("7) Grafico: cantidad de oro vendido por cliente")
    print("8) Grafico: total de ventas por mes")
    print("0) Salir")

def main():
    gestion = Gestion()
    graficos = Graficos()
    exportador = ExportadorPDF()

    while True:
        mostrarMenu()
        opcion = input("Selecciona una opcion: ").strip()

        try:
            if opcion == "1":
                gestion.informeUsuarios()
                log.info("Opcion 1 ejecutada: informeUsuarios")
            elif opcion == "2":
                gestion.informeTasaciones()
                log.info("Opcion 2 ejecutada: informeTasaciones")
            elif opcion == "3":
                gestion.informeVentas()
                log.info("Opcion 3 ejecutada: informeVentas")
            elif opcion == "4":
                gestion.informeEstados()
                log.info("Opcion 4 ejecutada: informeEstados")
            elif opcion == "5":
                gestion.informePrecioOro()
                log.info("Opcion 5 ejecutada: informePrecioOro")
            elif opcion == "6":
                exportador.exportarInformeCompleto()
                log.info("Opcion 6 ejecutada: exportarInformeCompleto")
            elif opcion == "7":
                graficos.graficoOroPorCliente()
                log.info("Opcion 7 ejecutada: graficoOroPorCliente")
            elif opcion == "8":
                graficos.graficoVentasPorMes()
                log.info("Opcion 8 ejecutada: graficoVentasPorMes")
            elif opcion == "0":
                log.info("Programa finalizado por el usuario")
                print("Has salido")
                break
            else:
                print("Opcion no valida")
                log.warning(f"Opcion no valida introducida: {opcion}")
        except Exception as e:
            log.error(f"Error al ejecutar la opcion {opcion}: {e}")

if __name__ == "__main__":
    main()
