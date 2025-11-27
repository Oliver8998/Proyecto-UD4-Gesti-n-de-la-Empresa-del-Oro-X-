from utils.config import session
from db.models.models import Usuario, Tasacion, Venta, Estado, PrecioOro
from sqlalchemy import func

class Services:

    def getUsuarios(self):
        return session.query(Usuario).all()

    # Tasaciones
    def getTasaciones(self):
        return session.query(Tasacion).all()

    def getTasacionesPorEstado(self, estado_desc):
        return session.query(Tasacion).join(Estado).filter(Estado.descripcion == estado_desc).all()

    def getVentas(self):
        return session.query(Venta).all()

    def getVentasPorMes(self):
        return session.query(
            func.date_trunc("month", Venta.fecha).label("mes"),
            func.sum(Venta.importe).label("total")
        ).group_by("mes").order_by("mes").all()

    def getEstados(self):
        return session.query(Estado).all()

    # Precio del oro
    def getPrecioOro(self):
        return session.query(PrecioOro).order_by(PrecioOro.fecha).all()

    def getPrecioOroPorFecha(self, fecha):
        return session.query(PrecioOro).filter(PrecioOro.fecha == fecha).first()

    def getVentas(self):
        ventas = session.query(Venta).all()
        from log.log import Log
        log = Log()
        log.info(f"Se han recuperado {len(ventas)} ventas de la BD")
        return ventas

