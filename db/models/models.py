from sqlalchemy import Column, Integer, String, Date, Boolean, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    dni = Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    nacionalidad = Column(String(50))
    telefono = Column(String(20))
    direccion = Column(String(200))
    activo = Column(Boolean, default=True)

    tasaciones = relationship("Tasacion", back_populates="cliente")


class Tasacion(Base):
    __tablename__ = "tasacion"

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    cantidad_gramos = Column(Numeric(10,2), nullable=False)
    precio_gramo = Column(Numeric(10,2), nullable=False)
    estado = Column(String(20), nullable=False)

    cliente_id = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    cliente = relationship("Cliente", back_populates="tasaciones")


class PrecioOro(Base):
    __tablename__ = "precio_oro"

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False, unique=True)
    precio_kg = Column(Numeric(12,2), nullable=False)
