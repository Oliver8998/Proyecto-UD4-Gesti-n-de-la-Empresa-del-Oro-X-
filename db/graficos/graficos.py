import matplotlib.pyplot as plt
from utils.config import session
from db.models.models import Usuario, Venta, Tasacion

class Graficos:

    def graficoOroPorCliente(self):
        ventas = session.query(Venta).all()
        datos = {}
        for v in ventas:
            nombre = f"{v.usuario.nombre} {v.usuario.apellidos}"
            gramos = v.tasacion.cantidad_gramos
            datos[nombre] = datos.get(nombre, 0) + float(gramos)

        clientes = list(datos.keys())
        cantidades = list(datos.values())

        plt.figure(figsize=(10, 6))
        plt.bar(clientes, cantidades, color="gold")
        plt.title("Cantidad de oro vendido por cliente")
        plt.xlabel("Cliente")
        plt.ylabel("Gramos vendidos")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig("graficoOroPorCliente.png")
        plt.show()

    def graficoVentasPorMes(self):
        ventas = session.query(Venta).all()
        datos = {}
        for v in ventas:
            mes = v.fecha.strftime("%Y-%m")
            datos[mes] = datos.get(mes, 0) + float(v.importe)

        meses = list(datos.keys())
        totales = list(datos.values())

        plt.figure(figsize=(10, 6))
        plt.plot(meses, totales, marker="o", color="blue")
        plt.title("Total de ventas por mes")
        plt.xlabel("Mes")
        plt.ylabel("Importe total (€)")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig("graficoVentasPorMes.png")
        plt.show()
