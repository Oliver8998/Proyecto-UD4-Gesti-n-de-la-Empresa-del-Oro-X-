import matplotlib.pyplot as plt
from services.services import Services
from log.log import Log

class Graficos:
    def __init__(self):
        self.serv = Services()
        self.log = Log()

    def graficoOroPorCliente(self):
        try:
            ventas = self.serv.getVentas()
            clientes = {}
            for v in ventas:
                nombre = f"{v.usuario.nombre} {v.usuario.apellidos}"
                gramos = float(v.tasacion.cantidad_gramos)
                clientes[nombre] = clientes.get(nombre, 0) + gramos

            nombres = list(clientes.keys())
            gramos_totales = list(clientes.values())

            plt.figure(figsize=(10,6))
            plt.bar(nombres, gramos_totales, color="gold")
            plt.xticks(rotation=45, ha="right")
            plt.title("Cantidad de oro vendido por cliente")
            plt.ylabel("Gramos")
            plt.tight_layout()
            plt.savefig("graficoOroPorCliente.png")
            plt.show()

            self.log.info("Grafico oro por cliente generado correctamente")
        except Exception as e:
            self.log.error(f"Error al generar grafico oro por cliente: {e}")

    def graficoVentasPorMes(self):
        try:
            datos = self.serv.getVentasPorMes()
            meses = [d.mes.strftime("%Y-%m") for d in datos]
            totales = [float(d.total) for d in datos]

            plt.figure(figsize=(10,6))
            plt.plot(meses, totales, marker="o", color="blue")
            plt.xticks(rotation=45, ha="right")
            plt.title("Total de ventas por mes")
            plt.ylabel("Importe (€)")
            plt.tight_layout()
            plt.savefig("graficoVentasPorMes.png")
            plt.show()

            self.log.info("Grafico ventas por mes generado correctamente")
        except Exception as e:
            self.log.error(f"Error al generar grafico ventas por mes: {e}")
