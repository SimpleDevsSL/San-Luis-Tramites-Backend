# San Luis Tramites Backend Modelo-Relacional

## Tablas:

* Tramites
* Requisitos
* Costos
* Sede
* Tramite_Requisito
* Tramite_Sede

---

## Especificación de Tablas



### Tramites

Tramites = {id, title, titulo_abreviado, description, fecha_ultima_actualizacion, definicion, destinatarios, consejo_puntano, fuentes_informacion, costo_id}

* id: Integer (clave primaria, identificador único del trámite)
* title: String
* titulo_abreviado: String
* description: Text
* fecha_ultima_actualizacion: Date
* definicion: Text
* destinatarios: Text
* consejo_puntano: Text
* fuentes_informacion: Text
* costo_id: Integer (clave foránea que referencia a Costos.id)

---

### Requisitos

Requisitos = {id, detalle}

* id: Integer (clave primaria, identificador único del requisito)
* detalle: String (ej: "DNI original en vigencia")

---

### Costos

Costos = {id, monto, fecha_actualizacion}

* id: Integer (clave primaria)
* monto: Decimal (monto del trámite)
* fecha_actualizacion: Date

---

### Sede

Sede = {id, direccion, horarios, url_mapa}

* id: Integer (clave primaria)
* direccion: String
* horarios: String
* url_mapa: String

---

### Tramite_Requisito

Tramite_Requisito = {tramite_id, requisito_id, obligatorio, orden}

* tramite_id: Integer (clave foránea que referencia a Tramites.id)
* requisito_id: Integer (clave foránea que referencia a Requisitos.id)
* obligatorio: Boolean
* orden: Integer

Clave primaria compuesta: {tramite_id, requisito_id}

---

### Tramite_Sede

Tramite_Sede = {tramite_id, sede_id}

* tramite_id: Integer (clave foránea que referencia a Tramites.id)
* sede_id: Integer (clave foránea que referencia a Sede.id)

Clave primaria compuesta: {tramite_id, sede_id}

---

## Relaciones (Implementadas en el Modelo Relacional)

* Tramites - Requisitos: Relación N:M implementada mediante la tabla intermedia Tramite_Requisito.
* Tramites - Sede: Relación N:M implementada mediante la tabla intermedia Tramite_Sede.
* Tramites - Costos: Relación 1:1 implementada mediante clave foránea costo_id en Tramites.

