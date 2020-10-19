---
permalink: /variant/
---

# Controlled Vocabulary for Audubon Core variant: List of Terms

**Title:** Controlled Vocabulary for Audubon Core variant: List of Terms

**Namespace URI:** http://rs.tdwg.org/acvariant/values/

**Preferred namespace abbreviation:** acvariant:

**Date version issued:** 2020-10-13

**Date created:** 2020-10-13

**Part of TDWG Standard:** http://www.tdwg.org/standards/638

**This version:** http://rs.tdwg.org/ac/doc/variant/2020-10-13

**Latest version:** http://rs.tdwg.org/ac/doc/variant/

**Abstract:** Audubon Core uses the terms `ac:variant` and `ac:variantLiteral` to provide information about the size, extent, and availability of the Service Access Point of a media item. This controlled vocabulary provides values for those terms. 

**Contributors:** Steven J Baskauf (Vanderbilt University Heard Libraries), Ed Baker (Natural History Museum, London), Dan Stowell (Queen Mary University of London / Alan Turing Institute)

**Creator:** TDWG Audubon Core Maintenance Group

**Bibliographic citation:** Audubon Core Maintenance Group. 2020. Controlled Vocabulary for Audubon Core variant: List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/ac/doc/variant/2020-10-13>


## 1 Introduction (informative)

This document includes terms intended to be used as a controlled value for Audubon Core terms `ac:variant` and `ac:variantLiteral`.

### 1.1 Status of the content of this document

Section 1 is informative (non-normative).

Section 2 is normative.

Section 3 is informative (non-normative).

In Section 4, the values of the `Term IRI`, `Definition`, and `Controlled value` are normative. The value of `Usage` (if it exists for a given term) is normative. The values of `Term Name` are non-normative, although one can expect that the namespace abbreviation prefix is one commonly used for the term namespace.  `Label` and the values of all other properties are non-normative.

### 1.2 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

## 2 Use of Terms

### 2.1 Relationship of value types to property terms

In accordance with [the Audubon Core Term List document](http://rs.tdwg.org/ac/doc/termlist/), unabbreviated term IRIs SHOULD be used as values of the property `ac:variant`. Controlled value strings SHOULD be used as values of the property `ac:variantLiteral`.

### 2.2 Relationship between values of ac:variantLiteral and ac:variant

An IRI for a term in this vocabulary denotes the same concept as the concept denoted by the controlled value string for the same term. Thus a client MAY infer an IRI value for `ac:variant` given a controlled value string for `ac:variantLiteral` even if that IRI is not explicitly stated. The practical implication is that data aggregators MAY materialize values for the preferred `ac:variant` property in cases where providers only provide values for `ac:variantLiteral`. 

## 3 Term index


[Best Quality](#acvariant_v006) |
[Good Quality](#acvariant_v005) |
[Lower Quality](#acvariant_v003) |
[Medium Quality](#acvariant_v004) |
[Offline](#acvariant_v007) |
[Thumbnail](#acvariant_v001) |
[Trailer](#acvariant_v002) |
[Visual](#acvariant_v008) |
[variant concept scheme](#acvariant_v) 

## 4 Vocabulary
<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acvariant_v"></a>Term Name  acvariant:v</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acvariant/values/v">http://rs.tdwg.org/acvariant/values/v</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-10-13</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acvariant/values/version/v-2020-10-13">http://rs.tdwg.org/acvariant/values/version/v-2020-10-13</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>variant concept scheme</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A SKOS Concept Scheme for controlled values for ac:variant</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>http://www.w3.org/2004/02/skos/core#ConceptScheme</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2020-10-13_30">http://rs.tdwg.org/decisions/decision-2020-10-13_30</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acvariant_v001"></a>Term Name  acvariant:v001</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acvariant/values/v001">http://rs.tdwg.org/acvariant/values/v001</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-10-13</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acvariant/values/version/v001-2020-10-13">http://rs.tdwg.org/acvariant/values/version/v001-2020-10-13</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Thumbnail</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Service Access Point provides a thumbnail image, short sound clip, or short movie clip that can be used in addition to the resource to represent the media object, typically at lower quality and higher compression than a preview object.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td> A typical size for a tiny thumbnail image may be 50-100 pixels in the longer dimension.</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Thumbnail</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2020-10-13_30">http://rs.tdwg.org/decisions/decision-2020-10-13_30</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acvariant_v002"></a>Term Name  acvariant:v002</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acvariant/values/v002">http://rs.tdwg.org/acvariant/values/v002</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-10-13</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acvariant/values/version/v002-2020-10-13">http://rs.tdwg.org/acvariant/values/version/v002-2020-10-13</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Trailer</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Service Access Point provides video clip preview, in the form of a specifically authored "Trailer", which may provide somewhat different content than the original resource.</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Trailer</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2020-10-13_30">http://rs.tdwg.org/decisions/decision-2020-10-13_30</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acvariant_v003"></a>Term Name  acvariant:v003</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acvariant/values/v003">http://rs.tdwg.org/acvariant/values/v003</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-10-13</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acvariant/values/version/v003-2020-10-13">http://rs.tdwg.org/acvariant/values/version/v003-2020-10-13</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Lower Quality</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Service Access Point provides a lower quality version of the media resource.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>an image suitable for web sites</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Lower Quality</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2020-10-13_30">http://rs.tdwg.org/decisions/decision-2020-10-13_30</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acvariant_v004"></a>Term Name  acvariant:v004</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acvariant/values/v004">http://rs.tdwg.org/acvariant/values/v004</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-10-13</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acvariant/values/version/v004-2020-10-13">http://rs.tdwg.org/acvariant/values/version/v004-2020-10-13</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Medium Quality</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Service Access Point provides a medium quality version of the media resource.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>shortened in duration, reduced size, using lower resolution or higher compression causing moderate artifacts</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Medium Quality</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2020-10-13_30">http://rs.tdwg.org/decisions/decision-2020-10-13_30</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acvariant_v005"></a>Term Name  acvariant:v005</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acvariant/values/v005">http://rs.tdwg.org/acvariant/values/v005</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-10-13</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acvariant/values/version/v005-2020-10-13">http://rs.tdwg.org/acvariant/values/version/v005-2020-10-13</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Good Quality</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Service Access Point provides a good quality version of the media resource intended for resources displayed as primary information.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>an image between 800 and 1600 pixels in width or height</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Good Quality</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2020-10-13_30">http://rs.tdwg.org/decisions/decision-2020-10-13_30</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acvariant_v006"></a>Term Name  acvariant:v006</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acvariant/values/v006">http://rs.tdwg.org/acvariant/values/v006</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-10-13</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acvariant/values/version/v006-2020-10-13">http://rs.tdwg.org/acvariant/values/version/v006-2020-10-13</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Best Quality</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Service Access Point provides the highest available quality of the media resource, whatever its resolution or quality level.</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Best Quality</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2020-10-13_30">http://rs.tdwg.org/decisions/decision-2020-10-13_30</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acvariant_v007"></a>Term Name  acvariant:v007</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acvariant/values/v007">http://rs.tdwg.org/acvariant/values/v007</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-10-13</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acvariant/values/version/v007-2020-10-13">http://rs.tdwg.org/acvariant/values/version/v007-2020-10-13</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Offline</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Service Access Point provides data about an offline resource.</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Offline</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2020-10-13_30">http://rs.tdwg.org/decisions/decision-2020-10-13_30</a></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="acvariant_v008"></a>Term Name  acvariant:v008</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Term IRI</td>
			<td><a href="http://rs.tdwg.org/acvariant/values/v008">http://rs.tdwg.org/acvariant/values/v008</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-10-13</td>
		</tr>
		<tr>
			<td>Term version IRI</td>
			<td><a href="http://rs.tdwg.org/acvariant/values/version/v008-2020-10-13">http://rs.tdwg.org/acvariant/values/version/v008-2020-10-13</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Visual</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Service Access Point provides a visual or graphic representation of a media resource that is not an image.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>a sonogram, an oscillogram</td>
		</tr>
		<tr>
			<td>Controlled value</td>
			<td>Visual</td>
		</tr>
		<tr>
			<td>Type</td>
			<td>Concept</td>
		</tr>
		<tr>
			<td>Executive Committee decision</td>
			<td><a href="http://rs.tdwg.org/decisions/decision-2020-10-13_30">http://rs.tdwg.org/decisions/decision-2020-10-13_30</a></td>
		</tr>
	</tbody>
</table>


