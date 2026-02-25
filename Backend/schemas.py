from pydantic import BaseModel
from typing import Optional, List
from decimal import Decimal

# ============================================================================
# SCHEMAS PARA REQUISITO
# ============================================================================

class RequisitoBase(BaseModel):
    """Base con campos comunes"""
    detalle: str

class RequisitoCreate(RequisitoBase):
    """Para CREAR un requisito (POST)"""
    pass

class Requisito(RequisitoBase):
    """Para DEVOLVER un requisito (GET)"""
    id: int
    
    class Config:
        from_attributes = True


# ============================================================================
# SCHEMAS PARA COSTO
# ============================================================================

class CostoBase(BaseModel):
    """Base con campos comunes"""
    monto: Decimal
    fecha_actualizacion: Optional[str] = None
    formas_pago: Optional[str] = None

class CostoCreate(CostoBase):
    """Para CREAR un costo (POST)"""
    pass

class Costo(CostoBase):
    """Para DEVOLVER un costo (GET)"""
    id: int
    
    class Config:
        from_attributes = True


# ============================================================================
# SCHEMAS PARA SEDE
# ============================================================================

class SedeBase(BaseModel):
    """Base con campos comunes"""
    direccion: str
    horarios: Optional[str] = None
    url_mapa: Optional[str] = None

class SedeCreate(SedeBase):
    """Para CREAR una sede (POST)"""
    pass

class Sede(SedeBase):
    """Para DEVOLVER una sede (GET)"""
    id: int
    
    class Config:
        from_attributes = True


# ============================================================================
# SCHEMAS PARA TRAMITE
# ============================================================================

class TramiteBase(BaseModel):
    """Base con campos comunes"""
    titulo: str
    titulo_abreviado: str
    description: str
    fecha_ultima_actualizacion: Optional[str] = None
    definicion: Optional[str] = None
    destinatarios: Optional[str] = None
    consejo_puntano: Optional[str] = None
    fuentes_informacion: Optional[str] = None

class TramiteCreate(TramiteBase):
    """
    Para CREAR un trámite (POST)
    El cliente envía solo los datos básicos
    """
    pass

class TramiteUpdate(BaseModel):
    """
    Para ACTUALIZAR un trámite (PUT)
    Todos los campos son opcionales
    """
    titulo: Optional[str] = None
    titulo_abreviado: Optional[str] = None
    description: Optional[str] = None
    fecha_ultima_actualizacion: Optional[str] = None
    definicion: Optional[str] = None
    destinatarios: Optional[str] = None
    consejo_puntano: Optional[str] = None
    fuentes_informacion: Optional[str] = None

class Tramite(TramiteBase):
    """
    Para DEVOLVER un trámite completo (GET)
    Incluye todas las relaciones
    """
    id: int
    costo: Optional[Costo] = None  # Relación 1:1
    requisitos: List[Requisito] = []  # Relación N:M
    sedes: List[Sede] = []  # Relación N:M
    
    class Config:
        from_attributes = True


# ============================================================================
# SCHEMAS SIMPLIFICADOS (para respuestas rápidas)
# ============================================================================

class TramiteSimple(TramiteBase):
    """
    Versión simplificada de un trámite
    Útil para listar trámites sin cargar todas las relaciones
    """
    id: int
    
    class Config:
        from_attributes = True


class TramiteConRequisitos(TramiteBase):
    """
    Trámite con solo sus requisitos
    Útil para páginas de requisitos
    """
    id: int
    requisitos: List[Requisito] = []
    
    class Config:
        from_attributes = True


class TramiteConSedes(TramiteBase):
    """
    Trámite con solo sus sedes
    Útil para páginas de ubicaciones
    """
    id: int
    sedes: List[Sede] = []
    
    class Config:
        from_attributes = True


class TramiteCompleto(TramiteBase):
    """
    Trámite con TODAS las relaciones
    Útil para detalle completo del trámite
    """
    id: int
    costo: Optional[Costo] = None
    requisitos: List[Requisito] = []
    sedes: List[Sede] = []
    
    class Config:
        from_attributes = True


# ============================================================================
# SCHEMAS PARA RELACIONES (Tramite-Requisito con atributos)
# ============================================================================

class TramiteRequisitoAsociacion(BaseModel):
    """
    Para CREAR la asociación entre trámite y requisito
    Incluye los atributos de la relación: obligatorio y orden
    """
    requisito_id: int
    obligatorio: bool = True
    orden: int

class TramiteRequisitoRespuesta(BaseModel):
    """
    Para DEVOLVER la asociación con toda la info
    """
    requisito: Requisito
    obligatorio: bool
    orden: int
    
    class Config:
        from_attributes = True


# ============================================================================
# SCHEMAS PARA RESPUESTAS DE LISTADO
# ============================================================================

class TramiteLista(BaseModel):
    """
    Para DEVOLVER un listado paginado de trámites
    """
    total: int
    pagina: int
    por_pagina: int
    tramites: List[TramiteSimple]