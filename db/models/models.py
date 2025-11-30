from sqlalchemy import Column, BigInteger, String, Date, Text, Boolean, UniqueConstraint, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "cliente"
    __table_args__ = (
        UniqueConstraint("dni", "email", name="uq_cliente_identidad"),
    )

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellidos = Column(String(150), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    dni = Column(String(20), nullable=False, unique=True)
    email = Column(String(120), unique=True)
    nacionalidad = Column(String(80), nullable=False)
    telefono = Column(String(25))
    direccion = Column(Text)
    activo = Column(Boolean, nullable=False, default=True)

    ventas = relationship("Venta", back_populates="cliente")

    def __repr__(self):
        return f"<Cliente id={self.id} nombre={self.nombre} apellidos={self.apellidos}>"

class Tasacion(Base):
    __tablename__ = "tasacion"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    fecha = Column(Date, nullable=False, unique=True)
    valor_kg_eur = Column(Numeric(12,3), nullable=False)

    ventas = relationship("Venta", back_populates="tasacion")

    def __repr__(self):
        return f"<Tasacion id={self.id} fecha={self.fecha} valor_kg_eur={self.valor_kg_eur}>"

class Estado(Base):
    __tablename__ = "estado"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(20), nullable=False, unique=True)

    ventas = relationship("Venta", back_populates="estado")

    def __repr__(self):
        return f"<Estado id={self.id} nombre={self.nombre}>"

class Venta(Base):
    __tablename__ = "venta"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_cliente = Column(BigInteger, ForeignKey("cliente.id", onupdate="RESTRICT", ondelete="RESTRICT"), nullable=False)
    id_tasacion = Column(BigInteger, ForeignKey("tasacion.id", onupdate="RESTRICT", ondelete="RESTRICT"), nullable=False)
    gramos = Column(Numeric(10,3), nullable=False)
    precio_unitario_eur = Column(Numeric(12,3))
    precio_total_eur = Column(Numeric(12,3))
    fecha = Column(Date, nullable=False)
    id_estado = Column(BigInteger, ForeignKey("estado.id", onupdate="RESTRICT", ondelete="RESTRICT"), nullable=False)
    id_articulo = Column(BigInteger)
    observaciones = Column(Text)

    cliente = relationship("Cliente", back_populates="ventas")
    tasacion = relationship("Tasacion", back_populates="ventas")
    estado = relationship("Estado", back_populates="ventas")

    def __repr__(self):
        return f"<Venta id={self.id} cliente={self.id_cliente} estado={self.id_estado}>"
