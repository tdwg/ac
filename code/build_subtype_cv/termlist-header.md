---
permalink: /subtype/
---

# Controlled Vocabulary for Audubon Core subtype: List of Terms

**Title:** Controlled Vocabulary for Audubon Core subtype: List of Terms

**Namespace URI:** http://rs.tdwg.org/acsubtype/values/

**Preferred namespace abbreviation:** acsubtype:

**Date version issued:** 2020-10-13

**Date created:** 2020-10-13

**Part of TDWG Standard:** http://www.tdwg.org/standards/638

**This version:** http://rs.tdwg.org/ac/doc/subtype/2020-10-13

**Latest version:** http://rs.tdwg.org/ac/doc/subtype/

**Abstract:** Audubon Core uses the terms `ac:subtype` and `ac:subtypeLiteral` to refine the type of a media item to a level more specific than the Dublin Core Type Vocabulary, `http://purl.org/dc/dcmitype/`. This controlled vocabulary provides values for `ac:subtype` and `ac:subtypeLiteral`. 

**Contributors:** Steven J Baskauf (Vanderbilt University Heard Libraries)

**Creator:** TDWG Audubon Core Maintenance Group

**Bibliographic citation:** Audubon Core Maintenance Group. 2020. Controlled Vocabulary for Audubon Core subtype: List of Terms. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/ac/doc/subtype/2020-10-13>


## 1 Introduction (informative)

This document includes terms intended to be used as a controlled value for Audubon Core terms `ac:subtype` and `ac:subtypeLiteral`. **Note:** Although this is a controlled vocabulary, the type of its terms is `rdfs:Class` rather than `skos:Concept` as in other controlled vocabularies because it indicates the type of the media item.

### 1.1 Status of the content of this document

Section 1 is informative (non-normative).

Section 2 is normative.

Section 3 is informative (non-normative).

In Section 4, the values of the `Term IRI`, `Definition`, and `Controlled value` are normative. The value of `Usage` (if it exists for a given term) is normative. The values of `Term Name` are non-normative, although one can expect that the namespace abbreviation prefix is one commonly used for the term namespace.  `Label` and the values of all other properties are non-normative.

### 1.2 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

## 2 Use of Terms

### 2.1 Relationship of value types to property terms

In accordance with [the Audubon Core Term List document](http://rs.tdwg.org/ac/doc/termlist/), unabbreviated term IRIs SHOULD be used as values of the property `ac:subtype`. Controlled value strings SHOULD be used as values of the property `ac:subtypeLiteral`.

### 2.2 Relationship between values of ac:subtypeLiteral and ac:subtype

An IRI for a term in this vocabulary denotes the same class as the class denoted by the controlled value string for the same term. Thus a client MAY infer an IRI value for `ac:subtype` given a controlled value string for `ac:subtypeLiteral` even if that IRI is not explicitly stated. The practical implication is that data aggregators MAY materialize values for the preferred `ac:subtype` property in cases where providers only provide values for `ac:subtypeLiteral`. 

## 3 Term index
