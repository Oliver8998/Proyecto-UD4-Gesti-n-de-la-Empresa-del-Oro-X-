import random
from db.models.models import Cliente, Tasacion, Estado, Venta
from db.config import Session
from log.log import LoggerApp
from sqlalchemy import func
from datetime import date, timedelta

logger = LoggerApp()
db_session = Session()

def precio_oro_actual():
    hoy = date.today()
    registro = db_session.query(Tasacion).filter_by(fecha=hoy).first()

    if registro:
        return registro.valor_kg_eur

    ultimo = db_session.query(Tasacion).order_by(Tasacion.fecha.desc()).first()
    if ultimo:
        variacion = random.uniform(-0.03, 0.03)
        nuevo = float(ultimo.valor_kg_eur) * (1 + variacion)
    else:
        nuevo = 3587.18

    nuevo_registro = Tasacion(fecha=hoy, valor_kg_eur=nuevo)
    db_session.add(nuevo_registro)
    db_session.commit()
    logger.info(f"Tasación creada para hoy: {nuevo} €/kg")
    return nuevo

def registrar_venta(id_cliente, gramos, observaciones=None, id_articulo=None):
    cliente = db_session.query(Cliente).get(id_cliente)
    if not cliente or not cliente.activo:
        logger.error("Cliente inválido o inactivo")
        return False

    edad = (date.today() - cliente.fecha_nacimiento).days // 365
    if edad < 18:
        logger.error("Cliente menor de edad, venta rechazada")
        return False

    precio_unitario = precio_oro_actual()
    precio_total = precio_unitario * float(gramos)

    estado = db_session.query(Estado).filter_by(nombre="TASACION").first()
    tasacion = db_session.query(Tasacion).filter_by(fecha=date.today()).first()

    venta = Venta(
        id_cliente=id_cliente,
        id_tasacion=tasacion.id,
        gramos=gramos,
        precio_unitario_eur=precio_unitario,
        precio_total_eur=precio_total,
        fecha=date.today(),
        id_estado=estado.id,
        id_articulo=id_articulo,
        observaciones=observaciones
    )
    db_session.add(venta)
    db_session.commit()
    logger.info(f"Venta registrada: Cliente {id_cliente}, {gramos} g, {precio_total} €")
    return True

def registrar_cliente(nombre, apellidos, fecha_nacimiento, dni, email, nacionalidad, telefono, direccion):
    duplicado = db_session.query(Cliente).filter(
        (Cliente.dni == dni) | (Cliente.email == email)
    ).first()

    if duplicado:
        logger.warning(f"Alta duplicada: DNI {dni} o Email {email}")
        return False

    nuevo = Cliente(
        nombre=nombre,
        apellidos=apellidos,
        fecha_nacimiento=fecha_nacimiento,
        dni=dni,
        email=email,
        nacionalidad=nacionalidad,
        telefono=telefono,
        direccion=direccion,
        activo=True
    )
    db_session.add(nuevo)
    db_session.commit()
    logger.info(f"Cliente registrado: {nombre} {apellidos}, DNI {dni}")
    return True

def mostrar_clientes():
    lista = db_session.query(Cliente).all()
    logger.info("Consulta de clientes")
    return lista

def ventas_mes(anio, mes):
    registros = db_session.query(Venta).filter(
        func.extract("year", Venta.fecha) == anio,
        func.extract("month", Venta.fecha) == mes
    ).all()
    logger.info(f"Consulta ventas {mes}/{anio}")
    return registros

def ventas_cliente(id_cliente):
    registros = db_session.query(Venta).filter(Venta.id_cliente == id_cliente).all()
    logger.info(f"Consulta ventas cliente {id_cliente}")
    return registros

def tasaciones_pendientes():
    estado_ok = db_session.query(Estado).filter_by(nombre="ACEPTADA").first()
    registros = db_session.query(Venta).filter(Venta.id_estado != estado_ok.id).all()
    logger.info("Consulta tasaciones pendientes")
    return registros

def cliente_mas_ventas():
    resultado = db_session.query(
        Cliente, func.count(Venta.id).label("total")
    ).join(Venta, Cliente.id == Venta.id_cliente).group_by(Cliente.id).order_by(func.count(Venta.id).desc()).first()
    logger.info("Consulta cliente con más ventas")
    return resultado

def clientes_inactivos():
    limite = date.today() - timedelta(days=90)
    subq = db_session.query(Venta.id_cliente, func.max(Venta.fecha).label("ultima")).group_by(Venta.id_cliente).subquery()
    registros = db_session.query(Cliente).join(subq, Cliente.id == subq.c.id_cliente).filter(subq.c.ultima < limite).all()
    logger.info("Consulta clientes inactivos últimos 3 meses")
    return registros
