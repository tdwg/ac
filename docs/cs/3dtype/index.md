# Controlled Vocabulary for Audiovisual Core Content Description: List of Terms

Title
: Controlled Vocabulary for Audiovisual Core Content Description: List of Terms

Namespace IRI
: <http://rs.tdwg.org/accd/values/>

Preferred namespace abbreviation
: accd:

Datum vydání verze
: 2026-08-18

Datum vytvoření
: 2026-08-18

Část standardu TDWG
: <http://www.tdwg.org/standards/638>

Tato verze
: <http://rs.tdwg.org/ac/doc/3dtype/2026-08-18>

Aktuální verze
: <http://rs.tdwg.org/ac/doc/3dtype/>

Abstract
: Audiovisual Core uses the terms ac:digital3DResourceType and ac:digital3DResourceTypeLiteral to describe the media format of a 3D resource. This controlled vocabulary provides values for those terms.

Přispěvatelé
: [Doug M. Boyer](https://orcid.org/0000-0002-8697-2999) ([Duke University](http://www.wikidata.org/entity/Q168751)), [Jon Blundell](https://orcid.org/0000-0003-2493-9912) ([Smithsonian Institution](http://www.wikidata.org/entity/Q131626)), [Gary J. Motz](https://orcid.org/0000-0002-6712-2139) ([Indiana Geological and Water Survey](http://www.wikidata.org/entity/Q6023194)), [Adam N. Rountrey](https://orcid.org/0000-0003-0939-9102) ([University of Michigan Museum of Paleontology](http://www.wikidata.org/entity/Q96220204)), [Rebecca Snyder](https://orcid.org/0000-0002-0028-6139) ([Smithsonian Institution](http://www.wikidata.org/entity/Q131626)), [Jocelyn Triplett](https://orcid.org/0000-0003-3452-2408) ([Duke University](http://www.wikidata.org/entity/Q168751)), [Kate Webbink](https://orcid.org/0000-0002-8347-0942) ([Field Museum of Natural History](http://www.wikidata.org/entity/Q1122595)), [Julie Winchester](https://orcid.org/0000-0001-6578-764X) ([Duke University](http://www.wikidata.org/entity/Q168751))

Tvůrce
: TDWG Audiovisual Core 3D Enhancement Task Group

Bibliografická citace
: TDWG Audiovisual Core 3D Enhancement Task Group. 2026. Controlled Vocabulary for Audiovisual Core 3D Resource Type: List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/ac/doc/3dtype/2026-08-18>

## 1 Úvod (informativní)

This document includes terms intended to be used as controlled values for Audiovisual Core terms `Iptc4xmpExt:CVterm` and `ac:CVtermLiteral`.

### 1.1 Status obsahu tohoto dokumentu

Oddíl 1 je informativní (nenormativní).

Oddíl 2 je normativní.

Oddíl 3 je informativní (nenormativní).

V oddíle 4 jsou hodnoty `Term IRI`, `Definice` a `Kontrolovaná hodnota` normativní. Hodnota `Použití` (pokud pro daný termín existuje) je normativní. Hodnoty `Název termínu` nejsou normativní, ačkoli lze očekávat, že prefix zkratky jmenného prostoru je prefix běžně používaný pro jmenný prostor termínu.  `Štítek` a hodnoty všech ostatních vlastností nejsou normativní.

### 1.2 Klíčová slova RFC 2119

Klíčová slova "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY" a "OPTIONAL" v tomto dokumentu je třeba interpretovat tak, jak je popsáno v [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) a [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174), pokud a pouze pokud jsou uvedena velkými písmeny, jak je uvedeno zde.

## 2 Použití termínů

### 2.1 Vztah hodnotových typů k pojmům vlastnictví

In accordance with [the Audiovisual Core Term List document](http://rs.tdwg.org/ac/doc/termlist/), unabbreviated term IRIs SHOULD be used as values of the property `Iptc4xmpExt:CVterm`. Controlled value strings SHOULD be used as values of the property `ac:CVtermLiteral`.

### 2.2 Relationship between values of ac:CVtermLiteral and Iptc4xmpExt:CVterm

IRI pro termín v tomto slovníku označuje stejný pojem jako pojem označený řízeným řetězcem hodnot pro stejný termín. Thus a client MAY infer an IRI value for `Iptc4xmpExt:CVterm` given a controlled value string for `ac:CVtermLiteral` even if that IRI is not explicitly stated. The practical implication is that data aggregators MAY materialize values for the preferred `Iptc4xmpExt:CVterm` property in cases where providers only provide values for `ac:CVtermLiteral`.

## 3 Index termínů



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

## 4 Slovník
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t"></a>Název termínu ac3dtype:t</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Termín IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t">http://rs.tdwg.org/ac3dtype/values/t</a></td>
		</tr>
		<tr>
			<td>Změněno</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Verze termínu IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Štítek</td>
			<td>3D resource type controlled vocabulary</td>
		</tr>
		<tr>
			<td>Definice</td>
			<td>A SKOS ConceptScheme to be used as a controlled vocabulary for the Audiovisual Core terms ac:digital3DResourceType and ac:digital3DResourceTypeLiteral</td>
		</tr>
		<tr>
			<td>Typ</td>
			<td>http://www.w3.org/2004/02/skos/core#ConceptScheme</td>
		</tr>
		<tr>
			<td>Rozhodnutí výkonného výboru</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0001"></a>Název termínu ac3dtype:t0001</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Termín IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0001">http://rs.tdwg.org/ac3dtype/values/t0001</a></td>
		</tr>
		<tr>
			<td>Změněno</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Verze termínu IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0001-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0001-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Štítek</td>
			<td>raster data</td>
		</tr>
		<tr>
			<td>Definice</td>
			<td>Gridded data composed of pixels that store values.</td>
		</tr>
		<tr>
			<td>Řízená hodnota</td>
			<td>rasterData</td>
		</tr>
		<tr>
			<td>Typ</td>
			<td>Koncept</td>
		</tr>
		<tr>
			<td>Rozhodnutí výkonného výboru</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0002"></a>Název termínu ac3dtype:t0002</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Termín IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0002">http://rs.tdwg.org/ac3dtype/values/t0002</a></td>
		</tr>
		<tr>
			<td>Změněno</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Verze termínu IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0002-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0002-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Štítek</td>
			<td>raw data</td>
		</tr>
		<tr>
			<td>Definice</td>
			<td>The initial uncompressed and unprocessed data generated through a 3D modality.</td>
		</tr>
		<tr>
			<td>Řízená hodnota</td>
			<td>rawData</td>
		</tr>
		<tr>
			<td>Typ</td>
			<td>Koncept</td>
		</tr>
		<tr>
			<td>Rozhodnutí výkonného výboru</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0003"></a>Název termínu ac3dtype:t0003</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Termín IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0003">http://rs.tdwg.org/ac3dtype/values/t0003</a></td>
		</tr>
		<tr>
			<td>Změněno</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Verze termínu IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0003-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0003-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Štítek</td>
			<td>sinogram</td>
		</tr>
		<tr>
			<td>Definice</td>
			<td>Raw data from a CT scanner with X-Ray Detector Configuration Type of Slot (scanned slot, slit, or spot). Projections are often analyzed and processed to create a reconstructed image stack.</td>
		</tr>
		<tr>
			<td>Definice odvozená z</td>
			<td><a href="http://www.morphosource.org/terms/mscv/Sinograms">http://www.morphosource.org/terms/mscv/Sinograms</a></td>
		</tr>
		<tr>
			<td>Řízená hodnota</td>
			<td>sinogram</td>
		</tr>
		<tr>
			<td>Typ</td>
			<td>Koncept</td>
		</tr>
		<tr>
			<td>Rozhodnutí výkonného výboru</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0004"></a>Název termínu ac3dtype:t0004</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Termín IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0004">http://rs.tdwg.org/ac3dtype/values/t0004</a></td>
		</tr>
		<tr>
			<td>Změněno</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Verze termínu IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0004-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0004-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Štítek</td>
			<td>multi-file projection series</td>
		</tr>
		<tr>
			<td>Definice</td>
			<td>Raw image data from a CT scanner with a X-Ray Detector Configuration Type of Area (single or tiled detector). Projections are often analyzed and processed to create a reconstructed image stack.</td>
		</tr>
		<tr>
			<td>Definice odvozená z</td>
			<td><a href="http://www.morphosource.org/terms/mscv/Projections">http://www.morphosource.org/terms/mscv/Projections</a> </td>
		</tr>
		<tr>
			<td>Řízená hodnota</td>
			<td>multiFileProjectionSeries</td>
		</tr>
		<tr>
			<td>Typ</td>
			<td>Koncept</td>
		</tr>
		<tr>
			<td>Rozhodnutí výkonného výboru</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0005"></a>Název termínu ac3dtype:t0005</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Termín IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0005">http://rs.tdwg.org/ac3dtype/values/t0005</a></td>
		</tr>
		<tr>
			<td>Změněno</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Verze termínu IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0005-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0005-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Štítek</td>
			<td>multi-file photo collection</td>
		</tr>
		<tr>
			<td>Definice</td>
			<td>Multiple overlapping photographs of an object.</td>
		</tr>
		<tr>
			<td>Řízená hodnota</td>
			<td>multiFilePhotoCollection</td>
		</tr>
		<tr>
			<td>Typ</td>
			<td>Koncept</td>
		</tr>
		<tr>
			<td>Rozhodnutí výkonného výboru</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0006"></a>Název termínu ac3dtype:t0006</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Termín IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0006">http://rs.tdwg.org/ac3dtype/values/t0006</a></td>
		</tr>
		<tr>
			<td>Změněno</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Verze termínu IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0006-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0006-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Štítek</td>
			<td>volume</td>
		</tr>
		<tr>
			<td>Definice</td>
			<td>Three-dimensional digital representation of an object. Rendered as a grid of three-dimensional pixels (aka voxels)</td>
		</tr>
		<tr>
			<td>Řízená hodnota</td>
			<td>volume</td>
		</tr>
		<tr>
			<td>Typ</td>
			<td>Koncept</td>
		</tr>
		<tr>
			<td>Rozhodnutí výkonného výboru</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0007"></a>Název termínu ac3dtype:t0007</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Termín IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0007">http://rs.tdwg.org/ac3dtype/values/t0007</a></td>
		</tr>
		<tr>
			<td>Změněno</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Verze termínu IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0007-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0007-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Štítek</td>
			<td>multi-file image slice series</td>
		</tr>
		<tr>
			<td>Definice</td>
			<td>Derived image data where each image represents a virtual slice of 3D volume. Images are stacked and arranged in series with specific spacing between slices in order to create the third dimension in a 3D volume.</td>
		</tr>
		<tr>
			<td>Definice odvozená z</td>
			<td><a href="http://www.morphosource.org/terms/mscv/ReconstructedImageStack">http://www.morphosource.org/terms/mscv/ReconstructedImageStack</a></td>
		</tr>
		<tr>
			<td>Řízená hodnota</td>
			<td>multiFileImageSliceSeries</td>
		</tr>
		<tr>
			<td>Typ</td>
			<td>Koncept</td>
		</tr>
		<tr>
			<td>Rozhodnutí výkonného výboru</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0008"></a>Název termínu ac3dtype:t0008</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Termín IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0008">http://rs.tdwg.org/ac3dtype/values/t0008</a></td>
		</tr>
		<tr>
			<td>Změněno</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Verze termínu IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0008-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0008-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Štítek</td>
			<td>single-file volume image</td>
		</tr>
		<tr>
			<td>Definice</td>
			<td>A single derived file where image data for all "virtual slices" of a 3D volume are included, allowing a three-dimensionally rendered representation of a 3D object. (formats like NRRD and 3Dtiff are examples)</td>
		</tr>
		<tr>
			<td>Řízená hodnota</td>
			<td>singleFileVolumeImage</td>
		</tr>
		<tr>
			<td>Typ</td>
			<td>Koncept</td>
		</tr>
		<tr>
			<td>Rozhodnutí výkonného výboru</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0009"></a>Název termínu ac3dtype:t0009</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Termín IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0009">http://rs.tdwg.org/ac3dtype/values/t0009</a></td>
		</tr>
		<tr>
			<td>Změněno</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Verze termínu IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0009-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0009-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Štítek</td>
			<td>vector</td>
		</tr>
		<tr>
			<td>Definice</td>
			<td>Image data defined by geometric points, lines, curves, and polygons.</td>
		</tr>
		<tr>
			<td>Řízená hodnota</td>
			<td>vector</td>
		</tr>
		<tr>
			<td>Typ</td>
			<td>Koncept</td>
		</tr>
		<tr>
			<td>Rozhodnutí výkonného výboru</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0010"></a>Název termínu ac3dtype:t0010</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Termín IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0010">http://rs.tdwg.org/ac3dtype/values/t0010</a></td>
		</tr>
		<tr>
			<td>Změněno</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Verze termínu IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0010-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0010-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Štítek</td>
			<td>point cloud with dependencies</td>
		</tr>
		<tr>
			<td>Definice</td>
			<td>A set of points in a 3D coordinate system with optional associated texture or color file</td>
		</tr>
		<tr>
			<td>Řízená hodnota</td>
			<td>pointCloudWithDependencies</td>
		</tr>
		<tr>
			<td>Typ</td>
			<td>Koncept</td>
		</tr>
		<tr>
			<td>Rozhodnutí výkonného výboru</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0011"></a>Název termínu ac3dtype:t0011</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Termín IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0011">http://rs.tdwg.org/ac3dtype/values/t0011</a></td>
		</tr>
		<tr>
			<td>Změněno</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>Verze termínu IRI</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0011-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0011-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Štítek</td>
			<td>polygonal mesh with dependencies</td>
		</tr>
		<tr>
			<td>Definice</td>
			<td>A wireframe or digital surface model consisting of polygons with optional associated texture or color file</td>
		</tr>
		<tr>
			<td>Řízená hodnota</td>
			<td>polygonalMeshWithDependencies</td>
		</tr>
		<tr>
			<td>Typ</td>
			<td>Koncept</td>
		</tr>
		<tr>
			<td>Rozhodnutí výkonného výboru</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>


