---
permalink: /structure/
---

# Audubon Core Structure

**Title:** Audubon Core Structure

**Date version issued:** 2021-10-05

**Date created:** 2013-10-23

**Part of TDWG Standard:** http://www.tdwg.org/standards/638

**This version:** http://rs.tdwg.org/ac/doc/structure/2021-10-05

**Latest version:** http://rs.tdwg.org/ac/doc/structure/

**Previous version:** [http://rs.tdwg.org/ac/doc/structure/2020-01-27](2020-01-27)

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
List](../termlist)**

**Contributors:** Robert A. Morris, Vijay Barve, Mihail Carausu, Vishwas
Chavan, José Cuadra, Chris Freeland, Gregor Hagedorn, Patrick Leary,
Dimitry Mozzherin, Annette Olson, Greg Riccardi, Ivan Teage, Steve Baskauf

**Creator:** GBIF/TDWG Multimedia Resources Task Group and Audubon Core Maintenance Group

**Bibliographic citation:** Audubon Core Maintenance Group. 2021. Audubon Core Structure. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/ac/doc/structure/2021-10-05

## 1 Introduction

This documentation describes the structure of the [TDWG](http://tdwg.org)
Audubon Core Multimedia Resources Metadata Standard (Audubon Core, or
simply AC).

**If you are unfamiliar with the Audubon Core, *please* read the
[Audubon Core Introduction](../introduction) before
reading this document.** The introduction lays out why there is perceived a need for a
biodiversity media resource metadata schema, and how the standard
attempts to use existing metadata standards where
possible.

For term details, see the [Audubon Core Terms List](../termlist) document and for a more detailed guide to the use of Audubon Core, see the [Audubon Core Guide](../guide) document.

During development, Audubon core was colloquially known as MRTG, after
its developers, the GBIF-TDWG Joint Multimedia Resources Metadata Task
Group. Please see the [Audubon Core Guide](../guide) and
also [MRTG Development History](http://www.keytonature.eu/wiki/MRTG_Development_History) for
the development history in detail.


### 1.1 Status of the content of this document

Sections 2 through 4 of this document are normative except for example sections, which are labeled as non-normative.  


### 1.2 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).


## 2 Terminology of this specification

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
    described in the [Audubon Core Core Term List](../termlist), and
    which describes a single multimedia resource (possibly including a
    Collection). One of these, the value of *Identifier* is a Globally
    Unique IDentifier (GUID), which may have been assigned to the
    resource by an external authority or by the provider of the metadata
    record.

In the [Audubon Core Term List](../termlist), every AC
term has a *term name* following a table entry *"Term:"*, a *URI*, a
plain text normative *Definition*, a recommended English *Label*, an
optional *Notes* attribute. In addition, a term has an attribute telling
whether it is mandatory and one telling whether it is repeatable.

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
e.g. school children. Labels MAY be used for navigation within the
Term List, and are often used within the Term List itself when a term is
mentioned within the documentation of another term. The Term List
provides indices both by name and label.

URI's for terms conform to the http URI scheme (see
http://en.wikipedia.org/wiki/URI_scheme,
http://www.w3.org/TR/uri-clarification, or
http://www.ietf.org/rfc/rfc2396.txt). Informally, one may understand
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


## 3 Multiplicity and Cardinality

A number of terms are repeatable. How to implement repeatability in a
given serialization is not defined by Audubon Core. The following
section gives advice on some best practices in the context of
repeatability.

The simplest case is a single repeatable term (e.g.,
dcterms:identifier). In representations based on an XML Schema that
permits elements to be repeated such a term may simply be repeated (e.g.
"`...<dcterms:identifier>http://example.com/123</dcterms:identifier><dcterms:identifier>http://example.com</dcterms:identifier>...`").
In serializations that do not easily lend themselves to repeatable
elements (e.g. "flat" schemata with all elements occurring only a single
time in an otherwise unstructured record) it is possible to define
separators to support a list of values within a single element (e.g.
"`...<dcterms:identifier>http://example.com/123;
http://example.com/456</dcterms:identifier>...`").

In certain cases pairs or tuples of properties are repeated. In Audubon
Core this situation occurs, for example, in the following cases:

  - The language-dependent metadata like title, description, etc. need
    to be associated with `ac:metadataLanguage`. One approach here is to
    use complete Audubon Core records together with the [Metadata Language](../termlist#ac_metadataLanguage)
    property; see there for further detail.
  - The values of properties about a Service Access Point MUST remain
    associated with that Service Access Point even if there are multiple
    Service Access Points. See
    [ac:hasServiceAccessPoint](../termlist#ac_hasServiceAccessPoint)
    for further details.
  - The terms `dwc:scientificName` and `dwc:identificationQualifier` MAY
    optionally be structured into pairs. (See the notes on
    [dwc:identificationQualifier](../termlist#dwc_identificationQualifier).)
  - The terms
    [Reviewer](../termlist#ac_reviewer),
    being the name of an individual providing some expert review of a
    resource, and the review text itself in [Reviewer Comments](../termlist#ac_reviewerComments)
    are desirable to store as pairs.


### 3.1 Structured serializations

Many serialization languages provide sufficiently structured forms to
deal with repeated terms unambiguously. In XML, we might define
a container element and use a nesting structure as in Section 3.1.1  Alternatively, in XML we may reference access points by identifier as in Section 3.1.2  Where such structures are impossible or undesirable, an alternative
solution is to permit only one access point per
container element, but to repeat the container element for a single media resource, as shown in section 3.1.3 This is similar
to one of the options discussed for multilingual metadata (see [Metadata Language](../termlist#ac_metadataLanguage)).

Note: In the examples, for human-readability the literal valued terms `dc:format` and `ac:variantLiteral` were used. However, it is designated best practice to use the IRI valued terms `dcterms:format` and `ac:variant` with controlled IRI values from the [controlled vocabulary for format](http://rs.tdwg.org/ac/doc/format/) and [controlled vocabulary for variant](http://rs.tdwg.org/ac/doc/variant/).  See the notes on [dc:format](http://rs.tdwg.org/ac/doc/termlist/#dc_format) and [ac:variantLiteral](http://rs.tdwg.org/ac/doc/termlist/#ac_variantLiteral) for more information.


#### 3.1.1 Nested XML structure example (non-normative)

    <MEDIA_METADATA_CONTAINER>
      <dcterms:identifier>http//:example.com/pictures/thePicture.jpg</dcterms:identifier>
      ...
      <ac:hasServiceAccessPoint>
        <dc:format>image/jpeg</dc:format>
        <ac:accessURI>http://example.com/fullres/thePicture.jpg</ac:accessURI>
        ...
      </ac:hasServiceAccessPoint>
      <ac:hasServiceAccessPoint>
        ...
      </ac:hasServiceAccessPoint>
    <MEDIA_METADATA_CONTAINER>


#### 3.1.2 XML reference by identifier example (non-normative)

    <MEDIA_METADATA_CONTAINER>
      <dcterms:identifier>http://example.com/pictures/thePicture.jpg</dcterms:identifier>
      ...
      <ac:hasServiceAccessPoint>http://example.com/pictures/thePicture.jpg#ac0001</ac:hasServiceAccessPoint>
      <ac:hasServiceAccessPoint>http://example.com/pictures/thePicture.jpg#ac0002</ac:hasServiceAccessPoint>
      <ac:ServiceAccessPoint id="http://example.com/pictures/thePicture.jpg#ac0001">
        <dc:format>image/jpeg</dc:format>
        <ac:accessURI>http://example.com/fullres/thePicture.jpg</ac:accessURI>
        ...
      </ac:ServiceAccessPoint>
      ...
    <MEDIA_METADATA_CONTAINER>



#### 3.1.3 Repeated container element XML example (non-normative)

    <MEDIA_METADATA_CONTAINER>
      <dcterms:identifier>http//:example.com/pictures/thePicture.jpg</dcterms:identifier>
      <dcterms:title>A red beech leaf</dcterms:title>
      <dct:format>image/jpeg</dc:format>
      <ac:accessURI>http://example.com/fullres/thePicture.jpg</ac:accessURI>
      ...
    <MEDIA_METADATA_CONTAINER>
    <MEDIA_METADATA_CONTAINER>
      <dcterms:identifier>http://example.com/pictures/thePicture.jpg</dcterms:identifier>
      <dc:format>image/png</dc:format>
      <ac:accessURI>http://example.com/fullres/thePicture-hires.png</ac:accessURI>
      ...
    <MEDIA_METADATA_CONTAINER>


### 3.2 Tabular serializations

The same data as in examples 3.1.1 through 3.1.3 can be serialized as a "flat" spreadsheet-like
table.  

In the example of Section 3.2.1, only the required identifier is repeated, but not
the title field. Whether to repeat all fields or whether to provide all
fields only in the first record, limiting later records to the
identifier and the service access point properties, is left to specific
implementations. In the example of Section 3.2.1, the `ac:hasServiceAccessPoint` property is suppressed
as unnecessary.

#### 3.2.1 Example of a table with each service access point in a separate row (non-normative)

<table class="table-responsive">
  <tbody>
    <tr>
      <td><strong>dcterms:identifier</strong></td>
      <td><strong>dcterms:title</strong></td>
      <td><strong>ac:variantLiteral</strong></td>
      <td><strong>dc:format</strong></td>
      <td><strong>ac:accessURI</strong></td>
    </tr>
    <tr>
      <td>http://example.com/pictures/thePicture.jpg</td>
      <td>A red beech leaf</td>
      <td>Best Quality</td>
      <td>image/jpeg</td>
      <td>http://example.com/fullres/thePicture.jpg</td>
    </tr>
    <tr>
      <td>http://example.com/pictures/thePicture.jpg</td>
      <td>&nbsp;</td>
      <td>Best Quality</td>
      <td>image/png</td>
      <td>http://example.com/fullres/thePicture-hires.png</td>
    </tr>
    <tr>
      <td>http://example.com/pictures/thePicture.jpg</td>
      <td>&nbsp;</td>
      <td>Thumbnail</td>
      <td>image/png</td>
      <td>http://example.com/thumbs/thePicture-thumb.png</td>
    </tr>
  </tbody>
</table>

Another approach (Section 3.2.2) also eliminates the need for the `ac:hasServiceAccessPoint` property when
flattening the ac structure. It is based on introducing new terms
exploiting values of the [ac:variantLiteral](../termlist#ac_variantLiteral):
"Thumbnail", "Trailer", "Lower Quality", "Medium Quality", "Good
Quality", "Best Quality", "Offline", as prefixes for additional
properties in a new namespace.

#### 3.2.2 Example of a table with metadata for all service access points in the same row (non-normative)

<table class="table-responsive">
  <tbody>
    <tr>
      <td><strong>dcterms:identifier</strong></td>
      <td><strong>dcterms:title</strong></td>
      <td><strong>acf:thumbnailAccessURI</strong></td>
      <td><strong>acf:thumbnailFormat</strong></td>
      <td><strong>acf:thumbnailImageWidth</strong></td>
      <td><strong>acf:thumbnailImageHeight</strong></td>
      <td><strong>acf:goodQualityAccessURI</strong></td>
      <td><strong>acf:goodQualityFormat</strong></td>
      <td><strong>acf:goodQualityImageWidth</strong></td>
      <td><strong>acf:goodQualityImageHeight</strong></td>
      <td><strong>acf:bestQualityAccessURI</strong></td>
      <td><strong>acf:bestQualityFormat</strong></td>
      <td><strong>acf:bestQualityImageWidth</strong></td>
      <td><strong>acf:bestQualityImageHeight</strong></td>
    </tr>
    <tr>
      <td>http://ex.com/pictures/thePicture.jpg</td>
      <td>A red beech leaf</td>
      <td>http://example.com/thumb/thePic.jpg</td>
      <td>image/jpeg</td>
      <td>100</td>
      <td>100</td>
      <td>http://ex.com/img/thePic.jpg</td>
      <td>image/jpeg</td>
      <td>1000</td>
      <td>1000</td>
      <td>http://ex.com/hr/thePic.png</td>
      <td>image/png</td>
      <td>10000</td>
      <td>10000</td>
    </tr>
  </tbody>
</table>

Note: `acf:` (for "Audubon Core Flat") is a made-up namespace.  Communities of interest might mint such terms in order to use this kind of structure.

## 4 Lists of plain text values

Some AC terms permit values that are lists to be represented as plain
text. The choice of how to separate list items is ultimately left to the
implementers of AC. Typical usage is to choose a punctuation mark such
as ",", ";", or "|". In these cases a special escape syntax needs to be
defined for cases in which the separator is part of the metadata value.
Unfortunately, even for standard list formats like CSV, different
software packages choose different escape methods, hindering
interchange. In the absence of an implementation-specific choice we
RECOMMEND to use "|" as separator and "\\|" as an escaped vertical bar.
