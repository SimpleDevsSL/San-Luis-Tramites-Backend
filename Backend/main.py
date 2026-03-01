from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc
from database import engine, SessionLocal, Base
from models import Tramite as TramiteModel, Requisito as RequisitoModel, Costo as CostoModel, Sede as SedeModel
from schemas import (
    Tramite, TramiteCreate, TramiteUpdate, TramiteSimple, TramiteCompleto,
    Requisito, RequisitoCreate,
    Costo, CostoCreate,
    Sede, SedeCreate,
    TramiteRequisitoAsociacion
)
from typing import List
from fastapi.middleware.cors import CORSMiddleware

# Crear las tablas en la BD (si no existen)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="San Luis Trámites API",
    description="API para gestionar trámites de la provincia de San Luis",
    version="1.0.0"
)

# Permitir orígenes de desarrollo (ajustar puertos según tu frontend)
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # usar ["*"] solo en desarrollo si hace falta
    allow_credentials=True,     # True si envías cookies/credentials
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# DEPENDENCIA: Obtener sesión de BD
# ============================================================================
def get_db():
    """Proporciona una sesión de BD a cada endpoint"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ============================================================================
# ENDPOINTS: HEALTH CHECK
# ============================================================================

@app.get("/health", tags=["Health"])
def health_check():
    """Verifica que el servidor está activo"""
    return {"status": "ok", "message": "Servidor activo"}


# ============================================================================
# ENDPOINTS: REQUISITOS
# ============================================================================

@app.post("/requisitos/", response_model=Requisito, tags=["Requisitos"])
def crear_requisito(requisito: RequisitoCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo requisito
    
    **Ejemplo:**
    ```json
    {
        "detalle": "DNI original en vigencia"
    }
    ```
    """
    db_requisito = RequisitoModel(**requisito.dict())
    db.add(db_requisito)
    db.commit()
    db.refresh(db_requisito)
    return db_requisito


@app.get("/requisitos/", response_model=List[Requisito], tags=["Requisitos"])
def listar_requisitos(db: Session = Depends(get_db)):
    """Lista todos los requisitos"""
    requisitos = db.query(RequisitoModel).all()
    return requisitos


@app.get("/requisitos/{requisito_id}", response_model=Requisito, tags=["Requisitos"])
def obtener_requisito(requisito_id: int, db: Session = Depends(get_db)):
    """Obtiene un requisito por ID"""
    requisito = db.query(RequisitoModel).filter(RequisitoModel.id == requisito_id).first()
    if not requisito:
        raise HTTPException(status_code=404, detail="Requisito no encontrado")
    return requisito


@app.delete("/requisitos/{requisito_id}", tags=["Requisitos"])
def eliminar_requisito(requisito_id: int, db: Session = Depends(get_db)):
    """Elimina un requisito"""
    requisito = db.query(RequisitoModel).filter(RequisitoModel.id == requisito_id).first()
    if not requisito:
        raise HTTPException(status_code=404, detail="Requisito no encontrado")
    db.delete(requisito)
    db.commit()
    return {"message": f"Requisito {requisito_id} eliminado"}


# ============================================================================
# ENDPOINTS: COSTOS
# ============================================================================

@app.post("/costos/", response_model=Costo, tags=["Costos"])
def crear_costo(costo: CostoCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo costo
    
    **Ejemplo:**
    ```json
    {
        "monto": 100.50,
        "fecha_actualizacion": "Enero 2026",
        "formas_pago": "Efectivo, Transferencia"
    }
    ```
    """
    db_costo = CostoModel(**costo.dict())
    db.add(db_costo)
    db.commit()
    db.refresh(db_costo)
    return db_costo


@app.get("/costos/", response_model=List[Costo], tags=["Costos"])
def listar_costos(db: Session = Depends(get_db)):
    """Lista todos los costos"""
    costos = db.query(CostoModel).all()
    return costos


@app.get("/costos/{costo_id}", response_model=Costo, tags=["Costos"])
def obtener_costo(costo_id: int, db: Session = Depends(get_db)):
    """Obtiene un costo por ID"""
    costo = db.query(CostoModel).filter(CostoModel.id == costo_id).first()
    if not costo:
        raise HTTPException(status_code=404, detail="Costo no encontrado")
    return costo


@app.put("/costos/{costo_id}", response_model=Costo, tags=["Costos"])
def actualizar_costo(costo_id: int, costo_data: CostoCreate, db: Session = Depends(get_db)):
    """Actualiza un costo"""
    costo = db.query(CostoModel).filter(CostoModel.id == costo_id).first()
    if not costo:
        raise HTTPException(status_code=404, detail="Costo no encontrado")
    
    datos = costo_data.dict(exclude_unset=True)
    for clave, valor in datos.items():
        setattr(costo, clave, valor)
    
    db.commit()
    db.refresh(costo)
    return costo


# ============================================================================
# ENDPOINTS: SEDES
# ============================================================================

@app.post("/sedes/", response_model=Sede, tags=["Sedes"])
def crear_sede(sede: SedeCreate, db: Session = Depends(get_db)):
    """
    Crea una nueva sede
    
    **Ejemplo:**
    ```json
    {
        "direccion": "Terrazas del Portezuelo, Km 783",
        "horarios": "Lunes a viernes de 8:00 a 14:00 hs",
        "url_mapa": "https://maps.google.com/?q=..."
    }
    ```
    """
    db_sede = SedeModel(**sede.dict())
    db.add(db_sede)
    db.commit()
    db.refresh(db_sede)
    return db_sede


@app.get("/sedes/", response_model=List[Sede], tags=["Sedes"])
def listar_sedes(db: Session = Depends(get_db)):
    """Lista todas las sedes"""
    sedes = db.query(SedeModel).all()
    return sedes


@app.get("/sedes/{sede_id}", response_model=Sede, tags=["Sedes"])
def obtener_sede(sede_id: int, db: Session = Depends(get_db)):
    """Obtiene una sede por ID"""
    sede = db.query(SedeModel).filter(SedeModel.id == sede_id).first()
    if not sede:
        raise HTTPException(status_code=404, detail="Sede no encontrada")
    return sede


@app.delete("/sedes/{sede_id}", tags=["Sedes"])
def eliminar_sede(sede_id: int, db: Session = Depends(get_db)):
    """Elimina una sede"""
    sede = db.query(SedeModel).filter(SedeModel.id == sede_id).first()
    if not sede:
        raise HTTPException(status_code=404, detail="Sede no encontrada")
    db.delete(sede)
    db.commit()
    return {"message": f"Sede {sede_id} eliminada"}


# ============================================================================
# ENDPOINTS: TRÁMITES (CRUD básico)
# ============================================================================

@app.post("/tramites/", response_model=TramiteCompleto, tags=["Trámites"])
def crear_tramite(tramite: TramiteCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo trámite
    
    **Ejemplo:**
    ```json
    {
        "titulo": "CIPE (DNI Provincial)",
        "titulo_abreviado": "CIPE",
        "description": "La Cedula de Identidad Provincial...",
        "fecha_ultima_actualizacion": "Enero 2026",
        "definicion": "El CIPE es...",
        "destinatarios": "Para todas las personas...",
        "consejo_puntano": "Anda temprano...",
        "fuentes_informacion": "Basado en..."
    }
    ```
    """
    db_tramite = TramiteModel(**tramite.dict())
    db.add(db_tramite)
    db.commit()
    db.refresh(db_tramite)
    return db_tramite


@app.get("/tramites/", response_model=List[TramiteCompleto], tags=["Trámites"])
def listar_tramites(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Lista todos los trámites (versión simplificada)
    
    **Parámetros:**
    - `skip`: Cantidad de registros a saltar (para paginación)
    - `limit`: Máximo de registros a devolver
    """
    tramites = db.query(TramiteModel).offset(skip).limit(limit).all()
    return tramites


@app.get("/tramites/{tramite_id}", response_model=TramiteCompleto, tags=["Trámites"])
def obtener_tramite(tramite_id: int, db: Session = Depends(get_db)):
    """Obtiene un trámite completo con todas sus relaciones"""
    tramite = db.query(TramiteModel).filter(TramiteModel.id == tramite_id).first()
    if not tramite:
        raise HTTPException(status_code=404, detail="Trámite no encontrado")
    return tramite


@app.put("/tramites/{tramite_id}", response_model=TramiteCompleto, tags=["Trámites"])
def actualizar_tramite(tramite_id: int, tramite_data: TramiteUpdate, db: Session = Depends(get_db)):
    """
    Actualiza un trámite
    
    **Nota:** Solo se actualizan los campos que envíes
    """
    tramite = db.query(TramiteModel).filter(TramiteModel.id == tramite_id).first()
    if not tramite:
        raise HTTPException(status_code=404, detail="Trámite no encontrado")
    
    # Solo actualiza campos que fueron enviados (exclude_unset=True)
    datos = tramite_data.dict(exclude_unset=True)
    for clave, valor in datos.items():
        setattr(tramite, clave, valor)
    
    db.commit()
    db.refresh(tramite)
    return tramite


@app.delete("/tramites/{tramite_id}", tags=["Trámites"])
def eliminar_tramite(tramite_id: int, db: Session = Depends(get_db)):
    """Elimina un trámite"""
    tramite = db.query(TramiteModel).filter(TramiteModel.id == tramite_id).first()
    if not tramite:
        raise HTTPException(status_code=404, detail="Trámite no encontrado")
    db.delete(tramite)
    db.commit()
    return {"message": f"Trámite {tramite_id} eliminado"}


# ============================================================================
# ENDPOINTS: ASOCIAR REQUISITOS A TRÁMITES (N:M)
# ============================================================================

@app.post("/tramites/{tramite_id}/requisitos/", tags=["Trámites"])
def agregar_requisito_a_tramite(
    tramite_id: int,
    asociacion: TramiteRequisitoAsociacion,
    db: Session = Depends(get_db)
):
    """
    Asocia un requisito a un trámite
    
    **Ejemplo:**
    ```json
    {
        "requisito_id": 1,
        "obligatorio": true,
        "orden": 1
    }
    ```
    """
    tramite = db.query(TramiteModel).filter(TramiteModel.id == tramite_id).first()
    if not tramite:
        raise HTTPException(status_code=404, detail="Trámite no encontrado")
    
    requisito = db.query(RequisitoModel).filter(RequisitoModel.id == asociacion.requisito_id).first()
    if not requisito:
        raise HTTPException(status_code=404, detail="Requisito no encontrado")
    
    # Verificar si ya está asociado
    if requisito in tramite.requisitos:
        raise HTTPException(status_code=400, detail="El requisito ya está asociado a este trámite")
    
    tramite.requisitos.append(requisito)
    db.commit()
    db.refresh(tramite)
    
    return {"message": "Requisito agregado al trámite", "tramite": tramite}


@app.delete("/tramites/{tramite_id}/requisitos/{requisito_id}", tags=["Trámites"])
def remover_requisito_de_tramite(tramite_id: int, requisito_id: int, db: Session = Depends(get_db)):
    """Desasocia un requisito de un trámite"""
    tramite = db.query(TramiteModel).filter(TramiteModel.id == tramite_id).first()
    if not tramite:
        raise HTTPException(status_code=404, detail="Trámite no encontrado")
    
    requisito = db.query(RequisitoModel).filter(RequisitoModel.id == requisito_id).first()
    if not requisito:
        raise HTTPException(status_code=404, detail="Requisito no encontrado")
    
    if requisito not in tramite.requisitos:
        raise HTTPException(status_code=400, detail="El requisito no está asociado a este trámite")
    
    tramite.requisitos.remove(requisito)
    db.commit()
    
    return {"message": "Requisito removido del trámite"}


# ============================================================================
# ENDPOINTS: ASOCIAR SEDES A TRÁMITES (N:M)
# ============================================================================

@app.post("/tramites/{tramite_id}/sedes/", tags=["Trámites"])
def agregar_sede_a_tramite(tramite_id: int, sede_id: int, db: Session = Depends(get_db)):
    """Asocia una sede a un trámite"""
    tramite = db.query(TramiteModel).filter(TramiteModel.id == tramite_id).first()
    if not tramite:
        raise HTTPException(status_code=404, detail="Trámite no encontrado")
    
    sede = db.query(SedeModel).filter(SedeModel.id == sede_id).first()
    if not sede:
        raise HTTPException(status_code=404, detail="Sede no encontrada")
    
    if sede in tramite.sedes:
        raise HTTPException(status_code=400, detail="La sede ya está asociada a este trámite")
    
    tramite.sedes.append(sede)
    db.commit()
    db.refresh(tramite)
    
    return {"message": "Sede agregada al trámite"}


@app.delete("/tramites/{tramite_id}/sedes/{sede_id}", tags=["Trámites"])
def remover_sede_de_tramite(tramite_id: int, sede_id: int, db: Session = Depends(get_db)):
    """Desasocia una sede de un trámite"""
    tramite = db.query(TramiteModel).filter(TramiteModel.id == tramite_id).first()
    if not tramite:
        raise HTTPException(status_code=404, detail="Trámite no encontrado")
    
    sede = db.query(SedeModel).filter(SedeModel.id == sede_id).first()
    if not sede:
        raise HTTPException(status_code=404, detail="Sede no encontrada")
    
    if sede not in tramite.sedes:
        raise HTTPException(status_code=400, detail="La sede no está asociada a este trámite")
    
    tramite.sedes.remove(sede)
    db.commit()
    
    return {"message": "Sede removida del trámite"}


# ============================================================================
# ENDPOINTS: ASOCIAR COSTO A TRÁMITE (1:1)
# ============================================================================

@app.post("/tramites/{tramite_id}/costo/", tags=["Trámites"])
def asignar_costo_a_tramite(tramite_id: int, costo_id: int, db: Session = Depends(get_db)):
    """Asigna un costo a un trámite"""
    tramite = db.query(TramiteModel).filter(TramiteModel.id == tramite_id).first()
    if not tramite:
        raise HTTPException(status_code=404, detail="Trámite no encontrado")
    
    costo = db.query(CostoModel).filter(CostoModel.id == costo_id).first()
    if not costo:
        raise HTTPException(status_code=404, detail="Costo no encontrado")
    
    tramite.costo_id = costo.id
    db.commit()
    db.refresh(tramite)
    
    return {"message": "Costo asignado al trámite"}


@app.delete("/tramites/{tramite_id}/costo/", tags=["Trámites"])
def remover_costo_de_tramite(tramite_id: int, db: Session = Depends(get_db)):
    """Desasocia el costo de un trámite"""
    tramite = db.query(TramiteModel).filter(TramiteModel.id == tramite_id).first()
    if not tramite:
        raise HTTPException(status_code=404, detail="Trámite no encontrado")
    
    tramite.costo_id = None
    db.commit()
    
    return {"message": "Costo removido del trámite"}