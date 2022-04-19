# subjectPart Controlled Vocabulary

**Title:** subjectPart Controlled Vocabulary

**Namespace URI:** http://rs.tdwg.org/acpart/values/

**Preferred namespace abbreviation:** acpart:

**Date version issued:** put ratification date here

**Date created:** put ratification date here

**Part of TDWG Standard:** http://www.tdwg.org/standards/638

**This version:** http://rs.tdwg.org/ac/doc/part/iso-date-here

**Latest version:** http://rs.tdwg.org/ac/doc/part/

**Abstract:** The Audubon Core term `subjectPart` describes the part of an organism morphology, behaviour, environment depicted in a media item or region of interest. The subjectPart Controlled Vocabulary provides terms that should be used as values for `ac:subjectPart` and its literal-valued analog `ac:subjectPartLiteral`. 

**Contributors:** Steven J. Baskauf (Vanderbilt University Libraries), Neil S. Cobb (Merriam-Powell Center for Environmental Research, Northern Arizona University), Jennifer C. Girón Duque (Natural Science Research Laboratory, Museum of Texas Tech University), Matthew Nielsen (Stockholm University), Mervin E. Pérez (University of Puerto Rico), Randy Singer (University of Michigan)

**Creator:** TDWG Views Controlled Vocabularies Task Group

**Bibliographic citation:** Views Controlled Vocabularies Task Group. 2022. subjectPart Controlled Vocabulary. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/ac/doc/part/>


## 1 Introduction (informative)

This document includes terms intended to be used as controlled values for the Audubon Core terms `ac:subjectPart` and `ac:subjectPartLiteral`. A [JSON-LD representation](https://tdwg.github.io/rs.tdwg.org/cvJson/acpart.json) of this SKOS Concept Scheme is available.

### 1.1 Status of the content of this document

Section 1 is informative (non-normative).

Section 2 is normative except as noted.

Section 3 is informative.

In Section 4, the values of the `Term IRI`, `Definition`, and `Controlled value` are normative. The value of `Usage` (if it exists for a given term) is normative.  The value of `Has broader concept` is normative. The values of `Term Name` are non-normative, although one can expect that the namespace abbreviation prefix is one commonly used for the term namespace.  `Label` and the values of all other properties (such as `Notes`) are non-normative.

### 1.2 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

## 2 Use of Terms

### 2.1 Relationship of value types to property terms

In accordance with the [Audubon Core Term List](http://rs.tdwg.org/ac/doc/termlist/) document, unabbreviated term IRIs MUST be used as values of the property `ac:subjectPart`. Controlled value strings SHOULD be used as values of the property `ac:subjectPartLiteral`.

### 2.2 Relationships with other concept schemes and collections (informative)

Particular `ac:subjectOrientation` values are appropriate for some `ac:subjectPart` values. The relationships between concepts in these two schemes are described by a [JSON-LD serialized SKOS Collection for each subject part](https://tdwg.github.io/rs.tdwg.org/cvJson/acorient_collection.json) that designates which subject orientations are appropriate for that part. Similarly, [JSON-LD serialized SKOS Collections have been established for some organism groups](https://tdwg.github.io/rs.tdwg.org/cvJson/acpart_collection.json) to indicate which subject parts exist for members of those groups. These collections are provided to aid application developers in filtering the concepts that should be presented to users and they may also be used for validation.

Neither of these Collections are normative and they are maintained outside of the Audubon Core standards framework in order to make their development agile.

## 3 Term index
