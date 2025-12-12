# Introducción al Audiovisual Core

Título
: Introducción al Audiovisual Core

Fecha de publicación de la versión
: 2023-02-24

Fecha de creación
: 2013-10-23

Parte del Estándar TDWG
: <http://www.tdwg.org/standards/638>

Esta versión
: <http://rs.tdwg.org/ac/doc/introduction/2023-02-24>

Última versión
: <http://rs.tdwg.org/ac/doc/introduction/>

Versión anterior
: <http://rs.tdwg.org/ac/doc/introduction/2013-10-23>

Resumen:
El Audiovisual Core es un conjunto de vocabularios diseñados para representar metadatos de recursos y colecciones multimedia sobre biodiversidad. Estos vocabularios tienen como objetivo representar información que ayudará a determinar si un recurso o colección en particular será adecuado para alguna aplicación particular de la ciencia de la biodiversidad antes de adquirir los medios. Entre otras cosas, los vocabularios abordan cuestiones como la gestión de los medios y las colecciones, las descripciones de su contenido, su cobertura taxonómica, geográfica y temporal, y las formas apropiadas de recuperarlos, atribuirlos y reproducirlos.

Contribuyentes
: [Robert A. Morris](https://orcid.org/0000-0002-6992-9446) ([University of Massachusetts at Boston, USA](http://www.wikidata.org/entity/Q15144)), [Vijay Barve](https://orcid.org/0000-0002-4852-2567) (), [Mihail Carausu](https://orcid.org/0000-0002-8234-0599) ([Danish Biodiversity Information Facility (DanBIF), Copenhagen, Denmark](http://www.wikidata.org/entity/Q1531570)), [Vishwas Chavan](https://orcid.org/0000-0002-3425-6499) ([Global Biodiversity Information Facility, Copenhagen, Denmark](http://www.wikidata.org/entity/Q1531570)), [José Cuadra](http://www.wikidata.org/entity/Q51883873) (), [Chris Freeland](https://orcid.org/0000-0002-2541-5822) ([Missouri Botanical Garden, St. Louis, USA](http://www.wikidata.org/entity/Q1852803)), [Gregor Hagedorn](https://orcid.org/0000-0001-7023-7386) ([JKI, Federal Research Institute for Cultivated Plants, Berlin, Germany](http://www.wikidata.org/entity/Q832099)), [Patrick Leary](https://orcid.org/0000-0001-5172-8577) (), [Dimitry Mozzherin](https://orcid.org/0000-0003-1593-1417) ([Encyclopedia of Life, Woods Hole, USA](http://www.wikidata.org/entity/Q82486)), [Annette Olson](https://orcid.org/0000-0002-0772-0022) ([American Association for the Advancement of Science](http://www.wikidata.org/entity/Q40358)), [Greg Riccardi](https://orcid.org/0000-0002-3850-9983) ([Florida State University, Tallahassee, USA](http://www.wikidata.org/entity/Q861548)), [Ivan Teage](https://orcid.org/0000-0003-4176-2274) (), [Steve Baskauf](https://orcid.org/0000-0003-4365-3135) ([Vanderbilt University, Nashville, TN, USA](http://www.wikidata.org/entity/Q29052))

Creador
: Grupo de Trabajo de Recursos Multimedia y Grupo de Mantenimiento del Audiovisual Core de GBIF/TDWG

Citación bibliográfica
: Grupo de Trabajo de Recursos Multimedia y Grupo de Mantenimiento del Audiovisual Core de GBIF/TDWG. 2023. Introducción al Audiovisual Core. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/ac/doc/introduction/2023-02-24>

## 1 Introducción

There are four documents included in the Audiovisual Core Standard.  Este documento ofrece una introducción general al Estándar Audiovisual Core. Para obtener información sobre la estructura del Audiovisual Core, consulte el documento [Estructura del Audiovisual Core](../structure/).  Para conocer detalles de los términos, consulte el documento [Lista de términos del Audiovisual Core](../termlist/).  
Para obtener una guía más detallada sobre el uso de Audiovisual Core, consulte el documento [Guía de Audiovisual Core](../guide/).

### 1.1 Estado del contenido de este documento

Todas las secciones de este documento no son normativas.

### 1.2 El alcance del Audiovisual Core

El esquema de metadatos de recursos multimedia del Audiovisual Core ("esquema AC" o simplemente "AC") es un conjunto de vocabularios de metadatos para describir recursos y colecciones multimedia relacionados con la biodiversidad. La especificación es independiente de cómo se puedan representar estos vocabularios para su uso por máquinas.

Los recursos multimedia son artefactos digitales o físicos que normalmente comprenden más que texto. Estos incluyen imágenes, obras de arte, dibujos, fotografías, sonido, videos, animaciones, materiales de presentación y medios interactivos en línea, incluidas, por ejemplo, herramientas de identificación. Una colección multimedia es un conjunto de dichos objetos, ya sean curados o no, y accesibles electrónicamente o no. A los efectos de este documento, consideramos que una colección de recursos multimedia en sí misma es un «recurso multimedia». Siempre que una discusión o especificación pueda aplicarse únicamente a una colección o a un único recurso multimedia, lo decimos explícitamente.

Las descripciones multimedia son registros digitales que documentan recursos o colecciones multimedia subyacentes. AC se enfoca en recursos multimedia relacionados con la biodiversidad. Comparte terminología y asuntos con muchos estándares conocidos e importantes para describir el acceso a recursos, como Dublin Core (DC), Darwin Core (DwC), Adobe Extensible Metadata Platform (XMP), el Consejo Internacional de Prensa y Telecomunicaciones (IPTC), el esquema del Grupo de Trabajo de Metadatos (MWG), el Esquema de Colecciones Naturales (NCD) y otros. Cuando existe una coincidencia exacta con el uso de dichos estándares, AC adopta sus identificadores y definiciones. Muchas colecciones de multimedia sobre biodiversidad ya cuentan con descripciones de sus medios expresadas en DwC o DC. Al utilizar dichos vocabularios cuando sea adecuado, AC pretende facilitar que dichas colecciones reutilicen sus descripciones existentes, complementadas con otros términos cuando sea necesario.

**Véase también:** [Descubrimiento y publicación de datos primarios sobre biodiversidad asociados con recursos multimedia: Estrategias y enfoques audiovisuales centrales.](https://journals.ku.edu/index.php/jbi/article/view/4117) R. Morris et al., _Biodiversity Informatics_, 8 de julio. 2013.

## 2 Términos del Audiovisual Core

Un registro del Núcleo Audiovisual es una descripción de un recurso multimedia que utiliza los [términos del Audiovisual Core](./terms). AC especifica dos tipos de términos: términos a nivel de registro y términos a nivel de acceso.
Los términos a nivel de registro se aplican al recurso multimedia que se describe. Casi todos los términos son términos a nivel de registro. Uno de estos términos, _hasServiceAccessPoint_, desempeña un papel especial al ayudar a recuperar el recurso que el registro describe. Un recurso multimedia puede tener más de un hasServiceAccessPoint, cada uno de los cuales proporciona valores de uno o más términos de nivel de acceso. Los términos de nivel de acceso documentan aspectos como la dirección web en la que se puede recuperar una representación digital del recurso, el tamaño del objeto recuperado, etc. Un registro de Audiovisual Core es, por lo tanto, una descripción que utiliza un conjunto de términos que se ajusta a los documentos normativos y que contiene al menos los cuatro términos obligatorios, que proporcionan un identificador, un tipo de recurso, el idioma de la descripción e información sobre derechos de autor. Cada uno de estos registros describe un único recurso multimedia (que posiblemente incluya una colección). El identificador puede haber sido asignado al recurso por una autoridad externa o por el proveedor del registro. En sentido estricto, el identificador es obligatorio solo para colecciones, pero en general, es altamente recomendado.

Cada término del Audiovisual Core tiene un nombre en texto plano, un identificador del término y una definición normativa en texto plano. Los identificadores de términos cumplen con la [especificación del Identificador Universal de Recursos (URI)](http://tools.ietf.org/html/rfc2616#section-3.2).
Normalmente, estos identificadores tienen un formato familiar para los usuarios del navegador, como las direcciones de las páginas web, que comienzan con "http://". De manera informal, esto se puede entender así: una URI http tiene la sintaxis de una dirección web, pero no se espera que al introducirla en un navegador web se devuelva información al navegador, y si así fuera, la información devuelta podría no ser relevante.

Debido a que las URL http son bastante largas, los documentos AC siguen la práctica estándar de introducir un prefijo corto que comprende un "calificador de espacio de nombres" separado por dos puntos de un nombre mnemónico estrechamente relacionado con el nombre del término. El espacio de nombres de aproximadamente el 50% de los términos que se toman prestados de otros vocabularios es el espacio de nombres del original. El espacio de nombres de los términos nuevos del AC es http://rs.tdwg.org/ac/terms/. En la [Lista de términos básicos audiovisuales](../termlist/), cada entrada de término tiene una fila con el nombre del término. Siguiendo la práctica de los [términos del Darwin Core](http://rs.tdwg.org/dwc/terms/), este nombre de término es generalmente un "nombre no calificado" precedido por un prefijo ampliamente aceptado que designa una abreviatura para el espacio de nombres. El resultado se conoce como un nombre calificado. Por ejemplo, la documentación wiki normativa para el término prestado dcterms:identifier tiene el URI http://purl.org/dc/terms/identifier. La primera parte, "http://purl.org/dc/terms/", corresponde al espacio de nombres. La mayoría de las URL de términos tomados de vocabularios externos, de hecho, generan documentación relevante para ese estándar externo cuando se utilizan como URL de una página web. A veces no es preciso porque la documentación es un documento PDF y varios URI (¡diferentes!) podrían aparentemente conducir al mismo lugar.

## 3 Implementaciones

Los documentos [Lista de términos de AC](../termlist/) y [Estructura del Audiovisual Core](../structure/) representan un _modelo de datos_. Para el uso real del Audiovisual Core, es necesario seleccionar una implementación, preferiblemente una con algún estatus designado por [TDWG](http://www.tdwg.org/). Las implementaciones conocidas se enumerarán en documentos complementarios que no se incluyen como parte del estándar Audiovisual Core.

## 4 Referencias

|                                                                                                                                                                 |                                                                                                                                      |                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- |
| [\[ACISS\]](https://github.com/tdwg/ac/issues)                                                            | https://github.com/tdwg/ac/issues                                                                    | AC issue tracker              |
| [\[CHANGE\]](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md#3-change-process) | http://rs.tdwg.org/vms/doc/specification/#3-change-process                           | TDWG vocabulary change policy |
| [\[DCMIU\]](http://wiki.dublincore.org/index.php/User_Guide)                                              | http://wiki.dublincore.org/index.php/User_Guide | Dublin Core User Guide        |
| [\[GUIDE\]](../guide/)                                                                                    | http://rs.tdwg.org/ac/doc/guide/                                                     | AC User Guide                 |
| [\[STRCT\]](../structure/)                                                                                | http://rs.tdwg.org/ac/doc/structure/                                                 | Introduction to AC structure  |
| [\[TERMS\]](../termlist/)                                                                                 | http://rs.tdwg.org/ac/doc/termlist/                                                  | AC Term List                  |
