# {document_title}

Título
: {document_title}

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

## 1 Introducción

Hay una serie de documentos incluidos en el Estándar Audiovisual Core.  Este documento proporciona detalles sobre los términos incluidos en la versión {ratification_date} del vocabulario Audiovisual Core. El documento [Introducción al Audiovisual Core](../introduction/) proporciona una breve introducción al Estándar Audiovisual Core. Para obtener información sobre la estructura del Audiovisual Core, consulte el documento [Estructura del Audiovisual Core](../structure/).  Para obtener una guía más detallada sobre el uso del Audiovisual Core, consulte el documento [Guía del Audiovisual Core](../guide/).

### 1.1 Estado del contenido de este documento

Las secciones 1.3 a 5 son normativas, excepto la Tabla 1.  En la Sección 7 y sus subsecciones, los valores de URI normativo, Definición, Obligatorio y Repetible son normativos. El valor de Uso (si existe para un término determinado) es normativo, ya que especifica cómo debe usarse un término prestado como parte del Audiovisual Core.  Los valores del nombre del término no son normativos, aunque se puede esperar que el prefijo de la abreviatura del espacio de nombres sea uno de uso común para el espacio de nombres del término.  Las etiquetas y los valores de todas las demás propiedades (como las notas) no son normativos.

### 1.2 Palabras clave RFC 2119

Las palabras clave "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY" y "OPTIONAL" en este documento deben interpretarse como se describe en [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) y [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174), únicamente cuando aparezcan en mayúsculas, tal como se muestra aquí.

### 1.3 Categorías de términos

Un registro de Audiovisual Core (AC) es una descripción de un recurso multimedia que utiliza los vocabularios del AC. Este documento especifica tres tipos de términos: aquellos que describen aspectos independientes de la representación de los medios, aquellos que describen aspectos dependientes de la representación y aquellos que designan partes específicas del elemento mediático.
La mayoría de los términos son independientes de la representación y se refieren a un "recurso multimedia abstracto". Uno de estos términos, `ac:hasServiceAccessPoint`, se refiere a
o contiene metadatos de punto de acceso al servicio dependientes de la representación,
que describen una representación digital del recurso multimedia abstracto (una instancia de la clase `ac:ServiceAccessPoint`).
Estos metadatos describen aspectos como la dirección web donde se puede recuperar una representación digital y el formato, la extensión o las licencias que describen dicha representación en particular. Un recurso multimedia puede proporcionar varios puntos de acceso para diferentes representaciones (por ejemplo, diferentes resoluciones). El recurso también puede estar vinculado a una o más regiones de interés (ROI) que definen partes dentro del elemento multimedia (instancias de la clase `ac:RegionOfInterest`).

## 2 Vocabulario prestado

Cuando los términos se toman prestados de otros vocabularios, AC utiliza los URI, las abreviaturas comunes y los prefijos de espacios de nombres que se usan en esos vocabularios. Las URI son normativas, pero las abreviaturas y los prefijos de espacios de nombres no tienen ningún impacto, excepto como ayuda para leer la documentación.

Tabla 1. Vocabularios de los cuales se han tomado prestados términos (no normativos)

Nota: Los URI de los términos en la mayoría de estos espacios de nombres no desvían la referencia a nada.  La documentación autorizada se puede obtener haciendo clic en los nombres del vocabulario en la tabla.

| Vocabulario                                                                                                                                                                                                                                                                                                                  | Abreviatura | Espacios de nombres y abreviaturas                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | --------------------------------------------------------------------------------------- |
| [Darwin Core](http://rs.tdwg.org/dwc/doc/list/)                                                                                                                                                                                                                                                                              | DwC         | `dwc: = http://rs.tdwg.org/dwc/terms/`                                                  |
| [Dublin Core](http://dublincore.org/documents/dcmi-terms/)                                                                                                                                                                                                                                                                   | DC          | `dc: = http://purl.org/dc/elements/1.1/, dcterms: = http://purl.org/dc/terms/`          |
| [Propiedades de Adobe XMP Core](https://github.com/adobe/XMP-Toolkit-SDK/blob/main/docs/XMPSpecificationPart1.pdf)                                                                                                                                                                                                           | XMP         | `xmp: = http://ns.adobe.com/xap/1.0/, xmpRights: = http://ns.adobe.com/xap/1.0/rights/` |
| [Propiedades adicionales de Adobe XMP](https://github.com/adobe/XMP-Toolkit-SDK/blob/main/docs/XMPSpecificationPart2.pdf)                                                                                                                                                                                                    | XMP         | `photoshop: = http://ns.adobe.com/photoshop/1.0/`                                       |
| [Estándar de metadatos de fotografías del Consejo Internacional de Prensa y Telecomunicaciones, esquema de extensión 1.1](http://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-201007_1.pdf)                                                                                               | IPTC        | `Iptc4xmpExt: = http://iptc.org/std/Iptc4xmpExt/2008-02-29/`                            |
| [Formato de archivo de imagen intercambiable de la Asociación de productos de imágenes y cámaras] (http://www.cipa.jp/std/documents/e/DC-008-2012_E.pdf)         | EXIF        | `exif: = http://ns.adobe.com/exif/1.0/`                                                 |
| [Ontología de la Música](http://musicontology.com/specification/)                                                                                                                                                                                                                                                            | MO          | `lo//purl.org/ontology/mo/`                                                             |
| Ontología de la descripción de la colección natural LSID de TDWG](https://github.com/tdwg/ontology/blob/master/ontology/voc/Collection.rdf) (referenciada en metadatos, pero no se toman términos prestados) | NCD         | `ncd: = http://rs.tdwg.org/ontology/voc/Collection#`                                    |

## 3 Espacios de nombres, prefijos y nombres de términos

El espacio de nombres de los términos tomados de otros vocabularios es el del original. El espacio de nombres de los términos de AC de novo es `http://rs.tdwg.org/ac/terms/`. En la tabla de términos, cada entrada de término tiene una fila con el nombre del término. Este término es generalmente un "nombre no calificado" precedido por un prefijo ampliamente aceptado que designa una abreviatura para el espacio de nombres. Se RECOMIENDA que los implementadores que necesiten un prefijo para el espacio de nombres AC utilicen "ac". En este documento web, al pasar el cursor sobre un término de la lista [Índice por nombre de término](#61-index-by-term-name) a continuación, se mostrará una URL completa que puede usarse en otros documentos web para enlazar con el tratamiento que _este_ documento da a ese término, incluso si proviene de un vocabulario prestado. Es muy importante tener en cuenta que algunos vocabularios, como los de la [Iniciativa de Metadatos Dublin Core (DCMI)](https://www.dublincore.org/), ofrecen versiones del mismo término en dos espacios de nombres diferentes: uno para valores de cadena y otro para URI, incluso cuando dicha separación es simplemente una recomendación, no un mandato. Consulte esta
[entrada wiki de DCMI](https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md)
sobre este tema. En los vocabularios donde se utiliza esta práctica, a menudo la seguimos e indicamos una referencia en las notas de nuestras descripciones de términos a la versión hermana del término. Un ejemplo es el par [dc:type](#dc_type) y [dcterms:type](#dcterms_type). Cuando un par de este tipo permite instancias repetidas (por ejemplo, como en el caso de [dc:source](#dc_source) y [dcterms:source](#dcterms_source)), puede ser necesario tener especial cuidado en algunas implementaciones de AC, ya que algunas implementaciones pueden no proporcionar la estructura suficiente para indicar claramente la asociación entre los miembros de un par en el caso de múltiples valores de cada uno. Este es un caso especial de la cuestión tratada en el material normativo sobre [Multiplicidad y Cardinalidad](../structure/#3-multiplicity-and-cardinality) en el documento Estructura del Audiovisual Core.

## 4 capas

(La propiedad de capa del Audiovisual Core ha quedado obsoleta a partir de 2020-01-27)

## 5 Términos literales vs. términos con valores URI

Algunos términos tienen dos versiones: una que espera un valor literal de cadena y la otra, un URI. En estas circunstancias, la versión que espera una cadena se nombra con el sufijo "Literal", por ejemplo, `ac:metadataLanguageLiteral`. En tales casos, se PUEDEN proporcionar ambas formas, pero se debe tener cuidado para garantizar que los usos reflejen la misma intención. En caso de ambigüedad, prevalece la versión URI. Todos los términos, incluidos aquellos con o sin el sufijo "Literal" específico, especifican en su definición si los valores requeridos son cadenas o URI.

## 6 Índices de vocabulario (no normativos)

