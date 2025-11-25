from db.models.models import Base
from db.config import engine

def crear_tablas():
    Base.metadata.create_all(bind=engine)
    print("tablas creadas correctamente")

if __name__ == "__main__":
    crear_tablas()
