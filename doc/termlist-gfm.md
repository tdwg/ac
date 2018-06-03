<div class="mw-cookiewarning-container">

<div class="mw-cookiewarning-text">

<span>Cookies help us deliver our services. By using our services, you
agree to our use of cookies.</span>

</div>

</div>

<div id="mw-page-base" class="noprint">

</div>

<div id="mw-head-base" class="noprint">

</div>

<div id="content" class="mw-body" data-role="main">

<span id="top"></span>

<div class="mw-indicators">

</div>

# Audubon Core Term List

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

For introductory material, see the normative **[Audubon Core
Structure](/wiki/Audubon_Core_Structure "Audubon Core Structure")** and
the non-normative introductory **[Audubon
Core](/wiki/Audubon_Core "Audubon Core")**
documents.

## <span id="Metadata_structure" class="mw-headline">Metadata structure</span>

**Date:** 23 October, 2013.

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
may not be changed without due process. A second version of Audubon
Core, [Audubon Core
Development](/wiki/Audubon_Core_Development "Audubon Core Development"),
will reflect the ongoing documentation changes and draft enhancements.

**Contributors:** Robert A. Morris, Vijay Barve, Mihail Carausu, Vishwas
Chavan, José Cuadra, Chris Freeland, Gregor Hagedorn, Patrick Leary,
Dimitry Mozzherin, Annette Olson, Greg Riccardi, Ivan Teage

**Legal:** This document is governed by the standard legal, copyright,
licensing provisions and disclaimers issued by the Taxonomic Databases
Working Group.

**Part of TDWG Standard:** <http://www.tdwg.org/standards/638/>.

**Document Status:** This document is a [TDWG Type 1 Normative
Document](http://www.tdwg.org/fileadmin/tdwg_std_drafts/tdwg_standards_documentation_specification.html#a_3).

Release 1.0 of this document has wiki revision 10759 with a permalink
<http://terms.gbif.org/w/index.php?oldid=10759>.  
This document has wiki revision ID 36898 with a permalink
<http://terms.gbif.org/w/index.php?oldid=36898>.



<div id="toc" class="toc">

<div id="toctitle">

## Contents

</div>

  - [<span class="tocnumber">1</span> <span class="toctext">Metadata
    structure</span>](#Metadata_structure)
  - [<span class="tocnumber">2</span> <span class="toctext">Borrowed
    Vocabulary</span>](#Borrowed_Vocabulary)
  - [<span class="tocnumber">3</span> <span class="toctext">Namespaces,
    Prefixes and Term
    Names</span>](#Namespaces.2C_Prefixes_and_Term_Names)
  - [<span class="tocnumber">4</span>
    <span class="toctext">Layers</span>](#Layers)
  - [<span class="tocnumber">5</span> <span class="toctext">Literal- vs.
    URI-valued Terms</span>](#Literal-_vs._URI-valued_Terms)
  - [<span class="tocnumber">6</span> <span class="toctext">Vocabulary
    Indices</span>](#Vocabulary_Indices)
      - [<span class="tocnumber">6.1</span> <span class="toctext">Index
        By Term Name</span>](#Index_By_Term_Name)
      - [<span class="tocnumber">6.2</span> <span class="toctext">Index
        By Label</span>](#Index_By_Label)
  - [<span class="tocnumber">7</span>
    <span class="toctext">Vocabularies</span>](#Vocabularies)
      - [<span class="tocnumber">7.1</span>
        <span class="toctext">Management
        Vocabulary</span>](#Management_Vocabulary)
      - [<span class="tocnumber">7.2</span>
        <span class="toctext">Attribution
        Vocabulary</span>](#Attribution_Vocabulary)
      - [<span class="tocnumber">7.3</span> <span class="toctext">Agents
        Vocabulary</span>](#Agents_Vocabulary)
      - [<span class="tocnumber">7.4</span>
        <span class="toctext">Content Coverage
        Vocabulary</span>](#Content_Coverage_Vocabulary)
      - [<span class="tocnumber">7.5</span>
        <span class="toctext">Geography
        Vocabulary</span>](#Geography_Vocabulary)
      - [<span class="tocnumber">7.6</span>
        <span class="toctext">Temporal Coverage
        Vocabulary</span>](#Temporal_Coverage_Vocabulary)
      - [<span class="tocnumber">7.7</span>
        <span class="toctext">Taxonomic Coverage
        Vocabulary</span>](#Taxonomic_Coverage_Vocabulary)
      - [<span class="tocnumber">7.8</span>
        <span class="toctext">Resource Creation
        Vocabulary</span>](#Resource_Creation_Vocabulary)
      - [<span class="tocnumber">7.9</span>
        <span class="toctext">Related Resources
        Vocabulary</span>](#Related_Resources_Vocabulary)
      - [<span class="tocnumber">7.10</span>
        <span class="toctext">Service Access Point
        Vocabulary</span>](#Service_Access_Point_Vocabulary)
  - [<span class="tocnumber">8</span>
    <span class="toctext">References</span>](#References)

</div>




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
different
resolutions).



## <span id="Borrowed_Vocabulary" class="mw-headline">Borrowed Vocabulary</span>

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
those
organizations.



## <span id="Namespaces.2C_Prefixes_and_Term_Names" class="mw-headline">Namespaces, Prefixes and Term Names</span>

The namespace of terms borrowed from other vocabularies is that of the
original. The namespace of de novo AC terms is
http://rs.tdwg.org/ac/terms/. In the table of terms, each term entry has
a row with the term name. This term name is generally an "unqualified
name" preceded by a widely accepted prefix designating an abbreviation
for the namespace It is recommended that implementers who need a
namespace prefix for the AC namespace use "ac". In this web document,
hovering over a term in the **[Index By Term
Name](#Index_By_Term_Name)** list below will reveal a complete URL that
can be used in other web documents to link to *this* document's
treatment of that term, even if it is from a borrowed vocabulary. It is
very important to note that some vocabularies, e.g those of the [Dublin
Core Metadata Initiative (DCMI)](http://dublincore.org/), provide
version of the same term in two different namespaces, one providing for
string values and one providing for URIs, even where that separation is
simply a recommendation, not a mandate. See this **[DCMI wiki
entry](http://wiki.dublincore.org/index.php/FAQ/DC_and_DCTERMS_Namespaces)**
on this topic. For vocabularies where such a practice is in place, we
often follow it and signal a reference in the Notes of our term
descriptions to the sister version of the term. An example is the pair
[dc:type](#dc:type) and [dcterms:type](#dcterms:type). When such a pair
allows repeated instances (e.g. as for [dc:source](#dc:source) and
[dcterms:source](#dcterms:source)), particular care may be required in
some implementations of AC, because some implementations may not provide
enough structure to clearly state the association between the members of
a pair in the case of multiple values of each. This is a special case of
the issue treated in the normative material on [Multiplicity and
Cardinality](/wiki/Audubon_Core_Structure#Multiplicity.2FCardinality "Audubon Core Structure").



## <span id="Layers" class="mw-headline">Layers</span>

The term set consists of two *Layers*, numbered *1* and *2*. The former
comprise the central terms, likely to be meaningful for most media, even
though only a few are mandatory. Implementers of AC representations
should provide for at least Layer 1 if possible, and application writers
should provide for robust treatment of Layer 1 terms, if only by
ignoring them. Layer 2 terms are more likely to be useful for particular
kinds of media or for applications requiring highly detailed resource
descriptions. Each term description below indicates the Layer to which
the term
belongs.



## <span id="Literal-_vs._URI-valued_Terms" class="mw-headline">Literal- vs. URI-valued Terms</span>

Some terms have two versions, one expecting a string literal value and
the other a URI. In these circumstances, the version expecting a string
is named with the suffix "Literal", e.g. ac:metadataLanguageLiteral. In
such cases, both forms may be provided, but care should be taken to
ensure that the uses reflect the same intent. In case of ambiguity, the
URI version prevails. All terms, including those whether or not with a
specific "Literal" suffix, specify in their definition whether the
required values are strings or
URIs.



## <span id="Vocabulary_Indices" class="mw-headline">Vocabulary Indices</span>

### <span id="Index_By_Term_Name" class="mw-headline">Index By Term Name</span>

(See also [Index By Label](#Index_By_Label))

**Management Vocabulary**

| [dcterms:identifier](#dcterms:identifier) | | [dc:type](#dc:type) | |
[dcterms:type](#dcterms:type) | |
[ac:subtypeLiteral](#ac:subtypeLiteral) | | [ac:subtype](#ac:subtype) |
| [dcterms:title](#dcterms:title) | |
[dcterms:modified](#dcterms:modified) | |
[xmp:MetadataDate](#xmp:MetadataDate) | |
[ac:metadataLanguageLiteral](#ac:metadataLanguageLiteral) | |
[ac:metadataLanguage](#ac:metadataLanguage) | |
[ac:providerManagedID](#ac:providerManagedID) | |
[xmp:Rating](#xmp:Rating) | | [ac:commenter](#ac:commenter) | |
[ac:commenterLiteral](#ac:commenterLiteral) | |
[ac:comments](#ac:comments) | | [ac:reviewer](#ac:reviewer) | |
[ac:reviewerLiteral](#ac:reviewerLiteral) | |
[ac:reviewerComments](#ac:reviewerComments) | |
[dcterms:available](#dcterms:available) | |
[ac:hasServiceAccessPoint](#ac:hasServiceAccessPoint) |

**Attribution Vocabulary**

| [dc:rights](#dc:rights) | | [dcterms:rights](#dcterms:rights) | |
[xmpRights:Owner](#xmpRights:Owner) | |
[xmpRights:UsageTerms](#xmpRights:UsageTerms) | |
[xmpRights:WebStatement](#xmpRights:WebStatement) | |
[ac:licenseLogoURL](#ac:licenseLogoURL) | |
[photoshop:Credit](#photoshop:Credit) | |
[ac:attributionLogoURL](#ac:attributionLogoURL) | |
[ac:attributionLinkURL](#ac:attributionLinkURL) | |
[ac:fundingAttribution](#ac:fundingAttribution) | |
[dc:source](#dc:source) | | [dcterms:source](#dcterms:source) |

**Agents Vocabulary**

| [dc:creator](#dc:creator) | | [dcterms:creator](#dcterms:creator) | |
[ac:providerLiteral](#ac:providerLiteral) | |
[ac:provider](#ac:provider) | |
[ac:metadataProviderLiteral](#ac:metadataProviderLiteral) | |
[ac:metadataProvider](#ac:metadataProvider) | |
[ac:metadataCreatorLiteral](#ac:metadataCreatorLiteral) | |
[ac:metadataCreator](#ac:metadataCreator) |

**Content Coverage Vocabulary**

| [dcterms:description](#dcterms:description) | |
[ac:caption](#ac:caption) | | [dc:language](#dc:language) | |
[dcterms:language](#dcterms:language) | |
[ac:physicalSetting](#ac:physicalSetting) | |
[Iptc4xmpExt:CVterm](#Iptc4xmpExt:CVterm) | |
[ac:subjectCategoryVocabulary](#ac:subjectCategoryVocabulary) | |
[ac:tag](#ac:tag) |

**Geography Vocabulary**

| [Iptc4xmpExt:LocationShown](#Iptc4xmpExt:LocationShown) | |
[Iptc4xmpExt:WorldRegion](#Iptc4xmpExt:WorldRegion) | |
[Iptc4xmpExt:CountryCode](#Iptc4xmpExt:CountryCode) | |
[Iptc4xmpExt:CountryName](#Iptc4xmpExt:CountryName) | |
[Iptc4xmpExt:ProvinceState](#Iptc4xmpExt:ProvinceState) | |
[Iptc4xmpExt:City](#Iptc4xmpExt:City) | |
[Iptc4xmpExt:Sublocation](#Iptc4xmpExt:Sublocation) |

**Temporal Coverage Vocabulary**

| [dcterms:temporal](#dcterms:temporal) | |
[xmp:CreateDate](#xmp:CreateDate) | | [ac:timeOfDay](#ac:timeOfDay) |

**Taxonomic Coverage Vocabulary**

| [ac:taxonCoverage](#ac:taxonCoverage) | |
[dwc:scientificName](#dwc:scientificName) | |
[dwc:identificationQualifier](#dwc:identificationQualifier) | |
[dwc:vernacularName](#dwc:vernacularName) | |
[dwc:nameAccordingTo](#dwc:nameAccordingTo) | |
[dwc:scientificNameID](#dwc:scientificNameID) | |
[ac:otherScientificName](#ac:otherScientificName) | |
[dwc:identifiedBy](#dwc:identifiedBy) | |
[dwc:dateIdentified](#dwc:dateIdentified) | |
[ac:taxonCount](#ac:taxonCount) | | [ac:subjectPart](#ac:subjectPart) |
| [dwc:sex](#dwc:sex) | | [dwc:lifeStage](#dwc:lifeStage) | |
[ac:subjectOrientation](#ac:subjectOrientation) |

**Resource Creation Vocabulary**

| [Iptc4xmpExt:LocationCreated](#Iptc4xmpExt:LocationCreated) | |
[ac:digitizationDate](#ac:digitizationDate) | |
[ac:captureDevice](#ac:captureDevice) | |
[ac:resourceCreationTechnique](#ac:resourceCreationTechnique) |

**Related Resources Vocabulary**

| [ac:IDofContainingCollection](#ac:IDofContainingCollection) | |
[ac:relatedResourceID](#ac:relatedResourceID) | |
[ac:providerID](#ac:providerID) | | [ac:derivedFrom](#ac:derivedFrom) |
| [ac:associatedSpecimenReference](#ac:associatedSpecimenReference) | |
[ac:associatedObservationReference](#ac:associatedObservationReference)
|

**Service Access Point Vocabulary**

| [ac:accessURI](#ac:accessURI) | | [dc:format](#dc:format) | |
[dcterms:format](#dcterms:format) | |
[ac:variantLiteral](#ac:variantLiteral) | | [ac:variant](#ac:variant) |
| [ac:variantDescription](#ac:variantDescription) | |
[ac:furtherInformationURL](#ac:furtherInformationURL) | |
[ac:licensingException](#ac:licensingException) | |
[ac:serviceExpectation](#ac:serviceExpectation) | |
[ac:hashFunction](#ac:hashFunction) | | [ac:hashValue](#ac:hashValue) |
| [exif:PixelXDimension](#exif:PixelXDimension) | |
[exif:PixelYDimension](#exif:PixelYDimension) |



### <span id="Index_By_Label" class="mw-headline">Index By Label</span>

(See also [Index By Term Name](#Index_By_Term_Name))

**Management Vocabulary**

| [Identifier](#Identifier) | | [Type](#Type) | | [Subtype](#Subtype) |
| [Title](#Title) | | [Modified](#Modified) | | [Metadata
Date](#Metadata_Date) | | [Metadata Language](#Metadata_Language) | |
[Provider-managed ID](#Provider-managed_ID) | | [Rating](#Rating) | |
[Commenter](#Commenter) | | [Comments](#Comments) | |
[Reviewer](#Reviewer) | | [Reviewer Comments](#Reviewer_Comments) | |
[Date Available](#Date_Available) | | [Service Access
Point](#Service_Access_Point) |

**Attribution Vocabulary** | [dc:rights](#dc:rights) | |
[dcterms:rights](#dcterms:rights) | | [Copyright
Statement](#Copyright_Statement) | | [Copyright Owner](#Copyright_Owner)
| | [Credit](#Credit) | | [License Terms](#License_Terms) | | [License
URL](#License_URL) | | [License Logo URL](#License_Logo_URL) | |
[Attribution Statement](#Attribution_Statement) | | [Attribution
URL](#Attribution_URL) | | [Attribution Link URL](#Attribution_Link_URL)
| | [Funding](#Funding) | | [Published Source](#Published_Source) |

**Agents Vocabulary**

| [Creator](#Creator) | | [Provider](#Provider) | | [Metadata
Provider](#Metadata_Provider) | | [Metadata Creator](#Metadata_Creator)
|

**Content Coverage Vocabulary**

| [Description](#Description) | | [Caption](#Caption) | |
[Language](#Language) | | [Physical Setting](#Physical_Setting) | |
[Subject Category](#Subject_Category) | | [Subject Category
Vocabulary](#Subject_Category_Vocabulary) | | [Tag](#Tag) |

**Geography Vocabulary**

| [Location Shown](#Location_Shown) | | [World Region](#World_Region) |
| [Country Code](#Country_Code) | | [Country Name](#Country_Name) | |
[Province or State](#Province_or_State) | | [City or Place
Name](#City_or_Place_Name) | | [Sublocation](#Sublocation) |

**Temporal Coverage Vocabulary**

| [Temporal Coverage](#Temporal_Coverage) | | [Original Date and
Time](#Original_Date_and_Time) | | [Time of Day](#Time_of_Day) |

**Taxonomic Coverage Vocabulary**

| [Taxon Coverage](#Taxon_Coverage) | | [Taxon Name](#Taxon_Name) | |
[Identification Qualifier](#Identification_Qualifier) | | [Common
Name](#Common_Name) | | [Name According To](#Name_According_To) | |
[Scientific Name ID](#Scientific_Name_ID) | | [Other Scientific
Name](#Other_Scientific_Name) | | [Identified By](#Identified_By) | |
[Date Identified](#Date_Identified) | | [Taxon Count](#Taxon_Count) | |
[Subject Part](#Subject_Part) | | [Subject Sex](#Subject_Sex) | |
[Subject Life Stage](#Subject_Life_Stage) | | [Subject
Orientation](#Subject_Orientation) |

**Resource Creation Vocabulary**

| [Location Created](#Location_Created) | | [Date and Time
Digitized](#Date_and_Time_Digitized) | | [Capture
Device](#Capture_Device) | | [Resource Creation
Technique](#Resource_Creation_Technique) |

**Related Resources Vocabulary**

| [ID of Containing Collection](#ID_of_Containing_Collection) | |
[Related Resource ID](#Related_Resource_ID) | | [Provider
ID](#Provider_ID) | | [Derived From](#Derived_From) | | [Associated
Specimen Reference](#Associated_Specimen_Reference) | | [Associated
Observation Reference](#Associated_Observation_Reference) |

**Service Access Point Vocabulary**

| [Access URI](#Access_URI) | | [Format](#Format) | |
[Variant](#Variant) | | [Variant Description](#Variant_Description) | |
[Further Information URL](#Further_Information_URL) | | [Licensing
Exception Statement](#Licensing_Exception_Statement) | | [Service
Expectation](#Service_Expectation) | | [Hash Function](#Hash_Function) |
| [Hash](#Hash) | | [Image Width](#Image_Width) | | [Image
Height](#Image_Height)
|



# <span id="Vocabularies" class="mw-headline">Vocabularies</span>

## <span id="Management_Vocabulary" class="mw-headline">Management Vocabulary</span>

| property | value |
|----------|-------|
| <a id="Identifier"></a>Term Name: | dcterms:identifier |
| Normative URI: | http://purl.org/dc/terms/identifier |
| Label | Identifier |
| | **Layer:** 1 — **Required:** Yes for media collections, No for media resources (but preferred if available). — **Repeatable:** Yes |
| Definition: | An arbitrary code that is unique for the resource, with the resource being either a provider, collection, or media item. |
| Defined by: | [dcterms:identifier](http://dublincore.org/documents/dcmi-terms/#terms-identifier) |
| Notes: | Using multiple identifiers implies that they have a same-as relationship, i.e. they all identify the same object (e. g. an object may have all of an http-URL, an lsid-URI, and a UUID). |

<a id="Type"></a>Term Name: dc:type
Normative URI:  http://purl.org/dc/elements/1.1/type
Label Type
  **Layer:** 1 — **Required:** Yes — **Repeatable:** No
Definition: dc:type may take as value any type term from the [DCMI Type Vocabulary](http://dublincore.org/documents/dcmi-type-vocabulary/#H7). Recommended terms are Collection, StillImage, Sound, MovingImage, InteractiveResource, Text. Values may be used either in their literal form, or with a full namespace (e. g. http://purl.org/dc/dcmitype/StillImage) from a controlled vocabulary, but the best practice is to use the literal form when using dc:type and use dcterms:type when you can supply the URI from a controlled vocabulary and implementers may require this practice. At least one of dc:type and dcterms:type must be supplied but, when feasible, supplying both may make the metadata more widely useful. The values of each should designate the same type, but in case of ambiguity dcterms:type prevails.
Defined by: [dc:type](http://purl.org/dc/elements/1.1/type)
Notes:  A Collection should be given type "Collection" when using dc:type. If the resource is a Collection, this item does *not* identify what types of objects it may contain. Following the DC recommendations for [the Text type](http://purl.org/dc/dcmitype/Text), images of text should be marked given as the string Text when provided as a string. **See also** the entry for [**dcterms:type**](#dcterms:type) in this document and see the **[DCMI FAQ on DC and DCTERMS Namespaces](http://wiki.dublincore.org/index.php/FAQ/DC_and_DCTERMS_Namespaces)** for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions.

Term Name: dcterms:type

Normative URI:

http://purl.org/dc/terms/type

Label

Type

 

**Layer:** 1 — **Required:** Yes — **Repeatable:** No

Definition:

A full URI preferably from among the type URIs specified in the [DCMI
Type
Vocabulary](http://dublincore.org/documents/dcmi-type-vocabulary/#H7).
Recommended terms are those URIs whose labels are Collection,
StillImage, Sound, MovingImage, InteractiveResource, or Text (e.g.
http://purl.org/dc/dcmitype/Collection). Also recommended are the full
URIs of ac:PanAndZoomImage, ac:3DStillImage, and ac: 3DMovingImage.
Values MUST NOT be a string, but a URI with full namespace (e. g.
http://purl.org/dc/dcmitype/StillImage) from a controlled vocabulary.
Implementers and communities of practice may determine whether specific
controlled vocabularies must be used. If the resource is a Collection,
this item does *not* identify what types of objects it may contain.
Following the DC recommendations at <http://purl.org/dc/dcmitype/Text>,
images of text should be with this URI.

Defined by:

[dcterms:type](http://dublincore.org/documents/dcmi-terms/#terms-type)

Notes:

Following the DC recommendations for [the Text
type](http://purl.org/dc/dcmitype/Text), images of text should be given
as http://purl.org/dc/dcmitype/Text when given as a URI. **See also**
the entry for [**dc:type**](#dc:type) in this document and see the
**[DCMI FAQ on DC and DCTERMS
Namespaces](http://wiki.dublincore.org/index.php/FAQ/DC_and_DCTERMS_Namespaces)**
for discussion of the rationale for terms in two namespaces. Normal
practice is to use the same Label if both are provided. Labels have no
effect on information discovery and are only suggestions. At least one
of dc:type and dcterms:type must be supplied but, when feasible,
supplying both may make the metadata more widely useful. The values of
each should designate the same type, but in case of ambiguity
dcterms:type prevails.

Term Name: ac:subtypeLiteral

Normative URI:

http://rs.tdwg.org/ac/terms/subtypeLiteral

Label

Subtype

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

The subtype should provide more specialization than the type. Possible
values are community-defined. For exmamples see the non-normative page
[AC\_Subtype\_Examples](/wiki/AC_Subtype_Examples "AC Subtype Examples").

Defined by:

[This item.](#subtypeLiteral)

Notes:

The subtypeLiteral term may not be applied to Collection objects.
However, the [Description](#Description) term in the Content Coverage
Vocabulary may add further description to a Collection object.

Term Name: ac:subtype

Normative URI:

http://rs.tdwg.org/ac/terms/subtype

Label

Subtype

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

Any URI may be used that provides for more specialization than the type.
Possible values are community-defined. For exmamples see the
non-normative page
[AC\_Subtype\_Examples](/wiki/AC_Subtype_Examples "AC Subtype Examples").

Defined by:

[This item.](#subtype)

Notes:

The subtype term may not be applied to Collection objects. However, the
[Description](#Description) term in the Content Coverage Vocabulary may
add further description to a Collection object. The subtype vocabulary
may be extended by users provided they identify the term by a URI which
is not in the ac namespace (for example, using
"http://my.inst.org/namespace/metadata/subtype/repair-manual").
Conforming applications may choose to ignore these. See
[ac:subtypeLiteral](#ac:subtypeLiteral) for usage with strings.

Term Name: dcterms:title

Normative URI:

http://purl.org/dc/terms/title

Label

Title

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

Concise title, name, or brief descriptive label of institution, resource
collection, or individual resource. This field should include the
complete title with all the subtitles, if any.

Defined by:

[dcterms:title](http://dublincore.org/documents/dcmi-terms/#terms-title)

Notes:

It is **strongly** suggested to provide a title. The title facilitates
interactions with humans: e.g., it could be used as display text of
hyperlinks or to provide a choice of images in a pick list. The title is
therefore highly useful and an effort should be made to provide it where
it is not already available. When the resource is a collection without
an institutional or official name, but with a thematic content, a
descriptive title, e. g. “Urban Ants of New England,” would be suitable.
In individual media resources depicting taxa, the scientific name or
names of taxa often form a good title. Common names in addition to or
instead of scientific names are also acceptable. Indications of action
or roles captured by the media resource, such as predatory acts, are
desirable (“Rattlesnake eating deer mouse”, “Pollinators of California
Native Plants”).

Term Name: dcterms:modified

Normative URI:

http://purl.org/dc/terms/modified

Label

Modified

 

**Layer:** 2 — **Required:** No — **Repeatable:** Yes

Definition:

Date that the media resource was altered. The date and time must comply
with the World Wide Web Consortium ([W3C](http://www.w3.org)) [datetime
practice](http://www.w3.org/TR/NOTE-datetime), which requires that date
and time representation correspond to ISO 8601:1998, but with year
fields always comprising 4 digits. This makes datetime records compliant
with
[8601:2004](http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=40874).
AC datetime values may also follow 8601:2004 for ranges by separating
two IS0 8601 datetime fields by a solidus ("forward slash", '/'). See
also the [wikipedia IS0 8601
entry](http://en.wikipedia.org/wiki/ISO_8601) for further explanation
and examples.

Defined
by:

[dcterms:modified](http://dublincore.org/documents/dcmi-terms/#terms-modified)

Notes:

dcterms:modified permits all modification dates to be recorded, or if
only one is recorded, it is assumed to be the latest. See also the
[wikipedia IS0 8601 entry](http://en.wikipedia.org/wiki/ISO_8601) for
further explanation and examples.

Term Name: xmp:MetadataDate

Normative URI:

http://ns.adobe.com/xap/1.0/MetadataDate

Label

Metadata Date

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

Point in time recording when the last modification to metadata (not
necessarily the media object itself) occurred. The date and time must
comply with the World Wide Web Consortium ([W3C](http://www.w3.org))
[datetime practice](http://www.w3.org/TR/NOTE-datetime), which requires
that date and time representation correspond to ISO 8601:1998, but with
year fields always comprising 4 digits. This makes datetime records
compliant with
[8601:2004](http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=40874).
AC datetime values may also follow 8601:2004 for ranges by separating
two IS0 8601 datetime fields by a solidus ("forward slash", '/'). See
also the [wikipedia IS0 8601
entry](http://en.wikipedia.org/wiki/ISO_8601) for further explanation
and examples.

Defined by:

Terms for Adobe XMP have URIs that are not resolvable. Instead, visit [,
XMP Specification Part 1,
Sec 8.4](http://www.adobe.com/content/dam/Adobe/en/devnet/xmp/pdfs/XMPSpecificationPart1.pdf)
for further documentation.

Notes:

This is not [dcterms:modified](#dcterms:modified), which refers to the
resource itself rather than its metadata. See also the [wikipedia
IS0 8601 entry](http://en.wikipedia.org/wiki/ISO_8601) for further
explanation and examples.

Term Name: ac:metadataLanguageLiteral

Normative URI:

http://rs.tdwg.org/ac/terms/metadataLanguageLiteral

Label

Metadata Language

 

**Layer:** 1 — **Required:** Yes — **Repeatable:** No

Definition:

Language of description and other metadata (but not necessarily of the
image itself) represented as an ISO639-2 three letter language code.
ISO639-1 two-letter codes are permitted but deprecated.

Defined by:

[This item.](#metadataLanguageLiteral)

Notes:

This is NOT [dc:language](#dc:language), which is about the resource,
not the metadata. Metadata Language is deliberately single-valued,
imposing on unstructured serializations a requirement that multi-lingual
metadata be represented as separate, complete, metadata records. Audubon
Core requires that each record also contains the language-neutral terms.
In the absence of this requirement, metadata consumers would need to
know which terms are language-neutral and merge these terms from all
provided metadataLanguages into a single record. Metadata consumers may
re-combine the information based on the dcterms:identifier that
identifies the multimedia resource. At least one of ac:metadataLanguage
and ac:metadataLanguageLiteral must be supplied but, when feasible,
supplying both may make the metadata more widely useful. They must
specify the same language. In case of ambiguity, ac:metadataLanguage
prevails. Nothing in this document would, however, prevent an
implementer, e. g. of an XML-Schema representation, from providing a
fully hierarchical schema in which language neutral terms occur only a
single time, and only the language-specific terms are repeated in a way
that unambigously relates them to a metadata language. In RDF it may be
a simple repetition of plain literals associated with a language (e.g.,
xml:lang attribute in RDF/XML). The language attribute would then be
required in Audubon Core and would replace
[ac:metadataLanguage](#ac:metadataLanguage).

Term Name: ac:metadataLanguage

Normative URI:

http://rs.tdwg.org/ac/terms/metadataLanguage

Label

Metadata Language

 

**Layer:** 1 — **Required:** Yes — **Repeatable:** No

Definition:

URI from the [ISO639-2 list of URIs for ISO 3-letter language
codes.](http://id.loc.gov/vocabulary/iso639-2)

Defined by:

[This item.](#metadataLanguage)

Notes:

This is NOT [dcterms:language](#dcterms:language), which is about the
resource, not the metadata. Metadata Language is deliberately
single-valued, imposing on unstructured serializations a requirement
that multi-lingual metadata be represented as separate, complete,
metadata records. Audubon Core requires that each record also contains
the language-neutral terms. In the absence of this requirement, metadata
consumers would need to know which terms are language-neutral and merge
these terms from all provided metadataLanguages into a single record.
Metadata consumers may re-combine the information based on the
dcterms:identifier that identifies the multimedia resource. At least one
of ac:metadataLanguage and ac:metadataLanguageLiteral must be supplied
but, when feasible, supplying both may make the metadata more widely
useful. They must specify the same language. In case of ambiguity,
ac:metadataLanguage prevails. Nothing in this document would, however,
prevent an implementer, e. g. of an XML-Schema representation, from
providing a fully hierarchical schema in which language neutral terms
occur only a single time, and only the language-specific terms are
repeated in a way that unambigously relates them to a metadata language.
In RDF it may be a simple repetition of plain literals associated with a
language (e.g., xml:lang attribute in RDF/XML). The language attribute
would then be required in Audubon Core and would replace
[ac:metadataLanguage](#ac:metadataLanguage).

Term Name: ac:providerManagedID

Normative URI:

http://rs.tdwg.org/ac/terms/providerManagedID

Label

Provider-managed ID

 

**Layer:** 2 — **Required:** No — **Repeatable:** No

Definition:

A free-form identifier (a simple number, an alphanumeric code, a URL,
etc.) that is unique and meaningful primarily for the data provider.

Defined by:

[This item.](#providerManagedID)

Notes:

Ideally, this would be a globally unique identifier (GUID), but the
provider is encouraged to supply any form of identifier that simplifies
communications on resources within their project and helps to locate
individual data items in the provider's data repositories. It is the
provider's decision whether to expose this value or not.

Term Name: xmp:Rating

Normative URI:

http://ns.adobe.com/xap/1.0/Rating

Label

Rating

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

A rating of the media resources, provided by record originators or
editors, with -1 defining “rejected”, “0” defining “unrated”, and “1”
(worst) to “5” (best).

Defined by:

Terms for Adobe XMP have URIs that are not resolvable. Instead, visit [,
XMP Specification Part 1,
Sec 8.4](http://www.adobe.com/content/dam/Adobe/en/devnet/xmp/pdfs/XMPSpecificationPart1.pdf)
for further documentation. The Adobe documentation describes this as "A
user-assigned rating for this file. The value must be -1 or in the range
\[0..5\], where -1 indicates “rejected” and 0 indicates “unrated”. If
xmp:Rating is not present, a value of 0 may be assumed. Anticipated
usage is for a typical “star rating” UI, with the addition of a notion
of rejection." Values may be decimal numbers in the permitted range.

Notes:

The origin of the rating is not communicated. It may, e. g., be based on
user feedback or on editorial ratings. If Rating is not present, a value
of 0 may be assumed. By "user-assigned" is meant assigned by the
originator or editor of the record using the term.

Term Name: ac:commenterLiteral

Normative URI:

http://rs.tdwg.org/ac/terms/commenterLiteral

Label

Commenter

 

**Layer:** 2 — **Required:** No — **Repeatable:** default No

Definition:

A name or the literal "anonymous" (= anonymously commented).

Defined by:

[This item.](#commenterLiteral)

Notes:

See also [Reviewer Comments](#Reviewer_Comments) for the distinction
between Comments and Reviewer Comments. See also **See also** the entry
for [**ac:commenter**](#ac:commenter) in this document and the section
**[Namespaces, Prefixes and Term
Names](#Namespaces.2C_Prefixes_and_Term_Names)** for discussion of the
rationale for separate terms taking URI values from those taking Literal
values where both are possible. Normal practice is to use the same Label
if both are provided. Labels have no effect on information discovery and
are only suggestions.

Term Name: ac:commenter

Normative URI:

http://rs.tdwg.org/ac/terms/commenter

Label

Commenter

 

**Layer:** 2 — **Required:** No — **Repeatable:** default No

Definition:

A URI denoting a person, using some controlled vocabulary such as FOAF.
Implementers and communities of practice may produce restrictions or
recommendations on the choice of vocabularies. **See also** the entry
for [**ac:commenterLiteral**](#ac:commenterLiteral) in this document and
the section **[Namespaces, Prefixes and Term
Names](#Namespaces.2C_Prefixes_and_Term_Names)** for discussion of the
rationale for separate terms taking URI values from those taking Literal
values where both are possible. Normal practice is to use the same Label
if both are provided. Labels have no effect on information discovery and
are only suggestions.

Defined by:

[This item.](#commenter)

Notes:

See also [Reviewer Comments](#Reviewer_Comments) for the distinction
between Comments and Reviewer Comments.

Term Name: ac:comments

Normative URI:

http://rs.tdwg.org/ac/terms/comments

Label

Comments

 

**Layer:** 2 — **Required:** No — **Repeatable:** Yes

Definition:

Any comment provided on the media resource, as free-form text. Best
practice would also identify the commenter.

Defined by:

[This item.](#comments)

Notes:

Comments may refer to the resource itself (e. g., asserting a taxon name
or location of a biological subject in an image), or to the relation
between resource and associated metadata (e. g., asserting that the
taxon name given in the metadata is wrong, without asserting a positive
identification). There is a separate item for [Reviewer
Comments](#Reviewer_Comments), which is defined more as an expert-level
review.Implementers or communities of practice might establish
conventions about the meaning of the absence of a commenter, but this
specification is silent on that matter.

Term Name: ac:reviewerLiteral

Normative URI:

http://rs.tdwg.org/ac/terms/reviewerLiteral

Label

Reviewer

 

**Layer:** 2 — **Required:** No — **Repeatable:** Yes

Definition:

String providing the name of a reviewer. If present, then resource is
peer-reviewed, even if [Reviewer Comments](#Reviewer_Comments) is absent
or empty. Its presence tells whether an expert in the subject featured
in the media has reviewed the media item or collection and approved its
metadata description; must display a name or the literal "anonymous" (=
anonymously reviewed).

Defined by:

[This item.](#reviewerLiteral)

Notes:

Provider is asserting they accept this review as competent. See also
**See also** the entry for [**ac:reviewer**](#ac:reviewer) in this
document and the section **[Namespaces, Prefixes and Term
Names](#Namespaces.2C_Prefixes_and_Term_Names)** for discussion of the
rationale for separate terms taking URI values from those taking Literal
values where both are possible. Normal practice is to use the same Label
if both are provided. Labels have no effect on information discovery and
are only suggestions.

Term Name: ac:reviewer

Normative URI:

http://rs.tdwg.org/ac/terms/reviewer

Label

Reviewer

 

**Layer:** 2 — **Required:** No — **Repeatable:** Yes

Definition:

URI for a reviewer. If present, then resource is peer-reviewed, even if
there are [Reviewer Comments](#Reviewer_Comments) is absent or empty.
Its presence tells whether an expert in the subject featured in the
media has reviewed the media item or collection and approved its
metadata description; must display a name or the literal "anonymous" (=
anonymously reviewed).

Defined by:

[This item.](#reviewer)

Notes:

Provider is asserting they accept this review as competent. **See also**
the entry for [**ac:reviewerLiteral**](#ac:reviewerLiteral) in this
document and the section **[Namespaces, Prefixes and Term
Names](#Namespaces.2C_Prefixes_and_Term_Names)** for discussion of the
rationale for separate terms taking URI values from those taking Literal
values where both are possible. Normal practice is to use the same Label
if both are provided. Labels have no effect on information discovery and
are only suggestions.

Term Name: ac:reviewerComments

Normative URI:

http://rs.tdwg.org/ac/terms/reviewerComments

Label

Reviewer Comments

 

**Layer:** 2 — **Required:** No — **Repeatable:** Yes

Definition:

Any comment provided by a reviewer with expertise in the subject, as
free-form text.

Defined by:

[This item.](#reviewerComments)

Notes:

Reviewer Comments may refer to the resource itself (e. g., asserting a
taxon name or location of a biological subject in an image), or to the
relation between resource and associated metadata (e. g., asserting that
the taxon name given in the metadata is wrong, without asserting a
positive identification). There is a separate item “Comments” for text
from commenters of unrecorded expertise.

Term Name: dcterms:available

Normative URI:

http://purl.org/dc/terms/available

Label

Date Available

 

**Layer:** 2 — **Required:** No — **Repeatable:** No

Definition:

The date (often a range) that the resource became or will become
available. The date and time must comply with the World Wide Web
Consortium ([W3C](http://www.w3.org)) [datetime
practice](http://www.w3.org/TR/NOTE-datetime), which requires that date
and time representation correspond to ISO 8601:1998, but with year
fields always comprising 4 digits. This makes datetime records compliant
with
[8601:2004](http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=40874).
AC datetime values may also follow 8601:2004 for ranges by separating
two IS0 8601 datetime fields by a solidus ("forward slash", '/'). See
also the [wikipedia IS0 8601
entry](http://en.wikipedia.org/wiki/ISO_8601) for further explanation
and examples.

Defined
by:

[dcterms:available](http://dublincore.org/documents/dcmi-terms/#terms-available)

Notes:

A use case is the harvesting of metadata published before the media are
available, which are pending a formal publication elsewhere. One
important example is the case of metadata that documents an occurrence,
which metadata harvesters might exploit without use of the media. See
also the [wikipedia IS0 8601
entry](http://en.wikipedia.org/wiki/ISO_8601) for further explanation
and examples.

Term Name: ac:hasServiceAccessPoint

Normative URI:

http://rs.tdwg.org/ac/terms/hasServiceAccessPoint

Label

Service Access Point

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

In a chosen serialization (RDF, XML Schema, etc.) the potentially
multiple service access points (e.g., for different resolutions of an
image) might be provided in a referenced or in a nested object. This
property identifies one such access point. That is, each of potentially
multiple values of hasServiceAccessPoint identifies a set of
representation-dependent metadata using the properties defined under the
section **[Service Access Point
Vocabulary](/wiki/Audubon_Core_Term_List#Service_Access_Point_Vocabulary "Audubon Core Term List")**.

Defined by:

[This item.](#hasServiceAccessPoint)

Notes:

Some serializations may flatten the model of service-access points by
(a) dropping ac:hasServiceAccessPoint, [ac:variant](#ac:variant) and
[ac:variantLiteral](#ac:variantLiteral), (b) repeating properties from
the [Service Access Point Vocabulary](#Service_Access_Point_Vocabulary)
and prefixing them with values of
[ac:variantLiteral](#ac:variantLiteral). If such a flat serialization is
necessary for services, we recommend to select from among term names of
the form "AB" where "A" is one of thumbnail, trailer, lowerQuality,
mediumQuality, goodQuality, bestQuality, offline and "B" is one of
AccessURI, Format, Extent, FurtherInformationURL, LicensingException,
ServiceExpectation (example: thumbnailAccessURI). Implementers in
specific constraint languages such as XML Schema or RDF may wish to make
Access URI and perhaps dcterms:format mandatory on instances of the
service access
point.





## <span id="Attribution_Vocabulary" class="mw-headline">Attribution Vocabulary</span>

Term Name: dc:rights

Normative URI:

http://purl.org/dc/elements/1.1/rights

Label

Copyright Statement

 

**Layer:** 1 — **Required:** Yes — **Repeatable:** No

Definition:

Information about rights held in and over the resource. A full-text,
readable copyright statement, as required by the national legislation of
the copyright holder. On collections, this applies to all contained
objects, unless the object itself has a different statement. Examples:
“Copyright XY 2008, all rights reserved”, “© 2008 XY Museum” , "Public
Domain.", "Copyright unknown." Do not place just the name of the
copyright holder(s) here\! That belongs in a list in the xmpRights:Owner
field, which should be supplied if dc:rights is not 'Public Domain',
which is appropriate only if the resource is known to be not under
copyright. **See also** the entry for
[**dcterms:rights**](#dcterms:rights) in this document and see the
**[DCMI FAQ on DC and DCTERMS
Namespaces](http://wiki.dublincore.org/index.php/FAQ/DC_and_DCTERMS_Namespaces)**
for discussion of the rationale for terms in two namespaces. Normal
practice is to use the same Label if both are provided. Labels have no
effect on information discovery and are only suggestions.

Defined by:

[dc:rights](http://purl.org/dc/elements/1.1/rights)

Notes:

This expresses rights over the media resource, not over the metadata
text. At least one of dcterms:rights and dc:rights must be supplied but,
when feasible, supplying both may make the metadata more widely useful.
They must specify the same rights. In case of ambiguity, dcterms:rights
prevails.

Term Name: dcterms:rights

Normative URI:

http://purl.org/dc/terms/rights

Label

Copyright Statement

 

**Layer:** 1 — **Required:** Yes — **Repeatable:** No

Definition:

A URI pointing to structured information about rights held in and over
the resource. Examples include
http://creativecommons.org/licenses/by/3.0/legalcode and
http://creativecommons.org/publicdomain/zero/1.0/. At least one of
dcterms:rights and dc:rights must be supplied but, when feasible,
supplying both may make the metadata more widely useful. They must
specify the same rights. In case of ambiguity, dcterms:rights prevails.

Defined
by:

[dcterms:rights](http://dublincore.org/documents/dcmi-terms/#terms-rights)

Notes:

This expresses rights over the media resource, not over the metadata
text. **See also** the entry for [**dc:rights**](#dc:rights) in this
document and see the **[DCMI FAQ on DC and DCTERMS
Namespaces](http://wiki.dublincore.org/index.php/FAQ/DC_and_DCTERMS_Namespaces)**
for discussion of the rationale for terms in two namespaces. Normal
practice is to use the same Label if both are provided. Labels have no
effect on information discovery and are only suggestions.

Term Name: xmpRights:Owner

Normative URI:

http://ns.adobe.com/xap/1.0/rights/Owner

Label

Copyright Owner

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

A list of the names of the owners of the copyright. 'Unknown' is an
acceptable value, but 'Public Domain' is not.

Defined by:

Terms for Adobe XMP have URIs that are not resolvable. Instead, visit [,
XMP Specification Part 1,
Sec 8.5](http://www.adobe.com/content/dam/Adobe/en/devnet/xmp/pdfs/XMPSpecificationPart1.pdf)
for further documentation.

Notes:

Some providers use dc:publisher for this purpose, but it seems doubtful
that the publisher is by necessity the copyright owner. 'Public Domain'
is not an appropriate value because it denotes something that is not
under copyright. In this case, omit or leave empty xmpRights:Owner, and
put 'Public Domain' in the Copyright Statement
([dc:rights](#dc:rights)). Except for 'Public Domain' resources, it is
strongly urged that this field be supplied.

Term Name: xmpRights:UsageTerms

Normative URI:

http://ns.adobe.com/xap/1.0/rights/UsageTerms

Label

License Terms

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

The license statement defining how resources may be used. Information on
a collection applies to all contained objects unless the object has a
different statement.

Defined by:

Terms for Adobe XMP have URIs that are not resolvable. Instead, visit [,
XMP Specification Part 1,
Sec 8.5](http://www.adobe.com/content/dam/Adobe/en/devnet/xmp/pdfs/XMPSpecificationPart1.pdf)
for further documentation.

Notes:

Example: "Available under Creative Commons BY-SA 3.0 license". This also
describes the commercial availability of items. Buying an identification
tool or media resource is essentially the purchase of an individual
license. Examples for such License statements: “Available through
bookstores” for a commercially published CD, and “Individual licenses
available for purchase” for a high-resolution image. Note that the
medium or low resolution levels of the same image may be available under
open access licenses. In general, this term determines the default
licensing for the media. License terms specific to variants or
representations of the media resource (e.g., different resolutions) are
dealt within the section on [Service Access Point
Vocabulary](#Service_Access_Point_Vocabulary)

Term Name: xmpRights:WebStatement

Normative URI:

http://ns.adobe.com/xap/1.0/rights/WebStatement

Label

License URL

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

A URL defining or further elaborating on the license statement (e. g., a
web page explaining the precise terms of use).

Defined by:

Terms for Adobe XMP have URIs that are not resolvable. Instead, visit [,
XMP Specification Part 1,
Sec 8.5](http://www.adobe.com/content/dam/Adobe/en/devnet/xmp/pdfs/XMPSpecificationPart1.pdf)
for further documentation.

Notes:

The value of this field may provide a complete definition of the terms
of use. For Creative Commons, the appropriate value is the URL of the
defining Web page for the license. Example:
<http://creativecommons.org/licenses/by-nc-sa/3.0/us/>. Where different
quality variants (e. g. different resolutions of images) are published
under different licenses, the AC term “Licensing Exception Statement”
supports variant-specific licenses.

Term Name: ac:licenseLogoURL

Normative URI:

http://rs.tdwg.org/ac/terms/licenseLogoURL

Label

License Logo URL

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

A URL providing access to a logo that symbolizes the License.

Defined by:

[This item.](#licenseLogoURL)

Notes:

The originating metadata provider is strongly urged to choose a suitable
logo as a graphical representation of the license. Failure to do so may
leave downstream aggregators in a difficult position to supply a logo
that adequately represents the professional, legal, or social aims of
the licensors (license givers). Example:
http://i.creativecommons.org/l/by-nc-sa/3.0/us/88x31.png provides access
to this:
![88x31.png](http://i.creativecommons.org/l/by-nc-sa/3.0/us/88x31.png)

Term Name: photoshop:Credit

Normative URI:

http://ns.adobe.com/photoshop/1.0/Credit

Label

Credit

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

free text for "Please cite this as…"

Defined by:

IPTC terms have URIs that are not resolvable. Instead, visit [IPTC
Standard Photo Metadata
(July 2010)](http://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-201007_1.pdf)
for further documentation. AC follows the URI namespace of the Adobe XMP
implementation of IPTC terms. This term is one of several with XMP
namespace http://ns.adobe.com/photoshop/1.0/ (recommended prefix
"photoshop".)

Notes:

IPTC also refers to this generically as a "Credit Line" as it is
frequently displayed with the media.

Term Name: ac:attributionLogoURL

Normative URI:

http://rs.tdwg.org/ac/terms/attributionLogoURL

Label

Attribution URL

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

The URL of the icon or logo image to appear in source attribution.

Defined by:

[This item.](#attributionLogoURL)

Notes:

Entering this URL into a browser should only result in the icon (not in
a webpage including the icon).

Term Name: ac:attributionLinkURL

Normative URI:

http://rs.tdwg.org/ac/terms/attributionLinkURL

Label

Attribution Link URL

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

The URL where information about ownership, attribution, etc. of the
resource may be found.

Defined by:

[This item.](#attributionLinkURL)

Notes:

This URL may be used in creating a clickable logo. Providers should
consider making this link as specific and useful to consumers as
possible, e. g., linking to a metadata page of the specific image
resource rather than to a generic page describing the owner or provider
of a resource.

Term Name: ac:fundingAttribution

Normative URI:

http://rs.tdwg.org/ac/terms/fundingAttribution

Label

Funding

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

Organizations or individuals who funded the creation of the resource.

Defined by:

[This item.](#fundingAttribution)

Term Name: dc:source

Normative URI:

http://purl.org/dc/elements/1.1/source

Label

Published Source

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

A string providing an identifiable source from which the described
resources was derived.

Defined by:

[dc:source](http://purl.org/dc/elements/1.1/source)

Notes:

If the resource was digitized from a non-digital resource, or was also
previously published in a digital or printed publication, this describes
the original. Do not put generally "related" publications in here. This
field normally contains a free-form text description. If a URI is
available it should be provided in [dcterms:source](#dcterms:source).
Can be repeatable if a montage of images. Information about further
provenance beyond the ultimate source should be put in the
[derivedFrom](#derivedFrom) attribute. **See also** the entry for
[**dcterms:source**](#dcterms:source) in this document and see the
**[DCMI FAQ on DC and DCTERMS
Namespaces](http://wiki.dublincore.org/index.php/FAQ/DC_and_DCTERMS_Namespaces)**
for discussion of the rationale for terms in two namespaces. Normal
practice is to use the same Label if both are provided. Labels have no
effect on information discovery and are only suggestions

Term Name: dcterms:source

Normative URI:

http://purl.org/dc/terms/source

Label

Published Source

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

URI for an identifiable source from which the described resources was
derived.

Defined
by:

[dcterms:source](http://dublincore.org/documents/dcmi-terms/#terms-source)

Notes:

If the resource was digitized from a non-digital resource, or was also
previously published in a digital or printed publication, this describes
the original. If a string is required for this, use
[dc:source](#dc:source). Do not put generally "related" publications in
here. A URI that can be resolved and dereferenced to provide a
description of the source resource may also be used here. For example,
"<http://www.loc.gov/pictures/item/fsa1998021539/PP/>" is the address of
a web page that provides a description the original negative of a famous
picture by the photographer Dorothea Lange and so would be an
appropriate value of dcterms:source. The term may be repeatable if a
montage of images. Information about further provenance beyond the
ultimate source should be put in the [derivedFrom](#derivedFrom)
attribute. **See also** the entry for [**dc:source**](#dc:source) in
this document and see the **[DCMI FAQ on DC and DCTERMS
Namespaces](http://wiki.dublincore.org/index.php/FAQ/DC_and_DCTERMS_Namespaces)**
for discussion of the rationale for terms in two namespaces. Normal
practice is to use the same Label if both are provided. Labels have no
effect on information discovery and are only
suggestions.



## <span id="Agents_Vocabulary" class="mw-headline">Agents Vocabulary</span>

Term Name: dc:creator

Normative URI:

http://purl.org/dc/elements/1.1/creator

Label

Creator

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

The person or organization responsible for creating the media resource.

Defined by:

[dc:creator](http://purl.org/dc/elements/1.1/creator)

Notes:

The value may be simple text including contact information. Note that
the [Creator](#Creator) need not be the [Copyright
Owner](#Copyright_Owner).

**See also** the entry for [**dcterms:creator**](#dcterms:creator) in
this document and see the **[DCMI FAQ on DC and DCTERMS
Namespaces](http://wiki.dublincore.org/index.php/FAQ/DC_and_DCTERMS_Namespaces)**
for discussion of the rationale for terms in two namespaces. Normal
practice is to use the same Label if both are provided. Labels have no
effect on information discovery and are only suggestions.

.

Term Name: dcterms:creator

Normative URI:

http://purl.org/dc/terms/creator

Label

Creator

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

A URI representing the person or organization responsible for creating
the media resource.

Defined
by:

[dcterms:creator](http://dublincore.org/documents/dcmi-terms/#terms-creator)

Notes:

Note that the [Creator](#Creator) need not be the [Copyright
Owner](#Copyright_Owner).

**See also** the entry for [**dc:creator**](#dc:creator) in this
document and see the **[DCMI FAQ on DC and DCTERMS
Namespaces](http://wiki.dublincore.org/index.php/FAQ/DC_and_DCTERMS_Namespaces)**
for discussion of the rationale for terms in two namespaces. Normal
practice is to use the same Label if both are provided. Labels have no
effect on information discovery and are only suggestions.

.

Term Name: ac:providerLiteral

Normative URI:

http://rs.tdwg.org/ac/terms/providerLiteral

Label

Provider

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

Person or organization responsible for presenting the media resource. If
no separate Metadata Provider is given, this also attributes the
metadata.

Defined by:

[This item.](#providerLiteral)

Notes:

Media resources and their metadata may be served from different
institutions, e. g. in the case of aggregators adding user annotations,
taxon identifications, or ratings. **See also** the entry for
[**ac:provider**](#ac:provider) in this document and the section
**[Namespaces, Prefixes and Term
Names](#Namespaces.2C_Prefixes_and_Term_Names)** for discussion of the
rationale for separate terms taking URI values from those taking Literal
values where both are possible. Normal practice is to use the same Label
if both are provided. Labels have no effect on information discovery and
are only suggestions.

Term Name: ac:provider

Normative URI:

http://rs.tdwg.org/ac/terms/provider

Label

Provider

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

URI for person or organization responsible for presenting the media
resource. If no separate Metadata Provider is given, this also
attributes the metadata.

Defined by:

[This item.](#provider)

Notes:

Media resources and their metadata may be served from different
institutions, e. g. in the case of aggregators adding user annotations,
taxon identifications, or ratings. **See also** the entry for
[**ac:providerLiteral**](#ac:providerLiteral) in this document and the
section **[Namespaces, Prefixes and Term
Names](#Namespaces.2C_Prefixes_and_Term_Names)** for discussion of the
rationale for separate terms taking URI values from those taking Literal
values where both are possible. Normal practice is to use the same Label
if both are provided. Labels have no effect on information discovery and
are only suggestions.

Term Name: ac:metadataCreatorLiteral

Normative URI:

http://rs.tdwg.org/ac/terms/metadataCreatorLiteral

Label

Metadata Creator

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

Person or organization originally creating the resource metadata record.

Defined by:

[This item.](#metadataCreatorLiteral)

Notes:

**See also** the entry for [**ac:metadataCreator**](#ac:metadataCreator)
in this document and the section **[Namespaces, Prefixes and Term
Names](#Namespaces.2C_Prefixes_and_Term_Names)** for discussion of the
rationale for separate terms taking URI values from those taking Literal
values where both are possible. Normal practice is to use the same Label
if both are provided. Labels have no effect on information discovery and
are only suggestions.

Term Name: ac:metadataCreator

Normative URI:

http://rs.tdwg.org/ac/terms/metadataCreator

Label

Metadata Creator

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

Person or organization originally creating the resource metadata record.

Defined by:

[This item.](#metadataCreator)

Notes:

**See also** the entry for
[**ac:metadataCreatorLiteral**](#ac:metadataCreatorLiteral) in this
document and the section **[Namespaces, Prefixes and Term
Names](#Namespaces.2C_Prefixes_and_Term_Names)** for discussion of the
rationale for separate terms taking URI values from those taking Literal
values where both are possible. Normal practice is to use the same Label
if both are provided. Labels have no effect on information discovery and
are only suggestions.

Term Name: ac:metadataProviderLiteral

Normative URI:

http://rs.tdwg.org/ac/terms/metadataProviderLiteral

Label

Metadata Provider

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

Person or organization originally responsible for providing the resource
metadata record.

Defined by:

[This item.](#metadataProviderLiteral)

Notes:

Media resources and their metadata may be served from different
institutions, e. g. in the case of aggregators adding user annotations,
taxon identifications, or ratings. Compare [Provider](#Provider). **See
also** the entry for [**ac:metadataProvider**](#ac:metadataProvider) in
this document and the section **[Namespaces, Prefixes and Term
Names](#Namespaces.2C_Prefixes_and_Term_Names)** for discussion of the
rationale for separate terms taking URI values from those taking Literal
values where both are possible. Normal practice is to use the same Label
if both are provided. Labels have no effect on information discovery and
are only suggestions.

Term Name: ac:metadataProvider

Normative URI:

http://rs.tdwg.org/ac/terms/metadataProvider

Label

Metadata Provider

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

URI of person or organization originally responsible for providing the
resource metadata record.

Defined by:

[This item.](#metadataProvider)

Notes:

Media resources and their metadata may be served from different
institutions, e. g. in the case of aggregators adding user annotations,
taxon identifications, or ratings. Compare [Provider](#Provider). **See
also** the entry for
[**ac:metadataProviderLiteral**](#ac:metadataProviderLiteral) in this
document and the section **[Namespaces, Prefixes and Term
Names](#Namespaces.2C_Prefixes_and_Term_Names)** for discussion of the
rationale for separate terms taking URI values from those taking Literal
values where both are possible. Normal practice is to use the same Label
if both are provided. Labels have no effect on information discovery and
are only
suggestions.



## <span id="Content_Coverage_Vocabulary" class="mw-headline">Content Coverage Vocabulary</span>

Term Name: dcterms:description

Normative URI:

http://purl.org/dc/terms/description

Label

Description

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

Description of collection or individual resource, containing the Who,
What, When, Where and Why as free-form text. This normative document is
silent on the nature of formatting in the text. It is the role of
implementers of an AC concrete representation (e.g., an XML Schema, an
RDF representation, etc.) to decide and document how formatting advice
will be represented in descriptions serialized according to such
representations.

Defined
by:

[dcterms:description](http://dublincore.org/documents/dcmi-terms/#terms-description)

Notes:

It optionally allows the presentation of detailed information and will
in most cases be shown together with the resource title. If both a
description and a caption are present in the metadata, a description is
typically displayed instead of the resource, whereas a caption is
displayed together with the resource. The description should aim to be a
good proxy for the underlying media resource in cases where only text
can be shown, whereas the caption may only make sense when shown
together with the media. Often only one of description or caption is
present; choose the term most appropriate for your metadata.

Term Name: ac:caption

Normative URI:

http://rs.tdwg.org/ac/terms/caption

Label

Caption

 

**Layer:** 2 — **Required:** No — **Repeatable:** No

Definition:

As alternative or in addition to description, a caption is free-form
text to be displayed together with (rather than instead of) a resource
that is suitable for captions (especially images).

Defined by:

[This item.](#caption)

Notes:

If both description and caption are present in the metadata, a
description is typically displayed instead of the resource, a caption
together with the resource. Often only one of description or caption is
present; choose the term most appropriate for your metadata.

Term Name: dc:language

Normative URI:

http://purl.org/dc/elements/1.1/language

Label

Language

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

Language(s) of resource itself represented in the ISO639-2 three-letter
language code. ISO639-1 two-letter codes are permitted but deprecated.

Defined by:

[dc:language](http://purl.org/dc/elements/1.1/language)

Notes:

An image may contain language such as superimposed labels. If an image
is of a natural scene or organism, without any language included, the
resource is language-neutral (ISO code “zxx”). Resources with present
but unknown language are to be coded as undetermined (ISO code “und”).
Regional dialects or other special cases should conform to the [ISO639-5
Alpha-3 Code for Language Families and
Groups](http://id.loc.gov/vocabulary/iso639-5.html) where possible or
the [IETF Best Practices for Tags Identifying
Languages](http://tools.ietf.org/html/rfc5646) where not. **See also**
the entry for [**dcterms:language**](#dcterms:language) in this document
and see the **[DCMI FAQ on DC and DCTERMS
Namespaces](http://wiki.dublincore.org/index.php/FAQ/DC_and_DCTERMS_Namespaces)**
for discussion of the rationale for terms in two namespaces. Normal
practice is to use the same Label if both are provided. Labels have no
effect on information discovery and are only suggestions.

Term Name: dcterms:language

Normative URI:

http://purl.org/dc/terms/language

Label

Language

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

URI from the [ISO639-2 list of URIs for ISO 3-letter language
codes.](http://id.loc.gov/vocabulary/iso639-2)

Defined
by:

[dcterms:language](http://dublincore.org/documents/dcmi-terms/#terms-language)

Notes:

An image may contain language such as superimposed labels. If an image
is of a natural scene or organism, without any language included, the
resource is language-neutral with URI
<http://id.loc.gov/vocabulary/iso639-2/zxx> corresponding to ISO
ISO639-2 code “zxx”. Resources with present but unknown language are to
be coded as undetermined, with URI
<http://id.loc.gov/vocabulary/iso639-2/und> corresponding to ISO639-2
code “und”. Regional dialects or other special cases should conform to
the [ISO639-5 Alpha-3 Code for Language Families and
Groups](http://id.loc.gov/vocabulary/iso639-5.html) where possible, or
[IETF Best Practices for Tags Identifying
Languages](http://tools.ietf.org/html/rfc5646) where not. **See also**
the entry for [**dc:language**](#dc:language) in this document and see
the **[DCMI FAQ on DC and DCTERMS
Namespaces](http://wiki.dublincore.org/index.php/FAQ/DC_and_DCTERMS_Namespaces)**
for discussion of the rationale for terms in two namespaces. Normal
practice is to use the same Label if both are provided. Labels have no
effect on information discovery and are only suggestions.

Term Name: ac:physicalSetting

Normative URI:

http://rs.tdwg.org/ac/terms/physicalSetting

Label

Physical Setting

 

**Layer:** 2 — **Required:** No — **Repeatable:** Yes

Definition:

The setting of the content represented in media such as images, sounds,
and movies if the provider deems them relevant. Constrained vocabulary
of: "Natural" = Object in its natural setting of the object (e. g.
living organisms in their natural environment); "Artificial" = Object in
an artificial environment (e. g. living organisms in an artificial
environment such as a zoo, garden, greenhouse, or laboratory); "Edited"
= Human media editing of a natural setting or media acquisition with a
separate media background such as a photographic backdrop.

Defined by:

[This item.](#physicalSetting)

Notes:

Multiple values may be needed for movies or montages. See also
[ac:resourceCreationTechnique](#ac:resourceCreationTechnique) which
should be used to describe any modifications to the resource itself.
Communities of practice should form best practices for the use of these
controlled terms.

Term Name: Iptc4xmpExt:CVterm

Normative URI:

http://iptc.org/std/Iptc4xmpExt/2008-02-29/CVterm

Label

Subject Category

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

Controlled vocabulary of subjects to support broad classification of
media items. Terms from various controlled vocabularies may be used.
AC-recommended vocabularies are preferred and may be unqualified
literals (not a full URI). For terms from other vocabularies either a
precise URI should be used, or, as long as all unqualified terms in all
vocabularies are unique, metadata should provide the source vocabularies
using the Subject Category Vocabulary term.

Defined by:

IPTC terms have URIs that are not resolvable, but AC follows the URI
namespace usage of the Adobe XMP implementation of IPTC terms described
in [IPTC Standard Photo Metadata
(July 2010)](http://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-201007_1.pdf).

Notes:

Recommended sets include: the NASA Global Change Master Directory (GCMD)
<sup>[\[1\]](#cite_note-1)</sup>, K2N <sup>[\[2\]](#cite_note-2)</sup>,
the BioComplexity Thesaurus<sup>[\[3\]](#cite_note-3)</sup>, the
Description Type GBIF Vocabulary <sup>[\[4\]](#cite_note-4)</sup>, the
TDWG Species Profile Model <sup>[\[5\]](#cite_note-5)</sup>, the Plinian
Core <sup>[\[6\]](#cite_note-6)</sup>, the European Environmental Agency
GEneral Multilingual Environmental Thesaurus(GEMET)
<sup>[\[7\]](#cite_note-7)</sup> and the LTER Controlled
Vocabulary.<sup>[\[8\]](#cite_note-8)</sup>. The vocabulary may include
major taxonomic groups (such as “vertebrates” or “fungi”) or ecosystem
terms (“savannah”, “temperate rain forest”, “forest fires”, “aquatic
vertebrates”). Other formal classifications (published in print or
online) such as habitat, fuel, invasive species, agroproductivity,
fisheries, migratory species etc. are also suitable.

Term Name: ac:subjectCategoryVocabulary

Normative URI:

http://rs.tdwg.org/ac/terms/subjectCategoryVocabulary

Label

Subject Category Vocabulary

 

**Layer:** 2 — **Required:** No — **Repeatable:** Yes

Definition:

Any vocabulary or formal classification from which terms in the Subject
Category have been drawn.

Defined by:

[This item.](#subjectCategoryVocabulary)

Notes:

The AC recommended vocabularies do not need to be cited here. There is
no required linkage between individual [Subject
Category](#Subject_Category) terms and the vocabulary; the mechanism is
intended to support discovery of the normative URI for a term, but not
guarantee it.

Term Name: ac:tag

Normative URI:

http://rs.tdwg.org/ac/terms/tag

Label

Tag

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

General keywords or tags.

Defined by:

[This item.](#tag)

Notes:

Tags may be multi-worded phrases. Where scientific names, common names,
geographic locations, etc. are separable, those should go into the more
specific coverage metadata items provided further below. Examples:
"flower diagram". Character or part keywords like "leaf", or "flower
color" are especially
desirable.



## <span id="Geography_Vocabulary" class="mw-headline">Geography Vocabulary</span>

All geography terms from the DarwinCore [version of 9
Dec 2009](http://rs.tdwg.org/dwc/2009-12-07/terms/#dcterms) are deemed
included in the Core Layer. Specifically, this includes exactly those
which are declared by DarwinCore to be in DarwinCore Class
[Location](http://rs.tdwg.org/dwc/2009-12-07/terms/#dcterms:Location).
Note that [dwc:locality](http://rs.tdwg.org/dwc/terms/locality) may be
used, but as applied to media this term may be ambiguous as to whether
it applies to the location depicted or the location at which the media
was created. When disambiguating information is available, it is better
to use the terms Location Shown and Location Created. The latter is in
the Resource Creation Vocabulary.

Location Created and Location Shown are separated in the current version
of IPTC, and the metadata working group (MWG
2010)<sup>[\[9\]](#cite_note-MWG2010-9)</sup> also recommends this. We
follow this below in order to support the expected future increase of
automatic GPS-based coordinate recording. As a special case, the AC
group recommends to change the semantics of Location Shown in the case
of biodiversity specimens, where the original location may differ from
the current location at which the specimen is held in a collection. In
this case, Location Shown should exclusively refer to the location where
a specimen was originally collected (gathering or sampling location).
Use Location Created to express the location where the resource was
created (a specimen was digitized).

Term Name: Iptc4xmpExt:LocationShown

Normative URI:

http://iptc.org/std/Iptc4xmpExt/2008-02-29/LocationShown

Label

Location Shown

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

The location that is depicted the media content, irrespective of the
location at which the resource has been created.

Defined by:

IPTC terms have URIs that are not resolvable, but AC follows the URI
namespace usage of the Adobe XMP implementation of IPTC terms described
in [IPTC Standard Photo Metadata
(July 2010)](http://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-201007_1.pdf).

Term Name: Iptc4xmpExt:WorldRegion

Normative URI:

http://iptc.org/std/Iptc4xmpExt/2008-02-29/WorldRegion

Label

World Region

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

Name of a world region in some high level classification, such as names
for continents, waterbodies, or island groups, whichever is most
appropriate. The terms preferably are derived from a controlled
vocabulary.

Defined by:

IPTC terms have URIs that are not resolvable, but AC follows the URI
namespace usage of the Adobe XMP implementation of IPTC terms described
in [IPTC Standard Photo Metadata
(July 2010)](http://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-201007_1.pdf).

Notes:

The equivalent DarwinCore fields here forces primary metadata providers
to classify world region terms into separate properties for “continent”
“waterbody”, “IslandGroup”. By contrast, the Iptc4xmpExt vocabulary
only specifies that a World Region is something at the top of a
hierarchy of locations.

Term Name: Iptc4xmpExt:CountryCode

Normative URI:

http://iptc.org/std/Iptc4xmpExt/2008-02-29/CountryCode

Label

Country Code

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

The geographic location of the specific entity or entities documented by
the media item, expressed through a constrained vocabulary of countries
using 2-letter ISO country code (e. g. "it, si").

Defined by:

IPTC terms have URIs that are not resolvable, but AC follows the URI
namespace usage of the Adobe XMP implementation of IPTC terms described
in [IPTC Standard Photo Metadata
(July 2010)](http://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-201007_1.pdf).

Notes:

Accepted exceptions to be used instead of ISO codes are: "Global",
"Marine", "Europe", “N-America”, “C-America”, “S-America”, "Africa",
“Asia”, “Oceania”, ATA = "Antarctica", XEU = "European Union", XAR =
"Arctic", "ZZZ" = "Unknown country" (3 letter abbreviations from IPTC
codes). This list may be extended as necessary.

Term Name: Iptc4xmpExt:CountryName

Normative URI:

http://iptc.org/std/Iptc4xmpExt/2008-02-29/CountryName

Label

Country Name

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

This field can be free text, but where possible, the use of
http://iptc.org/std/Iptc4xmpExt/2008-02-29/CountryCode is preferred.

Defined by:

IPTC terms have URIs that are not resolvable, but AC follows the URI
namespace usage of the Adobe XMP implementation of IPTC terms described
in [IPTC Standard Photo Metadata
(July 2010)](http://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-201007_1.pdf).

Term Name: Iptc4xmpExt:ProvinceState

Normative URI:

http://iptc.org/std/Iptc4xmpExt/2008-02-29/ProvinceState

Label

Province or State

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

Optionally, the geographic unit immediately below the country level
(individual states in federal countries, provinces, or other
administrative units) in which the subject of the media resource (e. g.,
species, habitats, or events) were located (if such information is
available in separate fields).

Defined by:

IPTC terms have URIs that are not resolvable, but AC follows the URI
namespace usage of the Adobe XMP implementation of IPTC terms described
in [IPTC Standard Photo Metadata
(July 2010)](http://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-201007_1.pdf).

Term Name: Iptc4xmpExt:City

Normative URI:

http://iptc.org/std/Iptc4xmpExt/2008-02-29/City

Label

City or Place Name

 

**Layer:** 2 — **Required:** No — **Repeatable:** Yes

Definition:

Optionally, the name of a city or place commonly found in gazetteers
(such as a mountain or national park) in which the subjects (e. g.,
species, habitats, or events) were located.

Defined by:

IPTC terms have URIs that are not resolvable, but AC follows the URI
namespace usage of the Adobe XMP implementation of IPTC terms described
in [IPTC Standard Photo Metadata
(July 2010)](http://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-201007_1.pdf).

Term Name: Iptc4xmpExt:Sublocation

Normative URI:

http://iptc.org/std/Iptc4xmpExt/2008-02-29/Sublocation

Label

Sublocation

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

Free-form text location details of the location of the subjects, down to
the village, forest, or geographic feature etc., below the
[Iptc4xmpExt:City](#Iptc4xmpExt:City) place name, especially information
that could not be found in a gazetteer.

Defined by:

IPTC terms have URIs that are not resolvable, but AC follows the URI
namespace usage of the Adobe XMP implementation of IPTC terms described
in [IPTC Standard Photo Metadata
(July 2010)](http://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-201007_1.pdf).



## <span id="Temporal_Coverage_Vocabulary" class="mw-headline">Temporal Coverage Vocabulary</span>

Term Name: dcterms:temporal

Normative URI:

http://purl.org/dc/terms/temporal

Label

Temporal Coverage

 

**Layer:** 2 — **Required:** No — **Repeatable:** No

Definition:

The coverage (extent or scope) of the content of the resource. Temporal
coverage will typically include temporal period (a period label, date,
or date range) to which the subjects of the media or media collection
relate. If dates are mentioned, they should follow ISO 8601. When the
resource is a Collection, this refers to the temporal coverage of the
collection. Following
[dcterms:temporal](http://dublincore.org/documents/dcmi-terms/#terms-temporal)
, the value must be a URI.

Defined
by:

[dcterms:temporal](http://dublincore.org/documents/dcmi-terms/#terms-temporal)

Notes:

See the DCMI [User Guide dcterms:temporal
entry](http://wiki.dublincore.org/index.php/User_Guide/Publishing_Metadata#dcterms:temporal)
for an example. [dc:coverage](http://purl.org/dc/elements/1.1/coverage)
may be used for string values of temporal coverage, but use the
[Geography Vocabulary](#Geography_Vocabulary) for geographic coverage.
String examples for use with
[dc:coverage](http://purl.org/dc/elements/1.1/coverage) include
"Jurassic", "Elizabethan", "Spring, 1957". 2008-01-01/2008-06-30. If the
resource is video or audio, it refers to the time span, if any, depicted
by the resource. For live-media this is closely related to [Original
Date and Time](#Original_Date_and_Time) (Example: the time depicted by a
time-lapse video file of organism development), but for media with
fictional content it is not.

Term Name: xmp:CreateDate

Normative URI:

http://ns.adobe.com/xap/1.0/CreateDate

Label

Original Date and Time

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

The date of the creation of the original resource from which the digital
media was derived or created. The date and time must comply with the
World Wide Web Consortium ([W3C](http://www.w3.org)) [datetime
practice](http://www.w3.org/TR/NOTE-datetime), which requires that date
and time representation correspond to ISO 8601:1998, but with year
fields always comprising 4 digits. This makes datetime records compliant
with
[8601:2004](http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=40874).
AC datetime values may also follow 8601:2004 for ranges by separating
two IS0 8601 datetime fields by a solidus ("forward slash", '/'). See
also the [wikipedia IS0 8601
entry](http://en.wikipedia.org/wiki/ISO_8601) for further explanation
and examples.

Defined by:

Terms for Adobe XMP have URIs that are not resolvable. Instead, visit [,
XMP Specification Part 1,
Sec 8.4](http://www.adobe.com/content/dam/Adobe/en/devnet/xmp/pdfs/XMPSpecificationPart1.pdf)
for further documentation.

Notes:

What constitutes "original" is determined by the metadata author.
Example: Digitization of a photographic slide of a map would normally
give the date at which the map was created; however a photographic work
of art including the same map as its content may give the date of the
original photographic exposure. Imprecise or unknown dates can be
represented as ISO dates or ranges. Compare also Date and Time Digitized
in the Resource Creation Vocabulary. See also the [wikipedia IS0 8601
entry](http://en.wikipedia.org/wiki/ISO_8601) for further explanation
and examples.

Term Name: ac:timeOfDay

Normative URI:

http://rs.tdwg.org/ac/terms/timeOfDay

Label

Time of Day

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

Free text information beyond exact clock times.

Defined by:

[This item.](#timeOfDay)

Notes:

Examples in English: *afternoon*,
*twilight*.



## <span id="Taxonomic_Coverage_Vocabulary" class="mw-headline">Taxonomic Coverage Vocabulary</span>

Term Name: ac:taxonCoverage

Normative URI:

http://rs.tdwg.org/ac/terms/taxonCoverage

Label

Taxon Coverage

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

A higher taxon (e. g., a genus, family, or order) at the level of the
genus or higher, that covers all taxa that are the primary subject of
the resource (which may be a media item or a collection).

Defined by:

<http://rs.tdwg.org/ontology/voc/Collection#taxonCoverage>

Notes:

Example: Where the subject of an image is several species of ducks with
trees visible in the background, Taxon Coverage would still be Anatidae
(and not Biota). Example: “Aves” for a bird key or a bird image
collection. Do not add a rank (“Class Aves”) in this field. Note that
this somewhat expands the usage of
[ncd:taxonCoverage](http://rs.tdwg.org/ontology/voc/Collection#taxonCoverage)
which, however has not yet been adopted by TDWG, and which specifies at
the Family level or higher. For collections it is recommended to follow
ncd:taxonCoverage to avoid conflicts between an AC record and a record
arising from use of the un-adopted NCD. If the resource contains a
single taxon, this should be placed in Scientific Taxon Name. In this
case Taxon Coverage may be left empty, but if not, care should be taken
that the entries do not conflict. Example: If Scientific Taxon Name is
*Quercus alba* then Taxon Coverage, if provided at all, should be
*Quercus*.

Term Name: dwc:scientificName

Normative URI:

http://rs.tdwg.org/dwc/terms/scientificName

Label

Scientific Taxon Name

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

Scientific names of taxa represented in the media resource (with date
and name authorship information if available) of the lowest level
taxonomic rank that can be applied.

Defined by:

[dwc:scientificName](http://rs.tdwg.org/dwc/terms/#scientificName)

Notes:

The Scientific Taxon Name may possibly be of a higher rank, e.g., a
genus or family name, if this is the most specific identification
available. Where multiple taxa are the subject of the media item,
multiple names may be given. If possible, add this information here even
if the title or caption of the resource already contains scientific
taxon names. Where the list of scientific taxon names is impractically
large (e.g., media collections or identification tools), the number of
taxa should be given in [Taxon Count](#Taxon_Count) (see below). If
possible, avoid repeating the [Taxonomic Coverage](#Taxonomic_Coverage)
here. Do not use abbreviated Genus names ("P. vulgaris"). It is
recommended to provide author citation to scientific names, to avoid
ambiguities in the presence of homonyms (the same name created by
different authors for different taxa). Identifier qualifications should
be supplied in the Identification Qualifier term rather than here (i. e.
“Abies cf. alba” is deprecated, to be replaced with Scientific Taxon
Name = “Abies alba” and Identification Qualifier = “cf. species”).

Term Name: dwc:identificationQualifier

Normative URI:

http://rs.tdwg.org/dwc/terms/identificationQualifier

Label

Identification Qualifier

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

A brief phrase or a standard abbreviation ("cf. genus", "cf. species",
"cf. var.", "aff. species", etc.) to express the determiner's doubts
with respect to a specified taxonomic rank about the identification
given in [Scientific Taxon Name](#Scientific_Taxon_Name).

Defined
by:

[dwc:identificationQualifier](http://rs.tdwg.org/dwc/terms/#identificationQualifier)

Notes:

Splitting identification qualification and [Scientific Taxon
Name](#Scientific_Taxon_Name) into separate fields is recommended
practice in cases where only a single taxon name is available, or if the
exchange format is able to keep relations between multiple names and
identification qualifiers. Where the exchange format only supports
simple multiplicities, a media item with multiple [Scientific Taxon
Names](#Scientific_Taxon_Name), some with, some without identification
qualifiers, may have to be transferred with "cf." or "aff." qualifiers
remaining embedded in the [Scientific Taxon
Name](#Scientific_Taxon_Name).

For discussion of Darwin Core usage see
[here](http://code.google.com/p/darwincore/wiki/Identification).

Example: For the determinations “cf. Fusarium oxysporum f. sp.
palmarum”, “Fusarium cf. oxysporum f. sp. palmarum”, “Fusarium
oxysporum cf. f. sp. palmarum” the Scientific Taxon Name would always be
“Fusarium oxysporum f. sp. palmarum”, with Identification Qualifier “cf.
genus”, “cf. species” and “cf. f.sp.”, respectively. In most cases only
the lowest taxon is in doubt, but cases exist where good reasons exist
to suspect a specific or even infraspecific determination, without
having a save generic identification.

Term Name: dwc:vernacularName

Normative URI:

http://rs.tdwg.org/dwc/terms/vernacularName

Label

Common Name

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

Common (= vernacular) names of the subject in one or several languages.
The ISO language name should be given in parentheses after the name if
not all names are given by values of the Metadata Language term.

Defined by:

[dwc:vernacularName](http://rs.tdwg.org/dwc/terms/#vernacularName)

Notes:

The ISO language code after the name should be formatted as in the
following example: 'abete bianco (it); Tanne (de); White Fir (en)'. If
names are known to be male- or female-specific, this may be specified as
in: 'ewe (en-female); ram (en-male);'.

Term Name: dwc:nameAccordingTo

Normative URI:

http://rs.tdwg.org/dwc/terms/nameAccordingTo

Label

Name According To

 

**Layer:** 2 — **Required:** No — **Repeatable:** Yes

Definition:

The taxonomic authority used to apply the name to the taxon, e. g., a
person, book or web service.

Defined by:

[dwc:nameAccordingTo](http://rs.tdwg.org/dwc/terms/#nameAccordingTo)

Notes:

Examples are "Flora of North America", "Landrum 1981, Monograph of the
Genus Myrceugenia (Myrtaceae)", "Peterson Field Guide to Birds of North
America", or "Expert identification by J.Smith". The definition at
[dwc:nameAccordingTo](http://rs.tdwg.org/dwc/terms/#nameAccordingTo) is:
'The reference to the source in which the specific taxon concept
circumscription is defined or implied - traditionally signified by the
Latin "sensu" or "sec." (from secundum, meaning "according to"). For
taxa that result from identifications, a reference to the keys,
monographs, experts and other sources should be given.'

Term Name: dwc:scientificNameID

Normative URI:

http://rs.tdwg.org/dwc/terms/scientificNameID

Label

Scientific Name ID

 

**Layer:** 2 — **Required:** No — **Repeatable:** Yes

Definition:

An identifier for the nomenclatural (not taxonomic) details of a
scientific name.

Defined by:

See
[dwc:scientificNameID](http://rs.tdwg.org/dwc/terms/#scientificNameID)
and also the [DwC Taxon
attributes](http://code.google.com/p/darwincore/wiki/Taxon).

Term Name: ac:otherScientificName

Normative URI:

http://rs.tdwg.org/ac/terms/otherScientificName

Label

Other Scientific Name

 

**Layer:** 2 — **Required:** No — **Repeatable:** Yes

Definition:

One or several Scientific Taxon Names that are synonyms to the
Scientific Taxon Name may be provided here.

Defined by:

[This item.](#otherScientificName)

Notes:

The primary purpose of this is in support of resource discovery, not
developing a taxonomic synonymy. Misidentification or misspellings may
thus be of interest. Where multiple taxa are present in a resource and
multiple [Scientific Taxon Names](#Scientific_Taxon_Name) are given, the
association between synonyms and names may not be deducible from the AC
record alone.

Term Name: dwc:identifiedBy

Normative URI:

http://rs.tdwg.org/dwc/terms/identifiedBy

Label

Identified By

 

**Layer:** 2 — **Required:** No — **Repeatable:** Yes

Definition:

The name(s) of the person(s) who applied the [Scientific Taxon
Name](#Scientific_Taxon_Name) to the media item or the occurrence
represented in the media item.

Defined by:

[dwc:identifiedBy](http://rs.tdwg.org/dwc/terms/#identifiedBy)

Term Name: dwc:dateIdentified

Normative URI:

http://rs.tdwg.org/dwc/terms/dateIdentified

Label

Date Identified

 

**Layer:** 2 — **Required:** No — **Repeatable:** No

Definition:

The date on which the person(s) given under [Identfied
By](#Identified_By) applied a [Scientific Taxon
Name](#Scientific_Taxon_Name) to the resource.

Defined by:

[dwc:dateIndentified](http://rs.tdwg.org/dwc/terms/#dateIndentified)

Term Name: ac:taxonCount

Normative URI:

http://rs.tdwg.org/ac/terms/taxonCount

Label

Taxon Count

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

An exact or estimated number of taxa at the lowest applicable taxon rank
(usually species or infraspecific) represented by the media resource
(item or collection).

Defined by:

[This item.](#taxonCount)

Notes:

Primarily intended for resource collections and singular resources
dealing with sets of taxa (e. g., identification tools, videos). It is
recommended to give an exact or estimated number of specific taxa when a
complete list of taxa is not available or practical. The count should
contain only the taxa covered fully or primarily by the resource. For a
taxon page and most images this will be “1”, i. e. other taxa mentioned
on the side or in the background should not be counted. However,
sometimes a resource may illustrate an ecological or behavioral entity
with multiple species, e. g., a host-pathogen interaction; taxon count
would then indicate the known number of species in this interaction.
This should be a single integer number. Leave the field empty if you
cannot estimate the information (do not enter 0). Additional taxon
counts at higher levels (e. g. how many families are covered by a
digital Fauna) should be given verbatim in the resource description, not
here.

Term Name: ac:subjectPart

Normative URI:

http://rs.tdwg.org/ac/terms/subjectPart

Label

Subject Part

 

**Layer:** 2 — **Required:** No — **Repeatable:** Yes

Definition:

The portion or product of organism morphology, behaviour, environment,
etc. that is either predominantly shown or particularly well exemplified
by the media resource.

Defined by:

[This item.](#subjectPart)

Notes:

No formal encoding scheme as yet exists. Examples are "whole body",
"head", "flower", "leaf", "canopy" (of a rain forest stand). Several
anatomical ontologies are emerging in <http://www.obofoundry.org/>

Term Name: dwc:sex

Normative URI:

http://rs.tdwg.org/dwc/terms/sex

Label

Subject Sex

 

**Layer:** 2 — **Required:** No — **Repeatable:** Yes

Definition:

A description of the sex of any organisms featured within the media,
when relevant to the subject of the media, e. g., male, female,
hermaphrodite, dioecious.

Defined by:

[dwc:sex](http://rs.tdwg.org/dwc/terms/#sex)

Term Name: dwc:lifeStage

Normative URI:

http://rs.tdwg.org/dwc/terms/lifeStage

Label

Subject Life Stage

 

**Layer:** 2 — **Required:** No — **Repeatable:** Yes

Definition:

A description of the life-cycle stage of any organisms featured within
the media, when relevant to the subject of the media, e. g., larvae,
juvenile, adult.

Defined by:

[dwc:lifeStage](http://rs.tdwg.org/dwc/terms/#lifeStage)

Term Name: ac:subjectOrientation

Normative URI:

http://rs.tdwg.org/ac/terms/subjectOrientation

Label

Subject Orientation

 

**Layer:** 2 — **Required:** No — **Repeatable:** Yes

Definition:

Specific orientation (= direction, view angle) of the subject
represented in the media resource with respect to the acquisition
device.

Defined by:

[This item.](#subjectOrientation)

Notes:

Examples: "dorsal", "ventral", "frontal", etc. No formal encoding scheme
as yet exists. The term is repeatable e.g., in the case of a composite
image, consisting of a combination of different view orientations.

Term Name: dwc:preparations

Normative URI:

http://rs.tdwg.org/dwc/terms/preparations

Label

Subject Preparation Technique

 

**Layer:** 2 — **Required:** No — **Repeatable:** No

Definition:

Free form text describing the techniques used to prepare the subject of
the media, prior to or while creating the media resource.

Defined by:

[dwc:preparations](http://rs.tdwg.org/dwc/terms/#preparations)

Notes:

Examples for such techniques are: Insect under CO<sub>2</sub>, cooled to
immobility, preservation with ethanol or formaldehyde. See also
[Resource Creation Technique](#Resource_Creation_Technique) for
technical aspects of digital media object
creation.



## <span id="Resource_Creation_Vocabulary" class="mw-headline">Resource Creation Vocabulary</span>

Term Name: Iptc4xmpExt:LocationCreated

Normative URI:

http://iptc.org/std/Iptc4xmpExt/2008-02-29/LocationCreated

Label

Location Created

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

The location at which the media recording instrument was placed when the
media was created.

Defined by:

IPTC terms have URIs that are not resolvable, but AC follows the URI
namespace usage of the Adobe XMP implementation of IPTC terms described
in [IPTC Standard Photo Metadata
(July 2010)](http://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-201007_1.pdf).

Notes:

The distinction between the location shown and created is often
irrelevant, and metadata may be assumed to be referring to location
shown. It is recommended that the [Location Shown](#Location_Shown)
field above always be used when known. However, in the case of position
data automatically recorded by the instrument (e. g. EXIF GPS data)
[Location Created](#Location_Created) should be used to maintain
information accuracy. When one but not both of these locations are
present, AC is silent about whether the provided one entails the other.
A best practices document for a particular AC implementation might
address this.

Term Name: ac:digitizationDate

Normative URI:

http://rs.tdwg.org/ac/terms/digitizationDate

Label

Date and Time Digitized

 

**Layer:** 2 — **Required:** No — **Repeatable:** No

Definition:

Date the first digital version was created, if different from [Original
Date and Time](#Original_Date_and_Time) found in the [Temporal Coverage
Vocabulary](#Temporal_Coverage_Vocabulary). The date and time must
comply with the World Wide Web Consortium ([W3C](http://www.w3.org))
[datetime practice](http://www.w3.org/TR/NOTE-datetime), which requires
that date and time representation correspond to ISO 8601:1998, but with
year fields always comprising 4 digits. This makes datetime records
compliant with
[8601:2004](http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=40874).
AC datetime values may also follow 8601:2004 for ranges by separating
two IS0 8601 datetime fields by a solidus ("forward slash", '/'). See
also the [wikipedia IS0 8601
entry](http://en.wikipedia.org/wiki/ISO_8601) for further explanation
and examples.

Defined by:

[This item.](#digitizationDate)

Notes:

This is often *not* the media creation or modification date. For
example, if photographic prints have been scanned, the date of that
scanning is what this term carries, but Original Date and Time is that
depicted in the print. Use the international (ISO/xml) format
yyyy-mm-ddThh:mm (e. g. "2007-12-31" or "2007-12-31T14:59"). Where
available, timezone information should be added. In the case of digital
images containing EXIF, whereas the EXIF capture date does not contain
time zone information, but EXIF GPSDateStamp and GPSTimeStamp may be
relevant as these include time-zone information. Compare also MWG
(2010)<sup>[\[9\]](#cite_note-MWG2010-9)</sup>, which has best practice
advice on handling time-zone-less EXIF date/time data. See also the
[wikipedia IS0 8601 entry](http://en.wikipedia.org/wiki/ISO_8601) for
further explanation and examples.

Term Name: ac:captureDevice

Normative URI:

http://rs.tdwg.org/ac/terms/captureDevice

Label

Capture Device

 

**Layer:** 2 — **Required:** No — **Repeatable:** No

Definition:

Free form text describing the device or devices used to create the
resource.

Defined by:

[This item.](#captureDevice)

Notes:

It is best practice to record the device; this may include a combination
such as camera plus lens, or camera plus microscope. Examples: "Canon
Supershot 2000", "Makroscan Scanner 2000", "Zeiss Axioscope with Camera
IIIu", "SEM (Scanning Electron Microscope)".

Term Name: ac:resourceCreationTechnique

Normative URI:

http://rs.tdwg.org/ac/terms/resourceCreationTechnique

Label

Resource Creation Technique

 

**Layer:** 2 — **Required:** No — **Repeatable:** No

Definition:

Information about technical aspects of the creation and digitization
process of the resource. This includes modification steps ("retouching")
after the initial resource capture.

Defined by:

[This item.](#resourceCreationTechnique)

Notes:

Examples: Encoding method or settings, numbers of channels, lighting,
audio sampling rate, frames per second, data rate, interlaced or
progressive, multiflash lighting, remote control, automatic interval
exposure.

Annotating whether and how a resource has been modified or edited
significantly in ways that are not immediately obvious to, or expected
by, consumers is of special significance. Examples for images are:
Removing a distracting twig from a picture, moving an object to a
different surrounding, changing the color in parts of the image, or
blurring the background of an image. Modifications that are standard
practice and expected or obvious are not necessary to document; examples
of such practices include changing resolution, cropping, minor
sharpening or overall color correction, and clearly perceptible
modifications (e.g., addition of arrows or labels, or the placement of
multiple pictures into a table.) If it is only known that significant
modifications were made, but no details are known, a general statement
like “Media may have been manipulated to improve appearance” may be
appropriate.

See also Subject Preparation
Technique.



## <span id="Related_Resources_Vocabulary" class="mw-headline">Related Resources Vocabulary</span>

Term Name: ac:IDofContainingCollection

Normative URI:

http://rs.tdwg.org/ac/terms/IDofContainingCollection

Label

ID of Containing Collection

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

If the resource is contained in a Collection, this field identifies that
Collection uniquely. Its form is not specified by this normative
document, but is left to implementers of specific implementations.

Defined by:

[This item.](#IDofContainingCollection)

Notes:

Repeatable: A media resource may be member of multiple collections

Term Name: ac:relatedResourceID

Normative URI:

http://rs.tdwg.org/ac/terms/relatedResourceID

Label

Related Resource ID

 

**Layer:** 2 — **Required:** No — **Repeatable:** Yes

Definition:

Resource related in ways not specified through a collection, e.g.,
before-after images; time-lapse series; different orientations/angles of
view

Defined by:

[This item.](#relatedResourceID)

Notes:

The value references a related media item. Examples of relations are:
Images taken in a sequence or defined time series, an exposure or focus
series (e.g. for stacking), different framing or views (top, side,
bottom) of the same subject, or an overview plus several details. The
property makes such related media items discoverable, but does not
indicate the nature of this relationship. More specific properties may
be defined in a later version of AC.

Term Name: ac:providerID

Normative URI:

http://rs.tdwg.org/ac/terms/providerID

Label

Provider ID

 

**Layer:** 2 — **Required:** No — **Repeatable:** No

Definition:

A globally unique ID of the provider of the current AC metadata record.

Defined by:

[This item.](#providerID)

Notes:

Only to be used if the annotated resource is not a provider itself -
this item is for relating the resource to a provider, using an arbitrary
code that is unique for a provider, contributing partner, or aggregator,
or other roles (potentially defined by MARC, OAI) and by which the media
resources are linked to the provider.

Term Name: ac:derivedFrom

Normative URI:

http://rs.tdwg.org/ac/terms/derivedFrom

Label

Derived From

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

A reference to an original resource from which the current one is
derived.

Defined by:

[This item.](#derivedFrom)

Notes:

Derivation of one resource from another is of special interest for
identification tools (e. g. a key from an unpublished data set, as in
FRIDA, or a PDA key from a PC or web key) or web services (e. g. a name
synonymization service being derived from a specific data set). It may
very rarely also be known where one image or sound recording is derived
from another (but compare the separate mechanism to be used for
quality/resolution levels). – Human readable, or doi number, or URL.
Simple name of parent for human readable. Can be repeated if a montage
of images.

Term Name: ac:associatedSpecimenReference

Normative URI:

http://rs.tdwg.org/ac/terms/associatedSpecimenReference

Label

Associated Specimen Reference

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

A reference to a specimen associated with this resource.

Defined by:

[This item.](#associatedSpecimenReference)

Notes:

Supports finding a specimen resource, where additional information is
available. If several resources relate to the same specimen, these are
implicitly related. Examples: for NHM “BM 23974324” for a barcoded or
“BM Smith 32” for a non-barcoded specimen; for UNITS: “TSB 28637”; for
PMSL: “PMSL-Lepidoptera-2534781”. Ideally this may be a URI identifying
a specimen record that is available online.

Term Name: ac:associatedObservationReference

Normative URI:

http://rs.tdwg.org/ac/terms/associatedObservationReference

Label

Associated Observation Reference

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

A reference to an observation associated with this resource.

Defined by:

[This
item.](#associatedObservationReference)



## <span id="Service_Access_Point_Vocabulary" class="mw-headline">Service Access Point Vocabulary</span>

These terms are representation-dependent metadata, referring to specific
digital representations of a resource (e.g., a specific resolution,
quality, or format). They are used within whatever a particular AC
implementation assigns to the value of
[hasServiceAccessPoint](#hasServiceAccessPoint), whose label is simply
"Service Access Point." Note that it is possible for an implementation
to use syntactic conventions that avoid direct use of
hasServiceAccessPoint, as illustrated in the final example in the
section
**[Multiplicity/Cardinality](/wiki/Audubon_Core_Structure#Multiplicity.2FCardinality "Audubon Core Structure")**
in the normative document [Audubon Core
Structure](/wiki/Audubon_Core_Structure "Audubon Core Structure").

Term Name: ac:accessURI

Normative URI:

http://rs.tdwg.org/ac/terms/accessURI

Label

Access URI

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

A URI that uniquely identifies a service that provides a representation
of the underlying resource. If this resource can be acquired by an http
request, its http URL should be given. If not, but it has some URI in
another URI scheme, that may be given here.

Defined by:

[This item.](#accessURI)

Notes:

Value might point to something offline, such as a published CD, etc. For
example, the doi of an published CD would be a suitable value.

Term Name: dc:format

Normative URI:

http://purl.org/dc/elements/1.1/format

Label

Format

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

A string describing the technical format of the resource (file format or
physical medium).

Defined by:

[dc:format](http://purl.org/dc/elements/1.1/format)

Notes:

Recommended best practice is to use a controlled vocabulary such as the
list of Internet Media Types \[MIME\]. This term is recommended for
offline digital content. In cases where the provided URL includes a
standard file extension from which the format can be inferred, it is
permissible to not provide this item.

Three types of values are recommended: (a) any MIME type; (b) common
file extensions like txt, doc, odf, jpg/jpeg, png, pdf; (c) the
following special values: Data-CD, Audio-CD, Video-CD, Data-DVD,
Audio-DVD, Video-DVD-PAL, Video-DVD-NTSC, photographic slide,
photographic print. Compare Type for the content-type.



**See also** the entry for [**dcterms:format**](#dcterms:format) in this
document and see the **[DCMI FAQ on DC and DCTERMS
Namespaces](http://wiki.dublincore.org/index.php/FAQ/DC_and_DCTERMS_Namespaces)**
for discussion of the rationale for terms in two namespaces. Normal
practice is to use the same Label if both are provided. Labels have no
effect on information discovery and are only suggestions.

Term Name: dcterms:format

Normative URI:

http://purl.org/dc/terms/format

Label

Format

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

URI referencing the technical format of the resource (file format or
physical medium).

Defined
by:

[dcterms:format](http://dublincore.org/documents/dcmi-terms/#terms-format)

Notes:

See [DCMI
User\_Guide](http://wiki.dublincore.org/index.php/User_Guide/Publishing_Metadata#dcterms:format)
for examples. **See also** the entry for [**dc:format**](#dc:format) in
this document and see the **[DCMI FAQ on DC and DCTERMS
Namespaces](http://wiki.dublincore.org/index.php/FAQ/DC_and_DCTERMS_Namespaces)**
for discussion of the rationale for terms in two namespaces. Normal
practice is to use the same Label if both are provided. Labels have no
effect on information discovery and are only suggestions.

Term Name: ac:variantLiteral

Normative URI:

http://rs.tdwg.org/ac/terms/variantLiteral

Label

Variant

 

**Layer:** 2 — **Required:** No — **Repeatable:** Yes

Definition:

Text that describes this Service Access Point variant.

Defined by:

[This item.](#variantLiteral)

Notes:

This is an alternative to ac:variant where using a string is preferred
over a URI. It is best practice to use ac:variant instead of
ac:variantLiteral wherever practical. Value may be free text, but it is
suggested to consider including terminology based on the following:  

  - Thumbnail: Service Access Point provides a thumbnail image, short
    sound clip, or short movie clip that can be used in addition to the
    resource to represent the media object, typically at lower quality
    and higher compression than a preview object. A typical size for a
    tiny thumbnail image may be 50-100 pixels in the longer dimension.
  - Trailer: Service Access Point provides video clip preview, in the
    form of a specifically authored "Trailer", which may provide
    somewhat different content than the original resource.
  - Lower Quality: Service Access Point provides a lower quality version
    of the media resource, suitable e. g. for web sites.
  - Medium Quality: Service Access Point provides a medium quality
    version of the media resource, e. g. shortened in duration, or
    reduced size, using lower resolution or higher compression causing
    moderate artifacts.
  - Good Quality: Service Access Point provides a good quality version
    of the media resource intended for resources displayed as primary
    information; e. g. an image between 800 and 1600 px in width or
    height.
  - Best Quality: Service Access Point provides the highest available
    quality of the media resource, whatever its resolution or quality
    level.
  - Offline: Service Access Point provides data about an offline
    resource.

Term Name: ac:variant

Normative URI:

http://rs.tdwg.org/ac/terms/variant

Label

Variant

 

**Layer:** 1 — **Required:** No — **Repeatable:** Yes

Definition:

A URI designating what this Service Access Point provides. Some
suggested values are the URIs ac:Thumbnail, ac:Trailer, ac:LowerQuality,
ac:MediumQuality, ac:GoodQuality, ac:BestQuality, and ac:Offline.
Additional URIs from communities of practice may be introduced.

Defined by:

[This item.](#variant)

Term Name: ac:variantDescription

Normative URI:

http://rs.tdwg.org/ac/terms/variantDescription

Label

Variant Description

 

**Layer:** 2 — **Required:** No — **Repeatable:** No

Definition:

Text that describes this Service Access Point variant

Defined by:

[This item.](#variantDescription)

Notes:

Most variants (thumb, low-res, high-res) are self-explanatory and it is
best practice to leave this property empty if no special description is
needed. It is provided for cases that require additional information
(e.g., video shortened instead of simply quality reduced).

Term Name: ac:furtherInformationURL

Normative URI:

http://rs.tdwg.org/ac/terms/furtherInformationURL

Label

Further Information URL

 

**Layer:** 2 — **Required:** No — **Repeatable:** No

Definition:

The URL of a Web site that provides additional information about the
version of the media resource that is provided by the Service Access
Point.

Defined by:

[This item.](#furtherInformationURL)

Term Name: ac:licensingException

Normative URI:

http://rs.tdwg.org/ac/terms/licensingException

Label

Licensing Exception Statement

 

**Layer:** 2 — **Required:** No — **Repeatable:** No

Definition:

The licensing statement for this variant of the media resource if
different from that given in the License Statement property of the
resource.

Defined by:

[This item.](#licencingException)

Notes:

Required only if this version has different licensing than that of the
media resource. For example, the highest resolution version may be more
restricted than lower resolution versions

Term Name: ac:serviceExpectation

Normative URI:

http://rs.tdwg.org/ac/terms/serviceExpectation

Label

Service Expectation

 

**Layer:** 2 — **Required:** No — **Repeatable:** No

Definition:

A term that describes what service expectations users may have of the
ac:accessURL. Recommended terms include *online* (denotes that the URL
is expected to deliver the resource), *authenticate* (denotes that the
URL delivers a login or other authentication interface requiring
completion before delivery of the resource) *published(non digital)*
(denotes that the URL is the identifier of a non-digital published work,
for example a doi.) Communities should develop their own controlled
vocabularies for Service Expectations.

Defined by:

[This item.](#serviceExpectation)

Term Name: ac:hashFunction

Normative URI:

http://rs.tdwg.org/ac/terms/hashFunction

Label

Hash Function

 

**Layer:** 2 — **Required:** No — **Repeatable:** No

Definition:

The cryptographic hash function used to compute the value given in the
Hash Value.

Defined by:

[This item.](#hashFunction)

Notes:

Recommended values include MD5, SHA-1, SHA-224,SHA-256, SHA-384,
SHA-512, SHA-512/224 and SHA-512/256.

Term Name: ac:hashValue

Normative URI:

http://rs.tdwg.org/ac/terms/hashValue

Label

Hash

 

**Layer:** 2 — **Required:** No — **Repeatable:** No

Definition:

The value computed by a hash function applied to the media that will be
delivered at the access point.

Defined by:

[This item.](#hashValue)

Notes:

Best practice is to also specify the hash function by supplying a value
of the [Hash Function](#Hash_Function) term, using one of the standard
literals from the Notes there.

Term Name: exif:PixelXDimension

Normative URI:

http://ns.adobe.com/exif/1.0/PixelXDimension

Label

Image Width

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

The width in pixels of the media specified by the access point.

Defined by:

Terms for Adobe XMP have URIs that are not resolvable. Instead, visit [,
XMP Specification Part 2,
Sec 3.4.2](http://www.adobe.com/content/dam/Adobe/en/devnet/xmp/pdfs/XMPSpecificationPart2.pdf)
for further documentation.

Term Name: exif:PixelYDimension

Normative URI:

http://ns.adobe.com/exif/1.0/PixelYDimension

Label

Image Height

 

**Layer:** 1 — **Required:** No — **Repeatable:** No

Definition:

The height in pixels of the media specified by the access point.

Defined by:

Terms for Adobe XMP have URIs that are not resolvable. Instead, visit [,
XMP Specification Part 2,
Sec 3.4.2](http://www.adobe.com/content/dam/Adobe/en/devnet/xmp/pdfs/XMPSpecificationPart2.pdf)
for further
    documentation.



<div>

# <span id="References" class="mw-headline">References</span>

1.  <span id="cite_note-1"><span class="mw-cite-backlink">[↑](#cite_ref-1)</span>
    <span class="reference-text">NASA Global Change Master Directory
    <http://gcmd.nasa.gov/></span></span>
2.  <span id="cite_note-2"><span class="mw-cite-backlink">[↑](#cite_ref-2)</span>
    <span class="reference-text">Subject Categories defined in Key to
    Nature: <http://www.keytonature.eu/wiki/Subject_Category>
    </span></span>
3.  <span id="cite_note-3"><span class="mw-cite-backlink">[↑](#cite_ref-3)</span>
    <span class="reference-text">BioComplexity Thesaurus
    <http://thesaurus.nbii.gov></span></span>
4.  <span id="cite_note-4"><span class="mw-cite-backlink">[↑](#cite_ref-4)</span>
    <span class="reference-text"> GBIF Description Types
    <http://rs.gbif.org/vocabulary/gbif/description_type.xml>
    </span></span>
5.  <span id="cite_note-5"><span class="mw-cite-backlink">[↑](#cite_ref-5)</span>
    <span class="reference-text"> Species Profile Model
    (<http://rs.tdwg.org/ontology/voc/SPMInfoItems.rdf>
    </span></span>
6.  <span id="cite_note-6"><span class="mw-cite-backlink">[↑](#cite_ref-6)</span>
    <span class="reference-text">Plinian Core
    (<http://www.gbif.es/plinian/doku.php>)</span></span>
7.  <span id="cite_note-7"><span class="mw-cite-backlink">[↑](#cite_ref-7)</span>
    <span class="reference-text">GEMET
    <http://www.eionet.europa.eu/gemet></span></span>
8.  <span id="cite_note-8"><span class="mw-cite-backlink">[↑](#cite_ref-8)</span>
    <span class="reference-text">LTER Controlled Vocabulary
    <http://vocab.lternet.edu/> </span></span>
9.  <span id="cite_note-MWG2010-9"><span class="mw-cite-backlink">↑
    <sup>[9.0](#cite_ref-MWG2010_9-0)</sup>
    <sup>[9.1](#cite_ref-MWG2010_9-1)</sup></span>
    <span class="reference-text">(MWG 2010) Metadata Working Group
    Guidelines for Handling Image Metadata, Version 2.0,November 2010
    <http://www.metadataworkinggroup.org/pdf/mwg_guidance.pdf>
    </span></span>

-----

</div>

<div class="printfooter">

Retrieved from
"<https://terms.tdwg.org/w/index.php?title=Audubon_Core_Term_List&oldid=36898>"

</div>

<div id="catlinks" class="catlinks">

<div id="mw-normal-catlinks" class="mw-normal-catlinks">

[Classes](/wiki/Special:Categories "Special:Categories"):

  - [Pages using duplicate arguments in template
    calls](/w/index.php?title=Class:Pages_using_duplicate_arguments_in_template_calls&action=edit&redlink=1 "Class:Pages using duplicate arguments in template calls (page does not exist)")
  - [Audubon
Core](/wiki/Class:Audubon_Core "Class:Audubon Core")

</div>

</div>

<div class="visualClear">

</div>

<div id="mw-navigation">

## Navigation menu

<div id="mw-head">

<div id="p-personal" data-role="navigation" data-aria-labelledby="p-personal-label">

### Personal tools

  - <span id="pt-uls">[English](#)</span>
  - <span id="pt-login">[Log
    in](/w/index.php?title=Special:UserLogin&returnto=Audubon+Core+Term+List "You are encouraged to log in; however, it is not mandatory [o]")</span>
  - <span id="pt-createaccount">[Request
    account](/wiki/Special:RequestAccount "You are encouraged to create an account and log in; however, it is not mandatory")</span>
  - <span id="pt-openidlogin">[Use
    OpenID](/w/index.php?title=Special:OpenIDLogin&returnto=Audubon_Core_Term_List)</span>

</div>

<div id="left-navigation">

<div id="p-namespaces" class="vectorTabs" data-role="navigation" data-aria-labelledby="p-namespaces-label">

### Namespaces

  - <span id="ca-nstab-main"><span>[Page](/wiki/Audubon_Core_Term_List "View the content page [c]")</span></span>
  - <span id="ca-talk"><span>[Discussion](/w/index.php?title=Talk:Audubon_Core_Term_List&action=edit&redlink=1 "Discussion about the content page [t]")</span></span>

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

  - <span id="ca-view"><span>[Read](/wiki/Audubon_Core_Term_List)</span></span>
  - <span id="ca-form_edit"><span>[View
    form](/w/index.php?title=Audubon_Core_Term_List&action=formedit)</span></span>
  - <span id="ca-viewsource"><span>[View
    source](/w/index.php?title=Audubon_Core_Term_List&action=edit "This page is protected.
    You can view its source [e]")</span></span>
  - <span id="ca-history"><span>[View
    history](/w/index.php?title=Audubon_Core_Term_List&action=history "Past revisions of this page [h]")</span></span>

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
    here](/wiki/Special:WhatLinksHere/Audubon_Core_Term_List "A list of all wiki pages that link here [j]")</span>
  - <span id="t-recentchangeslinked">[Related
    changes](/wiki/Special:RecentChangesLinked/Audubon_Core_Term_List "Recent changes in pages linked from this page [k]")</span>
  - <span id="t-upload">[Upload
    file](//species-id.net/openmedia/Special:UploadWizard?uselang=en "Upload files [u]")</span>
  - <span id="t-specialpages">[Special
    pages](/wiki/Special:SpecialPages "A list of all special pages [q]")</span>
  - <span id="t-print">[Printable
    version](/w/index.php?title=Audubon_Core_Term_List&printable=yes "Printable version of this page [p]")</span>
  - <span id="t-permalink">[Permanent
    link](/w/index.php?title=Audubon_Core_Term_List&oldid=36898 "Permanent link to this revision of the page")</span>
  - <span id="t-info">[Page
    information](/w/index.php?title=Audubon_Core_Term_List&action=info "More information about this page")</span>
  - <span id="t-smwbrowselink">[Browse
    properties](/wiki/Special:Browse/Audubon_Core_Term_List)</span>
  - <span id="t-cite">[Cite this
    page](/w/index.php?title=Special:CiteThisPage&page=Audubon_Core_Term_List&id=36898 "Information on how to cite this page")</span>

</div>

</div>

</div>

</div>

<div id="footer" data-role="contentinfo">

  - <span id="footer-info-lastmod">This page was last modified on 26
    September 2015, at 20:39.</span>
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
