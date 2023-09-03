from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cadena de conexion para mysql
CADENA_CONEXION = 'mysql+mysqlconnector://root:admin123@localhost/task_admin'

motor = create_engine(CADENA_CONEXION)
Session = sessionmaker(bind=motor)
session = Session()

Base = declarative_base()
