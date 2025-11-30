import matplotlib.pyplot as plt
from db.config import Session
from db.models.models import Cliente, Venta
from decimal import Decimal
from datetime import datetime
from log.log import LoggerApp

logger = LoggerApp()

def oro_por_cliente():
    sesion = Session()
    datos = sesion.query(Cliente.nombre, Cliente.apellidos, Venta.gramos)\
                  .join(Venta, Cliente.id == Venta.id_cliente)\
                  .all()

    acumulado = {}
    for nombre, apellidos, gramos in datos:
        clave = f"{nombre} {apellidos}"
        if clave not in acumulado:
            acumulado[clave] = Decimal(0)
        acumulado[clave] += gramos

    etiquetas = list(acumulado.keys())
    valores = [float(v) for v in acumulado.values()]

    plt.bar(etiquetas, valores)
    plt.title("Oro vendido por cliente")
    plt.xlabel("Cliente")
    plt.ylabel("Gramos")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    marca_tiempo = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archivo = f"oro_por_cliente_{marca_tiempo}.png"
    plt.savefig(archivo)
    plt.show()

    logger.info(f"Gráfico generado: oro por cliente → {archivo}")


def ventas_por_mes():
    sesion = Session()
    anio = datetime.now().year

    acumulado = {m: Decimal(0) for m in range(1, 13)}

    registros = sesion.query(Venta.fecha, Venta.precio_total_eur).all()
    for fecha, total in registros:
        if fecha.year == anio:
            acumulado[fecha.month] += total

    meses = [str(m) for m in sorted(acumulado.keys())]
    valores = [float(acumulado[m]) for m in sorted(acumulado.keys())]

    plt.bar(meses, valores)
    plt.title("Ventas por mes")
    plt.xlabel("Mes")
    plt.ylabel("Total (€)")
    plt.tight_layout()

    marca_tiempo = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archivo = f"ventas_por_mes_{marca_tiempo}.png"
    plt.savefig(archivo)
    plt.show()

    logger.info(f"Gráfico generado: ventas por mes → {archivo}")
