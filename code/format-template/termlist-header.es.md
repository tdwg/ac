# Controlled Vocabulary for Dublin Core format: List of Terms

Title
: Controlled Vocabulary for Dublin Core format: List of Terms

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

Abstract
: Audiovisual Core borrows the Dublin Core terms dc:format and dcterms:format to provide information about the physical or electronic format of a media item. This controlled vocabulary provides values for those two terms.

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

De acuerdo con el [documento de la Lista de términos del Audiovisual Core](http://rs.tdwg.org/ac/doc/termlist/), los términos IRI no abreviados DEBEN usarse como valores de la propiedad `dcterms:format`. Las cadenas de valores controlados DEBEN usarse como valores de la propiedad `dc:format`.

### 2.2 Relación entre conceptos y esquemas de conceptos

La entrada para la propiedad `dc:format` en el [documento de lista de términos del núcleo audiovisual](http://rs.tdwg.org/ac/doc/termlist/#dc_format) especifica que se RECOMIENDAN tres tipos de valores de cadena: tipos de medios de Internet (tipos MIME), valores de cadena especiales para medios físicos o extensiones de archivo de uso común. Este vocabulario controlado define dos esquemas de conceptos SKOS: un esquema de conceptos para tipos de medios y medios físicos (los primeros dos tipos de valores especificados para `dc:type`) y un esquema de conceptos para extensiones de archivos (el último tipo de valor recomendado). Debido a que la Autoridad de Números Asignados de Internet (IANA) mantiene un [registro de tipos de medios](https://www.iana.org/assignments/media-types/media-types.xhtml) y Audiovisual Core mantiene una lista controlada de tipos de medios físicos, se RECOMIENDA utilizar valores del esquema de concepto de tipos de medios y medios físicos en lugar del esquema de concepto de extensiones de archivo.

El esquema conceptual para los tipos de medios y medios físicos define una relación `skos:broader` entre cada tipo de medio específico o medio físico y uno de los seis [tipos de medios de nivel superior definidos por RFC 2046](https://tools.ietf.org/html/rfc2046#page-4V) que están relacionados con multimedia: aplicación, audio, imagen, modelo, texto y video. Esta relación PUEDE ser utilizada por usuarios para inferir la categoría general del formato del elemento multimedia.

El esquema conceptual para extensiones de archivos define conceptos para muchas extensiones de archivos comunes utilizadas en archivos multimedia digitales. Estos conceptos generalmente están relacionados con uno de los tipos de medios y medios físicos mediante una relación "skos:exactMatch". Los creadores de metadatos PUEDEN usar un valor controlado del esquema de concepto de extensiones de archivo, pero debido a la relación `skos:exactMatch` declarada, los agregadores PUEDEN sustituir el valor equivalente del esquema de concepto de tipos de medios y medios físicos.

### 2.3 Ejemplos de flujos de trabajo (no normativos)

Flujo de trabajo 1: Un proveedor de datos utiliza hojas de cálculo que contienen una columna para valores literales para `dc:format`. Las hojas de cálculo se llenan con extensiones de archivo que son valores de cadena controlados desde el esquema de conceptos para extensiones de archivo. Las hojas de cálculo se proporcionan a un agregador cuyo software "busca" los valores de cadena controlados en el esquema de conceptos para extensiones de archivo y determina los conceptos equivalentes del esquema de conceptos para tipos de medios y medios físicos. Los IRI del esquema conceptual para tipos de medios y medios físicos se utilizan como valores estandarizados para `dcterms:format` en la base de datos del agregador.

Flujo de trabajo 2: Un agregador de datos adquiere datos sobre elementos multimedia que incluyen nombres de archivos o URL, pero ninguna información de formato. El agregador extrae las extensiones de archivo de los archivos o URL y utiliza los esquemas de concepto para asignar un valor IRI `dcterms:format` del esquema de concepto para tipos de medios y medios físicos a cada elemento. En los casos en que un elemento tiene una extensión de archivo que no corresponde a una de las cadenas de valores controlados en el esquema de conceptos para extensiones de archivo, el agregador utiliza una tabla de valores de extensión de archivo alternativos, mantenida por la comunidad, para determinar el concepto de formato apropiado para el elemento multimedia.

Flujo de trabajo 3: Un agregador de datos recopila elementos multimedia de un repositorio de datos abierto. El servidor remoto proporciona el tipo de medio a través de un encabezado `Content-Type` y la extensión del archivo se determina a partir del nombre del archivo. El agregador verifica el valor del tipo de medio con el valor de la extensión del archivo y utiliza las relaciones `skos:exactMatch` en los esquemas de conceptos de SKOS para determinar si los valores son consistentes. Los pares de valores inconsistentes se marcan para verificación manual. Las extensiones de archivos previamente desconocidas se marcan para investigación adicional y posible inclusión en la tabla de valores de extensiones de archivos alternativos mantenida por la comunidad.

## 3 Índice de Términos
