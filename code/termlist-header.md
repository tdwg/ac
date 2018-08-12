---
layout: page
title: Audubon Core Term List
permalink: /terms
---

For introductory material, see the **[Audubon
Core Introduction](introduction.md)** and **[Audubon Core
Structure](structure.md)** documents.

**Title:** Audubon Core Term List

**Date version issued:** 2013-10-23

**Date created:** 2013-10-23

**Part of TDWG Standard:** http://www.tdwg.org/standards/638/

**This version:** http://rs.tdwg.org/ac/doc/termlist/2013-10-23

**Latest version:** http://rs.tdwg.org/ac/doc/termlist/

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
meeting in October 2013. This is a normative document and the definition
may not be changed without due process.

**Contributors:** Robert A. Morris, Vijay Barve, Mihail Carausu, Vishwas
Chavan, José Cuadra, Chris Freeland, Gregor Hagedorn, Patrick Leary,
Dimitry Mozzherin, Annette Olson, Greg Riccardi, Ivan Teage

**Creator:** GBIF/TDWG Multimedia Resources Task Group

**Bibliographic citation:** Multimedia Resources Task Group. 2013. Audubon Core Term List. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/ac/doc/termlist/


## 1 Introduction

There are four documents included in the Aububon Core Standard.  This document provides details about the terms included in Audubon Core vocabulary. The [Audubon Core Introduction](introduction.md) document provides a brief introduction to the Audubon Core Standard. For information about the structure of Audubon Core, see the [Audubon Core Structure](structure.md) document.  For a more detailed guide to the use of Audubon Core, see the [Audubon Core Guide](guide.md) document.


### 1.1 Status of the content of this document

Sections 1.2 through 5 are normative.  In Section 7 and its subparts, the values of the Normative URI, Definition, Layer, Required, and Repeatable are normative. The values of Term Name is non-normative, although one can expect that the namespace abbreviation prefix is one commonly used for the term namespace.  Labels and the values of all other properties (such as notes) are non-normative.


### 1.2 Categories of terms

An Audubon Core (AC) record is a description of a multimedia resource
using the AC vocabularies. Two kinds of terms are specified by this
document: those terms which describe representation-independent aspects
of the media and those which describe representation-dependent aspects.
Most terms are representation-independent, referring to an "abstract
multimedia resource". One such term, *hasServiceAccessPoint*, refers to
or contains representation-dependent service access point metadata
describing a digital representation of the abstract multimedia resource.
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
Common such usage for abbreviations and namespace prefixes are Darwin
Core (DwC, dwc:), the Dublin Core Metadata Initiative(DC, comprising two
namespaces, with prefixes dc: and dcterms:), Adobe XMP (XMP, xmp:),
International Press and Telecommunications Council (IPTC, Iptc4xmpExt:),
the Exchangeable Image File Format (EXIF, exif:) and the TDWG Ontologies
Natural History Collection class (NCD, ncd:). Hypertext links in the
term table entries will bring the reader to appropriate documentation of
those organizations.


## 3 Namespaces, Prefixes and Term Names

The namespace of terms borrowed from other vocabularies is that of the
original. The namespace of de novo AC terms is
http://rs.tdwg.org/ac/terms/. In the table of terms, each term entry has
a row with the term name. This term name is generally an "unqualified
name" preceded by a widely accepted prefix designating an abbreviation
for the namespace It is recommended that implementers who need a
namespace prefix for the AC namespace use "ac". In this web document,
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
normative material on [Multiplicity and Cardinality](structure.md#3-multiplicity-and-cardinality).


## 4 Layers

The term set consists of two *Layers*, numbered *1* and *2*. The former
comprise the central terms, likely to be meaningful for most media, even
though only a few are mandatory. Implementers of AC representations
should provide for at least Layer 1 if possible, and application writers
should provide for robust treatment of Layer 1 terms, if only by
ignoring them. Layer 2 terms are more likely to be useful for particular
kinds of media or for applications requiring highly detailed resource
descriptions. Each term description below indicates the Layer to which
the term belongs.


## 5 Literal- vs. URI-valued Terms

Some terms have two versions, one expecting a string literal value and
the other a URI. In these circumstances, the version expecting a string
is named with the suffix "Literal", e.g. ac:metadataLanguageLiteral. In
such cases, both forms may be provided, but care should be taken to
ensure that the uses reflect the same intent. In case of ambiguity, the
URI version prevails. All terms, including those whether or not with a
specific "Literal" suffix, specify in their definition whether the
required values are strings or URIs.



## 6 Vocabulary Indices
