from db.config import session
from db.models.models import Cliente, Tasacion, PrecioOro

def mostrar_menu():
    print("\n--------------------")
    print("1) Insertar cliente")
    print("2) Listar clientes")
    print("3) Listar tasaciones")
    print("4) Listar precios del oro")
    print("5) Salir")
    print("\n--------------------")

def insertar_cliente():
    nombre = input("Nombre: ")
    apellidos = input("Apellidos ")
    email = input("Email ")
    cliente = Cliente(nombre=nombre, apellidos=apellidos, email=email, activo=True)
    session.add(cliente)
    session.commit()
    print("Cliente guardado correctamente")

def listar_clientes():
    clientes = session.query(Cliente).all()
    for c in clientes:
        print(f"{c.id} - {c.nombre} {c.apellidos} ({c.email})")

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
            listar_tasaciones()
        elif opcion == "4":
            listar_precios_oro()
        elif opcion == "5":
            print("Has salido")
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()
