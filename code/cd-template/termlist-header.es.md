# {document_title}

Título
: {document_title}

Espacio de nombres IRI
: <http://rs.tdwg.org/accd/values/>

Abreviatura preferida del namespce
: accd:

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

This document includes terms intended to be used as controlled values for Audiovisual Core terms `Iptc4xmpExt:CVterm` and `ac:CVtermLiteral`.

### 1.1 Estado del contenido de este documento

La Sección 1 es informativa (no normativa).

La sección 2 es normativa.

La Sección 3 es informativa (no normativa).

En la Sección 4, los valores de `Término IRI`, `Definición` y `Valor controlado` son normativos. El valor de `Uso` (si existe para un término determinado) también es normativo. Los valores del `Nombre del término` no son normativos, aunque se puede esperar que el prefijo del namespace abreviado sea uno comúnmente utilizado para ese namespace.  La `Etiqueta` y los valores de todas las demás propiedades no son normativos.

### 1.2 Palabras clave RFC 2119

Las palabras clave "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY" y "OPTIONAL" en este documento deben interpretarse como se describe en [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) y [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174), únicamente cuando aparezcan en mayúsculas, tal como se muestra aquí.

## 2 Uso de los Términos

### 2.1 Relación de los tipos de valor con los términos de propiedad

In accordance with [the Audiovisual Core Term List document](http://rs.tdwg.org/ac/doc/termlist/), unabbreviated term IRIs SHOULD be used as values of the property `Iptc4xmpExt:CVterm`. Controlled value strings SHOULD be used as values of the property `ac:CVtermLiteral`.

### 2.2 Relationship between values of ac:CVtermLiteral and Iptc4xmpExt:CVterm

Una IRI para un término en este vocabulario denota la misma clase que la clase denotada por la cadena de valor controlado para el mismo término. Thus a client MAY infer an IRI value for `Iptc4xmpExt:CVterm` given a controlled value string for `ac:CVtermLiteral` even if that IRI is not explicitly stated. The practical implication is that data aggregators MAY materialize values for the preferred `Iptc4xmpExt:CVterm` property in cases where providers only provide values for `ac:CVtermLiteral`.

## 3 Índice de Términos
