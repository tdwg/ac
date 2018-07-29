<a id="top"></a>

# Audubon Core Structure

**Title:** Audubon Core Structure

**Date version issued:** 2013-10-23

**Date created:** 2013-10-23

**Part of TDWG Standard:** http://www.tdwg.org/standards/638/

**This version:** http://rs.tdwg.org/ac/doc/structure/2013-10-23

**Latest version:** http://rs.tdwg.org/ac/doc/structure/

**Abstract:** The Audubon Core is a set of vocabularies designed to
represent metadata for biodiversity multimedia resources and
collections. These vocabularies aim to represent information that will
help to determine whether a particular resource or collection will be
fit for some particular biodiversity science application before
acquiring the media. Among others, the vocabularies address such
concerns as the management of the media and collections, descriptions of
their content, their taxonomic, geographic, and temporal coverage, and
the appropriate ways to retrieve, attribute and reproduce them. This
document contains material introductory to the **[Audubon Core Term
List](termlist.md)**

**Contributors:** Robert A. Morris, Vijay Barve, Mihail Carausu, Vishwas
Chavan, José Cuadra, Chris Freeland, Gregor Hagedorn, Patrick Leary,
Dimitry Mozzherin, Annette Olson, Greg Riccardi, Ivan Teage

**Creator:** GBIF/TDWG Multimedia Resources Task Group

**Bibliographic citation:** Multimedia Resources Task Group. 2013. Audubon Core Structure. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/ac/doc/structure/

## Table of Contents

<a href='#Introduction'>1 Introduction</a><br/>
<a href='#Status'>1.1 Status of the content of this document</a><br/>
<a href='#Terminology_of_this_specification'>2 Terminology of this specification</a><br/>
<a href='#Multiplicity.2FCardinality'>3 Multiplicity/Cardinality</a><br/>
<a href='#Structured_serializations'>3.1 Structured serializations</a><br/>
<a href='#Nested_XML'>3.1.1 Nested XML structure example (non-normative)</a><br/>
<a href='#XML_by_reference'>3.1.2 XML reference by identifier example (non-normative)</a><br/>
<a href='#Repeated_XML'>3.1.3 Repeated container element XML example (non-normative)</a><br/>
<a href='#Tabular_serializations'>3.2 Tabular serializations</a><br/>
<a href='#Separate_row_table'>3.2.1 Example of a table with each service access point in a separate row (non-normative)</a><br/>
<a href='#Same_row_table'>3.2.2 Example of a table with metadata for all service access points in the same row (non-normative)</a><br/>
<a href='#Lists_of_plain_text_values'>4 Lists of plain text values</a><br/>

## <a id="Introduction">1 Introduction</a>

This documentation describes the structure of the [TDWG](http://tdwg.org)
Audubon Core Multimedia Resources Metadata Standard (Audubon Core, or
simply AC).

**If you are unfamiliar with the Audubon Core, *please* read the
[Audubon Core Introduction](introduction.md) before
reading this document.** The introduction lays out why there is perceived a need for a
biodiversity media resource metadata schema, and how the standard
attempts to use existing metadata standards where
possible.

For term details, see the **[Audubon Core Terms List](termlist.md)** document and for a more detailed guide to the use of Audubon Core, see the **[Audubon
Core Guide](guide.md)** document.

During development, Audubon core was colloquially known as MRTG, after
its developers, the GBIF-TDWG Joint Multimedia Resources Metadata Task
Group. Please see the **[Audubon Core Guide](guide.md)** and
also **[MRTG Development
History](http://www.keytonature.eu/wiki/MRTG_Development_History)** for
the development history in detail.

### <a id="Status">1.1 Status of the content of this document</a>

Sections 2 through 4 of this document are normative except for example sections, which are labeled as non-normative.  

## <a id="Terminology_of_this_specification">2 Terminology of this specification</a>

There are many ways to organize metadata specifications, particularly as
to the nomenclature of the constituents of the metadata. Note the
following as they apply to the Audubon Core:

  - A *Multimedia Resource* is anything that a provider identifies as
    belonging to one of the possible values of the AC *Type* term and
    optionally one or more of the *Subtype* term values. A mechanism is
    provided by which providers can supply a privately defined subtype
    that will not collide with the AC defined Subtype values.
  - An AC *record* is a set of terms with any values conforming to this
    document, and which contain at least the four mandatory terms
    described in the [Audubon Core Core Term List](termlist.md), and
    which describes a single multimedia resource (possibly including a
    Collection). One of these, the value of *Identifier* is a Globally
    Unique IDentifier (GUID), which may have been assigned to the
    resource by an external authority or by the provider of the metadata
    record.
  - AC terms are divided into two *Layers*. Those characterized as in
    *Layer 1*, including the four mandatory terms, should be
    meaningfully handled by all consuming client applications. Only
    wholly complete consuming applications need handle those in the
    *Layer 2.* What is meant by "meaningfully handle" is up to
    implementers of this normative specification. It could be as simple
    as "gracefully ignore".

In the [Audubon Core Term List](termlist.md), every AC
term has a *term name* following a table entry *"Term:"*, a *URI*, a
plain text normative *Definition*, a recommended English *Label*, an
optional *Notes* attribute. In addition, a term has an attribute telling
whether it is mandatory, one telling whether it is repeatable, and one
telling whether it is in Layer 1 or 2. Layer 2 comprises terms likely to
only occur for certain media. For example, the term *DateAvailable* will
apply only to media that are embargoed, but for which the provider is
prepared to make the metadata immediately available.

AC metadata can describe either individual multimedia resources or
collections of resources. A few, but not many, of the AC properties have
different values for collections than for individual media. If no such
distinction is mentioned, AC does not assume one.

Term Names for terms borrowed from other vocabularies are those in use
for the corresponding term in those vocabularies. Term Names are
intended principally for navigation in the AC documentation. Term Labels
are suggestions for English labels in applications. They are
recommendations only and are offered only in English, with the added
expectation that they may clarify intended usage of the term.
Communities may wish to promulgate recommendations for Labels in other
languages, or even alternative English Labels for specialized audiences,
e.g. school children. Labels are may be used for navigation within the
Term List, and are often used within the Term List itself when a term is
mentioned within the documentation of another term. The Term List
provides indices both by name and label.

URI's for terms conform to the http URI scheme (See
<http://en.wikipedia.org/wiki/URI_scheme>,
<http://www.w3.org/TR/uri-clarification/>, or
<http://www.ietf.org/rfc/rfc2396.txt>.) Informally, one may understand
this as follows: an http URI has the syntax of an http URL, but there is
no expectation that putting it in a web browser will result in any
information being returned to the browser, and if there is, it may have
no relevance. This conformance requirement applies only to the URIs that
identify AC terms. A few AC terms permit **values** to be taken from
another controlled vocabulary chosen by the user. In this case, those
values may involve URIs conforming to a scheme given by that external
vocabulary, and AC is silent on what that scheme is.

The Notes field of a term's documentation points to further information,
if any exists, about the term. In particular, for terms borrowed from
other vocabularies, this field generally carries a link to the
originating vocabulary's documentation for that
term.

## <a id="Multiplicity.2FCardinality">3 Multiplicity/Cardinality</a>

A number of terms are repeatable. How to implement repeatability in a
given serialization is not defined by Audubon Core. The following
section gives advice on some best practices in the context of
repeatability.

The simplest case is a single repeatable term (e.g.,
dcterms:identifier). In representations based on an XML Schema that
permits elements to be repeated such a term may simply be repeated (e.g.
"...<dcterms:identifier\>http://example.com/123</dcterms:identifier\><dcterms:identifier\>http://example.com/456</dcterms:identifier\>...").
In serializations that do not easily lend themselves to repeatable
elements (e.g. "flat" schemata with all elements occurring only a single
time in an otherwise unstructured record) it is possible to define
separators to support a list of values within a single element (e.g.
"...<dcterms:identifier\>http://example.com/123;
http://example.com/456</dcterms:identifier\>...").

In certain cases pairs or tuples of properties are repeated. In Audubon
Core this situation occurs, for example, in the following cases:

  - The language-dependent metadata like title, description, etc. need
    to be associated with ac:metadataLanguage. One approach here is to
    use complete Audubon Core records together with the [Metadata Language](termlist.md#ac_metadataLanguage)
    property; see there for further detail.
  - The values of properties about a Service Access Point must remain
    associated with that Service Access Point even if there are multiple
    Service Access Points. See
    [hasServiceAccessPoint](termlist.md#ac_hasServiceAccessPoint)
    for further details.
  - The terms dwc:scientificName and dwc:identificationQualifier may
    optionally be structured into pairs. (See the notes on
    [dwc:identificationQualifier](termlist.md#dwc_identificationQualifier).)
  - The terms
    [Reviewer](termlist.md#ac_Reviewer),
    being the name of an individual providing some expert review of a
    resource, and the review text itself in [Reviewer Comments](termlist.md#ac_Reviewer_Comments)
    are desirable to store as pairs.

### <a id="Structured_serializations">3.1 Structured serializations</a>

Many serialization languages provide sufficiently structured forms to
deal with repeated terms unambiguously. In XML, we might define
a container element and use a nesting structure as in Section 3.2.  Alternatively, in XML we may reference access points by identifier as in Section 3.3.  Where such structures are impossible or undesirable, an alternative
solution is to permit only one access point per
container element, but to repeat the container element for a single media resource, as shown in section 3.4. This is similar
to one of the options discussed for multilingual metadata (see [Metadata Language](termlist.md#ac_metadataLanguage)).


### <a id="Nested_XML">3.1.1 Nested XML structure example (non-normative)</a>

    <MEDIA_METADATA_CONTAINER>
      <dcterms:identifier>http//:example.com/pictures/thePicture.jpg</dcterms:identifier>
      ...
      <ac:hasServiceAccessPoint>
        <dcterms:format>jpg</dcterms:format>
        <ac:accessURI>http://example.com/fullres/thePicture.jpg</ac:accessURI>
        ...
      </ac:hasServiceAccessPoint>
      <ac:hasServiceAccessPoint>
        ...
      </ac:hasServiceAccessPoint>
    <MEDIA_METADATA_CONTAINER>

### <a id="XML_by_reference">3.1.2 XML reference by identifier example (non-normative)</a>

    <MEDIA_METADATA_CONTAINER>
      <dcterms:identifier>http://example.com/pictures/thePicture.jpg</dcterms:identifier>
      ...
      <ac:hasServiceAccessPoint>http://example.com/pictures/thePicture.jpg#ac0001</ac:hasServiceAccessPoint>
      <ac:hasServiceAccessPoint>http://example.com/pictures/thePicture.jpg#ac0002</ac:hasServiceAccessPoint>
      <ac-classes:ServiceAccessPoint id="http://example.com/pictures/thePicture.jpg#ac0001">
        <dcterms:format>jpg</dcterms:format>
        <ac:accessURI>http://example.com/fullres/thePicture.jpg</ac:accessURI>
        ...
      </ac-classes:ServiceAccessPoint>
      ...
    <MEDIA_METADATA_CONTAINER>

Note: ac-classes:ServiceAccessPoint is a made-up term for the Service Access Point class.  An official term may be designated at some future time.

### <a id="Repeated_XML">3.1.3 Repeated container element XML example (non-normative)</a>

    <MEDIA_METADATA_CONTAINER>
      <dcterms:identifier>http//:example.com/pictures/thePicture.jpg</dcterms:identifier>
      <dcterms:title>A red beech leaf</dcterms:title>
      <dcterms:format>jpg</dcterms:format>
      <ac:accessURI>http://example.com/fullres/thePicture.jpg</ac:accessURI>
      ...
    <MEDIA_METADATA_CONTAINER>
    <MEDIA_METADATA_CONTAINER>
      <dcterms:identifier>http://example.com/pictures/thePicture.jpg</dcterms:identifier>
      <dcterms:format>png</dcterms:format>
      <ac:accessURI>http://example.com/fullres/thePicture-hires.png</ac:accessURI>
      ...
    <MEDIA_METADATA_CONTAINER>

### <a id="Tabular_serializations">3.2 Tabular serializations</a>

The same data as in examples 3.2 through 3.4 can be serialized as a "flat" spreadsheet-like
table.  

In the example of Section 3.6, only the required identifier is repeated, but not
the title field. Whether to repeat all fields or whether to provide all
fields only in the first record, limiting later records to the
identifier and the service access point properties, is left to specific
implementations. In the example of Section 3.6, the ac:hasServiceAccessPoint property is suppressed
as unnecessary.

Another approach also eliminates the need for the ac:hasServiceAccessPoint property when
flattening the ac structure. It is based on introducing new terms
exploiting values of the [ac:variantLiteral](termlist.md#ac_variantLiteral):
"Thumbnail", "Trailer", "Lower Quality", "Medium Quality", "Good
Quality", "Best Quality", "Offline", as prefixes for additional
properties in a new namespace.

### <a id="Separate_row_table">3.2.1 Example of a table with each service access point in a separate row (non-normative)</a>

|                                            |                   |                |                    |                                                 |
| ------------------------------------------ | ----------------- | -------------- | ------------------ | ----------------------------------------------- |
| **dcterms:identifier**                     | **dcterms:title** | **ac:variant** | **dcterms:format** | **ac:accessURI**                                |
| http://example.com/pictures/thePicture.jpg | A red beech leaf  | Best Quality   | jpg                | http://example.com/fullres/thePicture.jpg       |
| http://example.com/pictures/thePicture.jpg |                   | Best Quality   | png                | http://example.com/fullres/thePicture-hires.png |
| http://example.com/pictures/thePicture.jpg |                   | Thumbnail      | png                | http://example.com/thumbs/thePicture-thumb.png  |

### <a id="Same_row_table">3.2.2 Example of a table with metadata for all service access points in the same row (non-normative)</a>

|                                       |                   |                                     |                         |                             |                              |                              |                           |                               |                                |                              |                           |                               |                                |
| ------------------------------------- | ----------------- | ----------------------------------- | ----------------------- | --------------------------- | ---------------------------- | ---------------------------- | ------------------------- | ----------------------------- | ------------------------------ | ---------------------------- | ------------------------- | ----------------------------- | ------------------------------ |
| **dcterms:identifier**                | **dcterms:title** | **acf:thumbnailAccessURI**          | **acf:thumbnailFormat** | **acf:thumbnailImageWidth** | **acf:thumbnailImageHeight** | **acf:goodQualityAccessURI** | **acf:goodQualityFormat** | **acf:goodQualityImageWidth** | **acf:goodQualityImageHeight** | **acf:bestQualityAccessURI** | **acf:bestQualityFormat** | **acf:bestQualityImageWidth** | **acf:bestQualityImageHeight** |
| http://ex.com/pictures/thePicture.jpg | A red beech leaf  | http://example.com/thumb/thePic.jpg | image/jpeg              | 100                         | 100                          | http://ex.com/img/thePic.jpg | image/jpeg                | 1000                          | 1000                           | http://ex.com/hr/thePic.png  | image/png\</nowiki\>      | 10000                         | 10000                          |

Note: acf: (for "Audubon Core Flat") is a made-up namespace.  Communities of interest might mint such terms in order to use this kind of structure.

## <a id="Lists_of_plain_text_values">4 Lists of plain text values</a>

Some AC terms permit values that are lists to be represented as plain
text. The choice of how to separate list items is ultimately left to the
implementers of AC. Typical usage is to choose a punctuation mark such
as ",", ";", or "|". In these cases a special escape syntax needs to be
defined for cases in which the separator is part of the metadata value.
Unfortunately, even for standard list formats like CSV, different
software packages choose different escape methods, hindering
interchange. In the absence of an implementation-specific choice we
recommend to use "|" as separator and "\\|" as an escaped vertical bar.



-----------------
This document is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). ![http://creativecommons.org/licenses/by/4.0/](https://licensebuttons.net/l/by/4.0/88x31.png).

Copyright 2013 - Biodiversity Information Standards - TDWG - [Contact Us](http://www.tdwg.org/about-tdwg/contact-us/)