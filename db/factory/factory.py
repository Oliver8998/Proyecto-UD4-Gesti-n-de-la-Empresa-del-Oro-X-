from faker import Faker
from datetime import date, timedelta
import random
from db.config import session, engine
from db.models.models import Base, Cliente, Tasacion, PrecioOro

Base.metadata.create_all(bind=engine)

fake = Faker("es_ES")

def generar_clientes():
    lista_clientes = []
    for _ in range(20):
        cliente = Cliente(
            nombre=fake.first_name(),
            apellidos=fake.last_name(),
            fecha_nacimiento=fake.date_of_birth(minimum_age=18, maximum_age=75),
            dni=fake.unique.ssn(),
            email=fake.unique.email(),
            nacionalidad=fake.country(),
            telefono=fake.phone_number(),
            direccion=fake.address(),
            activo=True
        )
        lista_clientes.append(cliente)
        session.add(cliente)
    session.commit()
    return lista_clientes

def generarPreciosOro():

    precio = 113000
    fecha = date(2025, 1, 1)
    hoy = date.today()

    while fecha <= hoy:
        cambio = random.choice([-200, -100, 0, 100, 200])
        precio += cambio
        session.add(PrecioOro(fecha=fecha, precio_kg=precio))
        fecha += timedelta(days=1)

    session.commit()

def generarTasaciones(clientes):
    estados = ["aceptada"] * 400 + ["rechazada"] * 30 + ["tasacion"] * 20
    fecha_inicio = date(2025, 1, 1)
    hoy = date.today()

    for estado in estados:
        cliente = random.choice(clientes)
        gramos = random.randint(1, 100)
        precio_oro = session.query(PrecioOro).order_by(PrecioOro.fecha.desc()).first()
        precio_gramo = precio_oro.precio_kg / 1000 if precio_oro else 113

        tasacion = Tasacion(
            fecha=fake.date_between(start_date=fecha_inicio, end_date=hoy),
            cantidad_gramos=gramos,
            estado=estado,
            precio_gramo=precio_gramo,
            cliente=cliente
        )
        session.add(tasacion)

    session.commit()

if __name__ == "__main__":
    clientes = generar_clientes()
    generarPreciosOro()
    generarTasaciones(clientes)
    print("Los datos iniciales se han insertado en la base de datos")
