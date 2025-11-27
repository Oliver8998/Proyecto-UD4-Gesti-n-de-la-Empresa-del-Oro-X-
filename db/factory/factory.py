# factory.py
from datetime import date, timedelta
import random
from utils.config import session
from db.models.models import Usuario, Estado, Tasacion, Venta, PrecioOro

def seedUsuarios():
    for i in range(1, 21):
        u = Usuario(
            nombre=f"Usuario{i}",
            apellidos=f"Apellido{i}",
            email=f"usuario{i}@example.com"
        )
        session.add(u)
    session.commit()
    print("20 usuarios insertados")

def seedEstados():
    estados = ["aceptada", "rechazada", "tasacion"]
    for e in estados:
        session.add(Estado(descripcion=e))
    session.commit()
    print("Estados insertados")

def seedTasaciones():
    usuarios = session.query(Usuario).all()
    estados = {e.descripcion: e for e in session.query(Estado).all()}

    # 400 aceptadas
    for _ in range(400):
        t = Tasacion(
            fecha=date(2025, 1, 1) + timedelta(days=random.randint(0, 300)),
            cantidad_gramos=round(random.uniform(10, 100), 2),
            valor_estimado=round(random.uniform(500, 5000), 2),
            usuario_id=random.choice(usuarios).id,
            estado_id=estados["aceptada"].id
        )
        session.add(t)

    # 30 rechazadas
    for _ in range(30):
        t = Tasacion(
            fecha=date(2025, 1, 1) + timedelta(days=random.randint(0, 300)),
            cantidad_gramos=round(random.uniform(10, 100), 2),
            valor_estimado=round(random.uniform(500, 5000), 2),
            usuario_id=random.choice(usuarios).id,
            estado_id=estados["rechazada"].id
        )
        session.add(t)

    # 20 tasacion
    for _ in range(20):
        t = Tasacion(
            fecha=date(2025, 1, 1) + timedelta(days=random.randint(0, 300)),
            cantidad_gramos=round(random.uniform(10, 100), 2),
            valor_estimado=round(random.uniform(500, 5000), 2),
            usuario_id=random.choice(usuarios).id,
            estado_id=estados["tasacion"].id
        )
        session.add(t)

    session.commit()
    print("Tasaciones insertadas")

def seedVentas():
    tasaciones = session.query(Tasacion).join(Estado).filter(Estado.descripcion=="aceptada").all()
    for t in tasaciones:
        v = Venta(
            fecha=t.fecha + timedelta(days=random.randint(0, 5)),
            importe=t.valor_estimado,
            usuario_id=t.usuario_id,
            tasacion_id=t.id
        )
        session.add(v)
    session.commit()
    print("Ventas insertadas")

def seedPrecioOro():
    inicio = date(2025, 1, 1)
    hoy = date.today()
    dias = (hoy - inicio).days
    for i in range(dias + 1):
        f = inicio + timedelta(days=i)
        precio = round(random.uniform(50000, 60000), 2)  # EUR/kg
        session.add(PrecioOro(fecha=f, precio_kg=precio))
    session.commit()
    print("PrecioOro insertado desde 2025-01-01 hasta hoy")

def seedAll():
    seedUsuarios()
    seedEstados()
    seedTasaciones()
    seedVentas()
    seedPrecioOro()

if __name__ == "__main__":
    seedAll()
