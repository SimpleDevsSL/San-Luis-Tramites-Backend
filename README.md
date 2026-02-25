# San-Luis-Tramites-Backend

Documento mínimo para arrancar el proyecto localmente (FastAPI + SQLite).

Requisitos
- Python 3.11 or 3.12 recomendado (SQLAlchemy en requirements.txt puede no ser compatible con Python 3.14).
- Git

Pasos rápidos (Linux)

1. Clonar y entrar al directorio Backend
```bash
git clone <repo-url>
cd San-Luis-Tramites-Backend/Backend
```

2. Crear y activar el entorno virtual
```bash
python -m venv venv
source venv/bin/activate
```

3. Instalar dependencias
```bash
pip install -r requirements.txt
```
(archivo de dependencias: [Backend/requirements.txt](Backend/requirements.txt))

4. Levantar la API con uvicorn
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```
- App principal: [Backend/main.py](Backend/main.py)  
- Documentación interactiva: http://localhost:8000/docs

5. Cargar datos de prueba
```bash
python load_data.py
```
- Script de carga: [Backend/load_data.py](Backend/load_data.py)  
- Crea/usa la base SQLite en `Backend/tramites.db` (configuración en [Backend/database.py](Backend/database.py))

Qué hace `load_data.py`
- Borra datos existentes y carga un conjunto de trámites, requisitos, costos y sedes de ejemplo en la BD SQLite para pruebas.

Notas
- Cambios al modelo relacional: ver [Backend/models.py](Backend/models.py) y los esquemas en [Backend/schemas.py](Backend/schemas.py).
- Si usas Python 3.14 y ves errores de SQLAlchemy, baja a Python 3.11/3.12 o actualiza SQLAlchemy.
