from sqlalchemy import Column, Integer, String, Date, Boolean, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    activo = Column(Boolean, default=True)

    tasaciones = relationship("Tasacion", back_populates="usuario")
    ventas = relationship("Venta", back_populates="usuario")


class Estado(Base):
    __tablename__ = "estado"

    id = Column(Integer, primary_key=True)
    descripcion = Column(String(50), nullable=False)

    tasaciones = relationship("Tasacion", back_populates="estado")


class Tasacion(Base):
    __tablename__ = "tasacion"

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    cantidad_gramos = Column(Numeric(10,2), nullable=False)
    valor_estimado = Column(Numeric(10,2), nullable=False)

    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    estado_id = Column(Integer, ForeignKey("estado.id"), nullable=False)

    usuario = relationship("Usuario", back_populates="tasaciones")
    estado = relationship("Estado", back_populates="tasaciones")
    ventas = relationship("Venta", back_populates="tasacion")


class Venta(Base):
    __tablename__ = "venta"

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    importe = Column(Numeric(10,2), nullable=False)

    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    tasacion_id = Column(Integer, ForeignKey("tasacion.id"), nullable=False)

    usuario = relationship("Usuario", back_populates="ventas")
    tasacion = relationship("Tasacion", back_populates="ventas")
