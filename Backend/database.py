from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite guardará la BD en un archivo llamado "tramites.db" en la carpeta actual
DATABASE_URL = "sqlite:///./tramites.db"

# create_engine: Crea la conexión a la BD
# check_same_thread=False: Necesario para SQLite en desarrollo
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# SessionLocal: Crea sesiones (conexiones) a la BD cuando las necesites
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base: Clase base de la que heredarán todos nuestros modelos
Base = declarative_base()