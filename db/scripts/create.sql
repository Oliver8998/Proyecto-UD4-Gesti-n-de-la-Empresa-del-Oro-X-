CREATE TABLE cliente (
    id BIGSERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(150) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    dni VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE,
    nacionalidad VARCHAR(80) NOT NULL,
    telefono VARCHAR(25),
    direccion TEXT,
    activo BOOLEAN DEFAULT TRUE NOT NULL
);

CREATE TABLE tasacion (
    id BIGSERIAL PRIMARY KEY,
    fecha DATE UNIQUE NOT NULL,
    valor_kg_eur NUMERIC(12,3) NOT NULL CHECK (valor_kg_eur > 0)
);

CREATE TABLE estado (
    id BIGSERIAL PRIMARY KEY,
    nombre VARCHAR(20) UNIQUE NOT NULL
);

INSERT INTO estado (nombre) VALUES
('TASACION'),
('ACEPTADA'),
('RECHAZADA');

CREATE TABLE venta (
    id BIGSERIAL PRIMARY KEY,
    id_cliente BIGINT NOT NULL REFERENCES cliente(id) ON UPDATE RESTRICT ON DELETE RESTRICT,
    id_tasacion BIGINT NOT NULL REFERENCES tasacion(id) ON UPDATE RESTRICT ON DELETE RESTRICT,
    gramos NUMERIC(10,3) NOT NULL CHECK (gramos > 0),
    precio_unitario_eur NUMERIC(12,3),
    precio_total_eur NUMERIC(12,3) CHECK (precio_total_eur >= 0),
    fecha DATE NOT NULL,
    id_estado BIGINT NOT NULL REFERENCES estado(id) ON UPDATE RESTRICT ON DELETE RESTRICT,
    id_articulo BIGINT,
    observaciones TEXT
);
