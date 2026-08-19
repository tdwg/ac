# Controlled Vocabulary for Audiovisual Core Content Description: List of Terms

Title
: Controlled Vocabulary for Audiovisual Core Content Description: List of Terms

Espacio de nombres IRI
: <http://rs.tdwg.org/accd/values/>

Abreviatura preferida del namespce
: accd:

Fecha de publicación de la versión
: 2026-08-18

Fecha de creación
: 2026-08-18

Parte del Estándar TDWG
: <http://www.tdwg.org/standards/638>

Esta versión
: <http://rs.tdwg.org/ac/doc/3dtype/2026-08-18>

Última versión
: <http://rs.tdwg.org/ac/doc/3dtype/>

Resumen
: Audiovisual Core uses the terms ac:digital3DResourceType and ac:digital3DResourceTypeLiteral to describe the media format of a 3D resource. This controlled vocabulary provides values for those terms.

Colaboradores
: [Doug M. Boyer](https://orcid.org/0000-0002-8697-2999) ([Duke University](http://www.wikidata.org/entity/Q168751)), [Jon Blundell](https://orcid.org/0000-0003-2493-9912) ([Smithsonian Institution](http://www.wikidata.org/entity/Q131626)), [Gary J. Motz](https://orcid.org/0000-0002-6712-2139) ([Indiana Geological and Water Survey](http://www.wikidata.org/entity/Q6023194)), [Adam N. Rountrey](https://orcid.org/0000-0003-0939-9102) ([University of Michigan Museum of Paleontology](http://www.wikidata.org/entity/Q96220204)), [Rebecca Snyder](https://orcid.org/0000-0002-0028-6139) ([Smithsonian Institution](http://www.wikidata.org/entity/Q131626)), [Jocelyn Triplett](https://orcid.org/0000-0003-3452-2408) ([Duke University](http://www.wikidata.org/entity/Q168751)), [Kate Webbink](https://orcid.org/0000-0002-8347-0942) ([Field Museum of Natural History](http://www.wikidata.org/entity/Q1122595)), [Julie Winchester](https://orcid.org/0000-0001-6578-764X) ([Duke University](http://www.wikidata.org/entity/Q168751))

Creador
: TDWG Audiovisual Core 3D Enhancement Task Group

Cita bibliográfica
: TDWG Audiovisual Core 3D Enhancement Task Group. 2026. Controlled Vocabulary for Audiovisual Core 3D Resource Type: List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/ac/doc/3dtype/2026-08-18>

## 1. Introducción (Informativa)

Este documento incluye términos destinados a ser utilizados como valores controlados para los términos principales de Audiovisual Core `Iptc4xmpExt:CVterm` y `ac:CVtermLiteral`.

### 1.1 Estado del contenido de este documento

La Sección 1 es informativa (no normativa).

La sección 2 es normativa.

La Sección 3 es informativa (no normativa).

En la Sección 4, los valores de `Término IRI`, `Definición` y `Valor controlado` son normativos. El valor de `Uso` (si existe para un término determinado) también es normativo. Los valores del `Nombre del término` no son normativos, aunque se puede esperar que el prefijo del namespace abreviado sea uno comúnmente utilizado para ese namespace.  La `Etiqueta` y los valores de todas las demás propiedades no son normativos.

### 1.2 Palabras clave RFC 2119

Las palabras clave "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY" y "OPTIONAL" en este documento deben interpretarse como se describe en [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) y [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174), únicamente cuando aparezcan en mayúsculas, tal como se muestra aquí.

## 2 Uso de los Términos

### 2.1 Relación de los tipos de valor con los términos de propiedad

De acuerdo con el [documento de la Lista de Términos Básicos Audiovisuales](http://rs.tdwg.org/ac/doc/termlist/), los términos IRI no abreviados DEBEN usarse como valores de la propiedad `Iptc4xmpExt:CVterm`. Las cadenas de valores controlados DEBEN usarse como valores de la propiedad `ac:CVtermLiteral`.

### 2.2 Relación entre los valores de ac:CVtermLiteral y Iptc4xmpExt:CVterm

Una IRI para un término en este vocabulario denota la misma clase que la clase denotada por la cadena de valor controlado para el mismo término. Por lo tanto, un cliente PUEDE inferir un valor IRI para `Iptc4xmpExt:CVterm` dada una cadena de valor controlado para `ac:CVtermLiteral` incluso si ese IRI no se indica explícitamente. La implicación práctica es que los agregadores de datos PUEDEN materializar valores para la propiedad preferida `Iptc4xmpExt:CVterm` en los casos en que los proveedores solo proporcionan valores para `ac:CVtermLiteral`.

## 3 Índice de Términos



[3D resource type controlled vocabulary](#ac3dtype_t) |
[multi-file image slice series](#ac3dtype_t0007) |
[multi-file photo collection](#ac3dtype_t0005) |
[multi-file projection series](#ac3dtype_t0004) |
[point cloud with dependencies](#ac3dtype_t0010) |
[polygonal mesh with dependencies](#ac3dtype_t0011) |
[raster data](#ac3dtype_t0001) |
[raw data](#ac3dtype_t0002) |
[single-file volume image](#ac3dtype_t0008) |
[sinogram](#ac3dtype_t0003) |
[vector](#ac3dtype_t0009) |
[volume](#ac3dtype_t0006)

## 4 Vocabulario
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t"></a>Nombre de Término ac3dtype:t</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t">http://rs.tdwg.org/ac3dtype/values/t</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>3D resource type controlled vocabulary</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>A SKOS ConceptScheme to be used as a controlled vocabulary for the Audiovisual Core terms ac:digital3DResourceType and ac:digital3DResourceTypeLiteral</td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>http://www.w3.org/2004/02/skos/core#ConceptScheme</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0001"></a>Nombre de Término ac3dtype:t0001</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0001">http://rs.tdwg.org/ac3dtype/values/t0001</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0001-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0001-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>raster data</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>Gridded data composed of pixels that store values.</td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>rasterData</td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0002"></a>Nombre de Término ac3dtype:t0002</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0002">http://rs.tdwg.org/ac3dtype/values/t0002</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0002-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0002-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>raw data</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>The initial uncompressed and unprocessed data generated through a 3D modality.</td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>rawData</td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0003"></a>Nombre de Término ac3dtype:t0003</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0003">http://rs.tdwg.org/ac3dtype/values/t0003</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0003-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0003-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>sinogram</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>Raw data from a CT scanner with X-Ray Detector Configuration Type of Slot (scanned slot, slit, or spot). Projections are often analyzed and processed to create a reconstructed image stack.</td>
		</tr>
		<tr>
			<td>Definición derivada de</td>
			<td><a href="http://www.morphosource.org/terms/mscv/Sinograms">http://www.morphosource.org/terms/mscv/Sinograms</a></td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>sinogram</td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0004"></a>Nombre de Término ac3dtype:t0004</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0004">http://rs.tdwg.org/ac3dtype/values/t0004</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0004-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0004-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>multi-file projection series</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>Raw image data from a CT scanner with a X-Ray Detector Configuration Type of Area (single or tiled detector). Projections are often analyzed and processed to create a reconstructed image stack.</td>
		</tr>
		<tr>
			<td>Definición derivada de</td>
			<td><a href="http://www.morphosource.org/terms/mscv/Projections">http://www.morphosource.org/terms/mscv/Projections</a> </td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>multiFileProjectionSeries</td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0005"></a>Nombre de Término ac3dtype:t0005</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0005">http://rs.tdwg.org/ac3dtype/values/t0005</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0005-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0005-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>multi-file photo collection</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>Multiple overlapping photographs of an object.</td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>multiFilePhotoCollection</td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0006"></a>Nombre de Término ac3dtype:t0006</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0006">http://rs.tdwg.org/ac3dtype/values/t0006</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0006-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0006-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>volume</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>Three-dimensional digital representation of an object. Rendered as a grid of three-dimensional pixels (aka voxels)</td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>volume</td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0007"></a>Nombre de Término ac3dtype:t0007</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0007">http://rs.tdwg.org/ac3dtype/values/t0007</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0007-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0007-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>multi-file image slice series</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>Derived image data where each image represents a virtual slice of 3D volume. Images are stacked and arranged in series with specific spacing between slices in order to create the third dimension in a 3D volume.</td>
		</tr>
		<tr>
			<td>Definición derivada de</td>
			<td><a href="http://www.morphosource.org/terms/mscv/ReconstructedImageStack">http://www.morphosource.org/terms/mscv/ReconstructedImageStack</a></td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>multiFileImageSliceSeries</td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0008"></a>Nombre de Término ac3dtype:t0008</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0008">http://rs.tdwg.org/ac3dtype/values/t0008</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0008-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0008-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>single-file volume image</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>A single derived file where image data for all "virtual slices" of a 3D volume are included, allowing a three-dimensionally rendered representation of a 3D object. (formats like NRRD and 3Dtiff are examples)</td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>singleFileVolumeImage</td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0009"></a>Nombre de Término ac3dtype:t0009</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0009">http://rs.tdwg.org/ac3dtype/values/t0009</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0009-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0009-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>vector</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>Image data defined by geometric points, lines, curves, and polygons.</td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>vector</td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0010"></a>Nombre de Término ac3dtype:t0010</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0010">http://rs.tdwg.org/ac3dtype/values/t0010</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0010-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0010-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>point cloud with dependencies</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>A set of points in a 3D coordinate system with optional associated texture or color file</td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>pointCloudWithDependencies</td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0011"></a>Nombre de Término ac3dtype:t0011</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0011">http://rs.tdwg.org/ac3dtype/values/t0011</a></td>
		</tr>
		<tr>
			<td>Modificado</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Versión de Término IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0011-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0011-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Etiqueta</td>
			<td>polygonal mesh with dependencies</td>
		</tr>
		<tr>
			<td>Definición</td>
			<td>A wireframe or digital surface model consisting of polygons with optional associated texture or color file</td>
		</tr>
		<tr>
			<td>Valor controlado</td>
			<td>polygonalMeshWithDependencies</td>
		</tr>
		<tr>
			<td>Tipo</td>
			<td>Concepto</td>
		</tr>
		<tr>
			<td>Decisión del Comité Ejecutivo</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>


