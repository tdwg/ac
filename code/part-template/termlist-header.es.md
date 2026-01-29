# Controlled Vocabulary for Audiovisual Core subjectPart: List of Terms

Title
: Controlled Vocabulary for Audiovisual Core subjectPart: List of Terms

IRI del espacio de nombres
: <http://rs.tdwg.org/acpart/values/>

Abreviatura de espacio de nombres preferida
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
: The Audiovisual Core term subjectPart describes the part of an organism morphology, behaviour, environment depicted in a media item or region of interest. The subjectPart Controlled Vocabulary provides terms that should be used as values for ac:subjectPart and its literal-valued analog ac:subjectPartLiteral.

Colaboradores
: {contributors}

Creador
: {creator}

Cita bibliográfica
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

## 1. Introducción (Informativa)

Este documento incluye términos destinados a ser utilizados como valores controlados para los términos del Audiovisual Core `ac:subjectPart` y `ac:subjectPartLiteral`. Una [representación JSON-LD](https://tdwg.github.io/rs.tdwg.org/cvJson/acpart.json) de este esquema de concepto SKOS está disponible (incluyendo traducciones a varios idiomas). Para más información sobre cómo utilizar este vocabulario, consulte la [guía del usuario de vocabularios controlados subjectPart y subjectOrientation](https://github.com/tdwg/ac/blob/master/views/views_user_guide.pdf).

### 1.1 Estado del contenido de este documento

La Sección 1 es informativa (no normativa).

La Sección 2 es normativa salvo que se indique lo contrario.

La Sección 3 es informativa.

En la Sección 4, los valores de `Término IRI`, `Definición` y `Valor controlado` son normativos. El valor de `Uso` (si existe para un término determinado) también es normativo.  El valor de `tiene un concepto más amplio` es normativo. Los valores del `Nombre del término` no son normativos, aunque se puede esperar que el prefijo del namespace abreviado sea uno comúnmente utilizado para ese namespace.  `Etiqueta` y los valores de todas las demás propiedades (como `Ejemplos` o `Notas`) no son normativos.

### 1.2 Palabras clave RFC 2119

Las palabras clave "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY" y "OPTIONAL" en este documento deben interpretarse como se describe en [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) y [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174), únicamente cuando aparezcan en mayúsculas, tal como se muestra aquí.

### 1.3 Reportes de comentarios de los usuarios

Para obtener una perspectiva sobre el desarrollo de esta [mejora de vocabulario](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md#4-vocabulary-enhancements), consulte el [Informe de requerimientos finales](https://github.com/tdwg/ac/blob/master/views/final-requirements.md) utilizado para determinar los requisitos del vocabulario. El Informe sobre la Experiencia de Implementación se publicó en _Biodiversity Information Science and Standards_ 7:e94188 y está disponible en <http://doi.org/10.3897/biss.7.94188>

## 2 Uso de los Términos

### 2.1 Relación de los tipos de valor con los términos de propiedad

De acuerdo con el documento [Lista de términos del Audiovisual Core](http://rs.tdwg.org/ac/doc/termlist/), los IRI de los términos no abreviados DEBEN usarse como valores de la propiedad `ac:subjectOrientation`. Las cadenas de valores controlados DEBEN usarse como valores de la propiedad `ac:subjectOrientationLiteral`.

### 2.2 Relaciones con otros esquemas conceptuales y colecciones (informativo)

Algunos valores particulares de `ac:subjectOrientation` son apropiados para algunos valores de `ac:subjectPart`. Las relaciones entre los conceptos en estos dos esquemas se describen mediante una [Colección SKOS serializada JSON-LD para cada parte del sujeto](https://tdwg.github.io/rs.tdwg.org/cvJson/acorient_collection.json) que designa qué orientaciones temáticas son apropiadas para esa parte. De manera similar, [se han establecido colecciones SKOS serializadas JSON-LD para algunos grupos de organismos](https://tdwg.github.io/rs.tdwg.org/cvJson/acpart_collection.json) para indicar qué partes del sujeto existen para los miembros de esos grupos. Estas colecciones se proporcionan para ayudar a los desarrolladores de aplicaciones a filtrar los conceptos que deben presentarse a los usuarios y también pueden usarse para la validación.

Hay disponibles listas de colecciones legibles por humanos de cadenas de valores controlados para [subjectPart](https://ac.tdwg.org/part_collections) y [subjectOrientation](https://ac.tdwg.org/orient_collections).

Ninguna de estas colecciones es normativa y se mantienen fuera del marco de estándares del Audiovisual Core para agilizar su desarrollo.

## 3 Índice de Términos
