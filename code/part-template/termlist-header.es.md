# {document_title}

Title
: {document_title}

Namespace IRI
: <http://rs.tdwg.org/acpart/values/>

Preferred namespace abbreviation
: acpart:

Fecha de publicación de la versión
: {ratification_date}

Fecha de creación
: {created_date}

Parte del Estándar TDWG
: <{standard_iri}>

Esta versión
: <{current_iri}{ratification_date}>

Última versión
: <{current_iri}>

{previous_version_slot}

Abstract
: {abstract}

Colaboradores
: {contributors}

Creador
: {creator}

Cita bibliográfica
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

## 1 Introduction (informative)

This document includes terms intended to be used as controlled values for the Audiovisual Core terms `ac:subjectPart` and `ac:subjectPartLiteral`. A [JSON-LD representation](https://tdwg.github.io/rs.tdwg.org/cvJson/acpart.json) (including translations to multiple languages) of this SKOS Concept Scheme is available. For more information about how to use this vocabulary, see the [subjectPart and subjectOrientation Controlled Vocabularies User Guide](https://github.com/tdwg/ac/blob/master/views/views_user_guide.pdf).

### 1.1 Estado del contenido de este documento

Section 1 is informative (non-normative).

Section 2 is normative except as noted.

Section 3 is informative.

En la Sección 4, los valores de `Término IRI`, `Definición` y `Valor controlado` son normativos. El valor de `Uso` (si existe para un término determinado) también es normativo.  El valor de `tiene un concepto más amplio` es normativo. Los valores del `Nombre del término` no son normativos, aunque se puede esperar que el prefijo del namespace abreviado sea uno comúnmente utilizado para ese namespace.  `Label` and the values of all other properties (such as `Examples` or `Notes`) are non-normative.

### 1.2 Palabras clave RFC 2119

Las palabras clave "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY" y "OPTIONAL" en este documento deben interpretarse como se describe en [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) y [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174), únicamente cuando aparezcan en mayúsculas, tal como se muestra aquí.

### 1.3 User feedback reports

For perspective on the development of this [vocabulary enhancement](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md#4-vocabulary-enhancements), refer to the [final Feature Report](https://github.com/tdwg/ac/blob/master/views/final-requirements.md) used to determine the requirements for the vocabulary. The Implementation Experience Report was published in _Biodiversity Information Science and Standards_ 7:e94188 and is available at <http://doi.org/10.3897/biss.7.94188>

## 2 Uso de los Términos

### 2.1 Relationship of value types to property terms

In accordance with the [Audiovisual Core Term List](http://rs.tdwg.org/ac/doc/termlist/) document, unabbreviated term IRIs MUST be used as values of the property `ac:subjectPart`. Controlled value strings SHOULD be used as values of the property `ac:subjectPartLiteral`.

### 2.2 Relationships with other concept schemes and collections (informative)

Particular `ac:subjectOrientation` values are appropriate for some `ac:subjectPart` values. The relationships between concepts in these two schemes are described by a [JSON-LD serialized SKOS Collection for each subject part](https://tdwg.github.io/rs.tdwg.org/cvJson/acorient_collection.json) that designates which subject orientations are appropriate for that part. Similarly, [JSON-LD serialized SKOS Collections have been established for some organism groups](https://tdwg.github.io/rs.tdwg.org/cvJson/acpart_collection.json) to indicate which subject parts exist for members of those groups. These collections are provided to aid application developers in filtering the concepts that should be presented to users and they may also be used for validation.

Human-readable collection lists of controlled value strings are available for [subjectPart](https://ac.tdwg.org/part_collections) and [subjectOrientation](https://ac.tdwg.org/orient_collections).

Neither of these Collections are normative and they are maintained outside of the Audiovisual Core standards framework in order to make their development agile.

## 3 Índice de Términos
