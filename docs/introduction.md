---
layout: page
title: Audubon Core Introduction
permalink: /index.html
---

**Title:** Audubon Core Introduction

**Date version issued:** 2013-10-23

**Date created:** 2013-10-23

**Part of TDWG Standard:** http://www.tdwg.org/standards/638/

**This version:** http://rs.tdwg.org/ac/doc/introduction/2013-10-23

**Latest version:** http://rs.tdwg.org/ac/doc/introduction/

**Abstract:** The **Audubon Core** is a set of vocabularies designed to represent
metadata for biodiversity multimedia resources and collections. These
vocabularies aim to represent information that will help to determine
whether a particular resource or collection will be fit for some
particular biodiversity science application before acquiring the media.
Among others, the vocabularies address such concerns as the management
of the media and collections, descriptions of their content, their
taxonomic, geographic, and temporal coverage, and the appropriate ways
to retrieve, attribute and reproduce them.

**Contributors:** Robert A. Morris, Vijay Barve, Mihail Carausu, Vishwas
Chavan, José Cuadra, Chris Freeland, Gregor Hagedorn, Patrick Leary,
Dimitry Mozzherin, Annette Olson, Greg Riccardi, Ivan Teage

**Creator:** GBIF/TDWG Multimedia Resources Task Group

**Bibliographic citation:** Multimedia Resources Task Group. 2013. Audubon Core Introduction. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/ac/doc/introduction/

## 1 Introduction

There are four documents included in the Aububon Core Standard.  This document
provides a general introduction to the Audubon Core Standard. For information
about the structure of Audubon Core, see the [Audubon Core Structure](./structure)
document.  For term details, see the [Audubon Core Terms List](./terms) document.  
For a more detailed guide to the use of Audubon Core, see the
[Audubon Core Guide](./guide) document.

### 1.1 Status of the content of this document

All sections of this document are non-normative.  

### 1.2 The scope of Audubon Core

The Audubon Core Multimedia Resources Metadata schema (“AC schema”, or
simply “AC”) is a set of metadata vocabularies for describing
biodiversity-related multimedia resources and collections. The
specification is independent of how these vocabularies may be
represented for machine use.

Multimedia Resources are digital or physical artifacts which normally
comprise more than text. These include pictures, artwork, drawings,
photographs, sound, video, animations, presentation materials, and
interactive online media including, e.g., identification tools. A
multimedia collection is an assemblage of such objects, whether curated
or not, and whether electronically accessible or not. For the purposes
of this document we regard a collection of multimedia resources itself
as a ‘multimedia resource’. Wherever discussion or specification can
apply only to a collection or only to a single media resource, we say so
explicitly.

Multimedia descriptions are digital records that document underlying
multimedia resources or collections. AC is focused on
biodiversity-related multimedia resources. It shares terminology and
concerns with many well-known and important standards for describing
access to resources such as Dublin Core (DC), Darwin Core (DwC), the
Adobe Extensible Metadata Platform (XMP), the International Press and
Telecommunications Council (IPTC), the Metadata Working Group (MWG)
schema, the Natural Collections Schema (NCD), and others. Where there is
an exact match to the usage of such standards, AC adopts their
identifiers and definitions. Many collections of biodiversity multimedia
already have descriptions of their media expressed in DwC or DC. By
using those vocabularies where suitable, AC particularly intends to make
it easy for such collections to reuse their existing descriptions,
augmented where necessary by other
terms

**See also:** [Discovery and Publishing of Primary Biodiversity Data
associated with Multimedia Resources: The Audubon Core Strategies and
Approaches.](https://journals.ku.edu/index.php/jbi/article/view/4117) R.
Morris et al., *Biodiversity Informatics,* 8, jul. 2013.

## 2 Audubon Core terms

An Audubon Core record is a description of a multimedia resource using
the [Audubon Core terms](./terms). Two kinds
of terms are specified by AC: record-level terms and access-level terms.
Record-level terms apply to the media resource being described. Almost
all terms are record-level terms. One such term, *hasServiceAccessPoint*
plays a special role in helping to retrieve the resource that the record
describes. A multimedia resource may have more than one
hasServiceAccessPoint, each of which provides values of one or more
access-level terms. The access-level terms document such things as a web
address at which a digital representation of the resource can be
retrieved, the size of such a retrieved object, etc. An Audubon Core
record is thus a description using a set of terms that conforms to the
normative documents, and contains at least the four mandatory terms,
which provide an identifier, a resource type, the language of the
description, and copyright information. Every such record describes a
single multimedia resource (possibly including a Collection). The
identifier may have been assigned to the resource by an external
authority or by the provider of the record. Strictly speaking, the
identifier is required only for Collections, but is strongly recommended
in general.

Every Audubon Core term has a plain text Name, a term identifier and a
plain text normative Definition. Term identifiers conform to the
[Universal Resource Identifier (URI)
specification](http://tools.ietf.org/html/rfc2616#section-3.2).
Typically these identifiers have a form familiar to browser users as the
addresses of web pages, beginning with "http://". Informally, one may
understand this thusly: an http URI has the syntax of a web address, but
there is no expectation that putting it in a web browser will result in
any information being returned to the browser, and if it does, the
return may have no relevance.

Because http URIs are rather lengthy, AC documents follow a standard
practice of introducing a short prefix comprising a "namespace
qualifier" separated by a colon from a mnemonic name closely related to
the term's Name. The namespace of the roughly 50% of the terms that are
borrowed from other vocabularies is the namespace of the original. The
namespace of de novo AC terms is http://rs.tdwg.org/ac/terms/. In the [Audubon Core Term List](./terms), each
term entry has a row with the term name. Following the practice of the
[Darwin Core terms](http://rs.tdwg.org/dwc/terms/), this term name
is generally an "unqualified name" preceded by a widely accepted prefix
designating an abbreviation for the namespace. The result is known as a
qualified name. For example the normative wiki documentation for the
borrowed term dcterms:identifier has URI
http://purl.org/dc/terms/identifier. The first part,
"http://purl.org/dc/terms/" corresponds to the namespace. Most of the
URIs for terms borrowed from external vocabularies do in fact produce
relevant documentation for that external standard when used as a web
page URL. Sometimes it is not precise because the documentation is a PDF
document and several (different!) URIs might apparently lead
to the same place.

## 3 Implementations

The [AC Term List](./terms) and
[Audubon Core Structure](./structure)
documents represent a *data model.* For actual use of Audubon Core, it
is necessary to select an implementation, preferably one with some
status designated by [TDWG](http://www.tdwg.org/). Known
implementations will be listed in ancillary documents not included as part of the Audubon Core standard.

## 4 References

   |   |   
---|---|---
[\[ACISS\]](https://github.com/tdwg/ac/issues) | https://github.com/tdwg/ac/issues | AC issue tracker
[\[CHANGE\]](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md#3-change-process) | http://rs.tdwg.org/vms/doc/specification/#3-change-process | TDWG vocabulary change policy |
[\[DCMIU\]](http://wiki.dublincore.org/index.php/User_Guide) | http://wiki.dublincore.org/index.php/User_Guide | Dublin Core User Guide                         |
[\[GUIDE\]](./guide) | http://rs.tdwg.org/ac/doc/guide/ | AC User Guide
[\[STRCT\]](./structure) | http://rs.tdwg.org/ac/doc/structure/ | Introduction to AC structure
[\[TERMS\]](./terms) | http://rs.tdwg.org/ac/doc/termlist/ | AC Term List                            |
