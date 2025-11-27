# gestion.py
import csv
from services.services import Services
from utils.config import session
from db.models.models import Usuario, Tasacion, Venta, Estado

class Gestion:
    def __init__(self):
        self.serv = Services()

    def informeUsuarios(self):
        usuarios = self.serv.getUsuarios()
        with open("usuarios.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Id", "Nombre", "Apellidos", "Email", "Activo"])
            for u in usuarios:
                w.writerow([u.id, u.nombre, u.apellidos, u.email, u.activo])
        print("usuarios.csv generado")

    def informeTasaciones(self):
        tasaciones = self.serv.getTasaciones()
        with open("tasaciones.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Id", "Fecha", "Gramos", "Valor estimado", "Usuario Id", "Estado"])
            for t in tasaciones:
                w.writerow([t.id, t.fecha, t.cantidad_gramos, t.valor_estimado, t.usuario_id, t.estado.descripcion])
        print("tasaciones.csv generado")

    def informeVentas(self):
        ventas = self.serv.getVentas()
        with open("ventas.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Id", "Fecha", "Importe", "Usuario", "Tasacion"])
            for v in ventas:
                nombre = f"{v.usuario.nombre} {v.usuario.apellidos}"
                w.writerow([v.id, v.fecha, v.importe, nombre, v.tasacion_id])
        print("ventas.csv generado")

    def informeEstados(self):
        estados = self.serv.getEstados()
        with open("estados.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Id", "Descripcion"])
            for e in estados:
                w.writerow([e.id, e.descripcion])
        print("estados.csv generado")

    def informePrecioOro(self):
        precios = self.serv.getPrecioOro()
        with open("precioOro.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["ID", "Fecha", "Precio kg"])
            for p in precios:
                w.writerow([p.id, p.fecha, p.precio_kg])
        print("precioOro.csv generado")
