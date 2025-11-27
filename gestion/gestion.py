from db.config import session
from db.models.models import Cliente, Tasacion, PrecioOro
from sqlalchemy import func

class Gestion:
    def informeClientes(self):
        total = session.query(func.count(Cliente.id)).scalar()
        activos = session.query(func.count(Cliente.id)).filter(Cliente.activo == True).scalar()
        print("Informe de clientes")
        print("Total clientes:", total)
        print("Clientes activos:", activos)

    def informeTasaciones(self):
        total = session.query(func.count(Tasacion.id)).scalar()
        aceptadas = session.query(func.count(Tasacion.id)).filter(Tasacion.estado == "aceptada").scalar()
        rechazadas = session.query(func.count(Tasacion.id)).filter(Tasacion.estado == "rechazada").scalar()
        print("Informe de tasaciones")
        print("Total tasaciones:", total)
        print("Aceptadas:", aceptadas)
        print("Rechazadas:", rechazadas)

    def informePrecioOro(self):
        precio_max = session.query(func.max(PrecioOro.precio_kg)).scalar()
        precio_min = session.query(func.min(PrecioOro.precio_kg)).scalar()
        precio_prom = session.query(func.avg(PrecioOro.precio_kg)).scalar()
        print("Informe precio oro")
        print("Precio maximo:", round(precio_max, 2), "€/kg")
        print("Precio minimo:", round(precio_min, 2), "€/kg")
        print("Precio medio:", round(precio_prom, 2), "€/kg")
