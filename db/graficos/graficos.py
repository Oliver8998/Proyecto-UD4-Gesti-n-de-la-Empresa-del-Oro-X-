import matplotlib.pyplot as plt
from db.config import session
from db.models.models import PrecioOro

def graficoPrecioOro():

    #sacar todos los precios ordenados por la fecha
    precios = session.query(PrecioOro).order_by(PrecioOro.fecha.asc()).all()

    fechas = [p.fecha for p in precios]
    valores = [p.precio_kg for p in precios]

    plt.bar(fechas, valores)
    plt.title("evolución del precio del oro")
    plt.xlabel("fecha")
    plt.ylabel("€/kg")
    plt.savefig("graficoPrecioOro.png")
    plt.show()