from sqlalchemy import Column, Integer, String, Text, Date, Numeric, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# ============================================================================
# TABLA DE ASOCIACIÓN: Tramites_Requisitos (N:M)
# ============================================================================
# Esta tabla conecta trámites con requisitos y sus atributos específicos
tramites_requisitos = Table(
    'tramites_requisitos',
    Base.metadata,
    Column('tramite_id', Integer, ForeignKey('tramites.id'), primary_key=True),
    Column('requisito_id', Integer, ForeignKey('requisitos.id'), primary_key=True),
    Column('obligatorio', Boolean, default=True),  # ¿Es obligatorio este requisito?
    Column('orden', Integer)  # ¿En qué orden aparece? (1, 2, 3...)
)

# ============================================================================
# TABLA DE ASOCIACIÓN: Tramites_Sede (N:M)
# ============================================================================
# Esta tabla conecta trámites con las sedes donde se pueden hacer
tramites_sede = Table(
    'tramites_sede',
    Base.metadata,
    Column('tramite_id', Integer, ForeignKey('tramites.id'), primary_key=True),
    Column('sede_id', Integer, ForeignKey('sedes.id'), primary_key=True)
)

# ============================================================================
# MODELO: Tramite (Principal)
# ============================================================================
class Tramite(Base):
    __tablename__ = "tramites"
    
    # Columnas básicas
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)  # "CIPE (DNI Provincial)"
    titulo_abreviado = Column(String(50), nullable=False)  # "CIPE"
    description = Column(Text, nullable=False)  # Descripción detallada
    fecha_ultima_actualizacion = Column(String(50))  # "Enero 2026"
    definicion = Column(Text)  # "Qué es el CIPE..."
    destinatarios = Column(Text)  # "Para quiénes es..."
    consejo_puntano = Column(Text)  # "Trucos locales..."
    fuentes_informacion = Column(Text)  # "Fuentes de información..."
    
    # ====== RELACIONES CON OTRAS TABLAS ======
    
    # Relación 1:1 con Costo
    # Un trámite tiene exactamente un costo
    costo_id = Column(Integer, ForeignKey('costos.id'), nullable=True)
    costo = relationship("Costo", back_populates="tramite")
    
    # Relación N:M con Requisitos
    # Un trámite puede tener muchos requisitos
    requisitos = relationship(
        "Requisito",
        secondary=tramites_requisitos,
        back_populates="tramites"
    )
    
    # Relación N:M con Sedes
    # Un trámite se puede hacer en varias sedes
    sedes = relationship(
        "Sede",
        secondary=tramites_sede,
        back_populates="tramites"
    )


# ============================================================================
# MODELO: Requisito
# ============================================================================
class Requisito(Base):
    __tablename__ = "requisitos"
    
    id = Column(Integer, primary_key=True, index=True)
    detalle = Column(String(500), nullable=False)  # "DNI original en vigencia"
    
    # Relación N:M con Trámites
    tramites = relationship(
        "Tramite",
        secondary=tramites_requisitos,
        back_populates="requisitos"
    )


# ============================================================================
# MODELO: Costo
# ============================================================================
class Costo(Base):
    __tablename__ = "costos"
    
    id = Column(Integer, primary_key=True, index=True)
    monto = Column(Numeric(10, 2), nullable=False)  # $100.00 (máx 8 dígitos + 2 decimales)
    fecha_actualizacion = Column(String(50))  # "Enero 2026"
    formas_pago = Column(Text)  # "Efectivo, Transferencia, etc" (JSON o texto separado por comas)
    
    # Relación 1:1 con Trámite
    tramite = relationship("Tramite", back_populates="costo", uselist=False)


# ============================================================================
# MODELO: Sede
# ============================================================================
class Sede(Base):
    __tablename__ = "sedes"
    
    id = Column(Integer, primary_key=True, index=True)
    direccion = Column(String(500), nullable=False)  # "Terrazas del Portezuelo, Km 783"
    horarios = Column(String(200))  # "Lunes a viernes de 8:00 a 14:00 hs"
    url_mapa = Column(String(500))  # URL de Google Maps
    
    # Relación N:M con Trámites
    tramites = relationship(
        "Tramite",
        secondary=tramites_sede,
        back_populates="sedes"
    )