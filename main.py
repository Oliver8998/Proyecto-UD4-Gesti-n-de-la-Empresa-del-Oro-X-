from utils.config import session
from db.graficos.graficos import graficoPrecioOro
from db.models.models import Cliente, Tasacion, PrecioOro
from gestion.gestion import Gestion
from log.log import Log

log = Log()
gestion = Gestion()

def mostrarMenu():
    print("\n--------------------")
    print("1) Insertar cliente")
    print("2) Listar clientes")
    print("3) Modificar cliente")
    print("4) Eliminar cliente")
    print("5) Listar tasaciones")
    print("6) Listar precios del oro")
    print("7) Exportar informe de clientes a CSV")
    print("8) Exportar informe de tasaciones a CSV")
    print("9) Exportar informe de precio del oro a CSV")
    print("10) Generar grafico del precio del oro")
    print("11) Exportar PDF completo")
    print("0) Salir")
    print("--------------------")

def insertarCliente():
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    email = input("Email: ")
    cliente = Cliente(nombre=nombre, apellidos=apellidos, email=email, activo=True)
    session.add(cliente)
    session.commit()
    print("Cliente guardado correctamente")
    log.registrar(f"Cliente insertado: {nombre} {apellidos} ({email})")

def listarClientes():
    clientes = session.query(Cliente).all()
    for c in clientes:
        print(f"{c.id} - {c.nombre} {c.apellidos} ({c.email})")

def modificarCliente():
    listarClientes()
    id_cliente = input("Id del cliente a modificar: ")
    cliente = session.query(Cliente).get(int(id_cliente))
    if cliente:
        nuevo_nombre = input(f"Nuevo nombre ({cliente.nombre}): ") or cliente.nombre
        nuevo_apellidos = input(f"Nuevos apellidos ({cliente.apellidos}): ") or cliente.apellidos
        nuevo_email = input(f"Nuevo email ({cliente.email}): ") or cliente.email
        cliente.nombre = nuevo_nombre
        cliente.apellidos = nuevo_apellidos
        cliente.email = nuevo_email
        session.commit()
        print("Cliente actualizado correctamente")
        log.registrar(f"Cliente modificado: Id {id_cliente}")
    else:
        print("Cliente no encontrado")

def eliminarCliente():
    listarClientes()
    id_cliente = input("Id del cliente a eliminar: ")
    cliente = session.query(Cliente).get(int(id_cliente))
    if cliente:
        session.delete(cliente)
        session.commit()
        print("Se ha eliminado al cliente")
        log.registrar(f"Cliente eliminado: Id {id_cliente}")
    else:
        print("No se encuentra al cliente")

def listarTasaciones():
    tasaciones = session.query(Tasacion).all()
    for t in tasaciones:
        print(f"{t.id} - {t.estado} - {t.cantidad_gramos}g - Cliente {t.cliente_id}")

def listarPreciosOro():
    precios = session.query(PrecioOro).order_by(PrecioOro.fecha.desc()).limit(5).all()
    for p in precios:
        print(f"{p.fecha} - {p.precio_kg} €/kg")

def main():
    while True:
        mostrarMenu()
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            insertarCliente()
        elif opcion == "2":
            listarClientes()
        elif opcion == "3":
            modificarCliente()
        elif opcion == "4":
            eliminarCliente()
        elif opcion == "5":
            listarTasaciones()
        elif opcion == "6":
            listarPreciosOro()
        if opcion == "7":
            gestion.informeClientes()
        elif opcion == "8":
            gestion.informeTasaciones()
        elif opcion == "9":
            gestion.informePrecioOro()
        elif opcion == "10":
            graficoPrecioOro()
        elif opcion == "11":
            from utils.exportador import ExportadorPDF
            pdf = ExportadorPDF()
            pdf.exportarInformeCompleto()
        elif opcion == "0":
            print("Has salido")
            break
        else:
            print("Opción no valida")

if __name__ == "__main__":
    main()
