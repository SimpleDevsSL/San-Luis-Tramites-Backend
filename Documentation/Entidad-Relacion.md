# San Luis Trámites Backend – Modelo Entidad-Relación (Corregido)

## Entidades

* Tramites
* Requisitos
* Costos
* Sede

---

## Especificación de Entidades

### Tramites

Tramites = {id, title, titulo_abreviado, description, fecha_ultima_actualizacion, definicion, destinatarios, consejo_puntano, fuentes_informacion}

* id: Integer (identificador único del trámite)
* title: String
* titulo_abreviado: String
* description: String
* fecha_ultima_actualizacion: Date
* definicion: String
* destinatarios: String
* consejo_puntano: String
* fuentes_informacion: String

---

### Requisitos

Requisitos = {id, detalle}

* id: Integer (identificador único del requisito)
* detalle: String (ej: "DNI original en vigencia")

---

### Costos

Costos = {id, monto, fecha_actualizacion}

* id: Integer
* monto: Decimal
* fecha_actualizacion: Date

---

### Sede

Sede = {id, direccion, horarios, url_mapa}

* id: Integer
* direccion: String
* horarios: String
* url_mapa: String

---

## Relaciones

### Tramites – Requisitos

**Cardinalidad:** N:M

* Un trámite puede requerir múltiples requisitos.
* Un requisito puede estar asociado a múltiples trámites.

La relación puede tener atributos propios:

* obligatorio (Boolean)
* orden (Integer)

---

### Tramites – Sede

**Cardinalidad:** N:M

* Un trámite puede realizarse en varias sedes.
* Una sede puede ofrecer múltiples trámites.

---

### Tramites – Costos

**Cardinalidad:** 1:1

* Cada trámite posee un único costo asociado.
* El costo corresponde exclusivamente a ese trámite.

Nota: Para los enlaces oficiales (enlacesOficiales), se podría considerar una entidad adicional "EnlacesOficiales" si se expande en el futuro, pero por ahora se puede manejar como un campo adicional en Tramites si es necesario.

## Diagrama
![Diagrama ER del sistema de trámites](Tramites_ER.png)
