import random
from datetime import date, timedelta
from faker import Faker
from decimal import Decimal

from db.config import Session
from db.models.models import Cliente, Tasacion, Estado, Venta
from log.log import LoggerApp

logger = LoggerApp()
db_session = Session()
faker = Faker("es_ES")

def inicializar_datos():
    lista_clientes = []
    for _ in range(20):
        nuevo_cliente = Cliente(
            nombre=faker.first_name(),
            apellidos=faker.last_name(),
            fecha_nacimiento=faker.date_of_birth(minimum_age=18, maximum_age=70),
            dni=str(faker.unique.random_number(digits=8)) + faker.random_letter().upper(),
            email=faker.unique.email(),
            nacionalidad="Español",
            telefono=faker.phone_number(),
            direccion=faker.address(),
            activo=True
        )
        db_session.add(nuevo_cliente)
        lista_clientes.append(nuevo_cliente)

    db_session.commit()
    logger.info("Se han creado 20 clientes de prueba")

    fecha_inicio = date(2025, 1, 1)
    fecha_actual = date.today()
    dias_totales = (fecha_actual - fecha_inicio).days + 1

    precio_referencia = 3587.18
    for i in range(dias_totales):
        fecha_tasacion = fecha_inicio + timedelta(days=i)
        ya_existe = db_session.query(Tasacion).filter_by(fecha=fecha_tasacion).first()
        if not ya_existe:
            variacion = random.uniform(-0.03, 0.03)
            precio_referencia *= (1 + variacion)
            nueva_tasacion = Tasacion(fecha=fecha_tasacion, valor_kg_eur=precio_referencia)
            db_session.add(nueva_tasacion)

    db_session.commit()
    logger.info(f"Tasaciones registradas desde {fecha_inicio} hasta {fecha_actual}")

    estado_tasacion = db_session.query(Estado).filter_by(nombre="TASACION").first()
    estado_ok = db_session.query(Estado).filter_by(nombre="ACEPTADA").first()
    estado_fail = db_session.query(Estado).filter_by(nombre="RECHAZADA").first()

    todas_tasaciones = db_session.query(Tasacion).all()

    for _ in range(400):
        cliente = random.choice(lista_clientes)
        tasacion = random.choice(todas_tasaciones)
        gramos = Decimal(str(random.uniform(1, 100)))
        venta_ok = Venta(
            id_cliente=cliente.id,
            id_tasacion=tasacion.id,
            gramos=gramos,
            precio_unitario_eur=tasacion.valor_kg_eur / Decimal(1000),
            precio_total_eur=(tasacion.valor_kg_eur / Decimal(1000)) * gramos,
            fecha=tasacion.fecha,
            id_estado=estado_ok.id,
            observaciones="Venta aceptada"
        )
        db_session.add(venta_ok)

    for _ in range(30):
        cliente = random.choice(lista_clientes)
        tasacion = random.choice(todas_tasaciones)
        gramos = Decimal(str(random.uniform(1, 100)))
        venta_fail = Venta(
            id_cliente=cliente.id,
            id_tasacion=tasacion.id,
            gramos=gramos,
            precio_unitario_eur=tasacion.valor_kg_eur / Decimal(1000),
            precio_total_eur=(tasacion.valor_kg_eur / Decimal(1000)) * gramos,
            fecha=tasacion.fecha,
            id_estado=estado_fail.id,
            observaciones="Venta rechazada"
        )
        db_session.add(venta_fail)

    for _ in range(20):
        cliente = random.choice(lista_clientes)
        tasacion = random.choice(todas_tasaciones)
        gramos = Decimal(str(random.uniform(1, 100)))
        venta_tasacion = Venta(
            id_cliente=cliente.id,
            id_tasacion=tasacion.id,
            gramos=gramos,
            precio_unitario_eur=tasacion.valor_kg_eur / Decimal(1000),
            precio_total_eur=(tasacion.valor_kg_eur / Decimal(1000)) * gramos,
            fecha=tasacion.fecha,
            id_estado=estado_tasacion.id,
            observaciones="Venta en proceso de tasación"
        )
        db_session.add(venta_tasacion)

    db_session.commit()
    logger.info("Ventas iniciales creadas: 400 aceptadas, 30 rechazadas, 20 en tasación")
