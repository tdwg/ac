# Controlled Vocabulary for Audiovisual Core Content Description: List of Terms

Title
: Controlled Vocabulary for Audiovisual Core Content Description: List of Terms

Namespace IRI
: <http://rs.tdwg.org/accd/values/>

Preferred namespace abbreviation
: accd:

Date de publication de la dernière mise à jour
: 2026-08-18

Date de création
: 2026-08-18

Fait partie du standard TDWG
: <http://www.tdwg.org/standards/638>

Cette version
: <http://rs.tdwg.org/ac/doc/3dtype/2026-08-18>

Dernière version
: <http://rs.tdwg.org/ac/doc/3dtype/>

Version précédente
: Abstract
: Audiovisual Core uses the terms ac:digital3DResourceType and ac:digital3DResourceTypeLiteral to describe the media format of a 3D resource. This controlled vocabulary provides values for those terms.

Contributeurs
: [Doug M. Boyer](https://orcid.org/0000-0002-8697-2999) ([Duke University](http://www.wikidata.org/entity/Q168751)), [Jon Blundell](https://orcid.org/0000-0003-2493-9912) ([Smithsonian Institution](http://www.wikidata.org/entity/Q131626)), [Gary J. Motz](https://orcid.org/0000-0002-6712-2139) ([Indiana Geological and Water Survey](http://www.wikidata.org/entity/Q6023194)), [Adam N. Rountrey](https://orcid.org/0000-0003-0939-9102) ([University of Michigan Museum of Paleontology](http://www.wikidata.org/entity/Q96220204)), [Rebecca Snyder](https://orcid.org/0000-0002-0028-6139) ([Smithsonian Institution](http://www.wikidata.org/entity/Q131626)), [Jocelyn Triplett](https://orcid.org/0000-0003-3452-2408) ([Duke University](http://www.wikidata.org/entity/Q168751)), [Kate Webbink](https://orcid.org/0000-0002-8347-0942) ([Field Museum of Natural History](http://www.wikidata.org/entity/Q1122595)), [Julie Winchester](https://orcid.org/0000-0001-6578-764X) ([Duke University](http://www.wikidata.org/entity/Q168751))

Créateur :
TDWG Audiovisual Core 3D Enhancement Task Group

Citation :
TDWG Audiovisual Core 3D Enhancement Task Group. 2026. Controlled Vocabulary for Audiovisual Core 3D Resource Type: List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/ac/doc/3dtype/2026-08-18>

## 1 Introduction (informative)

This document includes terms intended to be used as controlled values for Audiovisual Core terms `Iptc4xmpExt:CVterm` and `ac:CVtermLiteral`.

### 1.1 Statut du contenu de ce document

Section 1 is informative (non-normative).

La section 2 est normative.

Section 3 is informative (non-normative).

Dans la section 4, les valeurs de l'`IRI du terme`, de la `Définition` et de la `Valeur contrôlée` sont normatives. La valeur de `Utilisation` (si elle existe pour un terme donné) est normative. Les valeurs de `Nom du Terme` ne sont pas normatives, bien que l'on puisse s'attendre à ce que le préfixe de l'abréviation de l'espace de noms soit celui couramment utilisé pour l'espace de noms du terme.  `Label` and the values of all other properties are non-normative.

### 1.2 Mots clés RFC 2119

Les mots clés "MUST/DOIT", "MUST NOT/NE DOIT PAS", "REQUIRED/OBLIGATOIRE", "SHALL/DEVRA", "SHALL NOT/NE DEVRA PAS", "SHOULD/DEVRAIT", "SHOULD NOT/NE DEVRAIT PAS", "RECOMMENDED/RECOMMANDÉ", "MAY/POURRAIT", et "OPTIONAL/OPTIONNEL" dans ce document doivent être interprétés comme défini dans les références [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) et [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174)] uniquement lorsqu’ils apparaissent en majuscules, comme ci-dessus.

## 2 Utilisation des termes

### 2.1 Relationship of value types to property terms

In accordance with [the Audiovisual Core Term List document](http://rs.tdwg.org/ac/doc/termlist/), unabbreviated term IRIs SHOULD be used as values of the property `Iptc4xmpExt:CVterm`. Controlled value strings SHOULD be used as values of the property `ac:CVtermLiteral`.

### 2.2 Relationship between values of ac:CVtermLiteral and Iptc4xmpExt:CVterm

An IRI for a term in this vocabulary denotes the same concept as the concept denoted by the controlled value string for the same term. Thus a client MAY infer an IRI value for `Iptc4xmpExt:CVterm` given a controlled value string for `ac:CVtermLiteral` even if that IRI is not explicitly stated. The practical implication is that data aggregators MAY materialize values for the preferred `Iptc4xmpExt:CVterm` property in cases where providers only provide values for `ac:CVtermLiteral`.

## 3 Index des termes



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

## 4 Vocabulaire
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t"></a>Nom du Terme ac3dtype:t</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t">http://rs.tdwg.org/ac3dtype/values/t</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>3D resource type controlled vocabulary</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>A SKOS ConceptScheme to be used as a controlled vocabulary for the Audiovisual Core terms ac:digital3DResourceType and ac:digital3DResourceTypeLiteral</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/2004/02/skos/core#ConceptScheme</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0001"></a>Nom du Terme ac3dtype:t0001</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0001">http://rs.tdwg.org/ac3dtype/values/t0001</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0001-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0001-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>raster data</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>Gridded data composed of pixels that store values.</td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>rasterData</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0002"></a>Nom du Terme ac3dtype:t0002</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0002">http://rs.tdwg.org/ac3dtype/values/t0002</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0002-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0002-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>raw data</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>The initial uncompressed and unprocessed data generated through a 3D modality.</td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>rawData</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0003"></a>Nom du Terme ac3dtype:t0003</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0003">http://rs.tdwg.org/ac3dtype/values/t0003</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0003-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0003-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>sinogram</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>Raw data from a CT scanner with X-Ray Detector Configuration Type of Slot (scanned slot, slit, or spot). Projections are often analyzed and processed to create a reconstructed image stack.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/Sinograms">http://www.morphosource.org/terms/mscv/Sinograms</a></td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>sinogram</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0004"></a>Nom du Terme ac3dtype:t0004</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0004">http://rs.tdwg.org/ac3dtype/values/t0004</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0004-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0004-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>multi-file projection series</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>Raw image data from a CT scanner with a X-Ray Detector Configuration Type of Area (single or tiled detector). Projections are often analyzed and processed to create a reconstructed image stack.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/Projections">http://www.morphosource.org/terms/mscv/Projections</a> </td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>multiFileProjectionSeries</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0005"></a>Nom du Terme ac3dtype:t0005</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0005">http://rs.tdwg.org/ac3dtype/values/t0005</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0005-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0005-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>multi-file photo collection</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>Multiple overlapping photographs of an object.</td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>multiFilePhotoCollection</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0006"></a>Nom du Terme ac3dtype:t0006</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0006">http://rs.tdwg.org/ac3dtype/values/t0006</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0006-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0006-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>volume</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>Three-dimensional digital representation of an object. Rendered as a grid of three-dimensional pixels (aka voxels)</td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>volume</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0007"></a>Nom du Terme ac3dtype:t0007</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0007">http://rs.tdwg.org/ac3dtype/values/t0007</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0007-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0007-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>multi-file image slice series</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>Derived image data where each image represents a virtual slice of 3D volume. Images are stacked and arranged in series with specific spacing between slices in order to create the third dimension in a 3D volume.</td>
		</tr>
		<tr>
			<td>definition_derived_from</td>
			<td><a href="http://www.morphosource.org/terms/mscv/ReconstructedImageStack">http://www.morphosource.org/terms/mscv/ReconstructedImageStack</a></td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>multiFileImageSliceSeries</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0008"></a>Nom du Terme ac3dtype:t0008</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0008">http://rs.tdwg.org/ac3dtype/values/t0008</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0008-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0008-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>single-file volume image</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>A single derived file where image data for all "virtual slices" of a 3D volume are included, allowing a three-dimensionally rendered representation of a 3D object. (formats like NRRD and 3Dtiff are examples)</td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>singleFileVolumeImage</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0009"></a>Nom du Terme ac3dtype:t0009</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0009">http://rs.tdwg.org/ac3dtype/values/t0009</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0009-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0009-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>vector</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>Image data defined by geometric points, lines, curves, and polygons.</td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>vector</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0010"></a>Nom du Terme ac3dtype:t0010</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0010">http://rs.tdwg.org/ac3dtype/values/t0010</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0010-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0010-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>point cloud with dependencies</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>A set of points in a 3D coordinate system with optional associated texture or color file</td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>pointCloudWithDependencies</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac3dtype_t0011"></a>Nom du Terme ac3dtype:t0011</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>IRI du terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/t0011">http://rs.tdwg.org/ac3dtype/values/t0011</a></td>
		</tr>
		<tr>
			<td>Modifié</td>
			<td>2026-08-18</td>
		</tr>
		<tr>
			<td>IRI de la version du Terme</td>
			<td><a href="http://rs.tdwg.org/ac3dtype/values/version/t0011-2026-08-18">http://rs.tdwg.org/ac3dtype/values/version/t0011-2026-08-18</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>polygonal mesh with dependencies</td>
		</tr>
		<tr>
			<td>Définition</td>
			<td>A wireframe or digital surface model consisting of polygons with optional associated texture or color file</td>
		</tr>
		<tr>
			<td>Valeur contrôlée</td>
			<td>polygonalMeshWithDependencies</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Décision du Comité Exécutif</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-08-18_64">http://rs.tdwg.org/decisions/decision-2026-08-18_64</a></td>
		</tr>
	</tbody>
</table>


