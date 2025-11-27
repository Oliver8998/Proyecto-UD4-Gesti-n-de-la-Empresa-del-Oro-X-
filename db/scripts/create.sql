CREATE TABLE Usuario (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE Estado (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(50) NOT NULL
);

CREATE TABLE Tasacion (
    id SERIAL PRIMARY KEY,
    cantidad_gramos NUMERIC(10,2) NOT NULL,
    valor_estimado NUMERIC(10,2) NOT NULL,
    usuario_id INT NOT NULL,
    estado_id INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(id),
    FOREIGN KEY (estado_id) REFERENCES Estado(id)
);

CREATE TABLE Ventas (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    importe NUMERIC(10,2) NOT NULL,
    usuario_id INT NOT NULL,
    tasacion_id INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(id),
    FOREIGN KEY (tasacion_id) REFERENCES Tasacion(id)
);

CREATE TABLE PrecioOro (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL UNIQUE,
    precio_kg NUMERIC(12,2) NOT NULL
);
