# subjectOrientation Controlled Vocabulary

**Title:** subjectOrientation Controlled Vocabulary

**Namespace URI:** http://rs.tdwg.org/acorient/values/

**Preferred namespace abbreviation:** acorient:

**Date version issued:** 2023-04-26

**Date created:** 2023-04-26

**Part of TDWG Standard:** http://www.tdwg.org/standards/638

**This version:** http://rs.tdwg.org/ac/doc/orient/2023-04-26

**Latest version:** http://rs.tdwg.org/ac/doc/orient/

**Abstract:** The Audiovisual Core term `subjectOrientation` describes the viewing orientation relative to an organism or part of an organism depicted in a media item or region of interest. The subjectOrientation Controlled Vocabulary provides terms that should be used as values for `ac:subjectOrientation` and its literal-valued analog `ac:subjectOrientationLiteral`. 

**Contributors:** Steven J. Baskauf (Vanderbilt University Libraries), Neil S. Cobb (Merriam-Powell Center for Environmental Research, Northern Arizona University), Jennifer C. Girón Duque (Natural Science Research Laboratory, Museum of Texas Tech University), Matthew Nielsen (Stockholm University), Mervin E. Pérez (Universidad de San Carlos de Guatemala), Randy Singer (University of Michigan)

**Creator:** TDWG Views Controlled Vocabularies Task Group

**Bibliographic citation:** Views Controlled Vocabularies Task Group. 2023. subjectOrientation Controlled Vocabulary. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/ac/doc/orient/2023-04-26>


## 1 Introduction (informative)

This document includes terms intended to be used as controlled values for the Audiovisual Core terms `ac:subjectOrientation` and `ac:subjectOrientationLiteral`. A [JSON-LD representation](https://tdwg.github.io/rs.tdwg.org/cvJson/acorient.json) (including translations to multiple languages) of this SKOS Concept Scheme is available. For more information about how to use this vocabulary, see the [subjectPart and subjectOrientation Controlled Vocabularies User Guide](https://github.com/tdwg/ac/blob/master/views/views_user_guide.pdf).

### 1.1 Status of the content of this document

Section 1 is informative (non-normative).

Section 2 is normative except as noted.

Section 3 is informative.

In Section 4, the values of the `Term IRI`, `Definition`, and `Controlled value` are normative. The value of `Usage` (if it exists for a given term) is normative.  The value of `Has broader concept` is normative. The values of `Term Name` are non-normative, although one can expect that the namespace abbreviation prefix is one commonly used for the term namespace.  `Label` and the values of all other properties (such as `Examples` or `Notes`) are non-normative.

### 1.2 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

### 1.3 User feedback reports
For perspective on the development of this [vocabulary enhancement](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md#4-vocabulary-enhancements), refer to the [final Feature Report](https://github.com/tdwg/ac/blob/master/views/final-requirements.md) used to determine the requirements for the vocabulary. The Implementation Experience Report was published in *Biodiversity Information Science and Standards* 7:e94188 and is available at <http://doi.org/10.3897/biss.7.94188>

## 2 Use of Terms

### 2.1 Relationship of value types to property terms

In accordance with the [Audiovisual Core Term List](http://rs.tdwg.org/ac/doc/termlist/) document, unabbreviated term IRIs MUST be used as values of the property `ac:subjectOrientation`. Controlled value strings SHOULD be used as values of the property `ac:subjectOrientationLiteral`.

### 2.2 Relationships with other concept schemes and collections (informative)

Particular `ac:subjectOrientation` values are appropriate for some `ac:subjectPart` values. The relationships between concepts in these two schemes are described by a [JSON-LD serialized SKOS Collection for each subject part](https://tdwg.github.io/rs.tdwg.org/cvJson/acorient_collection.json) that designates which subject orientations are appropriate for that part. Similarly, [JSON-LD serialized SKOS Collections have been established for some organism groups](https://tdwg.github.io/rs.tdwg.org/cvJson/acpart_collection.json) to indicate which subject parts exist for members of those groups. These collections are provided to aid application developers in filtering the concepts that should be presented to users and they may also be used for validation.

Human-readable collection lists of controlled value strings are available for [subjectPart](https://ac.tdwg.org/part_collections) and [subjectOrientation](https://ac.tdwg.org/orient_collections).

Neither of these Collections are normative and they are maintained outside of the Audiovisual Core standards framework in order to make their development agile.

## 3 Term index


[aboral side](#acorient_r0013) |
[anterior side](#acorient_r0001) |
[apical side](#acorient_r0010) |
[basal side](#acorient_r0011) |
[dorsal side](#acorient_r0006) |
[lateral side](#acorient_r0003) |
[left side](#acorient_r0005) |
[lower side](#acorient_r0009) |
[oral side](#acorient_r0012) |
[posterior side](#acorient_r0002) |
[right side](#acorient_r0004) |
[subject orientation concept scheme](#acorient_r) |
[unspecified orientation](#acorient_r0000) |
[upper side](#acorient_r0008) |
[ventral side](#acorient_r0007) 

## 4 Vocabulary
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acorient_r"></a>Term Name  acorient:r</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/r">http://rs.tdwg.org/acorient/values/r</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/version/r-2023-04-26">http://rs.tdwg.org/acorient/values/version/r-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>subject orientation concept scheme</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>a SKOS concept scheme for orientation</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/2004/02/skos/core#ConceptScheme</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acorient_r0000"></a>Term Name  acorient:r0000</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/r0000">http://rs.tdwg.org/acorient/values/r0000</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/version/r0000-2023-04-26">http://rs.tdwg.org/acorient/values/version/r0000-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>unspecified orientation</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>orientation is not known because it is not specified</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>unspecifiedOrientation</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2023-04-26_39 ">http://rs.tdwg.org/decisions/decision-2023-04-26_39 </a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acorient_r0001"></a>Term Name  acorient:r0001</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/r0001">http://rs.tdwg.org/acorient/values/r0001</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/version/r0001-2023-04-26">http://rs.tdwg.org/acorient/values/version/r0001-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>anterior side</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>view of the side towards the head or forward end of the organism</td>
		</tr>
		<tr>
			<td>Definition derived from:</td>
			<td><a href="http://purl.obolibrary.org/obo/BSPO_0000055">http://purl.obolibrary.org/obo/BSPO_0000055</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>anterior</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2023-04-26_39 ">http://rs.tdwg.org/decisions/decision-2023-04-26_39 </a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acorient_r0002"></a>Term Name  acorient:r0002</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/r0002">http://rs.tdwg.org/acorient/values/r0002</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/version/r0002-2023-04-26">http://rs.tdwg.org/acorient/values/version/r0002-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>posterior side</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>view of the side away from the head or towards the rear end of the organism</td>
		</tr>
		<tr>
			<td>Definition derived from:</td>
			<td><a href="http://purl.obolibrary.org/obo/BSPO_0000056">http://purl.obolibrary.org/obo/BSPO_0000056</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>posterior</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2023-04-26_39 ">http://rs.tdwg.org/decisions/decision-2023-04-26_39 </a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acorient_r0003"></a>Term Name  acorient:r0003</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/r0003">http://rs.tdwg.org/acorient/values/r0003</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/version/r0003-2023-04-26">http://rs.tdwg.org/acorient/values/version/r0003-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>lateral side</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>view of the side perpendicular to the main axis of the organism</td>
		</tr>
		<tr>
			<td>Definition derived from:</td>
			<td><a href="http://purl.obolibrary.org/obo/BSPO_0000066">http://purl.obolibrary.org/obo/BSPO_0000066</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>lateral</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2023-04-26_39 ">http://rs.tdwg.org/decisions/decision-2023-04-26_39 </a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acorient_r0004"></a>Term Name  acorient:r0004</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/r0004">http://rs.tdwg.org/acorient/values/r0004</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/version/r0004-2023-04-26">http://rs.tdwg.org/acorient/values/version/r0004-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>right side</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>view of the right side of a whole bilaterally symmetric organism</td>
		</tr>
		<tr>
			<td>Definition derived from:</td>
			<td><a href="http://purl.obolibrary.org/obo/BSPO_0000007">http://purl.obolibrary.org/obo/BSPO_0000007</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>right</td>
		</tr>
		<tr>
			<td>Has broader concept</td>
			<td><a href="#acorient_r0003">acorient:r0003</a></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2023-04-26_39 ">http://rs.tdwg.org/decisions/decision-2023-04-26_39 </a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acorient_r0005"></a>Term Name  acorient:r0005</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/r0005">http://rs.tdwg.org/acorient/values/r0005</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/version/r0005-2023-04-26">http://rs.tdwg.org/acorient/values/version/r0005-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>left side</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>view of the left side of a whole bilaterally symmetric organism</td>
		</tr>
		<tr>
			<td>Definition derived from:</td>
			<td><a href="http://purl.obolibrary.org/obo/BSPO_0000000">http://purl.obolibrary.org/obo/BSPO_0000000</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>left</td>
		</tr>
		<tr>
			<td>Has broader concept</td>
			<td><a href="#acorient_r0003">acorient:r0003</a></td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2023-04-26_39 ">http://rs.tdwg.org/decisions/decision-2023-04-26_39 </a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acorient_r0006"></a>Term Name  acorient:r0006</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/r0006">http://rs.tdwg.org/acorient/values/r0006</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/version/r0006-2023-04-26">http://rs.tdwg.org/acorient/values/version/r0006-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>dorsal side</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>view of the side dorsal to the frontal plane of a bilaterally symmetric organism</td>
		</tr>
		<tr>
			<td>Definition derived from:</td>
			<td><a href="http://purl.obolibrary.org/obo/BSPO_0000063">http://purl.obolibrary.org/obo/BSPO_0000063</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>dorsal</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2023-04-26_39 ">http://rs.tdwg.org/decisions/decision-2023-04-26_39 </a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acorient_r0007"></a>Term Name  acorient:r0007</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/r0007">http://rs.tdwg.org/acorient/values/r0007</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/version/r0007-2023-04-26">http://rs.tdwg.org/acorient/values/version/r0007-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>ventral side</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>view of the side ventral to the frontal plane of a bilaterally symmetric organism</td>
		</tr>
		<tr>
			<td>Definition derived from:</td>
			<td><a href="http://purl.obolibrary.org/obo/BSPO_0000068">http://purl.obolibrary.org/obo/BSPO_0000068</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>ventral</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2023-04-26_39 ">http://rs.tdwg.org/decisions/decision-2023-04-26_39 </a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acorient_r0008"></a>Term Name  acorient:r0008</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/r0008">http://rs.tdwg.org/acorient/values/r0008</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/version/r0008-2023-04-26">http://rs.tdwg.org/acorient/values/version/r0008-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>upper side</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>view of the side of the part oriented toward the central axis of a plant (adaxial)</td>
		</tr>
		<tr>
			<td>Definition derived from:</td>
			<td><a href="http://purl.obolibrary.org/obo/PATO_0002047">http://purl.obolibrary.org/obo/PATO_0002047</a></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>In plants, use this term rather than "dorsal". For types of plants or fungi having horizontal parts and lacking a clear central axis, this is the surface away from the ground. </td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>BSPO has adaxial/abaxial axis <a href="http://purl.obolibrary.org/obo/BSPO_0000195">http://purl.obolibrary.org/obo/BSPO_0000195</a> but not the sides defined by that axis</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>upper</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2023-04-26_39 ">http://rs.tdwg.org/decisions/decision-2023-04-26_39 </a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acorient_r0009"></a>Term Name  acorient:r0009</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/r0009">http://rs.tdwg.org/acorient/values/r0009</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/version/r0009-2023-04-26">http://rs.tdwg.org/acorient/values/version/r0009-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>lower side</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>view of the side of the part oriented away from the central axis of a plant (abaxial)</td>
		</tr>
		<tr>
			<td>Definition derived from:</td>
			<td><a href="http://purl.obolibrary.org/obo/PATO_0002046">http://purl.obolibrary.org/obo/PATO_0002046</a></td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>In plants, use this term rather than "ventral". For types of plants or fungi having horizontal parts and lacking a clear central axis, this is the surface towards the ground. </td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>BSPO has adaxial/abaxial axis <a href="http://purl.obolibrary.org/obo/BSPO_0000195">http://purl.obolibrary.org/obo/BSPO_0000195</a> but not the sides defined by that axis</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>lower</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2023-04-26_39 ">http://rs.tdwg.org/decisions/decision-2023-04-26_39 </a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acorient_r0010"></a>Term Name  acorient:r0010</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/r0010">http://rs.tdwg.org/acorient/values/r0010</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/version/r0010-2023-04-26">http://rs.tdwg.org/acorient/values/version/r0010-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>apical side</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>view of the side of the part oriented towards the end of the axis away from its attachment point (the apex)</td>
		</tr>
		<tr>
			<td>Definition derived from:</td>
			<td><a href="http://purl.obolibrary.org/obo/BSPO_0000057">http://purl.obolibrary.org/obo/BSPO_0000057</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>apical</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2023-04-26_39 ">http://rs.tdwg.org/decisions/decision-2023-04-26_39 </a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acorient_r0011"></a>Term Name  acorient:r0011</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/r0011">http://rs.tdwg.org/acorient/values/r0011</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/version/r0011-2023-04-26">http://rs.tdwg.org/acorient/values/version/r0011-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>basal side</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>view of the side of the part oriented towards the attachment point of the axis</td>
		</tr>
		<tr>
			<td>Definition derived from:</td>
			<td><a href="http://purl.obolibrary.org/obo/BSPO_0000058">http://purl.obolibrary.org/obo/BSPO_0000058</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>basal</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2023-04-26_39 ">http://rs.tdwg.org/decisions/decision-2023-04-26_39 </a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acorient_r0012"></a>Term Name  acorient:r0012</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/r0012">http://rs.tdwg.org/acorient/values/r0012</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/version/r0012-2023-04-26">http://rs.tdwg.org/acorient/values/version/r0012-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>oral side</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>view of the side of the organism oriented towards the oral opening</td>
		</tr>
		<tr>
			<td>Definition derived from:</td>
			<td><a href="http://purl.obolibrary.org/obo/BSPO_0015201">http://purl.obolibrary.org/obo/BSPO_0015201</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>oral</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2023-04-26_39 ">http://rs.tdwg.org/decisions/decision-2023-04-26_39 </a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acorient_r0013"></a>Term Name  acorient:r0013</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/r0013">http://rs.tdwg.org/acorient/values/r0013</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acorient/values/version/r0013-2023-04-26">http://rs.tdwg.org/acorient/values/version/r0013-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>aboral side</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>view of the side of the organism oriented away from the oral opening</td>
		</tr>
		<tr>
			<td>Definition derived from:</td>
			<td><a href="http://purl.obolibrary.org/obo/BSPO_0015202">http://purl.obolibrary.org/obo/BSPO_0015202</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>aboral</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2023-04-26_39 ">http://rs.tdwg.org/decisions/decision-2023-04-26_39 </a></td>
		</tr>
	</tbody>
</table>


