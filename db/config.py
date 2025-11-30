from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://app_oro:app_oro@localhost:5432/empresa_oro")
Session = sessionmaker(bind=engine)
session = Session()