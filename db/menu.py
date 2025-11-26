from db.config import session
from db.models.models import Cliente, Tasacion, PrecioOro
from log.log import Log

def mostrar_menu():
    print("\n--------------------")
    print("1) Insertar cliente")
    print("2) Listar clientes")
    print("3) Modificar cliente")
    print("4) Eliminar cliente")
    print("5) Listar tasaciones")
    print("6) Listar precios del oro")
    print("7) Salir")
    print("\n--------------------")

log = Log()

def insertar_cliente():
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    email = input("Email: ")
    cliente = Cliente(nombre=nombre, apellidos=apellidos, email=email, activo=True)
    session.add(cliente)
    session.commit()
    print("Cliente guardado correctamente")
    log.registrar(f"Cliente insertado: {nombre} {apellidos} ({email})")

def listar_clientes():
    clientes = session.query(Cliente).all()
    for c in clientes:
        print(f"{c.id} - {c.nombre} {c.apellidos} ({c.email})")

def modificar_cliente():
    listar_clientes()
    id_cliente = input("ID del cliente a modificar: ")
    cliente = session.query(Cliente).get(int(id_cliente))
    if cliente:
        nuevo_nombre = input(f"Nuevo nombre ({cliente.nombre}): ") or cliente.nombre
        nuevo_apellidos = input(f"Nuevo apellidos ({cliente.apellidos}): ") or cliente.apellidos
        nuevo_email = input(f"Nuevo email ({cliente.email}): ") or cliente.email
        cliente.nombre = nuevo_nombre
        cliente.apellidos = nuevo_apellidos
        cliente.email = nuevo_email
        session.commit()
        print("Cliente actualizado correctamente")
    else:
        print("Cliente no encontrado")

def eliminar_cliente():
    listar_clientes()
    id_cliente = input("ID del cliente a eliminar: ")
    cliente = session.query(Cliente).get(int(id_cliente))
    if cliente:
        session.delete(cliente)
        session.commit()
        print("Cliente eliminado correctamente")
    else:
        print("Cliente no encontrado")

def listar_tasaciones():
    tasaciones = session.query(Tasacion).all()
    for t in tasaciones:
        print(f"{t.id} - {t.estado} - {t.cantidad_gramos}g - Cliente {t.cliente_id}")

def listar_precios_oro():
    precios = session.query(PrecioOro).order_by(PrecioOro.fecha.desc()).limit(5).all()
    for p in precios:
        print(f"{p.fecha} - {p.precio_kg} €/kg")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            insertar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            modificar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            listar_tasaciones()
        elif opcion == "6":
            listar_precios_oro()
        elif opcion == "7":
            print("Has salido")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
