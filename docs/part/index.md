# Controlled Vocabulary for Audiovisual Core subjectPart: List of Terms

Title
: Controlled Vocabulary for Audiovisual Core subjectPart: List of Terms

Namespace IRI
: <http://rs.tdwg.org/acpart/values/>

Preferred namespace abbreviation
: acpart:

Date version issued
: 2023-04-26

Date created
: 2023-04-26

Part of TDWG Standard
: <http://www.tdwg.org/standards/638>

This version
: <http://rs.tdwg.org/ac/doc/part/2023-04-26>

Latest version
: <http://rs.tdwg.org/ac/doc/part/>

Abstract
: The Audiovisual Core term subjectPart describes the part of an organism morphology, behaviour, environment depicted in a media item or region of interest. The subjectPart Controlled Vocabulary provides terms that should be used as values for ac:subjectPart and its literal-valued analog ac:subjectPartLiteral.

Contributors
: [Steven J. Baskauf](https://orcid.org/0000-0003-4365-3135) ([Vanderbilt University Libraries, Nashville, TN, USA](http://www.wikidata.org/entity/Q16849893)), [Neil S. Cobb](https://orcid.org/0000-0002-6155-9444) ([Merriam-Powell Center for Environmental Research, Northern Arizona University, Flagstaff, AZ, USA](http://www.wikidata.org/entity/Q139901)), [Jennifer C. Girón Duque](https://orcid.org/0000-0002-0851-6883) ([Natural Science Research Laboratory, Museum of Texas Tech University, Lubbock, TX, USA](http://www.wikidata.org/entity/Q6941030)), [Matthew Nielsen](https://orcid.org/0000-0002-0388-1187) ([University of Oulu, Oulu, Finland](http://www.wikidata.org/entity/Q1357517)), [Mervin E. Pérez](https://orcid.org/0000-0003-4277-8948) ([Universidad de San Carlos de Guatemala, Guatemala City, Guatemala](http://www.wikidata.org/entity/Q607331)), [Randy Singer](https://orcid.org/0000-0003-2440-7625) ([University of Michigan, Ann Arbor, MI, USA](http://www.wikidata.org/entity/Q230492)), [Anna M. L. Klompen](https://orcid.org/0000-0001-8939-0057) ([University of Kansas, Lawrence, KS, USA](http://www.wikidata.org/entity/Q52413))

Creator
: TDWG Views Controlled Vocabularies Task Group

Bibliographic citation
: TDWG Views Controlled Vocabularies Task Group. 2023. Controlled Vocabulary for Audiovisual Core subjectPart: List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/ac/doc/part/2023-04-26>

## 1 Introduction (informative)

This document includes terms intended to be used as controlled values for the Audiovisual Core terms `ac:subjectPart` and `ac:subjectPartLiteral`. A [JSON-LD representation](https://tdwg.github.io/rs.tdwg.org/cvJson/acpart.json) (including translations to multiple languages) of this SKOS Concept Scheme is available. For more information about how to use this vocabulary, see the [subjectPart and subjectOrientation Controlled Vocabularies User Guide](https://github.com/tdwg/ac/blob/master/views/views_user_guide.pdf).

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

In accordance with the [Audiovisual Core Term List](http://rs.tdwg.org/ac/doc/termlist/) document, unabbreviated term IRIs MUST be used as values of the property `ac:subjectPart`. Controlled value strings SHOULD be used as values of the property `ac:subjectPartLiteral`.

### 2.2 Relationships with other concept schemes and collections (informative)

Particular `ac:subjectOrientation` values are appropriate for some `ac:subjectPart` values. The relationships between concepts in these two schemes are described by a [JSON-LD serialized SKOS Collection for each subject part](https://tdwg.github.io/rs.tdwg.org/cvJson/acorient_collection.json) that designates which subject orientations are appropriate for that part. Similarly, [JSON-LD serialized SKOS Collections have been established for some organism groups](https://tdwg.github.io/rs.tdwg.org/cvJson/acpart_collection.json) to indicate which subject parts exist for members of those groups. These collections are provided to aid application developers in filtering the concepts that should be presented to users and they may also be used for validation.

Human-readable collection lists of controlled value strings are available for [subjectPart](https://ac.tdwg.org/part_collections) and [subjectOrientation](https://ac.tdwg.org/orient_collections).

Neither of these Collections are normative and they are maintained outside of the Audiovisual Core standards framework in order to make their development agile.

## 3 Term index



[abdomen](#acpart_p0015) |
[antenna](#acpart_p0018) |
[bark](#acpart_p0002) |
[bud](#acpart_p0032) |
[cranium](#acpart_p0028) |
[egg](#acpart_p0031) |
[entire organism](#acpart_p0001) |
[eye](#acpart_p0024) |
[female cone](#acpart_p0011) |
[fin](#acpart_p0030) |
[flower](#acpart_p0012) |
[foreleg](#acpart_p0021) |
[forewing](#acpart_p0019) |
[fruit](#acpart_p0008) |
[genitalia](#acpart_p0026) |
[head](#acpart_p0013) |
[hindleg](#acpart_p0023) |
[hindwing](#acpart_p0020) |
[inflorescence](#acpart_p0007) |
[leaf](#acpart_p0005) |
[leg](#acpart_p0016) |
[male cone](#acpart_p0010) |
[mandible](#acpart_p0029) |
[midleg](#acpart_p0022) |
[seed](#acpart_p0009) |
[shell](#acpart_p0025) |
[skull](#acpart_p0027) |
[stem](#acpart_p0004) |
[strobilis (cone)](#acpart_p0006) |
[subject part concept scheme](#acpart_p) |
[thorax](#acpart_p0014) |
[twig](#acpart_p0003) |
[unspecified part](#acpart_p0000) |
[wing](#acpart_p0017)

## 4 Vocabulary
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acpart_p"></a>Term Name acpart:p</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p">http://rs.tdwg.org/acpart/values/p</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p-2023-04-26">http://rs.tdwg.org/acpart/values/version/p-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>subject part concept scheme</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>a SKOS concept scheme for ac:subjectOrientation</td>
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
			<th colspan="2"><a id="acpart_p0000"></a>Term Name acpart:p0000</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0000">http://rs.tdwg.org/acpart/values/p0000</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0000-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0000-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>unspecified part</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Part is not known because it is not specified</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>unspecifiedPart</td>
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
			<th colspan="2"><a id="acpart_p0001"></a>Term Name acpart:p0001</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0001">http://rs.tdwg.org/acpart/values/p0001</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0001-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0001-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>entire organism</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An entire multicellular organism</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/CARO_0000012">http://purl.obolibrary.org/obo/CARO_0000012</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="http://bioimages.vanderbilt.edu/baskauf/25638">http://bioimages.vanderbilt.edu/baskauf/25638</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>entireOrganism</td>
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
			<th colspan="2"><a id="acpart_p0002"></a>Term Name acpart:p0002</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0002">http://rs.tdwg.org/acpart/values/p0002</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0002-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0002-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>bark</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Plant tissue outside the vascular cambium</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/PO_0004518">http://purl.obolibrary.org/obo/PO_0004518</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="http://bioimages.vanderbilt.edu/baskauf/41910">http://bioimages.vanderbilt.edu/baskauf/41910</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>bark</td>
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
			<th colspan="2"><a id="acpart_p0003"></a>Term Name acpart:p0003</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0003">http://rs.tdwg.org/acpart/values/p0003</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0003-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0003-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>twig</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Plant shoot axis developed from axillary buds</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/PO_0025073">http://purl.obolibrary.org/obo/PO_0025073</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="http://bioimages.vanderbilt.edu/baskauf/63779">http://bioimages.vanderbilt.edu/baskauf/63779</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>twig</td>
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
			<th colspan="2"><a id="acpart_p0004"></a>Term Name acpart:p0004</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0004">http://rs.tdwg.org/acpart/values/p0004</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0004-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0004-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>stem</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Plant shoot axis that defines the primary axis</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/PO_0009047">http://purl.obolibrary.org/obo/PO_0009047</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="http://bioimages.vanderbilt.edu/baskauf/65236">http://bioimages.vanderbilt.edu/baskauf/65236</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>stem</td>
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
			<th colspan="2"><a id="acpart_p0005"></a>Term Name acpart:p0005</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0005">http://rs.tdwg.org/acpart/values/p0005</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0005-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0005-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>leaf</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Plant non-reproductive phyllome</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/PO_0025034">http://purl.obolibrary.org/obo/PO_0025034</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="http://bioimages.vanderbilt.edu/baskauf/41905">http://bioimages.vanderbilt.edu/baskauf/41905</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>leaf</td>
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
			<th colspan="2"><a id="acpart_p0006"></a>Term Name acpart:p0006</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0006">http://rs.tdwg.org/acpart/values/p0006</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0006-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0006-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>strobilis (cone)</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Plant reproductive system consisting of sporophylls</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/PO_0025083">http://purl.obolibrary.org/obo/PO_0025083</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="http://bioimages.vanderbilt.edu/baskauf/60561">http://bioimages.vanderbilt.edu/baskauf/60561</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>strobilis</td>
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
			<th colspan="2"><a id="acpart_p0007"></a>Term Name acpart:p0007</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0007">http://rs.tdwg.org/acpart/values/p0007</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0007-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0007-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>inflorescence</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Plant reproductive shoot system containing flowers</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/PO_0009049">http://purl.obolibrary.org/obo/PO_0009049</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="http://bioimages.vanderbilt.edu/baskauf/57919">http://bioimages.vanderbilt.edu/baskauf/57919</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>inflorescence</td>
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
			<th colspan="2"><a id="acpart_p0008"></a>Term Name acpart:p0008</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0008">http://rs.tdwg.org/acpart/values/p0008</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0008-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0008-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>fruit</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Plant structure developing from a flower</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/PO_0009001">http://purl.obolibrary.org/obo/PO_0009001</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="http://bioimages.vanderbilt.edu/baskauf/41891">http://bioimages.vanderbilt.edu/baskauf/41891</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>fruit</td>
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
			<th colspan="2"><a id="acpart_p0009"></a>Term Name acpart:p0009</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0009">http://rs.tdwg.org/acpart/values/p0009</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0009-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0009-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>seed</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Plant structure containing dormant embryo</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/PO_0009010">http://purl.obolibrary.org/obo/PO_0009010</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="http://bioimages.vanderbilt.edu/baskauf/30744">http://bioimages.vanderbilt.edu/baskauf/30744</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>seed</td>
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
			<th colspan="2"><a id="acpart_p0010"></a>Term Name acpart:p0010</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0010">http://rs.tdwg.org/acpart/values/p0010</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0010-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0010-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>male cone</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Plant strobilis bearing pollen</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/PO_0005031">http://purl.obolibrary.org/obo/PO_0005031</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="http://bioimages.vanderbilt.edu/baskauf/51365">http://bioimages.vanderbilt.edu/baskauf/51365</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>maleCone</td>
		</tr>
		<tr>
			<td>Has broader concept</td>
			<td><a href="#acpart_p0006">acpart:p0006</a></td>
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
			<th colspan="2"><a id="acpart_p0011"></a>Term Name acpart:p0011</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0011">http://rs.tdwg.org/acpart/values/p0011</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0011-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0011-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>female cone</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Plant strobilis bearing ovules</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/PO_0005032">http://purl.obolibrary.org/obo/PO_0005032</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="http://bioimages.vanderbilt.edu/baskauf/51363">http://bioimages.vanderbilt.edu/baskauf/51363</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>femaleCone</td>
		</tr>
		<tr>
			<td>Has broader concept</td>
			<td><a href="#acpart_p0006">acpart:p0006</a></td>
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
			<th colspan="2"><a id="acpart_p0012"></a>Term Name acpart:p0012</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0012">http://rs.tdwg.org/acpart/values/p0012</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0012-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0012-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>flower</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Plant reproductive shoot system containing a carpel</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/PO_0009046">http://purl.obolibrary.org/obo/PO_0009046</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="http://bioimages.vanderbilt.edu/baskauf/52498">http://bioimages.vanderbilt.edu/baskauf/52498</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>flower</td>
		</tr>
		<tr>
			<td>Has broader concept</td>
			<td><a href="#acpart_p0007">acpart:p0007</a></td>
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
			<th colspan="2"><a id="acpart_p0013"></a>Term Name acpart:p0013</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0013">http://rs.tdwg.org/acpart/values/p0013</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0013-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0013-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>head</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Anterior-most division of the body</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/UBERON_0000033">http://purl.obolibrary.org/obo/UBERON_0000033</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="https://monarch.calacademy.org/mnt/target-images/CASTYPE/00001/CASTYPE1503_h.jpg">https://monarch.calacademy.org/mnt/target-images/CASTYPE/00001/CASTYPE1503_h.jpg</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>head</td>
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
			<th colspan="2"><a id="acpart_p0014"></a>Term Name acpart:p0014</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0014">http://rs.tdwg.org/acpart/values/p0014</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0014-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0014-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>thorax</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The middle division of the insect body bearing locomotor appendages</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/UBERON_6000015">http://purl.obolibrary.org/obo/UBERON_6000015</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="https://mczbase.mcz.harvard.edu/specimen_images/entomology/large/MCZ-ENT00610536_Lasioglossum_oblongum_thl.jpg">https://mczbase.mcz.harvard.edu/specimen_images/entomology/large/MCZ-ENT00610536_Lasioglossum_oblongum_thl.jpg</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>thorax</td>
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
			<th colspan="2"><a id="acpart_p0015"></a>Term Name acpart:p0015</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0015">http://rs.tdwg.org/acpart/values/p0015</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0015-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0015-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>abdomen</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The posterior-most division of the insect body</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/UBERON_6000020">http://purl.obolibrary.org/obo/UBERON_6000020</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="https://commons.wikimedia.org/wiki/File:Halictus_scabiosae,_specimen_exonie54,_from_Botevgrad,_Bulgaria_10_(dorsal,_abdomen).jpg">https://commons.wikimedia.org/wiki/File:Halictus_scabiosae,_specimen_exonie54,_from_Botevgrad,_Bulgaria_10_(dorsal,_abdomen).jpg</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>abdomen</td>
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
			<th colspan="2"><a id="acpart_p0016"></a>Term Name acpart:p0016</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0016">http://rs.tdwg.org/acpart/values/p0016</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0016-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0016-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>leg</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Walking appendage</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/UBERON_0002101">http://purl.obolibrary.org/obo/UBERON_0002101</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="https://mczbase.mcz.harvard.edu/specimen_images/entomology/large/MCZ-ENT00000547_Halictus_albitarsis_hlg.jpg">https://mczbase.mcz.harvard.edu/specimen_images/entomology/large/MCZ-ENT00000547_Halictus_albitarsis_hlg.jpg</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>leg</td>
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
			<th colspan="2"><a id="acpart_p0017"></a>Term Name acpart:p0017</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0017">http://rs.tdwg.org/acpart/values/p0017</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0017-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0017-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>wing</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Appendage that is shaped in order to produce lift for flight through the air</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/UBERON_0000023">http://purl.obolibrary.org/obo/UBERON_0000023</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="https://commons.wikimedia.org/wiki/File:Monarch_Butterfly_Danaus_plexippus_Wing_2400px.jpg">https://commons.wikimedia.org/wiki/File:Monarch_Butterfly_Danaus_plexippus_Wing_2400px.jpg</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>wing</td>
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
			<th colspan="2"><a id="acpart_p0018"></a>Term Name acpart:p0018</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0018">http://rs.tdwg.org/acpart/values/p0018</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0018-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0018-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>antenna</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The paired, usually multiple jointed, sensory organs on the head</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/UBERON_0000972">http://purl.obolibrary.org/obo/UBERON_0000972</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="https://commons.wikimedia.org/wiki/File:Blatta_orientalis_male_from_Botevgrad,_Bulgaria_05.jpg">https://commons.wikimedia.org/wiki/File:Blatta_orientalis_male_from_Botevgrad,_Bulgaria_05.jpg</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>antenna</td>
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
			<th colspan="2"><a id="acpart_p0019"></a>Term Name acpart:p0019</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0019">http://rs.tdwg.org/acpart/values/p0019</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0019-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0019-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>forewing</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The paired insect wing that is continuous with the mesonotum</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/AISM_0000037">http://purl.obolibrary.org/obo/AISM_0000037</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="https://mczbase.mcz.harvard.edu/specimen_images/entomology/large/MCZ-ENT00017211_Melissa_porteri_fwg.jpg">https://mczbase.mcz.harvard.edu/specimen_images/entomology/large/MCZ-ENT00017211_Melissa_porteri_fwg.jpg</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>forewing</td>
		</tr>
		<tr>
			<td>Has broader concept</td>
			<td><a href="#acpart_p0017">acpart:p0017</a></td>
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
			<th colspan="2"><a id="acpart_p0020"></a>Term Name acpart:p0020</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0020">http://rs.tdwg.org/acpart/values/p0020</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0020-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0020-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>hindwing</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The paired insect wing that is continuous with the metanotum</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/AISM_0000038">http://purl.obolibrary.org/obo/AISM_0000038</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="https://mczbase.mcz.harvard.edu/specimen_images/entomology/large/MCZ-ENT00610195_Agapostemon_texanus_hwg.jpg">https://mczbase.mcz.harvard.edu/specimen_images/entomology/large/MCZ-ENT00610195_Agapostemon_texanus_hwg.jpg</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>hindwing</td>
		</tr>
		<tr>
			<td>Has broader concept</td>
			<td><a href="#acpart_p0017">acpart:p0017</a></td>
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
			<th colspan="2"><a id="acpart_p0021"></a>Term Name acpart:p0021</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0021">http://rs.tdwg.org/acpart/values/p0021</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0021-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0021-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>foreleg</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Leg of the prothoracic segment</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/UBERON_6004663">http://purl.obolibrary.org/obo/UBERON_6004663</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="https://www.morphbank.net/?id=861240">https://www.morphbank.net/?id=861240</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>foreleg</td>
		</tr>
		<tr>
			<td>Has broader concept</td>
			<td><a href="#acpart_p0016">acpart:p0016</a></td>
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
			<th colspan="2"><a id="acpart_p0022"></a>Term Name acpart:p0022</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0022">http://rs.tdwg.org/acpart/values/p0022</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0022-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0022-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>midleg</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Leg of the mesothoracic segment</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/FBbt_00004685">http://purl.obolibrary.org/obo/FBbt_00004685</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="https://www.morphbank.net/?id=102967">https://www.morphbank.net/?id=102967</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>midleg</td>
		</tr>
		<tr>
			<td>Has broader concept</td>
			<td><a href="#acpart_p0016">acpart:p0016</a></td>
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
			<th colspan="2"><a id="acpart_p0023"></a>Term Name acpart:p0023</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0023">http://rs.tdwg.org/acpart/values/p0023</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0023-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0023-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>hindleg</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Leg of the metathoracic segment</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/FBbt_00004707">http://purl.obolibrary.org/obo/FBbt_00004707</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="https://www.morphbank.net/?id=468627">https://www.morphbank.net/?id=468627</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>hindleg</td>
		</tr>
		<tr>
			<td>Has broader concept</td>
			<td><a href="#acpart_p0016">acpart:p0016</a></td>
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
			<th colspan="2"><a id="acpart_p0024"></a>Term Name acpart:p0024</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0024">http://rs.tdwg.org/acpart/values/p0024</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0024-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0024-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>eye</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An organ that detects light</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/UBERON_0000970">http://purl.obolibrary.org/obo/UBERON_0000970</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="https://commons.wikimedia.org/wiki/File:Compound_eye_of_a_Bumblebee.jpg">https://commons.wikimedia.org/wiki/File:Compound_eye_of_a_Bumblebee.jpg</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>eye</td>
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
			<th colspan="2"><a id="acpart_p0025"></a>Term Name acpart:p0025</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0025">http://rs.tdwg.org/acpart/values/p0025</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0025-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0025-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>shell</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A rigid covering that envelops an object</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/UBERON_0006612">http://purl.obolibrary.org/obo/UBERON_0006612</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="https://www.inaturalist.org/photos/251026905">https://www.inaturalist.org/photos/251026905</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>shell</td>
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
			<th colspan="2"><a id="acpart_p0026"></a>Term Name acpart:p0026</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0026">http://rs.tdwg.org/acpart/values/p0026</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0026-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0026-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>genitalia</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The outer sex organs</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/UBERON_0004176">http://purl.obolibrary.org/obo/UBERON_0004176</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="https://commons.wikimedia.org/wiki/File:Dragonfly,_U,_genitalia_top_2013-01-11-14.10.09_ZS_PMax_(8372440610).jpg">https://commons.wikimedia.org/wiki/File:Dragonfly,_U,_genitalia_top_2013-01-11-14.10.09_ZS_PMax_(8372440610).jpg</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>genitalia</td>
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
			<th colspan="2"><a id="acpart_p0027"></a>Term Name acpart:p0027</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0027">http://rs.tdwg.org/acpart/values/p0027</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0027-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0027-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>skull</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The part of the head consisting entirely of cranium and mandible</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/UBERON_0003129">http://purl.obolibrary.org/obo/UBERON_0003129</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="https://www.inaturalist.org/photos/251216754">https://www.inaturalist.org/photos/251216754</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>skull</td>
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
			<th colspan="2"><a id="acpart_p0028"></a>Term Name acpart:p0028</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0028">http://rs.tdwg.org/acpart/values/p0028</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0028-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0028-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>cranium</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Upper portion of the skull</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/UBERON_0003128">http://purl.obolibrary.org/obo/UBERON_0003128</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="http://arctos.database.museum/media/10508734">http://arctos.database.museum/media/10508734</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>cranium</td>
		</tr>
		<tr>
			<td>Has broader concept</td>
			<td><a href="#acpart_p0027">acpart:p0027</a></td>
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
			<th colspan="2"><a id="acpart_p0029"></a>Term Name acpart:p0029</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0029">http://rs.tdwg.org/acpart/values/p0029</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0029-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0029-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>mandible</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A dentary bone that is the only bone in one of the lateral halves of the lower jaw</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/UBERON_0001684">http://purl.obolibrary.org/obo/UBERON_0001684</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="http://arctos.database.museum/media/10473443">http://arctos.database.museum/media/10473443</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>mandible</td>
		</tr>
		<tr>
			<td>Has broader concept</td>
			<td><a href="#acpart_p0027">acpart:p0027</a></td>
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
			<th colspan="2"><a id="acpart_p0030"></a>Term Name acpart:p0030</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0030">http://rs.tdwg.org/acpart/values/p0030</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0030-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0030-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>fin</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An external projection of an aquatic animal used in propelling or guiding the body</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/UBERON_0008897">http://purl.obolibrary.org/obo/UBERON_0008897</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="https://www.inaturalist.org/photos/249623779">https://www.inaturalist.org/photos/249623779</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>fin</td>
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
			<th colspan="2"><a id="acpart_p0031"></a>Term Name acpart:p0031</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0031">http://rs.tdwg.org/acpart/values/p0031</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0031-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0031-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>egg</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The hard-shelled reproductive body produced by an animal</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/UBERON_0007379">http://purl.obolibrary.org/obo/UBERON_0007379</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="http://arctos.database.museum/media/10517057">http://arctos.database.museum/media/10517057</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>egg</td>
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
			<th colspan="2"><a id="acpart_p0032"></a>Term Name acpart:p0032</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/p0032">http://rs.tdwg.org/acpart/values/p0032</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-04-26</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acpart/values/version/p0032-2023-04-26">http://rs.tdwg.org/acpart/values/version/p0032-2023-04-26</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>bud</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An undeveloped shoot system</td>
		</tr>
		<tr>
			<td>Definition derived from</td>
			<td><a href="http://purl.obolibrary.org/obo/PO_0000055">http://purl.obolibrary.org/obo/PO_0000055</a></td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><a href="http://bioimages.vanderbilt.edu/baskauf/16256">http://bioimages.vanderbilt.edu/baskauf/16256</a></td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>bud</td>
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


