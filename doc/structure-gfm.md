<div id="mw-page-base" class="noprint">

</div>

<div id="mw-head-base" class="noprint">

</div>

<div id="content" class="mw-body" data-role="main">

<span id="top"></span>

<div class="mw-indicators">

</div>

# Audubon Core Structure

<div id="bodyContent" class="mw-body-content">

<div id="siteSub">

From TDWG Terms Wiki

</div>

<div id="contentSub">

</div>

<div id="jump-to-nav" class="mw-jump">

Jump to: [navigation](#mw-head), [search](#p-search)

</div>

<div id="mw-content-text" class="mw-content-ltr" lang="en" dir="ltr">

  
**Title:** Audubon Core

**Date:** 23 October, 2013.

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
List](/wiki/Audubon_Core_Term_List "Audubon Core Term List")**

**Contributors:** Robert A. Morris, Vijay Barve, Mihail Carausu, Vishwas
Chavan, Jose Cuadra, Chris Freeland, Gregor Hagedorn, Patrick Leary,
Dimitry Mozzherin, Annette Olson, Greg Riccardi, Ivan Teage

**Legal:** This document is governed by the standard legal, copyright,
licensing provisions and disclaimers issued by the Taxonomic Databases
Working Group.

**Part of TDWG Standard:** <http://www.tdwg.org/standards/638/>.

**Document Status:** This document is a [TDWG Type 1 Normative
Document](http://www.tdwg.org/fileadmin/tdwg_std_drafts/tdwg_standards_documentation_specification.html#a_3).

Release 1.0 of this document has wiki revision 10756 with a permalink
<http://terms.gbif.org/w/index.php?oldid=10756>.  
This document has wiki revision ID 10756 with a permalink
<http://terms.gbif.org/w/index.php?oldid=10756>.

<div id="toc" class="toc">

<div id="toctitle">

## Contents

</div>

  - [<span class="tocnumber">1</span> <span class="toctext">Terminology
    of this specification</span>](#Terminology_of_this_specification)
  - [<span class="tocnumber">2</span>
    <span class="toctext">Multiplicity/Cardinality</span>](#Multiplicity.2FCardinality)
  - [<span class="tocnumber">3</span> <span class="toctext">Lists of
    plain text values</span>](#Lists_of_plain_text_values)
  - [<span class="tocnumber">4</span> <span class="toctext">Term
    List</span>](#Term_List)
  - [<span class="tocnumber">5</span>
    <span class="toctext">Non-normative
    documents</span>](#Non-normative_documents)

</div>

  
This is the normative documentation for the [TDWG](http://tdwg.org)
Audubon Core Multimedia Resources Metadata Standard (Audubon Core, or
simply AC), During development, it was colloquially known as MRTG, after
its developers, the GBIF-TDWG Joint Multimedia Resources Metadata Task
Group. Please see the brief **[Audubon
Core](/wiki/Audubon_Core "Audubon Core")** non normative document and
also **[MRTG Development
History](http://www.keytonature.eu/wiki/MRTG_Development_History)** for
the development history in detail.

**If you are unfamiliar with the Audubon Core, *please* read the
[Audubon Core](/wiki/Audubon_Core "Audubon Core") introduction before
reading this page.** It lays out why there is perceived a need for a
biodiversity media resource metadata schema, and how the standard
attempts to use existing metadata standards where
possible.

## <span id="Terminology_of_this_specification" class="mw-headline">Terminology of this specification</span>

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
    described in the [Audubon Core Core Term
    List](/wiki/Audubon_Core_Term_List "Audubon Core Term List"), and
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

In the [Audubon Core Term
List](/wiki/Audubon_Core_Term_List "Audubon Core Term List"), every AC
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

## <span id="Multiplicity.2FCardinality" class="mw-headline">Multiplicity/Cardinality</span>

A number of terms are repeatable. How to implement repeatability in a
given serialization is not defined by Audubon Core. The following
section gives advice on some best practices in the context of
repeatability.

The simplest case is a single repeatable term (e.g.,
dcterms:identifier). In representations based on an XML Schema that
permits elements to be repeated such a term may simply be repeated (e.g.
"...\<dcterms:identifier\>http://example.com/123\</dcterms:identifier\>\<dcterms:identifier\>http://example.com/456\</dcterms:identifier\>...").
In serializations that do not easily lend themselves to repeatable
elements (e.g. "flat" schemata with all elements occurring only a single
time in an otherwise unstructured record) it is possible to define
separators to support a list of values within a single element (e.g.
"...\<dcterms:identifier\>http://example.com/123;
http://example.com/456\</dcterms:identifier\>...").

In certain cases pairs or tuples of properties are repeated. In Audubon
Core this situation occurs, for example, in the following cases:

  - The language-dependent metadata like title, description, etc. need
    to be associated with ac:metadataLanguage. One approach here is to
    use complete Audubon Core records together with the [Metadata
    Language](/wiki/Audubon_Core_Term_List#ac:metadataLanguage "Audubon Core Term List")
    property; see there for further detail.
  - The values of properties about a Service Access Point must remain
    associated with that Service Access Point even if there are multiple
    Service Access Points. See
    [hasServiceAccessPoint](/wiki/Audubon_Core_Term_List#ac:hasServiceAccessPoint "Audubon Core Term List")
    for further details.
  - The terms dwc:scientificName and dwc:identificationQualifier may
    optionally be structured into pairs. (See the notes on
    [dwc:identificationQualifier](/wiki/Audubon_Core_Term_List#dwc:identificationQualifier "Audubon Core Term List").)
  - The terms
    [Reviewer](/wiki/Audubon_Core_Term_List#ac:Reviewer "Audubon Core Term List"),
    being the name of an individual providing some expert review of a
    resource, and the review text itself in [Reviewer
    Comments](/wiki/Audubon_Core_Term_List#ac:Reviewer_Comments "Audubon Core Term List")
    are desirable to store as pairs.

Many serialization languages provide sufficiently structured forms to
deal with repeated terms unambiguously. For example, in XML might define
a container element and use a nesting structure something like this:

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

Another example may reference access points by identifier:

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

Note: ac-classes:ServiceAccessPoint a prefix of an illustrative
namespace. Namespace recommendations will be made when the normative
documents are approved.

Where such structure is impossible or undesirable, an alternative
solution is to to permit only one access point per
MEDIA\_METADATA\_CONTAINER, but to repeat the main
MEDIA\_METADATA\_CONTAINER for a single media resource. This is similar
to one of the options discussed for multilingual metadata (see [Metadata
Language](/wiki/Audubon_Core_Term_List#ac:metadataLanguage "Audubon Core Term List")).
An example in XML for this:

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

The same example as a spreadsheet-like
table:

|                                            |                   |                |                    |                                                 |
| ------------------------------------------ | ----------------- | -------------- | ------------------ | ----------------------------------------------- |
| **dcterms:identifier**                     | **dcterms:title** | **ac:variant** | **dcterms:format** | **ac:accessURI**                                |
| http://example.com/pictures/thePicture.jpg | A red beech leaf  | Best Quality   | jpg                | http://example.com/fullres/thePicture.jpg       |
| http://example.com/pictures/thePicture.jpg |                   | Best Quality   | png                | http://example.com/fullres/thePicture-hires.png |
| http://example.com/pictures/thePicture.jpg |                   | Thumbnail      | png                | http://example.com/thumbs/thePicture-thumb.png  |

In the example above, only the required identifier is repeated, but not
the title field. Whether to repeat all fields or whether to provide all
fields only in the first record, limiting later records to the
identifier and the service access point properties, is left to specific
implementations. In the example, hasAccessPoint property is suppressed
as unnecessary. Another approach reduces the need for the property when
flattening the ac structure. It is based on introducing new terms
exploiting values of the [Audubon\_Core\_Term\_List\#ac:variantLiteral
ac:variantLiteral](/wiki/Audubon_Core_Term_List#ac:variantLiteral_ac:variantLiteral "Audubon Core Term List"):
"Thumbnail", "Trailer", "Lower Quality", "Medium Quality", "Good
Quality", "Best Quality", "Offline", as prefixes for additional
properties in a new namespace, say acf (Audubon Core
Flat):

|                                       |                   |                                     |                         |                             |                              |                              |                           |                               |                                |                              |                           |                               |                                |
| ------------------------------------- | ----------------- | ----------------------------------- | ----------------------- | --------------------------- | ---------------------------- | ---------------------------- | ------------------------- | ----------------------------- | ------------------------------ | ---------------------------- | ------------------------- | ----------------------------- | ------------------------------ |
| **dcterms:identifier**                | **dcterms:title** | **acf:thumbnailAccessURI**          | **acf:thumbnailFormat** | **acf:thumbnailImageWidth** | **acf:thumbnailImageHeight** | **acf:goodQualityAccessURI** | **acf:goodQualityFormat** | **acf:goodQualityImageWidth** | **acf:goodQualityImageHeight** | **acf:bestQualityAccessURI** | **acf:bestQualityFormat** | **acf:bestQualityImageWidth** | **acf:bestQualityImageHeight** |
| http://ex.com/pictures/thePicture.jpg | A red beech leaf  | http://example.com/thumb/thePic.jpg | image/jpeg              | 100                         | 100                          | http://ex.com/img/thePic.jpg | image/jpeg                | 1000                          | 1000                           | http://ex.com/hr/thePic.png  | image/png\</nowiki\>      | 10000                         | 10000                          |

## <span id="Lists_of_plain_text_values" class="mw-headline">Lists of plain text values</span>

Some AC terms permit values that are lists to be represented as plain
text. The choice of how to separate list items is ultimately left to the
implementers of AC. Typical usage is to choose a punctuation mark such
as ",", ";", or "|". In these cases a special escape syntax needs to be
defined for cases in which the separator is part of the metadata value.
Unfortunately, even for standard list formats like CSV, different
software packages choose different escape methods, hindering
interchange. In the absence of an implementation-specific choice we
recommend to use "|" as separator and "\\|" as an escaped vertical bar.

## <span id="Term_List" class="mw-headline">Term List</span>

See: [Audubon Core Term
List](/wiki/Audubon_Core_Term_List "Audubon Core Term List")

## <span id="Non-normative_documents" class="mw-headline">Non-normative documents</span>

See: [Audubon Core](/wiki/Audubon_Core "Audubon Core") introduction;
[Audubon Core Offline Non Normative
Document](/wiki/Audubon_Core_Offline_Non_Normative_Document "Audubon Core Offline Non Normative Document")

</div>

<div class="printfooter">

Retrieved from
"<https://terms.tdwg.org/w/index.php?title=Audubon_Core_Structure&oldid=10756>"

</div>

<div id="catlinks" class="catlinks">

<div id="mw-normal-catlinks" class="mw-normal-catlinks">

[Class](/wiki/Special:Categories "Special:Categories"):

  - [Audubon
Core](/wiki/Class:Audubon_Core "Class:Audubon Core")

</div>

</div>

<div class="visualClear">

</div>

</div>

</div>

<div id="mw-navigation">

## Navigation menu

<div id="mw-head">

<div id="p-personal" data-role="navigation" data-aria-labelledby="p-personal-label">

### Personal tools

  - <span id="pt-uls">[English](#)</span>
  - <span id="pt-login">[Log
    in](/w/index.php?title=Special:UserLogin&returnto=Audubon+Core+Structure "You are encouraged to log in; however, it is not mandatory [o]")</span>
  - <span id="pt-createaccount">[Request
    account](/wiki/Special:RequestAccount "You are encouraged to create an account and log in; however, it is not mandatory")</span>
  - <span id="pt-openidlogin">[Use
    OpenID](/w/index.php?title=Special:OpenIDLogin&returnto=Audubon_Core_Structure)</span>

</div>

<div id="left-navigation">

<div id="p-namespaces" class="vectorTabs" data-role="navigation" data-aria-labelledby="p-namespaces-label">

### Namespaces

  - <span id="ca-nstab-main"><span>[Page](/wiki/Audubon_Core_Structure "View the content page [c]")</span></span>
  - <span id="ca-talk"><span>[Discussion](/wiki/Talk:Audubon_Core_Structure "Discussion about the content page [t]")</span></span>

</div>

<div id="p-variants" class="vectorMenu emptyPortlet" data-role="navigation" data-aria-labelledby="p-variants-label">

### <span>Variants</span>[](#)

<div class="menu">

</div>

</div>

</div>

<div id="right-navigation">

<div id="p-views" class="vectorTabs" data-role="navigation" data-aria-labelledby="p-views-label">

### Views

  - <span id="ca-view"><span>[Read](/wiki/Audubon_Core_Structure)</span></span>
  - <span id="ca-form_edit"><span>[View
    form](/w/index.php?title=Audubon_Core_Structure&action=formedit)</span></span>
  - <span id="ca-viewsource"><span>[View
    source](/w/index.php?title=Audubon_Core_Structure&action=edit "This page is protected.
    You can view its source [e]")</span></span>
  - <span id="ca-history"><span>[View
    history](/w/index.php?title=Audubon_Core_Structure&action=history "Past revisions of this page [h]")</span></span>

</div>

<div id="p-cactions" class="vectorMenu emptyPortlet" data-role="navigation" data-aria-labelledby="p-cactions-label">

### <span>More</span>[](#)

<div class="menu">

</div>

</div>

<div id="p-search" data-role="search">

### Search

<div id="simpleSearch">

</div>

</div>

</div>

</div>

<div id="mw-panel">

<div id="p-logo" data-role="banner">

[](/wiki/Main_Page "Visit the main page")

</div>

<div id="p-Terminology_Platform" class="portal" data-role="navigation" data-aria-labelledby="p-Terminology_Platform-label">

### Terminology Platform

<div class="body">

  - <span id="n-Terminology-Platform">[Terminology
    Platform](/wiki/Main_Page)</span>

</div>

</div>

<div id="p-navigation" class="portal" data-role="navigation" data-aria-labelledby="p-navigation-label">

### Navigation

<div class="body">

  - <span id="n-help">[Help](/wiki/Help:First_Help "The place to find out")</span>
  - <span id="n-Query-concepts">[Query
    concepts](/wiki/Special:RunQuery/Query_concept)</span>
  - <span id="n-recentchanges">[Recent
    changes](/wiki/Special:RecentChanges "A list of recent changes in the wiki [r]")</span>

</div>

</div>

<div id="p-tb" class="portal" data-role="navigation" data-aria-labelledby="p-tb-label">

### Tools

<div class="body">

  - <span id="t-whatlinkshere">[What links
    here](/wiki/Special:WhatLinksHere/Audubon_Core_Structure "A list of all wiki pages that link here [j]")</span>
  - <span id="t-recentchangeslinked">[Related
    changes](/wiki/Special:RecentChangesLinked/Audubon_Core_Structure "Recent changes in pages linked from this page [k]")</span>
  - <span id="t-upload">[Upload
    file](//species-id.net/openmedia/Special:UploadWizard?uselang=en "Upload files [u]")</span>
  - <span id="t-specialpages">[Special
    pages](/wiki/Special:SpecialPages "A list of all special pages [q]")</span>
  - <span id="t-print">[Printable
    version](/w/index.php?title=Audubon_Core_Structure&printable=yes "Printable version of this page [p]")</span>
  - <span id="t-permalink">[Permanent
    link](/w/index.php?title=Audubon_Core_Structure&oldid=10756 "Permanent link to this revision of the page")</span>
  - <span id="t-info">[Page
    information](/w/index.php?title=Audubon_Core_Structure&action=info "More information about this page")</span>
  - <span id="t-smwbrowselink">[Browse
    properties](/wiki/Special:Browse/Audubon_Core_Structure)</span>
  - <span id="t-cite">[Cite this
    page](/w/index.php?title=Special:CiteThisPage&page=Audubon_Core_Structure&id=10756 "Information on how to cite this page")</span>

</div>

</div>

</div>

</div>

<div id="footer" data-role="contentinfo">

  - <span id="footer-info-lastmod">This page was last modified on 23
    October 2013, at 02:35.</span>
  - <span id="footer-info-copyright">Content is available under
    [Creative Commons Attribution-Share Alike 4.0
    Unported](http://creativecommons.org/licenses/by-sa/4.0/). — This
    project is partly funded by the EU under grant agreement n°261532
    [(ViBRANT)](http://terms.gbif.org/wiki/ViBRANT)</span>

<!-- end list -->

  - <span id="footer-places-privacy">[Privacy
    policy](https://wikimediafoundation.org/wiki/Special:MyLanguage/Privacy_policy/en "wmf:Special:MyLanguage/Privacy policy/en")</span>
  - <span id="footer-places-about">[About TDWG Terms
    Wiki](/wiki/TDWG_Terms_Wiki:About "TDWG Terms Wiki:About")</span>
  - <span id="footer-places-disclaimer">[Disclaimers](/wiki/TDWG_Terms_Wiki:General_disclaimer "TDWG Terms Wiki:General disclaimer")</span>
  - <span id="footer-places-developers">[Developers](https://www.mediawiki.org/wiki/Special:MyLanguage/How_to_contribute)</span>

<!-- end list -->

  - <span id="footer-copyrightico">[![Creative Commons Attribution-Share
    Alike 4.0
    Unported](//species-id.net/s/media/f/f3/CC-BY-SA_3_icon_88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)</span>
  - <span id="footer-poweredbyico">[![Served by Plazi
    Biowikifarm.net](//species-id.net/s/media/3/37/Servedby_biowikifarm_88x31.png)](http://biowikifarm.net/)[![Powered
    by
    MediaWiki](//species-id.net/s/media/3/3d/Poweredby_mediawiki_64x31.png)](http://www.mediawiki.org/)[![Powered
    by Semantic
    MediaWiki](https://terms.tdwg.org/w/extensions/SemanticMediaWiki/res/images/smw_button.png)](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki)</span>

<div style="clear:both">

</div>

</div>
