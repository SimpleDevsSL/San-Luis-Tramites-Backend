"""
Script para cargar datos de prueba en la base de datos
Uso: python load_data.py
"""

from sqlalchemy.orm import Session
from database import SessionLocal, Base, engine
from models import Tramite as TramiteModel, Requisito as RequisitoModel, Costo as CostoModel, Sede as SedeModel
from decimal import Decimal

# Crear todas las tablas
Base.metadata.create_all(bind=engine)

# Datos de prueba (los datos que tenías en main.py)
DATOS_TRAMITES = [
    {
        "titulo": "CIPE (DNI Provincial)",
        "titulo_abreviado": "CIPE",
        "description": "La Cedula de Identidad Provincial Electronica es tu documento de identidad provincial. Te explicamos como sacarla paso a paso.",
        "fecha_ultima_actualizacion": "Enero 2026",
        "definicion": "El CIPE es la Cedula de Identidad Provincial Electronica de San Luis. Funciona como un complemento de tu DNI y es obligatoria para realizar muchos tramites provinciales.",
        "destinatarios": "Para todas las personas que residen en la provincia de San Luis y necesitan realizar tramites provinciales o acceder a servicios del gobierno provincial.",
        "consejo_puntano": "Anda temprano, antes de las 8:30. Despues de las 9 la fila crece rapido. Lleva toda la documentacion en una carpeta porque si te falta algo te mandan de vuelta.",
        "fuentes_informacion": "Informacion basada en datos publicados en tramites.sanluis.gob.ar al dia Enero 2026.",
        "requisitos": [
            "DNI original (argentino, en vigencia)",
            "Fotocopia de DNI (frente y dorso)",
            "Comprobante de domicilio (boleta de servicio a tu nombre o certificado de domicilio)",
            "Una foto 4x4 (en algunos puntos la toman en el momento)",
        ],
        "costo": {
            "monto": Decimal("0.00"),
            "fecha_actualizacion": "Enero 2026",
            "formas_pago": "Consultar valor actualizado en el sitio oficial (variable segun tipo de tramite)"
        },
        "sede": {
            "direccion": "Centro de Tramites, Terrazas del Portezuelo, Autopista Serranias Puntanas Km 783, San Luis Capital",
            "horarios": "Lunes a viernes de 8:00 a 14:00 hs",
            "url_mapa": "https://maps.google.com/?q=Terrazas+del+Portezuelo+San+Luis"
        }
    },
    {
        "titulo": "Licencia de Conducir – San Luis Capital",
        "titulo_abreviado": "Licencia de Conducir",
        "description": "Todo lo que necesitas saber para sacar o renovar tu licencia de conducir en San Luis Capital, sin vueltas.",
        "fecha_ultima_actualizacion": "Enero 2026",
        "definicion": "La licencia de conducir es el permiso obligatorio para poder manejar un vehiculo legalmente en la ciudad de San Luis.",
        "destinatarios": "Para cualquier persona con domicilio en San Luis Capital que necesite sacar su licencia por primera vez o renovarla.",
        "consejo_puntano": "Pedi el PDF con preguntas y respuestas para practicar el teorico. El curso solo no suele ser suficiente.",
        "fuentes_informacion": "Informacion basada en datos brindados en la Municipalidad de San Luis y sitios oficiales al dia Enero 2026.",
        "requisitos": [
            "Libre deuda municipal",
            "Libre deuda del Juzgado de Faltas",
            "CENAT (Certificado Nacional de Antecedentes de Transito) – $6800 (se paga en Rapipago)",
            "Tasa Municipal – $4500",
            "Examen medico – $10.000",
            "Curso Nacional de Transito (imprimir certificado)",
            "Curso de Genero (imprimir certificado)",
            "Curso Estrellas Amarillas (imprimir certificado)",
            "DNI",
            "Tarjeta Verde (Cedula del vehiculo)",
            "Seguro del vehiculo vigente",
        ],
        "costo": {
            "monto": Decimal("21300.00"),
            "fecha_actualizacion": "Enero 2026",
            "formas_pago": "Efectivo, Rapipago"
        },
        "sede": {
            "direccion": "Municipalidad de San Luis Capital",
            "horarios": "Lunes a viernes – consultar turnos disponibles",
            "url_mapa": "https://maps.google.com/?q=Municipalidad+de+San+Luis"
        }
    },
    {
        "titulo": "Rentas – Impuesto Automotor",
        "titulo_abreviado": "Impuesto Automotor",
        "description": "Como consultar, generar la boleta y pagar el impuesto automotor en la provincia de San Luis.",
        "fecha_ultima_actualizacion": "Enero 2026",
        "definicion": "El impuesto automotor es un tributo provincial que pagas anualmente por cada vehiculo registrado a tu nombre en San Luis. Se gestiona a traves de la Direccion Provincial de Rentas.",
        "destinatarios": "Para todos los propietarios de vehiculos (autos, motos, camionetas, etc.) registrados en la provincia de San Luis.",
        "consejo_puntano": "Podes generar la boleta y pagar todo desde la web, sin hacer fila. Si pagas antes del primer vencimiento, generalmente hay descuento por pronto pago.",
        "fuentes_informacion": "Informacion basada en datos publicados en rentas.sanluis.gob.ar al dia Enero 2026.",
        "requisitos": [
            "DNI del titular",
            "Numero de dominio (patente del vehiculo)",
            "Titulo o cedula del automotor (para verificar datos)",
        ],
        "costo": {
            "monto": Decimal("0.00"),
            "fecha_actualizacion": "Enero 2026",
            "formas_pago": "Pago online con tarjeta, Transferencia, Efectivo en bancos habilitados, Rapipago / Pago Facil"
        },
        "sede": {
            "direccion": "Direccion Provincial de Rentas, Edificio de Rentas, San Luis Capital",
            "horarios": "Lunes a viernes de 8:00 a 13:00 hs. Atencion online 24/7.",
            "url_mapa": "https://maps.google.com/?q=Rentas+San+Luis"
        }
    },
    {
        "titulo": "DOSEP – Afiliaciones y Ordenes",
        "titulo_abreviado": "DOSEP",
        "description": "Guia para afiliarte a DOSEP o gestionar ordenes medicas en la obra social de empleados publicos de San Luis.",
        "fecha_ultima_actualizacion": "Enero 2026",
        "definicion": "DOSEP es la obra social de los empleados publicos de la provincia de San Luis. Brinda cobertura medica, odontologica y farmaceutica.",
        "destinatarios": "Para empleados publicos de la provincia de San Luis y sus familiares directos (conyuge e hijos) que quieran afiliarse u obtener ordenes de atencion.",
        "consejo_puntano": "Muchas ordenes medicas se pueden gestionar online desde el portal de DOSEP. Revisa primero ahi antes de ir personalmente. Si vas presencial, anda antes de las 8.",
        "fuentes_informacion": "Informacion basada en datos publicados en dosep.sanluis.gob.ar al dia Enero 2026.",
        "requisitos": [
            "DNI original del titular",
            "CIPE vigente",
            "Ultimo recibo de sueldo",
            "Partida de nacimiento o libreta de matrimonio (para agregar familiares)",
            "DNI de los familiares a cargo",
        ],
        "costo": {
            "monto": Decimal("0.00"),
            "fecha_actualizacion": "Enero 2026",
            "formas_pago": "Descuento por recibo de haberes, Coseguros en efectivo o debito"
        },
        "sede": {
            "direccion": "DOSEP Central, Av. Illia y Junin, San Luis Capital",
            "horarios": "Lunes a viernes de 7:00 a 13:00 hs",
            "url_mapa": "https://maps.google.com/?q=DOSEP+San+Luis"
        }
    },
    {
        "titulo": "Boleto Estudiantil Gratuito",
        "titulo_abreviado": "Boleto Estudiantil",
        "description": "Como tramitar el boleto estudiantil gratuito para viajar en colectivo en San Luis siendo estudiante.",
        "fecha_ultima_actualizacion": "Enero 2026",
        "definicion": "El Boleto Estudiantil Gratuito es un beneficio provincial que permite a los estudiantes viajar gratis en el transporte publico de colectivos dentro de San Luis.",
        "destinatarios": "Para estudiantes regulares de nivel primario, secundario, terciario y universitario que residan en San Luis y usen el transporte publico.",
        "consejo_puntano": "Hacelo ni bien arranca el periodo de inscripcion porque despues hay mucha demanda y se forman filas largas. Tene el certificado de alumno regular listo con anticipacion.",
        "fuentes_informacion": "Informacion basada en datos publicados en sanluis.gob.ar al dia Enero 2026.",
        "requisitos": [
            "DNI original",
            "CIPE vigente",
            "Certificado de alumno regular actualizado (emitido por la institucion educativa)",
            "Comprobante de domicilio",
            "Foto 4x4 (en algunos casos se toma en el momento)",
        ],
        "costo": {
            "monto": Decimal("0.00"),
            "fecha_actualizacion": "Enero 2026",
            "formas_pago": "Gratuito"
        },
        "sede": {
            "direccion": "Centros de tramites habilitados y puntos especificos durante campanas de inscripcion. Consultar ubicaciones actualizadas en la web oficial.",
            "horarios": "Lunes a viernes de 8:00 a 14:00 hs (durante periodo de inscripcion)",
            "url_mapa": "https://maps.google.com/?q=Centro+de+Tramites+San+Luis"
        }
    },
]


def cargar_datos():
    """Carga los datos de prueba en la base de datos"""
    db = SessionLocal()
    
    try:
        print("🚀 Iniciando carga de datos...")
        
        # Limpiar datos existentes
        print("🗑️  Limpiando datos existentes...")
        db.query(TramiteModel).delete()
        db.query(RequisitoModel).delete()
        db.query(CostoModel).delete()
        db.query(SedeModel).delete()
        db.commit()
        
        for i, datos_tramite in enumerate(DATOS_TRAMITES, 1):
            print(f"\n📋 Cargando trámite {i}: {datos_tramite['titulo']}")
            
            # 1. Crear requisitos
            requisitos_objs = []
            for j, detalle_req in enumerate(datos_tramite['requisitos'], 1):
                req = RequisitoModel(detalle=detalle_req)
                db.add(req)
                db.flush()  # Para obtener el ID
                requisitos_objs.append(req)
                print(f"   ✅ Requisito {j}: {detalle_req[:50]}...")
            
            # 2. Crear costo
            datos_costo = datos_tramite['costo']
            costo = CostoModel(
                monto=datos_costo['monto'],
                fecha_actualizacion=datos_costo['fecha_actualizacion'],
                formas_pago=datos_costo['formas_pago']
            )
            db.add(costo)
            db.flush()
            print(f"   💰 Costo: ${datos_costo['monto']}")
            
            # 3. Crear sede
            datos_sede = datos_tramite['sede']
            sede = SedeModel(
                direccion=datos_sede['direccion'],
                horarios=datos_sede['horarios'],
                url_mapa=datos_sede['url_mapa']
            )
            db.add(sede)
            db.flush()
            print(f"   📍 Sede: {datos_sede['direccion'][:50]}...")
            
            # 4. Crear trámite
            tramite = TramiteModel(
                titulo=datos_tramite['titulo'],
                titulo_abreviado=datos_tramite['titulo_abreviado'],
                description=datos_tramite['description'],
                fecha_ultima_actualizacion=datos_tramite['fecha_ultima_actualizacion'],
                definicion=datos_tramite['definicion'],
                destinatarios=datos_tramite['destinatarios'],
                consejo_puntano=datos_tramite['consejo_puntano'],
                fuentes_informacion=datos_tramite['fuentes_informacion'],
                costo_id=costo.id
            )
            
            # 5. Asociar requisitos y sede al trámite
            for req in requisitos_objs:
                tramite.requisitos.append(req)
            tramite.sedes.append(sede)
            
            db.add(tramite)
            print(f"   📝 Trámite creado: {tramite.titulo}")
        
        # Confirmar todos los cambios
        db.commit()
        print("\n✨ ¡Datos cargados exitosamente!")
        print(f"✅ {len(DATOS_TRAMITES)} trámites cargados")
        
    except Exception as e:
        db.rollback()
        print(f"\n❌ Error al cargar datos: {str(e)}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    cargar_datos()