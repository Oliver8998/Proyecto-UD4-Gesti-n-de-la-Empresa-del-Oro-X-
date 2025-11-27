import csv
from services.services import Services
from log.log import Log

class Gestion:
    def __init__(self):
        self.serv = Services()
        self.log = Log()

    def informeUsuarios(self):
        try:
            usuarios = self.serv.getUsuarios()
            with open("usuarios.csv", "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["Id", "Nombre", "Apellidos", "Email", "Activo"])
                for u in usuarios:
                    w.writerow([u.id, u.nombre, u.apellidos, u.email, u.activo])
            self.log.info("usuarios.csv generado")
        except Exception as e:
            self.log.error(f"Error al generar usuarios.csv: {e}")

    def informeTasaciones(self):
        try:
            tasaciones = self.serv.getTasaciones()
            with open("tasaciones.csv", "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["Id", "Fecha", "Gramos", "Valor estimado", "Usuario Id", "Estado"])
                for t in tasaciones:
                    w.writerow([t.id, t.fecha, t.cantidad_gramos, t.valor_estimado, t.usuario_id, t.estado.descripcion])
            self.log.info("tasaciones.csv generado")
        except Exception as e:
            self.log.error(f"Error al generar tasaciones.csv: {e}")

    def informeVentas(self):
        try:
            ventas = self.serv.getVentas()
            with open("ventas.csv", "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["Id", "Fecha", "Importe", "Usuario", "Tasacion"])
                for v in ventas:
                    nombre = f"{v.usuario.nombre} {v.usuario.apellidos}"
                    w.writerow([v.id, v.fecha, v.importe, nombre, v.tasacion_id])
            self.log.info("ventas.csv generado")
        except Exception as e:
            self.log.error(f"Error al generar ventas.csv: {e}")

    def informeEstados(self):
        try:
            estados = self.serv.getEstados()
            with open("estados.csv", "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["Id", "Descripcion"])
                for e in estados:
                    w.writerow([e.id, e.descripcion])
            self.log.info("estados.csv generado")
        except Exception as e:
            self.log.error(f"Error al generar estados.csv: {e}")

    def informePrecioOro(self):
        try:
            precios = self.serv.getPrecioOro()
            with open("precioOro.csv", "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["Id", "Fecha", "Precio kg"])
                for p in precios:
                    w.writerow([p.id, p.fecha, p.precio_kg])
            self.log.info("precioOro.csv generado")
        except Exception as e:
            self.log.error(f"Error al generar precioOro.csv: {e}")
