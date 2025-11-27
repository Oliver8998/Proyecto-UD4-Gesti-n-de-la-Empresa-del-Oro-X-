import csv
from db.config import session
from db.models.models import Cliente, Tasacion, PrecioOro

class Gestion:

    def informeClientes(self):
        clientes = session.query(Cliente).all()
        with open("clientes.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Nombre", "Apellidos", "Email", "Activo"])
            for c in clientes:
                writer.writerow([c.id, c.nombre, c.apellidos, c.email, c.activo])
        print("Informe de clientes exportado a clientes.csv")

    def informeTasaciones(self):
        tasaciones = session.query(Tasacion).all()
        with open("tasaciones.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Estado", "Cantidad gramos", "Cliente ID"])
            for t in tasaciones:
                writer.writerow([t.id, t.estado, t.cantidad_gramos, t.cliente_id])
        print("Informe de tasaciones exportado a tasaciones.csv")

    def informePrecioOro(self):
        precios = session.query(PrecioOro).all()
        with open("precio_oro.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Fecha", "Precio kg"])
            for p in precios:
                writer.writerow([p.fecha, p.precio_kg])
        print("Informe de precio del oro exportado a precio_oro.csv")
