# Audubon Core Guide

**Title:** Audubon Core Guide

**Date version issued:** 2013-10-15

**Date created:** 2013-10-15

**Part of TDWG Standard:** http://www.tdwg.org/standards/638/

**This version:** http://rs.tdwg.org/ac/doc/guide/2013-10-15

**Latest version:** http://rs.tdwg.org/ac/doc/guide/

**Abstract:** The Audubon Core is a set of vocabularies designed to represent metadata for biodiversity multimedia resources and collections. This non-normative document provides some background to the aims and uses of the standard.

**Contributors:** Robert A. Morris, Vijay Barve, Mihail Carausu, Vishwas
Chavan, José Cuadra, Chris Freeland, Gregor Hagedorn, Patrick Leary,
Dimitry Mozzherin, Annette Olson, Greg Riccardi, Ivan Teage

**Creator:** GBIF/TDWG Multimedia Resources Task Group

**Bibliographic citation:** Multimedia Resources Task Group. 2013. Audubon Core Guide. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/ac/doc/guide/

## Table of Contents

[1 Introduction](#1-introduction)

[1.1 Status of the content of this document](#11-status-of-the-content-of-this-document)

[2 Summary](#2-summary)

[3 Audubon Core Terms](#3-audubon-core-terms)

[4 Motivation and Rationale](#4-motivation-and-rationale)

[5 Existing Standards](#5-existing-standards)

[6 Common Concerns with Other Biodiversity Information Standards](#6-common-concerns-with-other-biodiversity-information-standards)

[7 Concerns Not Emphasized in Other Biodiversity Information Standards](#7-concerns-not-emphasized-in-other-biodiversity-information-standards)

[8 Multimedia Resource Descriptions](#8-multimedia-resource-descriptions)

[9 Audubon Core Records](#9-audubon-core-records)

[10 Implementation and Compliance](#10-implementation-and-compliance)

[11 Further Information](#11-further-information)

[12 Appendix I: Glossary](#12-appendix-i-glossary)

[13 Appendix II: Audubon Core Development History](#13-appendix-ii-audubon-core-development-history)

[13.1 Timeline](#131-timeline)

[13.2 Document revision history](#132-document-revision-history)

[14 Endnotes](#14-endnotes)


## 1 Introduction

The Audubon Core Multimedia Resources Metadata Schema (Audubon Core) is a data standard for exchanging data describing biodiversity multimedia
resources and collections produced by the GBIF/TDWG joint Multimedia
Resources Metadata Task Group (MRTG).  The standard consists of four documents.  This document is a guide to the aims and uses of the standard. The [Audubon
Core Introduction](introduction.md) document provides a brief introduction to the Audubon Core Standard. For detailed information about the structure of Audubon Core, see the [Audubon Core Structure](structure.md) document.  For term details, see the [Audubon Core Terms List](termlist.md) document.

Acronyms and named institutions and projects are listed in a Glossary in
Appendix I.


### 1.1 Status of the content of this document

All sections of this document are non-normative.  


## 2 Summary

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
augmented where necessary by other terms.

This document accompanies the normative part of the AC standard,
comprising an introductory wiki document named simply Audubon Core <sup id="cit-1">[\[1\]](#fn-1)</sup>
and a wiki document named “Audubon Core Term List” <sup id="cit-2">[\[2\]](#fn-2)</sup>. The Term List
documents a series of terms, each of which is identified by a unique
Uniform Resource Identifier (URI), together with normative definitions.
In addition, MRTG will develop recommended representations for AC
descriptions in several important forms including RDF <sup id="cit-3">[\[3\]](#fn-3)</sup>, XML
Schema <sup id="cit-4">[\[4\]](#fn-4)</sup>, and Comma Separated Values (CSV) <sup id="cit-5">[\[5\]](#fn-5)</sup>.

Figure 1 below augments a portion of Figure 2 of the non-normative
portion of the NCD document <sup id="cit-6">[\[6\]](#fn-6)</sup>. It shows a number of kinds of
biodiversity data-centric resources and illustrates typical user
communities, data and metadata standards, and network services that
support the discovery, analysis, and integration of data. We extracted
from the NCD figure the resources and relationships between them, which
we augment with three types not in the main purview of NCD. These are:
Observations, Ecological Models, and the focus of this work, Multimedia
Resources. Applications exploiting each kind of these resources find
utility, or sometimes require the use of multimedia resources to
document them. For example, the Biological Heritage Library is a project
that provides scanned images of legacy literature at a far greater rate
than it can provide digitized versions based on optical character
recognition, and these images remain available as sources for any
subsequent derived products. Thus digitized legacy literature is
documented by the page images. Most scientific literature of course is
also illustrated by photographs, graphs, or other artifacts in the
purview of the Audubon Core. Even the providers of “Molecular DNA"
resources sometimes will offer original data as digital images of
microarray chips.

![](guide_fig_1.png)

Figure 1. Relationships of Multimedia Resources to primary types of
biodiversity resources


## 3 Audubon Core Terms

An Audubon Core record is a description, using the Audubon Core terms,
of a multimedia resource. Two kinds of terms are specified by AC:
*record-level terms* and *access-level terms.* Record-level terms apply
to the media resource being described. Almost all terms are record-level
terms. One such term, *serviceAccessPoint* plays a special role in
helping to retrieve the resource that the record describes. A multimedia
resource may have more than one serviceAccessPoint, each of which is
described by values of one or more access-level terms. The access-level
terms provide such things as a web address at which a digital
representation of the resource can be retrieved, the size of such a
retrieved object, etc.

An Audubon Core record is thus a set of terms that conforms to the
normative documents, contains at least the four mandatory terms
described below, and which provides metadata that describes a single
multimedia resource (possibly including a Collection). It usually
includes an identifier that may have been assigned to the resource by an
external authority or by the provider of the metadata record.

Every Audubon Core term has a plain text Name, a URI, and a plain text
normative Definition. URIs for terms conform to the http URI scheme.
Informally, one may understand this thusly: an http URI has the syntax
of an http URL, but there is no expectation that putting it in a web
browser will result in any information being returned to the browser,
and if it does, the return may have no relevance.

Because http URIs are rather lengthy, AC documents follow a standard
practice of introducing a short prefix comprising a "namespace
qualifier" separated by a colon from a mnemonic name closely related to
the term's Name. The namespace of terms borrowed from other vocabularies
is that of the original. The namespace of denovo AC terms is
http://rs.tdwg.org/ac/terms/. In the table of terms, each term entry has
a row with the term name. Following the practice of the Darwin Core term
list <sup id="cit-7">[\[7\]](#fn-7)</sup>, for borrowed terms, this term name is generally an
"unqualified name" preceded by a widely accepted prefix designating an
abbreviation for the namespace, whereas for denovo AC terms, no such
prefix is prepended. It is recommended that implementers who need a
namespace prefix for the AC namespace use "ac" wherever feasible. The
result is known as a qualified name. For example the normative wiki
documentation for the borrowed term dcterms:identifier has URI
http://purl.org/dc/terms/identifier. In this document we will follow the
qualified name convention that is established by the wiki rendering. In
fact, most of the URIs for terms borrowed from external vocabularies
(about half of them) do in fact resolve to something in relevant
documentation for that external standard. Sometimes it is not precise
because the documentation is a PDF document and several (different\!)
URIs might apparently resolve to the same place.

Examples from the normative Term List are shown
below.

<table>
	<tbody>
		<tr>
			<td>Term Name:</td>
			<td>dcterms:type</td>
		</tr>
		<tr>
			<td>Normative URI:</td>
			<td><a href="http://purl.org/dc/terms/type" rel="nofollow">http://purl.org/dc/terms/type</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Type</td>
		</tr>
		<tr>
			<td></td>
			<td>Layer:&nbsp;1 —&nbsp;Required:&nbsp;Yes —&nbsp;Repeatable:&nbsp;No</td>
		</tr>
		<tr>
			<td>Definition:</td>
			<td>Any type term from&nbsp;<a href="http://dublincore.org/documents/dcmi-type-vocabulary/#_blank" rel="nofollow">http://dublincore.org/documents/dcmi-type-vocabulary/</a>&nbsp;may be used. Recommended terms are&nbsp;<em>Collection</em>,&nbsp;<em>StillImage</em>,&nbsp;<em>Sound</em>,&nbsp;<em>MovingImage</em>,&nbsp;<em>InteractiveResource</em>,&nbsp;<em>Text</em>. Also recommended are<em>PanAndZoomImage</em>,&nbsp;<em>3DStillImage</em>, and&nbsp;<em>3DMovingImage</em>. Values may be used either in their literal form, or with a full namespace (e. g. <a href="http://purl.org/dc/dcmitype/StillImage" rel="nofollow">http://purl.org/dc/dcmitype/StillImage</a>) from a controlled vocabulary.</td>
		</tr>
		<tr>
			<td>Notes:</td>
			<td>A Collection should be given type&nbsp;<a href="http://purl.org/dc/dcmitype/Collection#_blank" rel="nofollow">http://purl.org/dc/dcmitype/Collection</a>. If the resource is a Collection, this item does&nbsp;<em>not</em>&nbsp;identify what types of objects it may contain. Following the DC recommendations at <a href="http://purl.org/dc/dcmitype/Text#_blank" rel="nofollow">http://purl.org/dc/dcmitype/Text</a>, images of text should be marked as&nbsp;<em>Text</em>.</td>
		</tr>
	</tbody>
</table>

<table>
	<tbody>
		<tr>
			<td>Term Name:</td>
			<td>subtype</td>
		</tr>
		<tr>
			<td>Normative URI:</td>
			<td><a href="http://rs.tdwg.org/ac/terms/subtype" rel="nofollow">http://rs.tdwg.org/ac/terms/subtype</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Subtype</td>
		</tr>
		<tr>
			<td></td>
			<td>Layer:&nbsp;1 —&nbsp;Required:&nbsp;No —&nbsp;Repeatable:&nbsp;Yes</td>
		</tr>
		<tr>
			<td>Definition:</td>
			<td>Any of Drawing, Painting, Logo, Icon, Illustration, Graphic, Photograph, Animation, Film, SlideShow, DesignPlan, Diagram, Map, MusicalNotation, IdentificationKey, ScannedText, RecordedText, RecordedOrganism, TaxonPage, MultimediaLearningObject, VirtualRealityEnvironment, GlossaryPage. Values may be be used either in their literal form, or with their full namespace.</td>
		</tr>
		<tr>
			<td>Notes:</td>
			<td>This does not apply to Collection objects. The vocabulary may be extended by users provided they identify the term by a URI which is not in the ac namespace (for example, using "<a href="http://my.inst.org/namespace/metadata/subtype/repair-manual" rel="nofollow">http://my.inst.org/namespace/metadata/subtype/repair-manual</a>". Conforming applications may choose to ignore these.</td>
		</tr>
	</tbody>
</table>

The principal namespace qualifiers for term URIs in this document are

- **dcterms:** The DCMI type vocabulary documented at
  http://dublincore.org/documents/dcmi-terms

- **dwc:** The Darwin Core vocabulary proposed at
  http://rs.tdwg.org/dwc/index.htm

- **Iptc4ampExt** Geographic extensions to IPTC with namespace
  http://iptc.org/std/Iptc4xmpExt/2008-02-29/ documented in
  http://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-201007_1.pdf

- **ac:** Terms defined in the normative documentation and not derived
  from other controlled vocabularies. The proposed namespace is
  http://rs.tdwg.org/ac/terms.

- **xmp:** The Adobe XMP vocabularies with namespace
  http://ns.adobe.com/xap/1.0/ documented in Section 8.4 of
  http://wwwimages.adobe.com/www.adobe.com/content/dam/Adobe/en/devnet/xmp/pdfs/XMPSpecificationPart1.pdf

- **xmpRights:** The Adobe XMP rights vocabulary with namespace at
  http://ns.adobe.com/xap/1.0/rights documented in Section 8.5 of
  http://www.images.adobe.com/www.adobe.com/content/dam/Adobe/en/devnet/xmp/pdfs/XMPSpecificationPart1.pdf


## 4 Motivation and Rationale

Many valuable multimedia resources exist that have no information stored
in databases. Some may have a web presence and others not. Even those
available online may not be adequately discoverable by search engines,
or may be lost in the noise of images from unreliable sources. A brief
descriptive record as defined by the Audubon Core standard can act as
the “business card” for a multimedia resource, providing enough
information to identify and locate media resources by researchers,
aggregators, decision makers, educators, or the general public.

The standard enables the aggregation of multimedia resource descriptions
from many sources and facilitates resource discovery, including
establishing relationships among multimedia resources in several
locations. AC records can also be used as an aid for multimedia
resources management processes, allowing an institution to take a step
back and see which collections are most in need of conservation or would
benefit from a higher priority for item-level cataloguing.

Among important uses identified by the Task Group, which are facilitated
by the metadata, are:

1.  Discovery;

2.  Evaluation of fitness-for-use prior to fetching a resource
    (especially relevant for off-line resources);

3.  Use of metadata records as potential taxon occurrence evidence, or
    other biological inferences such as evidence for species
    interactions, habitats, and phenotypic variation;

4.  Identification aids;

5.  Easing the burden of multimedia resource providers and producers to
    gather and serve resources contributed by a wide variety of
    producers and custodians, particularly those with little or no IT
    expertise or support.

To ensure that the barriers to use are as low as possible, only four
properties of an Audubon Core record are considered to be mandatory:

1.  Identifier (dcterms:identifier): An arbitrary code that is unique
    for the resource, with the resource being either a provider,
    collection, or media item. Whereas the identifier must be globally
    unique for providers and collections (e. g. a URI), identifiers for
    media items may be unique only within the context of a collection or
    provider. In fact the standard strongly recommends but does not
    require an Identifier for media items, though it does so for a
    provider or collection.

2.  Type (dcterms:type): Any dcmi type term from
    http://dublincore.org/documents/dcmi-type-vocabulary/ may be used.
    Recommended terms are Collection, StillImage, Sound, MovingImage,
    InteractiveResource, and Text.

3.  Metadata Language (ac:MetadataLanguage): Language of description and
    other metadata (but not necessarily of the image itself)

4.  Copyright Statement (dcterms:rights): Information about rights held
    in and over the resource. A full-text, readable copyright statement,
    as required by the national legislation of the copyright holder. On
    collections, this applies to all contained objects, unless the
    object itself has a different statement. When available, it is also
    recommended to provide the Copyright Owner using xmpRights:Owner

In addition it is strongly recommended to provide a concise title of the
resource, using dcterms:title


## 5 Existing Standards

The Audubon Core intends to provide metadata that describe either media
resources themselves or collections of them. There are several
well-known or newly emerging standards that address these concerns, so
one may ask: why not simply use them? In fact, AC does exactly that in
about half of its 80 elements, almost all of which are optional. Indeed,
as shown above, most of the mandatory terms come from external
controlled vocabularies. However, all existing controlled vocabularies,
most notably the widely used Dublin Core, present very few opportunities
to provide media resource content metadata that is specifically
biologically relevant. Use of the Dublin Core alone would make it
difficult to do media resource discovery with high precision. Thus, one
consequence of using Dublin Core alone would be that queries will not be
selective enough. By contrast the Darwin Core TDWG standard <sup id="cit-8">[\[8\]](#fn-8)</sup> has
more support for some such concerns, but little about important
intellectual property rights issues, or ways to express relationships
between alternate versions of media resources (e.g. different resolution
versions). In turn, neither of these controlled vocabularies has
mechanisms for capturing technical metadata, such as EXIF, which the
imaging systems themselves, or metadata embedding tools, such as Adobe
Photoshop(tm) and the GIMP open source image editor, can insert into
media files and streams. To address this, and in furtherance of the
above goals, the Audubon Core should be regarded as a synthesis of DC,
DwC, and, where those are inadequate, some forward looking metadata
standards that the camera manufacturers are presently planning to
support within the cameras themselves, much as they now use EXIF <sup id="cit-9">[\[9\]](#fn-9)</sup>.
Where any of these standards suffice, AC metadata terms and definitions
are those of such standards. In some instances, we find that none of
these address concerns that our experience suggests are held by a wide
variety of image contributors, especially those with limited access to
sophisticated IT staff or to Digital Librarians. The AC schema might be
regarded as an extension to the union of small subsets of several
accepted standards (together with a framework to insure that use of
metadata from these standards can be understood by people and machines
as referring to the same resource). Put another way, much of AC may be
viewed as a wrapper around DwC, DC, XMP, and IPTC <sup id="cit-10">[\[10\]](#fn-10)</sup>.

Since the overwhelming portion of the AC metadata fields are optional, a
resource provider that can already serve Dublin Core metadata, could
essentially serve little else but that, plus a suitable globally unique
identifier to tie all the metadata to the same object. Similarly, a
provider describing image content entirely with Darwin Core terms might
have little more to do. However, both such providers would find that
value-added services such as metadata-indexers and caching aggregators
and would be less likely to keep references to their media resources and
metadata than if they had richer metadata. This gives a clear strategy
for providers to increase the utility of their multimedia resources with
little or no impact on their IT cyberinfrastructure services. They may
need only to update mappings between their internal field names and the
metadata terms specified by AC, as personnel become available to do so.
As more resources become available to record additional metadata, and as
community annotation mechanisms arise to support this, they can add the
additional metadata at a pace determined by their own resources. If
harvesters of the metadata monitor the (optional) Metadata Date property
(xmp:MetadataDate), the updated metadata can automatically be pulled by
those value-added services, and more queries will return the provider's
metadata and references to its media resources.

## 6 Common Concerns with Other Biodiversity Information Standards

The Audubon Core regards Collections of Multimedia Resources themselves
as a kind of Resource. Many types of Collections are describable in the
pending TDWG Natural History Collections (NCD) proposed standard. If a
provider wishes only to provide for discovery of a multimedia Collection
without regard to discovery of and access to its contents (other than
sub Collections), it will often be immaterial whether NCD or AC
metadata, or both, are served. This is all the more so if the NCD
CollectionIdentifier and the Audubon Core Identifier have the same
value. While Audubon Core Collection types are richer than NCD types, it
is an open question whether Audubon Core's variety in this case is
useful.

There is substantial overlap with use of Darwin Core terms, notably with
respect to taxonomic, geographic, and temporal coverage of the data
being described by the metadata record. We use DwC terms for most of
those metadata and the entirety of the Darwin Core geolocation vocabulary
are included by reference. GPS point locations increasingly common in
image data created by cameras is easily mapped to the 'verbatim'
locality terms of Darwin Core.

## 7 Concerns Not Emphasized in Other Biodiversity Information Standards

Some of the concerns mentioned here are also those of bibliographic
metadata such as the Dublin Core. These are, however, not explicitly of
detailed concern in existing TDWG biodiversity standards, and some are
not adequately addressed by DC. Some such concerns are below.

**Size**: Individual multimedia resources such as images, and especially
video and sound are very large compared to specimen records, observation
data, or species descriptions. The main consequence of this is that
multimedia metadata must support use cases for which humans or software
agents can, without fetching the resource, attempt to assess the fitness
of the underlying media resource for the desired use, typically by use
of a search based on a fine-grained controlled vocabulary. However,
without hit-and-miss natural language searches, it is not possible, even
using both DC and DwC, for a metadata provider to answer a request of
the form "Supply me with sizes and URL access points for still images of
*Dictyophora indusiata* and which have Spanish metatdata available.

**Intellectual Property Rights**: DwC describes physical objects, whose
ownership is generally governed by property laws not considered part of
the Intellectual Property Rights corpus of law. Some impending standards
about scientific literature address these, but rarely are publication
reproduction permission issues as varied as for multimedia, which have a
history of being treated as creative works of art, not necessarily as
facts.

**Provenance**: For any scientific data, it is clearly important to know
how and when the data may have been changed from its original gathering.
This is particularly important for media, which are commonly edited for
one or another purpose. If carelessly done, this may destroy some if the
modified object's utility. No TDWG standards or proposed standards seem
very robust about provenance, including Audubon Core, which provides
only the Derived From property in order to provide a reference to
another resource. This is somewhat akin to the NCD DerivedCollection
term, which identifies a Collection record as having been produced by a
query to another Collection. However, that apparently does not identify
the source collection or the query. A future version of Audubon Core
will add more provenance terms.


## 8 Multimedia Resource Descriptions

The term Multimedia Resources encompasses a wide variety of objects of
interest to biologists and the communities with whom they interact for
research, education, and public service. Some instances of multimedia
are familiar. These include:

  - Still images from cameras, scanners, or medical and industrial
    imaging devices

  - Movies with or without sound

  - Audio recordings

In some of the above cases, these resources may exist in electronic or
non-electronic form or both. The electronic form may be analog or
digital, the latter being more amenable to storage and exchange with
computers. The digital form may have been born digital, i.e. originally
captured as a digital object, or it may have been created from a
non-digital object. As with biological specimen records, publications,
field notes, experimental data and other artifacts of the practice of
science, there is a large quantity of such material that has not yet
been digitized, yet which may be available, albeit with greater expense
and inconvenience than digital resources. These analog (including paper)
resources still require descriptive metadata to promote discovery and to
ascertain fitness-for-use. At least as important, some of the metadata
is itself of scientific and educational use even if the object is not
conveniently accessible. Evidence for georeferenced taxon occurrence is
one such use.

Audubon Core metadata also can describe resources less often thought of
as multimedia objects. These include:

  - Interactive software applications, either on the web or available
    for stand-alone use

  - Taxonomic identification keys

  - Collections of multimedia resources

  - Web sites not otherwise falling into one of the above categories


## 9 Audubon Core Records

The normative Audubon Core metadata record specification is independent
of the way in which those records are rendered into electronic form.
MRTG intends to publish specifications for such rendering represented
in, represented in XML constrained by an XML-Schema, and represented in
plain text as comma separated values (CSV). A simple RDF form at
http://terms.gbif.org/wiki/Audubon_Core_Term_List_RDF_Version is
generated programmatically from the normative document. MRTG intends to
publish more expressive forms of RDF.

The language of the normative Audubon Core specification is English, but
this in no way constrains applications from using labels or content of
the metadata in local languages. Because its language is English, each
metadata item in the normative document has an English label (which
might, for example be part of a user interface), but these, too, are not
required to be used by applications, although their use is strongly
encouraged, at least in documentation.

As mentioned earlier, an Audubon Core metadata record is a set of terms
describing the underlying multimedia resource that the record describes.
Each term is identified by a Uniform Resource Identifier (URI). These
are URIs of the attribute, not of the underlying resource, and they
simply specify which term is being provided. There are many URI schemes,
some of which have been registered with the Internet Assigned Names
Authority (IANA). All Audubon Core term URIs, conform to the http URI
Scheme. This is chosen because this widely used URI scheme uses the
familiar internet URL syntax as its URI syntax. But this familiarity
gives rise to a common misconception, namely that pasting the URI into a
browser URL line, or providing it to some other application that
respects the http protocol, should result in the application returning
some information about the object identified by the URI. Such behavior
is usually called resolution (or, more technically, resolution and
dereferencing) of the URI and is in no way guaranteed for Audubon Core
term URIs. Where possible, we in fact try to make http URIs be
resolvable, with the information returned being documentation for how
the metadata attribute identified by that URI is defined or use. To
reiterate: for Audubon Core term URIs, any such resolution will never
contain information about the underlying multimedia resource being
described. For this reason, few human-centric Audubon Core applications
should ever present the URIs to users, nor use them as linking
mechanisms. (One possible exception is an application for assigning
metadata to multimedia resources, where such a use may provide a
thesaurus entry aiding the user in the semantics of the metadata
property. However, the incidental nature of the resolution, and its lack
of guaranteed long term persistence, makes even this approach one that
should be considered with extreme caution.) Finally, note that some
external controlled vocabularies are defined in PDF or other documents
that do not have URL links directly to each defined term. In these
cases, any resolution available from the normative document may only
link to the beginning of the document, leaving it necessary to search in
the document for the referenced definition.

Associated to each Audubon Core property is its value. The datatype of
this value is also specified in the normative document. Datatypes can
include free text, specific literals taken from a controlled vocabulary
specified in the normative document, or a number of other datatypes
specified and described in the normative document. In the case of a
controlled vocabulary, it is important to note that whatever an
application may present in a user interface, any Audubon Core metadata
interchange should use the literals from a specified controlled
vocabulary when one is specified, even if the record is declared to be a
record in a different language than that of the controlled term. An
important example is the Type metadata field, which is recommended to
come from the corresponding vocabulary from Dublin Core, augmented by
some recommended in the normative document. (We also add to that an
optional field Subtype.) Similarly, agents answering Audubon Core
metadata queries MUST be able to consume and respond to queries framed
with the controlled vocabulary. Nothing in the normative document
prevents an Audubon Core data provider from asserting it has no records
with a given controlled term, nor from internally mapping between a
controlled vocabulary and its internal attributes, whose names may well
be in a language other than English. Only a small number of Audubon Core
properties take values in a specific, English-based controlled
vocabulary. This will become relevant only for metadata interchange. Of
the mandatory terms, only Type has any such requirements.

An Audubon Core record consists minimally of the four mandatory fields
(Identifier, Type, Metadata Language, and Copyright Statement).

In some cases, some metadata terms are necessarily related to others
(e.g. various versions of an image must be associated the "main"
version). However, spreadsheets and other flat sources of contributor
metadata are regarded as particularly important, and in many of these it
is difficult to represent such structural relationships. Consequently an
Audubon Core record is itself mainly flat, the exception being the
object of a property named *hasServiceAccessPoint*. This object itself
has further properties that describe how to fetch the actual media
described by the AC record. One consequence of this is that, for some
purposes, a metadata Provider might have to make several metadata
records available about the same underlying resource, because the
representation-neutral Audubon Core specification does not provide for
“subproperties” on its properties, or for relations in most cases. An
important case surrounds multilingual metadata. Because each metadata
record is in a fixed language specified by the Metadata Language
property (this is the language of the record, not the multimedia
resource, in case it should have one), a Provider might have to offer
several metadata records about the same multimedia resource. The values
of the four required terms must be provided in every metadata record,
even if repeated in other metadata records describing the same resource.
At the date of this writing, the normative document does not provide a
mechanism for identifying a metadata record that might be overarching,
in the sense that its optional terms may be regarded as defaults for any
not specified in other records about the same resource. This point is
under discussion on the MRTG Wiki.

Many items may be repeated in an Audubon Core record, but some may not,
as indicated in the normative document. For example the Modified item
corresponds to a date at which the media resource was modified and may
be repeated to reflect the history of the resource. By contrast, Date
Available is a single date or a single range of dates at which the
underlying resource became, or will become, available.


## 10 Implementation and Compliance

Audubon Core is defined in a way that is as representation-neutral as
possible. It provides natural language definitions of classes,
properties and instances that are identified by URIs and it makes
recommendations on the use and content of properties from other
vocabularies.

The URIs defined here may be used across a number of technologies, such
as namespaces in XML Schema-valid table documents, RDF, and column
headings in comma delimited text files.

This approach facilitates:

  - Embedding of Audubon Core data within other standards such as
    descriptions of specimens or literature.

  - The extension of Audubon Core records with other data types such as
    the extensive geographic controlled vocabularies of the Open
    Geospatial Consortium (OGC)

  - Cross walking between technologies such as a Comma Separated Value
    file, an RDF graph, an XML document and a JSON object.

The Audubon Core representation-neutral normative standard itself does
not provide an off-the-shelf, self validating exchange format. Multiple
such exchange formats meeting different requirements can be defined and
this standard allows mapping between them.


## 11 Further Information

  - Joint TDWG-GBIF MRTG Charter
    http://tdwg.org/charters/article/view/448/36


  - Discussion of the Audubon Core takes place at
    https://github.com/tdwg/ac/issues

  - Register for the mailing list tdwg-content@lists.tdwg.org at http://lists.tdwg.org/mailman/listinfo/tdwg-content. This email list tracks all discussion about the content of TDWG standards.


## 12 Appendix I: Glossary

<table>
  <tbody>
    <tr class="even">
      <td>DC</td>
      <td>Dublin Core. Metadata element set that is a standard for cross-domain information  resource discovery. http://dublincore.org/documents/dcmi-terms/</td>
    </tr>
    <tr class="odd">
      <td>DCMI</td>
      <td>Dublin Core Metadata Initiative. The organization engaged in developing Dublin Core metadata standard. http://dublincore.org/</td>
    </tr>
    <tr class="even">
      <td>DwC</td>
      <td>The Darwin Core is a TDWG standard for representation of specimen records. It has been in wide use for several years in a number of nonstandard, sometimes inconsistent, versions. A recently adopted standard version is at http://rs.tdwg.org/dwc/index.htm.</td>
    </tr>
    <tr class="odd">
      <td>EOL</td>
      <td>Encyclopedia of Life. Information about many species. http://eol.org</td>
    </tr>
    <tr class="even">
      <td>EXIF</td>
      <td>A widely used tagging format for digital image metadata that is often embedded in the image files, particularly by modern digital cameras. Many image rendering applications can read and display EXIF data. See http://en.wikipedia.org/wiki/Exchangeable_image_file_format for a history and description.</td>
    </tr>
    <tr class="odd">
      <td>GBIF</td>
      <td>Global Biodiversity Information Facility. Interoperable network of biodiversity databases and information technology tools. http://www.gbif.org/</td>
    </tr>
    <tr class="even">
      <td>IANA</td>
      <td>Internet Assigned Names Authority. Specifies the forms of, and registers instances of, names of various protocols in use on the internet. http://www.iana.org. See especially information on the <em>IANA http URI scheme</em> at http://en.wikipedia.org/wiki/URI_scheme</td>
    </tr>
    <tr class="odd">
      <td>IPTC</td>
      <td>IPTC is a mature standard from the International Press and Telecommunications Council. Its Intellectual Property Rights support finer-grained controlled vocabularies than DC, providing better machine processing for discovery and fitness-for-use. The current version is a vocabulary for XMP. http://www.iptc.org</td>
    </tr>
    <tr class="even">
      <td>JSON</td>
      <td>JavaScript Object Notation. Lightweight data-interchange format. http://www.json.org/</td>
    </tr>
    <tr class="odd">
      <td>Morphbank</td>
      <td>A specimen image repository http://www.morphbank.net/</td>
    </tr>
    <tr class="even">
      <td>MWG</td>
      <td>The Metadata Working Group is an industry consortium (Adobe, Apple, Canon, Microsoft, Nokia, and Sony) organized to specify how to exploit the Adobe Extensible Metadata Platform, XMP (http://en.wikipedia.org/wiki/Extensible_Metadata_Platform), for embedding metadata into common image file formats in several widely used controlled vocabularies. Although MWG's thrust is mainly toward consumer applications, over two dozen open source and commercial software products and platforms support XMP and Adobe has placed a Developers' Toolkit under an open source license. http://www.metadataworkinggroup.org/</td>
    </tr>
    <tr class="odd">
      <td>NBII</td>
      <td>The former U.S. National Biological Information Infrastructure. Its image library, the Library of Images From the Environment (LIFE), was at http://images.nbii.gov/ or http://life.nbii.gov/. If LIFE is reconstituted in any form, there might be a link there.</td>
    </tr>
    <tr class="even">
      <td>NCD</td>
      <td>Natural Collections Description is a draft data standard designed to describe collections of physical objects such as specimens. It can accommodate collections of media objects, but cannot relate them to descriptions of the objects themselves. http://www.tdwg.org/activities/ncd/</td>
    </tr>
    <tr class="odd">
      <td>OGC</td>
      <td>Open Geospatial Consortium. Provides standards for geospatial data representation and exchange. http://www.opengeospatial.org/</td>
    </tr>
    <tr class="even">
      <td>RDF</td>
      <td>Resource Description Framework. Lightweight ontology system to support knowledge exchange online. http://en.wikipedia.org/wiki/Resource_Description_Framework</td>
    </tr>
    <tr class="odd">
      <td>TDWG</td>
      <td>Taxonomic Databases Working Group. Now known as the Biodiversity Information Standards (TDWG), it is an international working group that develops standards and protocols for sharing biodiversity data. http://www.tdwg.org/</td>
    </tr>
    <tr class="even">
      <td>URI</td>
      <td>Unique Resource Identifier. Generic term for linking web resources including URLs. http://en.wikipedia.org/wiki/Uniform_Resource_Identifier</td>
    </tr>
    <tr class="odd">
      <td>XML</td>
      <td>Extensible Markup Language. A simple flexible text format playing an increasingly important role in the exchange of a wide variety of data on the Web. http://www.w3.org/XML/</td>
    </tr>
    <tr class="even">
      <td>XMP</td>
      <td>Adobe Extensible Metadata Platform (XMP) is a framework for embedding metadata into media files. Adobe provides a BSD-licensed open-source XMP developer’s toolkit which includes documentation about how to represent metadata in XMP. The XMP specification itself is licensed by Adobe under a &quot;Public Patent License&quot; http://wwwimages.adobe.com/www.adobe.com/content/dam/Adobe/en/devnet/xmp/pdfs/xmp_public_patent_license.pdf by which Adobe grants everyone the right to make XMP-compliant components of their applications, but it reserves the right to withdraw the license in case such a compliant component infringes &quot;Essential Claims&quot; of any patent. See http://www.adobe.com/devnet/xmp/ for download information. See Also MWG in this table.</td>
    </tr>
  </tbody>
</table>


## 13 Appendix II: Audubon Core Development History

The Audubon Core Multimedia Resources Metadata Schema (Audubon Core) standard is the culmination of work on multimedia
resource descriptions carried out by Key to Nature, the NBII Digital
Image Library, Morphbank, and others, together with input from a number
of other stakeholder communities including Encyclopedia of Life (EOL),
the Biodiversity Heritage Library (BHL) and the University of
Massachusetts-Boston. The Global Biodiversity Information Facility
(GBIF) commissioned the ‘Multimedia Resources Task Group (MRTG)’ in
March 2008 and the group was approved in December 2009 by Biodiversity
Information Standards (TDWG) as the ‘Joint GBIF-TDWG Task Group on
Multimedia Resources in Biodiversity’.

Participants in drafting the schema (in alphabetical order)

  - Mr. Mihail-Constantin Carausu, Danish Biodiversity Information
    Facility (DanBIF), Copenhagen, Denmark

  - Dr. Vishwas Chavan, Global Biodiversity Information Facility,
    Copenhagen, Denmark

  - Mr. Chris Freeland, Missouri Botanical Garden, St. Louis, USA

  - Dr. Gregor Hagedorn, JKI, Federal Research Institute for Cultivated
    Plants, Berlin, Germany

  - Prof. Robert A. Morris, University of Massachusetts at Boston, USA

  - Dr. Dimitry Mozzherin, Encyclopedia of Life, Woods Hole, USA

  - Dr Annette Olson, American Association for the Advancement of
    Science

  - Prof. Greg Riccardi, Florida State University, Tallahassee, USA

  - Dr. Éamonn Ó Tuama, Global Biodiversity Information Facility,
    Copenhagen, Denmark

The standard was developed by the Joint Task Group to fit with the suite of standards-based data management resources being developed by GBIF.

Funding was provided by the Global Biodiversity Information Facility.

Grateful thanks go to Woods Hole Marine Biological Laboratory and the
Encyclopedia of Life for hosting one of the meetings. This document,
including some narrative is adapted from a corresponding document
produced by the TDWG Natural Collections Descriptions (NCD) task group.


### 13.1 Timeline

2006, November TDWG Image Interest Group initiated

2008, March GBIF commissions Multimedia Resources Task Group (MRTG)

2008, June GBIF Multimedia Resources Task Group met in Copenhagen,
Denmark

2008, August GBIF Multimedia Resources Task Group meeting in Woods Hole,
USA

2008, October TDWG Image Interest Group met in Fremantle, Australia at
the ‘TDWG Annual Conference 2008’

2008, December Joint GBIF-TDWG Task Group on Multimedia Resources in
Biodiversity commissioned

2009, February GBIF Multimedia Resources Task Group met in Copenhagen,
Denmark to refine the metadata schema

2009, March GBIF – TDWG Multimedia Resources Metadata Schema (MRTG) ver.
0.4414 drafted and opened for informal comment, evolving through v 0.9

2010, February Schema v 0.9 submitted to TDWG for internal Review

2010, July TDWG Internal Review 1 completed

2010, November v1.0 submitted to TDWG Executive committee with response
to Internal Review 1. Proposed Standard renamed Audubon Core Multimedia
Resources Metadata Schema (AC).

2011, June Response to Internal Review 2 under way.

2011, September Responses to Internal Review 2 and 3 completed and
submitted to TDWG Executive Committee

2011, November Prepared responses to “Review g” and “Review h” and to
some comments of the Review Manager, Steve Baskauf. Prepare submission
for permission to have public comment.

January-November 2012 Further preparation for submission for permission
to have public comment


### 13.2 Document revision history

0.7v1

Harmonized document to the fact that Subtype is optional in normative
v0.7

Fix mismatched parentheses, extra spaces, missing spaces, etc.

ACv1.0 docv1.0

Harmonized to v1.0: replace “MRTG” with “Audubon Core” where used as
name of schema. Correct minor typos. Add “dcterms” as prefix.

ACv1.0 docv1.0

Further replacement of MRTG with “Audubon Core” or “AC”.

AC v1.0 docv 1.2

Address Internal Review 2 comments

Fix mismatched parentheses, extra spaces, missing spaces, etc.

AC v1.0 docv1.3

Remove requirement to have Copyright Owner provided.

AC v1.0 docv1.4

Clean up citations of six mandatory elements instead of five.

AC v1.0 docv1.5

Replace “keytonature.eu” with “species-id.net” to reflect move of
normative wiki. Remove some unused Glossary terms. Update docv to 1.5

AC v1.0docv1.6

Remove dcterms:title from mandatory list. Add description of it as
strongly recommended. Add mention of xmpRights:Owner in Copyright
Statement item in the mandatory list. Change to “four” the references of
“five” mandatory elements or remove the count altogether where text
becomes unambiguous. Mention acterms namespace. Correct Iptc4xmpExt
namespace to http://iptc.org/std/Iptc4xmpExt/2008-02-29/. Update docv to
1.6.

AC v1docv1.7

Clarify relation of this document to the normative docs. Set major major
text to left-align, unjustified.

AC v1.0docv1.8

Remove mention of crosswalks since no longer in normative termlist.

On p. 5 force URL of DwC terms into footnote.

Improved language about use of literals with dcterms.

AC v1.0docv1.91

Various minor grammar and punctuation corrections.

Reconciliation to current normative docs.

AC v1.0docv1.92

More minor grammar fixes.

AC v1.0docv1.93

Fixed inconsistent internal version references to current version. No
substantive or grammatical changes. Note that v1.92 was submitted to
TDWG executive committee with request for permission to hold public
review.

AC v1.0docv1.94

Change references from species-id wiki to gbif terms wiki. Adjust Fig 1

AC v1.0docv1.95

Correct “hasAccentPoint” to “hasAcccessPoint”. Remove text suggesting
this is a draft


## 14 Endnotes

<sup id="fn-1">[\[1\]](#cit-1)</sup>  http://terms.gbif.org/Audubon_Core

<sup id="fn-2">[\[2\]](#cit-2)</sup>  http://terms.gbif.org/Audubon_Core_Term_List

<sup id="fn-3">[\[3\]](#cit-3)</sup> http://www.w3.org/RDF/

<sup id="fn-4">[\[4\]](#cit-4)</sup> http://www.w3.org/standards/xml/schema

<sup id="fn-5">[\[5\]](#cit-5)</sup> http://en.wikipedia.org/wiki/Comma-separated_values

<sup id="fn-6">[\[6\]](#cit-6)</sup> http://www.tdwg.org/fileadmin/subgroups/ncd/NCD_090.doc

<sup id="fn-7">[\[7\]](#cit-7)</sup> http://rs.tdwg.org/dwc/terms/

<sup id="fn-8">[\[8\]](#cit-8)</sup> http://rs.tdwg.org/dwc/index.htm

<sup id="fn-9">[\[9\]](#cit-9)</sup> The Metadata Working Group (MWG,
    http://www.metadataworkinggroup.org/) is an industry consortium
    (Adobe, Apple, Canon, Microsoft, Nokia, and Sony) organized to
    specify how to exploit the Adobe Extensible Metadata Platform, XMP
    (http://en.wikipedia.org/wiki/Extensible_Metadata_Platform) for
    embedding into common image file formats metadata in several widely
    used controlled vocabularies. Although MWG's thrust is mainly toward
    consumer applications, over two dozen open source and commercial
    software products and platforms support XMP and Adobe has placed a
    Developers' Toolkit under an open source license. Along with
    proposals for standard serializations of the representation-neutral
    Audubon Core schema, MRTG intends to propose a TDWG Best Practice
    for embedding such serializations in multimedia files using XMP.

<sup id="fn-10">[\[10\]](#cit-10)</sup> IPTC is a mature standard from the International Press and
    Telecommunications Council (http://www.iptc.org). Its Intellectual
    Property Rights supports finer grained controlled vocabularies than
    DC, providing better machine processing for discovery and
    fitness-for-use.

-----------------
This document is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). ![http://creativecommons.org/licenses/by/4.0/](https://licensebuttons.net/l/by/4.0/88x31.png).

Copyright 2013 - Biodiversity Information Standards - TDWG - [Contact Us](http://www.tdwg.org/about-tdwg/contact-us/)
