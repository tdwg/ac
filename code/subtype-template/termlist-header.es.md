# Controlled Vocabulary for Audiovisual Core subtype: List of Terms

Title
: Controlled Vocabulary for Audiovisual Core subtype: List of Terms

IRI del espacio de nombres
: <http://rs.tdwg.org/acsubtype/values/>

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
: Audiovisual Core uses the terms ac:subtype and ac:subtypeLiteral to refine the type of a media item to a level more specific than the Dublin Core Type Vocabulary, http://purl.org/dc/dcmitype/. This controlled vocabulary provides values for ac:subtype and ac:subtypeLiteral.

Colaboradores
: {contributors}

Creador
: {creator}

Cita bibliográfica
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

## 1 Introducción (Informativa)

Este documento incluye términos destinados a ser utilizados como valores controlados para los términos del Audiovisual Core `ac:subjectPart` y `ac:subjectPartLiteral`. **Nota:** Aunque este es un vocabulario controlado, el tipo de sus términos es `rdfs:Class` en lugar de `skos:Concept` como en otros vocabularios controlados, porque indica el tipo del elemento multimedia.

### 1.1 Estado del contenido de este documento

La Sección 1 es informativa (no normativa).

La sección 2 es normativa.

La Sección 3 es informativa (no normativa).

En la Sección 4, los valores de `IRI del Término`, `Definición` y `Valor controlado` son normativos. El valor de `Uso` (si existe para un término determinado) también es normativo. Los valores del `Nombre del término` no son normativos, aunque se puede esperar que el prefijo del namespace abreviado sea uno comúnmente utilizado para ese namespace.  La `Etiqueta` y los valores de todas las demás propiedades no son normativos.

### 1.2 Palabras clave RFC 2119

Las palabras clave "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY" y "OPTIONAL" en este documento deben interpretarse como se describe en [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) y [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174), únicamente cuando aparezcan en mayúsculas, tal como se muestra aquí.

## 2 Uso de los Términos

### 2.1 Relación de los tipos de valor con los términos de propiedad

De acuerdo con el [documento de la Lista de términos del Audiovisual Core](http://rs.tdwg.org/ac/doc/termlist/), los términos IRI no abreviados DEBEN usarse como valores de la propiedad `dcterms:format`. Las cadenas de valores controlados DEBEN usarse como valores de la propiedad `ac:subtypeLiteral`.

### 2.2 Relación entre los valores de ac:subtypeLiteral y ac:subtype

Una IRI para un término en este vocabulario denota la misma clase que la clase denotada por la cadena de valor controlado para el mismo término. De esta manera, un usuario PUEDE inferir un valor IRI para `ac:subtype` dada una cadena de valor controlado para `ac:subtypeLiteral` incluso si ese IRI no se indica explícitamente. La implicación práctica es que los agregadores de datos PUEDEN materializar valores para la propiedad `ac:subtype` preferida en casos donde los proveedores solo proporcionan valores para `ac:subtypeLiteral`.

## 3 Índice de Términos
