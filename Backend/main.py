from fastapi import FastAPI

app = FastAPI()

tramites = [
  {
    "slug": "cipe",
    "title": "CIPE (DNI Provincial)",
    "shortTitle": "CIPE",
    "description": "La Cedula de Identidad Provincial Electronica es tu documento de identidad provincial. Te explicamos como sacarla paso a paso.",
    "lastUpdated": "Enero 2026",
    "queEs": "El CIPE es la Cedula de Identidad Provincial Electronica de San Luis. Funciona como un complemento de tu DNI y es obligatoria para realizar muchos tramites provinciales.",
    "paraQuienEs": "Para todas las personas que residen en la provincia de San Luis y necesitan realizar tramites provinciales o acceder a servicios del gobierno provincial.",
    "requisitos": [
      "DNI original (argentino, en vigencia)",
      "Fotocopia de DNI (frente y dorso)",
      "Comprobante de domicilio (boleta de servicio a tu nombre o certificado de domicilio)",
      "Una foto 4x4 (en algunos puntos la toman en el momento)",
    ],
    "costo": {
      "monto": "Consultar valor actualizado en el sitio oficial (variable segun tipo de tramite)",
      "formasDePago": ["Efectivo", "Transferencia bancaria", "Pago electronico"],
      "actualizacion": "Enero 2026",
    },
    "dondeYCuando": {
      "direccion": "Centro de Tramites, Terrazas del Portezuelo, Autopista Serranias Puntanas Km 783, San Luis Capital",
      "horarios": "Lunes a viernes de 8:00 a 14:00 hs",
      "mapsUrl": "https://maps.google.com/?q=Terrazas+del+Portezuelo+San+Luis",
    },
    "trucoPuntano": "Anda temprano, antes de las 8:30. Despues de las 9 la fila crece rapido. Lleva toda la documentacion en una carpeta porque si te falta algo te mandan de vuelta.",
    "enlacesOficiales": [
      {"label": "Web Oficial – Sacar turno CIPE", "url": "https://tramites.sanluis.gob.ar"},
    ],
    "fuentes": "Informacion basada en datos publicados en tramites.sanluis.gob.ar al dia Enero 2026.",
  },
  {
    "slug": "licencia-de-conducir",
    "title": "Licencia de Conducir – San Luis Capital",
    "shortTitle": "Licencia de Conducir",
    "description": "Todo lo que necesitas saber para sacar o renovar tu licencia de conducir en San Luis Capital, sin vueltas.",
    "lastUpdated": "Enero 2026",
    "queEs": "La licencia de conducir es el permiso obligatorio para poder manejar un vehiculo legalmente en la ciudad de San Luis.",
    "paraQuienEs": "Para cualquier persona con domicilio en San Luis Capital que necesite sacar su licencia por primera vez o renovarla.",
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
    "requisitosCategorias": [
      {
        "categoria": "Pagos obligatorios",
        "items": [
          "Libre deuda municipal",
          "Libre deuda del Juzgado de Faltas",
          "CENAT (Certificado Nacional de Antecedentes de Transito) – $6800 (se paga en Rapipago)",
          "Tasa Municipal – $4500",
          "Examen medico – $10.000",
        ],
      },
      {
        "categoria": "Cursos y certificados (imprimir ambos)",
        "items": [
          "Curso Nacional de Transito",
          "Curso de Genero",
          "Curso Estrellas Amarillas",
        ],
      },
      {
        "categoria": "Documentacion",
        "items": [
          "DNI",
          "Tarjeta Verde (Cedula del vehiculo)",
          "Seguro del vehiculo vigente",
        ],
      },
    ],
    "requisitosAviso": "Los certificados y papeles tienen una validez de 30 dias.",
    "costoDetalles": [
      {"concepto": "CENAT", "monto": "$6800"},
      {"concepto": "Tasa Municipal", "monto": "$4500"},
      {"concepto": "Examen Medico", "monto": "$10.000"},
      {"concepto": "Costo final de la licencia", "monto": "Depende de los años de validez que elijas"},
    ],
    "costo": {
      "monto": "El costo total depende de los años de validez que elijas para la licencia.",
      "formasDePago": ["Efectivo", "Rapipago"],
      "actualizacion": "Enero 2026",
    },
    "ubicaciones": [
      {
        "nombre": "Paso 1 – Solicitud inicial",
        "descripcion": "Dirigite a la Municipalidad (al frente de la UNSL) para solicitar turno y documentacion.",
      },
      {
        "nombre": "Paso 2 – Examen medico y foto",
        "descripcion": "Ingresa por la entrada lateral de la Municipalidad.",
      },
    ],
    "dondeYCuando": {
      "direccion": "Municipalidad de San Luis Capital",
      "horarios": "Lunes a viernes – consultar turnos disponibles",
      "mapsUrl": "https://maps.google.com/?q=Municipalidad+de+San+Luis",
    },
    "pasos": [
      {
        "titulo": "Preparacion Inicial",
        "descripcion": "Solicita turno y pedi todos los papeles necesarios en la Municipalidad.",
      },
      {
        "titulo": "Reunir Documentacion y Pagos",
        "descripcion": "Realiza todos los pagos y completa los cursos obligatorios. Imprimi los certificados.",
      },
      {
        "titulo": "Examen Medico",
        "descripcion": "Te sacan la foto, te entregan la planilla, vas al consultorio, pagas $10.000 y el medico firma la planilla.",
        "detalles": [
          "Te sacan la foto",
          "Te entregan planilla",
          "Vas al consultorio",
          "Pagas $10.000",
          "El medico firma la planilla",
        ],
      },
      {
        "titulo": "Examen Teorico",
        "descripcion": "Necesitas 45 respuestas correctas de 50. Consejo: Pedi el PDF con preguntas y respuestas para practicar.",
      },
      {
        "titulo": "Examen Practico",
        "descripcion": "Debes estacionar entre 2 conos y estacionar a 45 grados. Ir con el vehiculo y documentacion completa.",
        "detalles": [
          "Estacionar entre 2 conos",
          "Estacionar a 45 grados",
          "Ir con el vehiculo y documentacion completa",
        ],
      },
      {
        "titulo": "Pago Final",
        "descripcion": "Pagas los anos de validez y finalizas el tramite.",
      },
    ],
    "trucoPuntano": "Pedi el PDF con preguntas y respuestas para practicar el teorico. El curso solo no suele ser suficiente.",
    "enlacesOficiales": [
      {"label": "Web Oficial – Generar CENAT", "url": "https://www.argentina.gob.ar/cenat"},
      {"label": "Web Oficial – Sacar turno", "url": "https://www.sanluis.gob.ar"},
    ],
    "fuentes": "Informacion basada en datos brindados en la Municipalidad de San Luis y sitios oficiales al dia Enero 2026.",
  },
  {
    "slug": "rentas-automotor",
    "title": "Rentas – Impuesto Automotor",
    "shortTitle": "Impuesto Automotor",
    "description": "Como consultar, generar la boleta y pagar el impuesto automotor en la provincia de San Luis.",
    "lastUpdated": "Enero 2026",
    "queEs": "El impuesto automotor es un tributo provincial que pagas anualmente por cada vehiculo registrado a tu nombre en San Luis. Se gestiona a traves de la Direccion Provincial de Rentas.",
    "paraQuienEs": "Para todos los propietarios de vehiculos (autos, motos, camionetas, etc.) registrados en la provincia de San Luis.",
    "requisitos": [
      "DNI del titular",
      "Numero de dominio (patente del vehiculo)",
      "Titulo o cedula del automotor (para verificar datos)",
    ],
    "costo": {
      "monto": "El monto depende del modelo, año y valuacion del vehiculo. Se puede consultar online.",
      "formasDePago": ["Pago online con tarjeta", "Transferencia", "Efectivo en bancos habilitados", "Rapipago / Pago Facil"],
      "actualizacion": "Enero 2026",
    },
    "dondeYCuando": {
      "direccion": "Direccion Provincial de Rentas, Edificio de Rentas, San Luis Capital",
      "horarios": "Lunes a viernes de 8:00 a 13:00 hs. Atencion online 24/7.",
      "mapsUrl": "https://maps.google.com/?q=Rentas+San+Luis",
    },
    "trucoPuntano": "Podes generar la boleta y pagar todo desde la web, sin hacer fila. Si pagas antes del primer vencimiento, generalmente hay descuento por pronto pago.",
    "enlacesOficiales": [
      {"label": "Web Oficial – Generar boleta automotor", "url": "https://rentas.sanluis.gob.ar"},
    ],
    "fuentes": "Informacion basada en datos publicados en rentas.sanluis.gob.ar al dia Enero 2026.",
  },
  {
    "slug": "dosep",
    "title": "DOSEP – Afiliaciones y Ordenes",
    "shortTitle": "DOSEP",
    "description": "Guia para afiliarte a DOSEP o gestionar ordenes medicas en la obra social de empleados publicos de San Luis.",
    "lastUpdated": "Enero 2026",
    "queEs": "DOSEP es la obra social de los empleados publicos de la provincia de San Luis. Brinda cobertura medica, odontologica y farmaceutica.",
    "paraQuienEs": "Para empleados publicos de la provincia de San Luis y sus familiares directos (conyuge e hijos) que quieran afiliarse u obtener ordenes de atencion.",
    "requisitos": [
      "DNI original del titular",
      "CIPE vigente",
      "Ultimo recibo de sueldo",
      "Partida de nacimiento o libreta de matrimonio (para agregar familiares)",
      "DNI de los familiares a cargo",
    ],
    "costo": {
      "monto": "La afiliacion no tiene costo adicional al descuento de haberes. Las ordenes pueden tener coseguros segun la practica.",
      "formasDePago": ["Descuento por recibo de haberes", "Coseguros en efectivo o debito"],
      "actualizacion": "Enero 2026",
    },
    "dondeYCuando": {
      "direccion": "DOSEP Central, Av. Illia y Junin, San Luis Capital",
      "horarios": "Lunes a viernes de 7:00 a 13:00 hs",
      "mapsUrl": "https://maps.google.com/?q=DOSEP+San+Luis",
    },
    "trucoPuntano": "Muchas ordenes medicas se pueden gestionar online desde el portal de DOSEP. Revisa primero ahi antes de ir personalmente. Si vas presencial, anda antes de las 8.",
    "enlacesOficiales": [
      {"label": "Web Oficial – Portal DOSEP", "url": "https://www.dosep.sanluis.gob.ar"},
    ],
    "fuentes": "Informacion basada en datos publicados en dosep.sanluis.gob.ar al dia Enero 2026.",
  },
  {
    "slug": "boleto-estudiantil",
    "title": "Boleto Estudiantil Gratuito",
    "shortTitle": "Boleto Estudiantil",
    "description": "Como tramitar el boleto estudiantil gratuito para viajar en colectivo en San Luis siendo estudiante.",
    "lastUpdated": "Enero 2026",
    "queEs": "El Boleto Estudiantil Gratuito es un beneficio provincial que permite a los estudiantes viajar gratis en el transporte publico de colectivos dentro de San Luis.",
    "paraQuienEs": "Para estudiantes regulares de nivel primario, secundario, terciario y universitario que residan en San Luis y usen el transporte publico.",
    "requisitos": [
      "DNI original",
      "CIPE vigente",
      "Certificado de alumno regular actualizado (emitido por la institucion educativa)",
      "Comprobante de domicilio",
      "Foto 4x4 (en algunos casos se toma en el momento)",
    ],
    "costo": {
      "monto": "Gratuito. No tiene costo.",
      "formasDePago": [],
      "actualizacion": "Enero 2026",
    },
    "dondeYCuando": {
      "direccion": "Centros de tramites habilitados y puntos especificos durante campanas de inscripcion. Consultar ubicaciones actualizadas en la web oficial.",
      "horarios": "Lunes a viernes de 8:00 a 14:00 hs (durante periodo de inscripcion)",
      "mapsUrl": "https://maps.google.com/?q=Centro+de+Tramites+San+Luis",
    },
    "trucoPuntano": "Hacelo ni bien arranca el periodo de inscripcion porque despues hay mucha demanda y se forman filas largas. Tene el certificado de alumno regular listo con anticipacion.",
    "enlacesOficiales": [
      {"label": "Web Oficial – Boleto Estudiantil", "url": "https://www.sanluis.gob.ar"},
    ],
    "fuentes": "Informacion basada en datos publicados en sanluis.gob.ar al dia Enero 2026.",
  },
]

@app.get("/get-all-tramites")
def get_all_tramites():
    return tramites

@app.get("/health")
def health_check():
    return {"status": "ok"}