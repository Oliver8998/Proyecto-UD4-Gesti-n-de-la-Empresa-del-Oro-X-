from gestion.gestion import Gestion
from db.graficos.graficos import Graficos
from utils.exportador import ExportadorPDF

def mostrarMenu():
    print("=== Menu Principal ===")
    print("1) Exportar informe de usuarios a CSV")
    print("2) Exportar informe de tasaciones a CSV")
    print("3) Exportar informe de ventas a CSV")
    print("4) Exportar informe de estados a CSV")
    print("5) Exportar informe de precio del oro a CSV")
    print("6) Exportar PDF completo (informes + graficos)")
    print("7) Grafico: cantidad de oro vendido por cliente")
    print("8) Grafico: total de ventas por mes")
    print("0) Salir")

def main():
    gestion = Gestion()
    graficos = Graficos()
    exportador = ExportadorPDF()

    while True:
        mostrarMenu()
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            gestion.informeUsuarios()
        elif opcion == "2":
            gestion.informeTasaciones()
        elif opcion == "3":
            gestion.informeVentas()
        elif opcion == "4":
            gestion.informeEstados()
        elif opcion == "5":
            gestion.informePrecioOro()
        elif opcion == "6":
            exportador.exportarInformeCompleto()
        elif opcion == "7":
            graficos.graficoOroPorCliente()
        elif opcion == "8":
            graficos.graficoVentasPorMes()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida, intenta de nuevo.")
