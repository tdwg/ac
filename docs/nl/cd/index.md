# Controlled Vocabulary for Audiovisual Core Content Description: List of Terms

Title
: Controlled Vocabulary for Audiovisual Core Content Description: List of Terms

Namespace IRI
: <http://rs.tdwg.org/accd/values/>

Preferred namespace abbreviation
: accd:

Date version issued
: 2026-01-23

Date created
: 2026-01-23

Part of TDWG Standard
: <http://www.tdwg.org/standards/638>

This version
: <http://rs.tdwg.org/ac/doc/cd/2026-01-23>

Latest version
: <http://rs.tdwg.org/ac/doc/cd/>

Abstract
: Audiovisual Core uses the terms Iptc4xmpExt:CVterm and ac:CVtermLiteral to provide information about the content of all or part of a media item. This controlled vocabulary provides values for those terms.

Contributors
: [Steven J Baskauf](https://orcid.org/0000-0003-4365-3135) ([Vanderbilt University Heard Libraries](http://www.wikidata.org/entity/Q16849893)), [Edward Baker](https://orcid.org/0000-0002-5887-9543) ([Natural History Museum, London](http://www.wikidata.org/entity/Q309388)), [Dan Stowell](https://orcid.org/0000-0001-8068-3769) ([Queen Mary University of London](http://www.wikidata.org/entity/Q195668)), [Niels Klazenga](https://orcid.org/0000-0003-2224-6821) ([Royal Botanic Gardens Victoria](http://www.wikidata.org/entity/Q7373836))

Creator
: TDWG Audiovisual Core Maintenance Group

Bibliographic citation
: TDWG Audiovisual Core Maintenance Group. 2026. Controlled Vocabulary for Audiovisual Core Content Description: List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/ac/doc/cd/2026-01-23>

## 1 Introduction (informative)

This document includes terms intended to be used as controlled values for Audiovisual Core terms `Iptc4xmpExt:CVterm` and `ac:CVtermLiteral`.

### 1.1 Status of the content of this document

Section 1 is informative (non-normative).

Section 2 is normative.

Section 3 is informative (non-normative).

In Section 4, the values of the `Term IRI`, `Definition`, and `Controlled value` are normative. The value of `Usage` (if it exists for a given term) is normative. The values of `Term Name` are non-normative, although one can expect that the namespace abbreviation prefix is one commonly used for the term namespace.  `Label` and the values of all other properties are non-normative.

### 1.2 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) and [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) when, and only when, they appear in all capitals, as shown here.

## 2 Use of Terms

### 2.1 Relationship of value types to property terms

In accordance with [the Audiovisual Core Term List document](http://rs.tdwg.org/ac/doc/termlist/), unabbreviated term IRIs SHOULD be used as values of the property `Iptc4xmpExt:CVterm`. Controlled value strings SHOULD be used as values of the property `ac:CVtermLiteral`.

### 2.2 Relationship between values of ac:CVtermLiteral and Iptc4xmpExt:CVterm

An IRI for a term in this vocabulary denotes the same concept as the concept denoted by the controlled value string for the same term. Thus a client MAY infer an IRI value for `Iptc4xmpExt:CVterm` given a controlled value string for `ac:CVtermLiteral` even if that IRI is not explicitly stated. The practical implication is that data aggregators MAY materialize values for the preferred `Iptc4xmpExt:CVterm` property in cases where providers only provide values for `ac:CVtermLiteral`. 

## 3 Term index



[Barcode](#accd_c07) |
[Color Bar](#accd_c04) |
[Content Description Controlled Vocabulary](#accd_c) |
[Context](#accd_c02) |
[Label](#accd_c01) |
[Organism Part](#accd_c06) |
[Packet](#accd_c08) |
[Scale Bar](#accd_c03) |
[Spoken Description](#accd_c05)

## 4 vocabulary
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="accd_c"></a>term_name accd:c</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>term_iri</td>
			<td><a href="http://rs.tdwg.org/accd/values/c">http://rs.tdwg.org/accd/values/c</a></td>
		</tr>
		<tr>
			<td>modified</td>
			<td>2026-01-23</td>
		</tr>
		<tr>
			<td>term_version_iri</td>
			<td><a href="http://rs.tdwg.org/accd/values/version/c-2026-01-23">http://rs.tdwg.org/accd/values/version/c-2026-01-23</a></td>
		</tr>
		<tr>
			<td>label</td>
			<td>Content Description Controlled Vocabulary</td>
		</tr>
		<tr>
			<td>definition</td>
			<td>A SKOS ConceptScheme to be used as a controlled vocabulary for the Audiovisual Core terms ac:CVtermLiteral and Iptc4xmpExt:CVterm properties.</td>
		</tr>
		<tr>
			<td>usage</td>
			<td>Use the controlled value string as the value for ac:CVtermLiteral and use the term IRI as the value for Iptc4xmpExt:CVterm</td>
		</tr>
		<tr>
			<td>type</td>
			<td>http://www.w3.org/2004/02/skos/core#ConceptScheme</td>
		</tr>
		<tr>
			<td>executive_committee_decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-01-23_53">http://rs.tdwg.org/decisions/decision-2026-01-23_53</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="accd_c01"></a>term_name accd:c01</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>term_iri</td>
			<td><a href="http://rs.tdwg.org/accd/values/c01">http://rs.tdwg.org/accd/values/c01</a></td>
		</tr>
		<tr>
			<td>modified</td>
			<td>2026-01-23</td>
		</tr>
		<tr>
			<td>term_version_iri</td>
			<td><a href="http://rs.tdwg.org/accd/values/version/c01-2026-01-23">http://rs.tdwg.org/accd/values/version/c01-2026-01-23</a></td>
		</tr>
		<tr>
			<td>label</td>
			<td>Label</td>
		</tr>
		<tr>
			<td>definition</td>
			<td>Physical text providing metadata about the focal resource.</td>
		</tr>
		<tr>
			<td>notes</td>
			<td>The focal resource MAY be any kind of specimen.</td>
		</tr>
		<tr>
			<td>controlled_value</td>
			<td>label</td>
		</tr>
		<tr>
			<td>type</td>
			<td>concept</td>
		</tr>
		<tr>
			<td>executive_committee_decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-01-23_53">http://rs.tdwg.org/decisions/decision-2026-01-23_53</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="accd_c02"></a>term_name accd:c02</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>term_iri</td>
			<td><a href="http://rs.tdwg.org/accd/values/c02">http://rs.tdwg.org/accd/values/c02</a></td>
		</tr>
		<tr>
			<td>modified</td>
			<td>2026-01-23</td>
		</tr>
		<tr>
			<td>term_version_iri</td>
			<td><a href="http://rs.tdwg.org/accd/values/version/c02-2026-01-23">http://rs.tdwg.org/accd/values/version/c02-2026-01-23</a></td>
		</tr>
		<tr>
			<td>label</td>
			<td>Context</td>
		</tr>
		<tr>
			<td>definition</td>
			<td>A depicted feature that is the context in which the focal resource was located.</td>
		</tr>
		<tr>
			<td>usage</td>
			<td>If the media item includes a depiction of the focal resource, the focal resource SHOULD NOT be the main feature of the media item.</td>
		</tr>
		<tr>
			<td>examples</td>
			<td>the habitat in which an organism was found, the strata from which a fossil or mineral sample was removed</td>
		</tr>
		<tr>
			<td>controlled_value</td>
			<td>context</td>
		</tr>
		<tr>
			<td>type</td>
			<td>concept</td>
		</tr>
		<tr>
			<td>executive_committee_decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-01-23_53">http://rs.tdwg.org/decisions/decision-2026-01-23_53</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="accd_c03"></a>term_name accd:c03</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>term_iri</td>
			<td><a href="http://rs.tdwg.org/accd/values/c03">http://rs.tdwg.org/accd/values/c03</a></td>
		</tr>
		<tr>
			<td>modified</td>
			<td>2026-01-23</td>
		</tr>
		<tr>
			<td>term_version_iri</td>
			<td><a href="http://rs.tdwg.org/accd/values/version/c03-2026-01-23">http://rs.tdwg.org/accd/values/version/c03-2026-01-23</a></td>
		</tr>
		<tr>
			<td>label</td>
			<td>Scale Bar</td>
		</tr>
		<tr>
			<td>definition</td>
			<td>A linear graphic used to associate size with a dimension of the media item.</td>
		</tr>
		<tr>
			<td>examples</td>
			<td>a ruler</td>
		</tr>
		<tr>
			<td>controlled_value</td>
			<td>scaleBar</td>
		</tr>
		<tr>
			<td>type</td>
			<td>concept</td>
		</tr>
		<tr>
			<td>executive_committee_decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-01-23_53">http://rs.tdwg.org/decisions/decision-2026-01-23_53</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="accd_c04"></a>term_name accd:c04</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>term_iri</td>
			<td><a href="http://rs.tdwg.org/accd/values/c04">http://rs.tdwg.org/accd/values/c04</a></td>
		</tr>
		<tr>
			<td>modified</td>
			<td>2026-01-23</td>
		</tr>
		<tr>
			<td>term_version_iri</td>
			<td><a href="http://rs.tdwg.org/accd/values/version/c04-2026-01-23">http://rs.tdwg.org/accd/values/version/c04-2026-01-23</a></td>
		</tr>
		<tr>
			<td>label</td>
			<td>Color Bar</td>
		</tr>
		<tr>
			<td>definition</td>
			<td>Chromatic graphic used to calibrate the color profile of an image with the actual color of the object.</td>
		</tr>
		<tr>
			<td>controlled_value</td>
			<td>colorBar</td>
		</tr>
		<tr>
			<td>type</td>
			<td>concept</td>
		</tr>
		<tr>
			<td>executive_committee_decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-01-23_53">http://rs.tdwg.org/decisions/decision-2026-01-23_53</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="accd_c05"></a>term_name accd:c05</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>term_iri</td>
			<td><a href="http://rs.tdwg.org/accd/values/c05">http://rs.tdwg.org/accd/values/c05</a></td>
		</tr>
		<tr>
			<td>modified</td>
			<td>2026-01-23</td>
		</tr>
		<tr>
			<td>term_version_iri</td>
			<td><a href="http://rs.tdwg.org/accd/values/version/c05-2026-01-23">http://rs.tdwg.org/accd/values/version/c05-2026-01-23</a></td>
		</tr>
		<tr>
			<td>label</td>
			<td>Spoken Description</td>
		</tr>
		<tr>
			<td>definition</td>
			<td>Audio media that contains a voice description of the content of the media item.</td>
		</tr>
		<tr>
			<td>controlled_value</td>
			<td>spokenDescription</td>
		</tr>
		<tr>
			<td>type</td>
			<td>concept</td>
		</tr>
		<tr>
			<td>executive_committee_decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-01-23_53">http://rs.tdwg.org/decisions/decision-2026-01-23_53</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="accd_c06"></a>term_name accd:c06</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>term_iri</td>
			<td><a href="http://rs.tdwg.org/accd/values/c06">http://rs.tdwg.org/accd/values/c06</a></td>
		</tr>
		<tr>
			<td>modified</td>
			<td>2026-01-23</td>
		</tr>
		<tr>
			<td>term_version_iri</td>
			<td><a href="http://rs.tdwg.org/accd/values/version/c06-2026-01-23">http://rs.tdwg.org/accd/values/version/c06-2026-01-23</a></td>
		</tr>
		<tr>
			<td>label</td>
			<td>Organism Part</td>
		</tr>
		<tr>
			<td>definition</td>
			<td>All or part of an organism.</td>
		</tr>
		<tr>
			<td>usage</td>
			<td>The media item primarily depicts some part of a organism. If the organism is not the main feature that is depicted, context SHOULD be used instead.  If this value is used, the terms ac:subjectPart/ac:subjectPartLiteral and ac:subjectOrientation/ac:subjectOrientationLiteral SHOULD be used to provide more detailed information about what precisely is depicted and how the depicted part is oriented.</td>
		</tr>
		<tr>
			<td>notes</td>
			<td>The organism MAY be living or dead, and MAY be preserved.</td>
		</tr>
		<tr>
			<td>controlled_value</td>
			<td>organismPart</td>
		</tr>
		<tr>
			<td>type</td>
			<td>concept</td>
		</tr>
		<tr>
			<td>executive_committee_decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-01-23_53">http://rs.tdwg.org/decisions/decision-2026-01-23_53</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="accd_c07"></a>term_name accd:c07</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>term_iri</td>
			<td><a href="http://rs.tdwg.org/accd/values/c07">http://rs.tdwg.org/accd/values/c07</a></td>
		</tr>
		<tr>
			<td>modified</td>
			<td>2026-01-23</td>
		</tr>
		<tr>
			<td>term_version_iri</td>
			<td><a href="http://rs.tdwg.org/accd/values/version/c07-2026-01-23">http://rs.tdwg.org/accd/values/version/c07-2026-01-23</a></td>
		</tr>
		<tr>
			<td>label</td>
			<td>Barcode</td>
		</tr>
		<tr>
			<td>definition</td>
			<td>A visual pattern that provides machine-readable metadata about a resource.</td>
		</tr>
		<tr>
			<td>examples</td>
			<td>QR code, linear bar codes</td>
		</tr>
		<tr>
			<td>controlled_value</td>
			<td>barcode</td>
		</tr>
		<tr>
			<td>type</td>
			<td>concept</td>
		</tr>
		<tr>
			<td>executive_committee_decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-01-23_53">http://rs.tdwg.org/decisions/decision-2026-01-23_53</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="accd_c08"></a>term_name accd:c08</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>term_iri</td>
			<td><a href="http://rs.tdwg.org/accd/values/c08">http://rs.tdwg.org/accd/values/c08</a></td>
		</tr>
		<tr>
			<td>modified</td>
			<td>2026-01-23</td>
		</tr>
		<tr>
			<td>term_version_iri</td>
			<td><a href="http://rs.tdwg.org/accd/values/version/c08-2026-01-23">http://rs.tdwg.org/accd/values/version/c08-2026-01-23</a></td>
		</tr>
		<tr>
			<td>label</td>
			<td>Packet</td>
		</tr>
		<tr>
			<td>definition</td>
			<td>A small container attached to specimen mounting material used to contain all or part of the specimen..</td>
		</tr>
		<tr>
			<td>notes</td>
			<td>The container MAY contain parts of the specimen that have been removed from the main specimen and might otherwise be lost. It MAY also contain the entire specimen.</td>
		</tr>
		<tr>
			<td>examples</td>
			<td>fragmentation packet, envelope</td>
		</tr>
		<tr>
			<td>controlled_value</td>
			<td>packet</td>
		</tr>
		<tr>
			<td>type</td>
			<td>concept</td>
		</tr>
		<tr>
			<td>executive_committee_decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2026-01-23_53">http://rs.tdwg.org/decisions/decision-2026-01-23_53</a></td>
		</tr>
	</tbody>
</table>


