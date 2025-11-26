# {document_title}

Title
: {document_title}

Date de publication de la dernière mise à jour
: {ratification_date}

Date de création
: {created_date}

Fait partie du standard TDWG
: <{standard_iri}>

Cette version
: <{current_iri}{ratification_date}>

Dernière version
: <{current_iri}>

Version précédente
: {previous_version_slot}

Abstract
: {abstract}

Contributeurs
: {contributors}

Créateur :
{creator}

Citation :
{creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

## 1 Introduction

There are a number of documents included in the Audiovisual Core Standard.  This document provides details about the terms included in the {ratification_date} version of the Audiovisual Core vocabulary. The [Audiovisual Core Introduction](../introduction/) document provides a brief introduction to the Audiovisual Core Standard. For information about the structure of Audiovisual Core, see the [Audiovisual Core Structure](../structure/) document.  For a more detailed guide to the use of Audiovisual Core, see the [Audiovisual Core Guide](../guide/) document.

### 1.1 Statut du contenu de ce document

Sections 1.3 through 5 are normative, except for Table 1.  In Section 7 and its subparts, the values of the Normative URI, Definition, Required, and Repeatable are normative. The value of Usage (if it exists for a given term) is normative in that it specifies how a borrowed term should be used as part of Audiovisual Core.  The values of Term Name is non-normative, although one can expect that the namespace abbreviation prefix is one commonly used for the term namespace.  Labels and the values of all other properties (such as notes) are non-normative.

### 1.2 Mots clés RFC 2119

Les mots clés "MUST/DOIT", "MUST NOT/NE DOIT PAS", "REQUIRED/OBLIGATOIRE", "SHALL/DEVRA", "SHALL NOT/NE DEVRA PAS", "SHOULD/DEVRAIT", "SHOULD NOT/NE DEVRAIT PAS", "RECOMMENDED/RECOMMANDÉ", "MAY/POURRAIT", et "OPTIONAL/OPTIONNEL" dans ce document doivent être interprétés comme défini dans les références [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) et [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174)] uniquement lorsqu’ils apparaissent en majuscules, comme ci-dessus.

### 1.3 Categories of terms

An Audiovisual Core (AC) record is a description of a multimedia resource
using the AC vocabularies. Three kinds of terms are specified by this
document: those terms which describe representation-independent aspects
of the media, those which describe representation-dependent aspects, and those that designate specified parts of the media item.
Most terms are representation-independent, referring to an "abstract
multimedia resource". One such term, `ac:hasServiceAccessPoint`, refers to
or contains representation-dependent service access point metadata
describing a digital representation of the abstract multimedia resource (an instance of the `ac:ServiceAccessPoint` class).
These metadata describe such things as a web address at which a digital
representation can be retrieved, and the format, extent, or licenses
that describe a particular such representation. A multimedia resource
may provide several access points for different representations (e.g.,
different resolutions). The resource may also be linked to one or more Regions of Interest (ROI) that define parts within the media item (instances of the `ac:RegionOfInterest` class).

## 2 Borrowed Vocabulary

When terms are borrowed from other vocabularies, AC uses the URIs,
common abbreviations, and namespace prefixes in use in those
vocabularies. The URIs are normative, but abbreviations and namespace
prefixes have no impact except as an aid to reading the documentation.

Table 1. Vocabularies from which terms have been borrowed (non-normative)

Note: URIs for terms in most of these namespaces do not dereference to anything.  The authoritative documentation can be obtained by clicking on the vocabulary names in the table.

| Vocabulaire                                                                                                                                                                                            | Abbreviation | Namespaces and abbreviations                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ | --------------------------------------------------------------------------------------- |
| [Darwin Core](http://rs.tdwg.org/dwc/doc/list/)                                                                                                                                                        | DwC          | `dwc: = http://rs.tdwg.org/dwc/terms/`                                                  |
| [Dublin Core](http://dublincore.org/documents/dcmi-terms/)                                                                                                                                             | DC           | `dc: = http://purl.org/dc/elements/1.1/, dcterms: = http://purl.org/dc/terms/`          |
| [Adobe XMP Core Properties](https://github.com/adobe/XMP-Toolkit-SDK/blob/main/docs/XMPSpecificationPart1.pdf)                                                                                         | XMP          | `xmp: = http://ns.adobe.com/xap/1.0/, xmpRights: = http://ns.adobe.com/xap/1.0/rights/` |
| [Adobe XMP Additional Properties](https://github.com/adobe/XMP-Toolkit-SDK/blob/main/docs/XMPSpecificationPart2.pdf)                                                                                   | XMP          | `photoshop: = http://ns.adobe.com/photoshop/1.0/`                                       |
| [International Press and Telecommunications Council Photo Metadata Standard,Extension Schema 1.1](http://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-201007_1.pdf) | IPTC         | `Iptc4xmpExt: = http://iptc.org/std/Iptc4xmpExt/2008-02-29/`                            |
| [Camera and Imaging Products Association Exchangeable Image File Format](http://www.cipa.jp/std/documents/e/DC-008-2012_E.pdf)                                                                         | EXIF         | `exif: = http://ns.adobe.com/exif/1.0/`                                                 |
| [Music Ontology](http://musicontology.com/specification/)                                                                                                                                              | MO           | `mo: = http://purl.org/ontology/mo/`                                                    |
| [TDWG Natural Collection Description LSID Ontology](https://github.com/tdwg/ontology/blob/master/ontology/voc/Collection.rdf) (referenced in metadata, but no terms borrowed)       | NCD          | `ncd: = http://rs.tdwg.org/ontology/voc/Collection#`                                    |

## 3 Namespaces, Prefixes and Term Names

The namespace of terms borrowed from other vocabularies is that of the
original. The namespace of de novo AC terms is
`http://rs.tdwg.org/ac/terms/`. In the table of terms, each term entry has
a row with the term name. This term name is generally an "unqualified
name" preceded by a widely accepted prefix designating an abbreviation
for the namespace It is RECOMMENDED that implementers who need a
namespace prefix for the AC namespace use `ac`. In this web document,
hovering over a term in the [Index By Term Name](#61-index-by-term-name)
list below will reveal a complete URL that can be used in other web
documents to link to _this_ document's treatment of that term, even if
it is from a borrowed vocabulary. It is very important to note that some
vocabularies, e.g those of the
[Dublin Core Metadata Initiative (DCMI)](https://www.dublincore.org/),
provide versions of the same term in two different namespaces, one
providing for string values and one providing for URIs, even where that
separation is simply a recommendation, not a mandate. See this
[DCMI wiki entry](https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md)
on this topic. For vocabularies where such a practice is in place, we
often follow it and signal a reference in the Notes of our term
descriptions to the sister version of the term. An example is the pair
[dc:type](#dc_type) and [dcterms:type](#dcterms_type). When such a pair allows repeated instances (e.g. as for [dc:source](#dc_source) and [dcterms:source](#dcterms_source)), particular care may be required in some
implementations of AC, because
some implementations may not provide enough structure to clearly state
the association between the members of a pair in the case of multiple
values of each. This is a special case of the issue treated in the
normative material on [Multiplicity and Cardinality](../structure/#3-multiplicity-and-cardinality) in the Audiovisual Core Structure document.

## 4 Layers

(The Audiovisual Core layer property has been deprecated as of 2020-01-27)

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

