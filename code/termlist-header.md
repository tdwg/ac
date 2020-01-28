---
permalink: /termlist/
---

# Audubon Core Term List

**Title:** Audubon Core Term List

**Date version issued:** 2020-01-27

**Date created:** 2013-10-23

**Part of TDWG Standard:** http://www.tdwg.org/standards/638

**This version:** http://rs.tdwg.org/ac/doc/termlist/2020-01-27

**Latest version:** http://rs.tdwg.org/ac/doc/termlist/

**Previous version:** [http://rs.tdwg.org/ac/doc/termlist/2013-10-23](2013-10-23)

**Abstract:** The Audubon Core is a set of vocabularies designed to
represent metadata for biodiversity multimedia resources and
collections. It aims to represent information that will help to
determine whether a particular resource or collection will be fit for
some particular biodiversity science application before acquiring the
media. Among others, the vocabularies address such concerns as the
management of the media and collections, descriptions of their content,
their taxonomic, geographic, and temporal coverage, and the appropriate
ways to retrieve, attribute and reproduce them. This document contains a
list of attributes of each Audubon Core term, including a documentation
name, a specified URI, a recommended English label for user interfaces,
a definition, and some ancillary notes. The version shown here has been
adopted by Biodiversity Information Standards / TDWG at the general
meeting in October 2013. This document contains normative content that
may not be changed without due process.

**Contributors:** Robert A. Morris, Vijay Barve, Mihail Carausu, Vishwas
Chavan, José Cuadra, Chris Freeland, Gregor Hagedorn, Patrick Leary,
Dimitry Mozzherin, Annette Olson, Greg Riccardi, Ivan Teage, Steve Baskauf

**Creator:** GBIF/TDWG Multimedia Resources Task Group

**Bibliographic citation:** Multimedia Resources Task Group. 2020. Audubon Core Term List. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/ac/doc/termlist/


## 1 Introduction

There are four documents included in the Aububon Core Standard.  This document provides details about the terms included in Audubon Core vocabulary. The [Audubon Core Introduction](introduction.md) document provides a brief introduction to the Audubon Core Standard. For information about the structure of Audubon Core, see the [Audubon Core Structure](structure.md) document.  For a more detailed guide to the use of Audubon Core, see the [Audubon Core Guide](guide.md) document.


### 1.1 Status of the content of this document

Sections 1.3 through 5 are normative, except for Table 1.  In Section 7 and its subparts, the values of the Normative URI, Definition, Layer, Required, and Repeatable are normative. The value of Usage (if it exists for a given term) is normative in that it specifies how a borrowed term should be used as part of Audubon Core.  The values of Term Name is non-normative, although one can expect that the namespace abbreviation prefix is one commonly used for the term namespace.  Labels and the values of all other properties (such as notes) are non-normative.

### 1.2 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119. [RFC-2119](https://tools.ietf.org/html/rfc2119)

### 1.3 Categories of terms

An Audubon Core (AC) record is a description of a multimedia resource
using the AC vocabularies. Two kinds of terms are specified by this
document: those terms which describe representation-independent aspects
of the media and those which describe representation-dependent aspects.
Most terms are representation-independent, referring to an "abstract
multimedia resource". One such term, `ac:hasServiceAccessPoint`, refers to
or contains representation-dependent service access point metadata
describing a digital representation of the abstract multimedia resource (an instance of the `ac:ServiceAccessPoint` class).
These metadata describe such things as a web address at which a digital
representation can be retrieved, and the format, extent, or licenses
that describe a particular such representation. A multimedia resource
may provide several access points for different representations (e.g.,
different resolutions).


## 2 Borrowed Vocabulary

When terms are borrowed from other vocabularies, AC uses the URIs,
common abbreviations, and namespace prefixes in use in those
vocabularies. The URIs are normative, but abbreviations and namespace
prefixes have no impact except as an aid to reading the documentation.

Table 1. Vocabularies from which terms have been borrowed (non-normative)

Note: URIs for terms in most of these namespaces do not dereference to anything.  The authoritative documentation can be obtained by clicking on the vocabulary names in the table.

| Vocabulary | Abbreviation | Namespaces and abbreviations |
|------------|--------------|------------------------------|
| [Darwin Core](http://tdwg.github.io/dwc/terms/index.htm) | DwC         | dwc: = http://rs.tdwg.org/dwc/terms/
| [Dublin Core](http://dublincore.org/documents/dcmi-terms/) | DC          | dc: = http://purl.org/dc/elements/1.1/, dcterms: = http://purl.org/dc/terms/ |
| [Adobe XMP Core Properties](https://wwwimages2.adobe.com/content/dam/acom/en/devnet/xmp/pdfs/XMP%20SDK%20Release%20cc-2016-08/XMPSpecificationPart1.pdf) | XMP | xmp: = http://ns.adobe.com/xap/1.0/, xmpRights: = http://ns.adobe.com/xap/1.0/rights/ |
| [Adobe XMP Additional Properties](http://wwwimages.adobe.com/www.adobe.com/content/dam/acom/en/devnet/xmp/pdfs/XMP%20SDK%20Release%20cc-2014-12/XMPSpecificationPart2.pdf) | XMP | photoshop: = http://ns.adobe.com/photoshop/1.0/ |
| [International Press and Telecommunications Council Photo Metadata Standard,Extension Schema 1.1](http://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-201007_1.pdf) | IPTC | Iptc4xmpExt: = http://iptc.org/std/Iptc4xmpExt/2008-02-29/ |
| [Camera and Imaging Products Association Exchangeable Image File Format](http://www.cipa.jp/std/documents/e/DC-008-2012_E.pdf) | EXIF | exif: = http://ns.adobe.com/exif/1.0/ |
| [TDWG Natural Collection Description LSID Ontology](https://github.com/tdwg/ontology/blob/master/ontology/voc/Collection.rdf) (referenced in metadata, but no terms borrowed) | NCD | ncd: = http://rs.tdwg.org/ontology/voc/Collection# |


## 3 Namespaces, Prefixes and Term Names

The namespace of terms borrowed from other vocabularies is that of the
original. The namespace of de novo AC terms is
`http://rs.tdwg.org/ac/terms/`. In the table of terms, each term entry has
a row with the term name. This term name is generally an "unqualified
name" preceded by a widely accepted prefix designating an abbreviation
for the namespace It is RECOMMENDED that implementers who need a
namespace prefix for the AC namespace use `ac`. In this web document,
hovering over a term in the [Index By Term Name](#index-by-term-name)
list below will reveal a complete URL that can be used in other web
documents to link to *this* document's treatment of that term, even if
it is from a borrowed vocabulary. It is very important to note that some
vocabularies, e.g those of the
[Dublin Core Metadata Initiative (DCMI)](http://dublincore.org/),
provide versions of the same term in two different namespaces, one
providing for string values and one providing for URIs, even where that
separation is simply a recommendation, not a mandate. See this
[DCMI wiki entry](http://wiki.dublincore.org/index.php/FAQ/DC_and_DCTERMS_Namespaces)
on this topic. For vocabularies where such a practice is in place, we
often follow it and signal a reference in the Notes of our term
descriptions to the sister version of the term. An example is the pair
[dc:type](#dc_type) and [dcterms:type](#dcterms_type). When such a pair allows repeated instances (e.g. as for [dc:source](#dc_source) and [dcterms:source](#dcterms_source)), particular care may be required in some
implementations of AC, because
some implementations may not provide enough structure to clearly state
the association between the members of a pair in the case of multiple
values of each. This is a special case of the issue treated in the
normative material on [Multiplicity and Cardinality](structure.md#3-multiplicity-and-cardinality) in the Audubon Core Structure document.


## 4 Layers

(The Audubon Core layer property has been deprecated as of 2020-01-27)


## 5 Literal- vs. URI-valued Terms

Some terms have two versions, one expecting a string literal value and
the other a URI. In these circumstances, the version expecting a string
is named with the suffix "Literal", e.g. `ac:metadataLanguageLiteral`. In
such cases, both forms MAY be provided, but care should be taken to
ensure that the uses reflect the same intent. In case of ambiguity, the
URI version prevails. All terms, including those whether or not with a
specific "Literal" suffix, specify in their definition whether the
required values are strings or URIs.



## 6 Vocabulary Indices (non-normative)
