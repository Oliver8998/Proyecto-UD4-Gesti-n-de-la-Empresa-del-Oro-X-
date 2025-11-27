from datetime import date, timedelta
import random
from log.log import Log
from db.models.models import Usuario, Estado, Tasacion, Venta, PrecioOro

log = Log()

from utils.config import session
from db.models.models import Estado
import logging

def seedUsuarios():
    try:
        for i in range(1, 21):
            u = Usuario(
                nombre=f"Usuario{i}",
                apellidos=f"Apellido{i}",
                email=f"usuario{i}@example.com"
            )
            session.add(u)
        session.commit()
        log.info("20 usuarios insertados")
    except Exception as e:
        session.rollback()
        log.error(f"Error al insertar usuarios: {e}")

def seedEstados():
    try:
        estados = ["ACEPTADA", "RECHAZADA", "TASACION"]
        for e in estados:
            session.add(Estado(descripcion=e))
        session.commit()
        log.info("Estados insertados")
    except Exception as e:
        session.rollback()
        log.error(f"Error al insertar estados: {e}")

def seedTasaciones():
    try:
        usuarios = session.query(Usuario).all()
        estado_aceptada = session.query(Estado).filter_by(descripcion="ACEPTADA").first()
        estado_rechazada = session.query(Estado).filter_by(descripcion="RECHAZADA").first()
        estado_tasacion = session.query(Estado).filter_by(descripcion="TASACION").first()

        for _ in range(400):
            t = Tasacion(
                fecha=date(2025, 1, 1) + timedelta(days=random.randint(0, 300)),
                cantidad_gramos=round(random.uniform(10, 100), 2),
                valor_estimado=round(random.uniform(500, 5000), 2),
                usuario_id=random.choice(usuarios).id,
                estado_id=estado_aceptada.id
            )
            session.add(t)

        for _ in range(30):
            t = Tasacion(
                fecha=date(2025, 1, 1) + timedelta(days=random.randint(0, 300)),
                cantidad_gramos=round(random.uniform(10, 100), 2),
                valor_estimado=round(random.uniform(500, 5000), 2),
                usuario_id=random.choice(usuarios).id,
                estado_id=estado_rechazada.id
            )
            session.add(t)

        for _ in range(20):
            t = Tasacion(
                fecha=date(2025, 1, 1) + timedelta(days=random.randint(0, 300)),
                cantidad_gramos=round(random.uniform(10, 100), 2),
                valor_estimado=round(random.uniform(500, 5000), 2),
                usuario_id=random.choice(usuarios).id,
                estado_id=estado_tasacion.id
            )
            session.add(t)

        session.commit()
        log.info("Tasaciones insertadas")
    except Exception as e:
        session.rollback()
        log.error(f"Error al insertar tasaciones: {e}")

def seedVentas():
    try:
        estado_aceptada = session.query(Estado).filter_by(descripcion="ACEPTADA").first()
        tasaciones = session.query(Tasacion).filter_by(estado_id=estado_aceptada.id).all()

        log.info(f"Se encontraron {len(tasaciones)} tasaciones aceptadas")

        for t in tasaciones:
            v = Venta(
                fecha=t.fecha + timedelta(days=random.randint(0, 5)),
                importe=t.valor_estimado,
                usuario_id=t.usuario_id,
                tasacion_id=t.id
            )
            session.add(v)

        session.commit()
        log.info(f"{len(tasaciones)} ventas insertadas")
    except Exception as e:
        session.rollback()
        log.error(f"Error al insertar ventas: {e}")

def seedPrecioOro():
    try:
        inicio = date(2025, 1, 1)
        hoy = date.today()
        dias = (hoy - inicio).days
        for i in range(dias + 1):
            f = inicio + timedelta(days=i)
            precio = round(random.uniform(50000, 60000), 2)
            session.add(PrecioOro(fecha=f, precio_kg=precio))
        session.commit()
        log.info("PrecioOro insertado desde 2025-01-01 hasta hoy")
    except Exception as e:
        session.rollback()
        log.error(f"Error al insertar precio del oro: {e}")

def seedAll():
    seedUsuarios()
    seedEstados()
    seedTasaciones()
    seedVentas()
    seedPrecioOro()

if __name__ == "__main__":
    seedAll()
