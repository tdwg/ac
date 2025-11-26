# {document_title}

Título
: {document_title}

Espacio de nombres IRI
: <http://rs.tdwg.org/acformat/values/>

Abreviatura preferida del espacio de nombres
: acformat:

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

Resumen
: {abstract}

Colaboradores
: {contributors}

Creador
: {creator}

Cita bibliográfica
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

## 1. Introducción (Informativa)

Este documento incluye términos destinados a ser utilizados como un valor controlado para los términos de Dublin Core «dc:format» y «dcterms:format», que son tomados prestados por Audiovisual Core.

### 1.1 Estado del contenido de este documento

La Sección 1 es informativa (no normativa).

La Sección 2 es normativa salvo que se indique lo contrario.

La Sección 3 es informativa.

En la Sección 4, los valores de `Término IRI`, `Definición` y `Valor controlado` son normativos. El valor de `Uso` (si existe para un término determinado) también es normativo.  Los valores de `Tiene un concepto más amplio` y `Tiene coincidencia exacta` son normativos. Los valores del `Nombre del término` no son normativos, aunque se puede esperar que el prefijo del namespace abreviado sea uno comúnmente utilizado para ese namespace.  La `Etiqueta` y los valores de todas las demás propiedades no son normativos.

### 1.2 Palabras clave RFC 2119

Las palabras clave "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY" y "OPTIONAL" en este documento deben interpretarse como se describe en [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) y [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174), únicamente cuando aparezcan en mayúsculas, tal como se muestra aquí.

## 2 Uso de los Términos

### 2.1 Relación de los tipos de valor con los términos de propiedad

De acuerdo con el [documento de la Lista de términos básicos audiovisuales](http://rs.tdwg.org/ac/doc/termlist/), los términos IRI no abreviados DEBEN usarse como valores de la propiedad `dcterms:format`. Las cadenas de valores controlados DEBEN usarse como valores de la propiedad `dc:format`.

### 2.2 Relación entre conceptos y esquemas de conceptos

La entrada para la propiedad `dc:format` en el [documento de lista de términos del núcleo audiovisual](http://rs.tdwg.org/ac/doc/termlist/#dc_format) especifica que se RECOMIENDAN tres tipos de valores de cadena: tipos de medios de Internet (tipos MIME), valores de cadena especiales para medios físicos o extensiones de archivo de uso común. Este vocabulario controlado define dos esquemas de conceptos SKOS: un esquema de conceptos para tipos de medios y medios físicos (los primeros dos tipos de valores especificados para `dc:type`) y un esquema de conceptos para extensiones de archivos (el último tipo de valor recomendado). Debido a que la Autoridad de Números Asignados de Internet (IANA) mantiene un [registro de tipos de medios](https://www.iana.org/assignments/media-types/media-types.xhtml) y Audiovisual Core mantiene una lista controlada de tipos de medios físicos, se RECOMIENDA utilizar valores del esquema de concepto de tipos de medios y medios físicos en lugar del esquema de concepto de extensiones de archivo.

El esquema conceptual para los tipos de medios y medios físicos define una relación `skos:broader` entre cada tipo de medio específico o medio físico y uno de los seis [tipos de medios de nivel superior definidos por RFC 2046](https://tools.ietf.org/html/rfc2046#page-4V) que están relacionados con multimedia: aplicación, audio, imagen, modelo, texto y video. This relation MAY be used by clients to infer the general category of the media item format.

The concept scheme for file extensions defines concepts for many common file extensions used for digital media files. These concepts are usually related to one of the media types and physical media by a `skos:exactMatch` relation. Metadata creators MAY use a controlled value from the file extensions concept scheme, but because of the asserted `skos:exactMatch` relation aggregators MAY substitute the equivalent value from the media types and physical media concept scheme.

### 2.3 Example workflows (non-normative)

Workflow 1: A data provider uses spreadsheets containing a column for literal values for `dc:format`. The spreadsheets are populated with file extensions that are controlled string values from the concept scheme for file extensions. The spreadsheets are provided to an aggregator whose software "looks up" the controlled string values in the concept scheme for file extensions and determines the equivalent concepts from the concept scheme for media types and physical media. The IRIs from the concept scheme for media types and physical media are used as standardized values for `dcterms:format` in the aggregator's database.

Workflow 2: A data aggregator acquires data about multimedia items that includes file names or URLs, but no format information. The aggregator extracts the file extensions from the files or URLs and uses the concept schemes to assign a `dcterms:format` IRI value from the concept scheme for media types and physical media to each item. In cases where an item has a file extension that does not correspond to one of the controlled value strings in the concept scheme for file extensions, the aggregator uses a community-maintained table of alternate file extension values to determine the appropriate format concept for the media item.

Workflow 3: A data aggregator harvests media items from an open data repository. The remote server provides the media type via a `Content-Type` header and the file extension is determined from the file name. The aggregator cross-checks the media type value against the file extension value and uses the `skos:exactMatch` relations in the SKOS concept schemes to determine whether the values are consistent. Inconsistent pairs of values are flagged for manual checking. Previously unknown file extensions are flagged for additional research and possible inclusion in the community-maintained table of alternate file extension values.

## 3 Índice de Términos
