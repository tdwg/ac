<a id="top"></a>

# Audubon Core Term List

For introductory material, see the **[Audubon Core
Structure](Audubon_Core_Structure)**
and the introductory **[Audubon
Core](Audubon_Core)**
documents.

**Title:** Audubon Core Term List

**Date version issued:** 2013-10-23

**Date created:** 2013-10-23

**Part of TDWG Standard:** http://www.tdwg.org/standards/638/.

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
may not be changed without due process. A second version of Audubon
Core, [Audubon Core
Development](Audubon_Core_Development),
will reflect the ongoing documentation changes and draft enhancements.

**Contributors:** Robert A. Morris, Vijay Barve, Mihail Carausu, Vishwas
Chavan, Jos√© Cuadra, Chris Freeland, Gregor Hagedorn, Patrick Leary,
Dimitry Mozzherin, Annette Olson, Greg Riccardi, Ivan Teage

**Creator:** GBIF/TDWG Multimedia Resources Task Group

**Bibliographic citation:** Multimedia Resources Task Group. 2013. Audubon Core Term List. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/ac/doc/termlist/

## Table of Contents

<a href='#Introduction'>1 Introduction</a><br/>
<a href='#Borrowed_Vocabulary'>2 Borrowed Vocabulary</a><br/>
<a href='#Namespaces.2C_Prefixes_and_Term_Names'>3 Namespaces, Prefixes and Term Names</a><br/>
<a href='#Layers'>4 Layers</a><br/>
<a href='#Literal-_vs._URI-valued_Terms'>5 Literal- vs. URI-valued Terms</a><br/>
<a href='#Vocabulary_Indices'>6 Vocabulary Indices</a><br/>
<a href='#Index_By_Term_Name'>6.1 Index By Term Name</a><br/>
<a href='#Index_By_Label'>6.2 Index By Label</a><br/>
<a href='#Vocabularies'>7 Vocabularies</a><br/>
<a href='#Management_Vocabulary'>7.1 Management Vocabulary</a><br/>
<a href='#Attribution_Vocabulary'>7.2 Attribution Vocabulary</a><br/>
<a href='#Agents_Vocabulary'>7.3 Agents Vocabulary</a><br/>
<a href='#Content_Coverage_Vocabulary'>7.4 Content Coverage Vocabulary</a><br/>
<a href='#Geography_Vocabulary'>7.5 Geography Vocabulary</a><br/>
<a href='#Temporal_Coverage_Vocabulary'>7.6 Temporal Coverage Vocabulary</a><br/>
<a href='#Taxonomic_Coverage_Vocabulary'>7.7 Taxonomic Coverage Vocabulary</a><br/>
<a href='#Resource_Creation_Vocabulary'>7.8 Resource Creation Vocabulary</a><br/>
<a href='#Related_Resources_Vocabulary'>7.9 Related Resources Vocabulary</a><br/>
<a href='#Service_Access_Point_Vocabulary'>7.10 Service Access Point Vocabulary</a><br/>
<a href='#References'>8 References</a><br/>

## <a id="Introduction">1 Introduction</a>

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



## <a id="Borrowed_Vocabulary">2 Borrowed Vocabulary</a>

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



## <a id="Namespaces.2C_Prefixes_and_Term_Names">3 Namespaces, Prefixes and Term Names</a>

The namespace of terms borrowed from other vocabularies is that of the
original. The namespace of de novo AC terms is
http://rs.tdwg.org/ac/terms/. In the table of terms, each term entry has
a row with the term name. This term name is generally an "unqualified
name" preceded by a widely accepted prefix designating an abbreviation
for the namespace It is recommended that implementers who need a
namespace prefix for the AC namespace use "ac". In this web document,
hovering over a term in the **<a href='#Index_By_Term_Name'>Index By Term
Name</a>**
list below will reveal a complete URL that can be used in other web
documents to link to *this* document's treatment of that term, even if
it is from a borrowed vocabulary. It is very important to note that some
vocabularies, e.g those of the
<a href='http://dublincore.org/'>Dublin Core Metadata Initiative (DCMI)</a>,
provide version of the same term in two different namespaces, one
providing for string values and one providing for URIs, even where that
separation is simply a recommendation, not a mandate. See this
**<a href='http://wiki.dublincore.org/index.php/FAQ/DC_and_DCTERMS_Namespaces'>DCMI wiki entry</a>**
on this topic. For vocabularies where such a practice is in place, we
often follow it and signal a reference in the Notes of our term
descriptions to the sister version of the term. An example is the pair
<a href='#dc:type'>dc:type</a>
and
<a href='#dcterms:type'>dcterms:type</a>.
When such a pair allows repeated instances (e.g. as for
<a href='#dc:source'>dc:source</a>
and
<a href='#dcterms:source'>dcterms:source</a>),
particular care may be required in some implementations of AC, because
some implementations may not provide enough structure to clearly state
the association between the members of a pair in the case of multiple
values of each. This is a special case of the issue treated in the
normative material on <a href='https://terms.tdwg.org/wiki/Audubon_Core_Structure#Multiplicity.2FCardinality'>Multiplicity and
Cardinality</a>.



## <a id="Layers">4 Layers</a>

The term set consists of two *Layers*, numbered *1* and *2*. The former
comprise the central terms, likely to be meaningful for most media, even
though only a few are mandatory. Implementers of AC representations
should provide for at least Layer 1 if possible, and application writers
should provide for robust treatment of Layer 1 terms, if only by
ignoring them. Layer 2 terms are more likely to be useful for particular
kinds of media or for applications requiring highly detailed resource
descriptions. Each term description below indicates the Layer to which
the term belongs.



## <a id="Literal-_vs._URI-valued_Terms">5 Literal- vs. URI-valued Terms</a>

Some terms have two versions, one expecting a string literal value and
the other a URI. In these circumstances, the version expecting a string
is named with the suffix "Literal", e.g. ac:metadataLanguageLiteral. In
such cases, both forms may be provided, but care should be taken to
ensure that the uses reflect the same intent. In case of ambiguity, the
URI version prevails. All terms, including those whether or not with a
specific "Literal" suffix, specify in their definition whether the
required values are strings or URIs.



## <a id="Vocabulary_Indices">6 Vocabulary Indices</a>


### <a id="Index_By_Term_Name">6.1 Index By Term Name</a>

(See also <a href='#Index_By_Label'>Index By
Label</a>)

**Management Vocabulary**

|
[dcterms:identifier](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dcterms:identifier)
| |
[dc:type](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dc:type) |
|
[dcterms:type](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dcterms:type)
| |
[ac:subtypeLiteral](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:subtypeLiteral)
| |
[ac:subtype](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:subtype)
| |
[dcterms:title](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dcterms:title)
| |
[dcterms:modified](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dcterms:modified)
| |
[xmp:MetadataDate](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#xmp:MetadataDate)
| |
[ac:metadataLanguageLiteral](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:metadataLanguageLiteral)
| |
[ac:metadataLanguage](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:metadataLanguage)
| |
[ac:providerManagedID](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:providerManagedID)
| |
[xmp:Rating](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#xmp:Rating)
| |
[ac:commenter](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:commenter)
| |
[ac:commenterLiteral](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:commenterLiteral)
| |
[ac:comments](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:comments)
| |
[ac:reviewer](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:reviewer)
| |
[ac:reviewerLiteral](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:reviewerLiteral)
| |
[ac:reviewerComments](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:reviewerComments)
| |
[dcterms:available](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dcterms:available)
| |
[ac:hasServiceAccessPoint](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:hasServiceAccessPoint)
|

**Attribution Vocabulary**

|
[dc:rights](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dc:rights)
| |
[dcterms:rights](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dcterms:rights)
| |
[xmpRights:Owner](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#xmpRights:Owner)
| |
[xmpRights:UsageTerms](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#xmpRights:UsageTerms)
| |
[xmpRights:WebStatement](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#xmpRights:WebStatement)
| |
[ac:licenseLogoURL](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:licenseLogoURL)
| |
[photoshop:Credit](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#photoshop:Credit)
| |
[ac:attributionLogoURL](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:attributionLogoURL)
| |
[ac:attributionLinkURL](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:attributionLinkURL)
| |
[ac:fundingAttribution](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:fundingAttribution)
| |
[dc:source](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dc:source)
| |
[dcterms:source](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dcterms:source)
|

**Agents Vocabulary**

|
[dc:creator](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dc:creator)
| |
[dcterms:creator](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dcterms:creator)
| |
[ac:providerLiteral](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:providerLiteral)
| |
[ac:provider](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:provider)
| |
[ac:metadataProviderLiteral](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:metadataProviderLiteral)
| |
[ac:metadataProvider](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:metadataProvider)
| |
[ac:metadataCreatorLiteral](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:metadataCreatorLiteral)
| |
[ac:metadataCreator](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:metadataCreator)
|

**Content Coverage Vocabulary**

|
[dcterms:description](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dcterms:description)
| |
[ac:caption](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:caption)
| |
[dc:language](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dc:language)
| |
[dcterms:language](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dcterms:language)
| |
[ac:physicalSetting](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:physicalSetting)
| |
[Iptc4xmpExt:CVterm](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Iptc4xmpExt:CVterm)
| |
[ac:subjectCategoryVocabulary](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:subjectCategoryVocabulary)
| | [ac:tag](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:tag)
|

**Geography Vocabulary**

|
[Iptc4xmpExt:LocationShown](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Iptc4xmpExt:LocationShown)
| |
[Iptc4xmpExt:WorldRegion](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Iptc4xmpExt:WorldRegion)
| |
[Iptc4xmpExt:CountryCode](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Iptc4xmpExt:CountryCode)
| |
[Iptc4xmpExt:CountryName](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Iptc4xmpExt:CountryName)
| |
[Iptc4xmpExt:ProvinceState](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Iptc4xmpExt:ProvinceState)
| |
[Iptc4xmpExt:City](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Iptc4xmpExt:City)
| |
[Iptc4xmpExt:Sublocation](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Iptc4xmpExt:Sublocation)
|

**Temporal Coverage Vocabulary**

|
[dcterms:temporal](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dcterms:temporal)
| |
[xmp:CreateDate](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#xmp:CreateDate)
| |
[ac:timeOfDay](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:timeOfDay)
|

**Taxonomic Coverage Vocabulary**

|
[ac:taxonCoverage](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:taxonCoverage)
| |
[dwc:scientificName](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dwc:scientificName)
| |
[dwc:identificationQualifier](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dwc:identificationQualifier)
| |
[dwc:vernacularName](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dwc:vernacularName)
| |
[dwc:nameAccordingTo](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dwc:nameAccordingTo)
| |
[dwc:scientificNameID](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dwc:scientificNameID)
| |
[ac:otherScientificName](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:otherScientificName)
| |
[dwc:identifiedBy](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dwc:identifiedBy)
| |
[dwc:dateIdentified](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dwc:dateIdentified)
| |
[ac:taxonCount](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:taxonCount)
| |
[ac:subjectPart](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:subjectPart)
| |
[dwc:sex](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dwc:sex) |
|
[dwc:lifeStage](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dwc:lifeStage)
| |
[ac:subjectOrientation](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:subjectOrientation)
|

**Resource Creation Vocabulary**

|
[Iptc4xmpExt:LocationCreated](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Iptc4xmpExt:LocationCreated)
| |
[ac:digitizationDate](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:digitizationDate)
| |
[ac:captureDevice](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:captureDevice)
| |
[ac:resourceCreationTechnique](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:resourceCreationTechnique)
|

**Related Resources Vocabulary**

|
[ac:IDofContainingCollection](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:IDofContainingCollection)
| |
[ac:relatedResourceID](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:relatedResourceID)
| |
[ac:providerID](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:providerID)
| |
[ac:derivedFrom](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:derivedFrom)
| |
[ac:associatedSpecimenReference](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:associatedSpecimenReference)
| |
[ac:associatedObservationReference](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:associatedObservationReference)
|

**Service Access Point Vocabulary**

|
[ac:accessURI](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:accessURI)
| |
[dc:format](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dc:format)
| |
[dcterms:format](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dcterms:format)
| |
[ac:variantLiteral](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:variantLiteral)
| |
[ac:variant](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:variant)
| |
[ac:variantDescription](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:variantDescription)
| |
[ac:furtherInformationURL](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:furtherInformationURL)
| |
[ac:licensingException](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:licensingException)
| |
[ac:serviceExpectation](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:serviceExpectation)
| |
[ac:hashFunction](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:hashFunction)
| |
[ac:hashValue](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ac:hashValue)
| |
[exif:PixelXDimension](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#exif:PixelXDimension)
| |
[exif:PixelYDimension](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#exif:PixelYDimension)
|



### <a id="Index_By_Label">6.2 Index By Label</a>

(See also <a href='#Index_By_Term_Name'>Index By Term
Name</a>)

**Management Vocabulary**

|
[Identifier](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Identifier)
| | [Type](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Type) | |
[Subtype](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Subtype) |
| [Title](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Title) | |
[Modified](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Modified)
| | [Metadata
Date](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Metadata_Date)
| | [Metadata
Language](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Metadata_Language)
| | [Provider-managed
ID](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Provider-managed_ID)
| | [Rating](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Rating)
| |
[Commenter](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Commenter)
| |
[Comments](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Comments)
| |
[Reviewer](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Reviewer)
| | [Reviewer
Comments](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Reviewer_Comments)
| | [Date
Available](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Date_Available)
| | [Service Access
Point](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Service_Access_Point)
|

**Attribution Vocabulary** |
[dc:rights](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dc:rights)
| |
[dcterms:rights](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#dcterms:rights)
| | [Copyright
Statement](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Copyright_Statement)
| | [Copyright
Owner](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Copyright_Owner)
| | [Credit](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Credit)
| | [License
Terms](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#License_Terms)
| | [License
URL](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#License_URL) | |
[License Logo
URL](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#License_Logo_URL)
| | [Attribution
Statement](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Attribution_Statement)
| | [Attribution
URL](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Attribution_URL)
| | [Attribution Link
URL](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Attribution_Link_URL)
| |
[Funding](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Funding) |
| [Published
Source](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Published_Source)
|

**Agents Vocabulary**

| [Creator](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Creator)
| |
[Provider](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Provider)
| | [Metadata
Provider](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Metadata_Provider)
| | [Metadata
Creator](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Metadata_Creator)
|

**Content Coverage Vocabulary**

|
[Description](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Description)
| |
[Caption](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Caption) |
|
[Language](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Language)
| | [Physical
Setting](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Physical_Setting)
| | [Subject
Category](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Subject_Category)
| | [Subject Category
Vocabulary](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Subject_Category_Vocabulary)
| | [Tag](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Tag) |

**Geography Vocabulary**

| [Location
Shown](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Location_Shown)
| | [World
Region](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#World_Region)
| | [Country
Code](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Country_Code) |
| [Country
Name](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Country_Name) |
| [Province or
State](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Province_or_State)
| | [City or Place
Name](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#City_or_Place_Name)
| |
[Sublocation](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Sublocation)
|

**Temporal Coverage Vocabulary**

| [Temporal
Coverage](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Temporal_Coverage)
| | [Original Date and
Time](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Original_Date_and_Time)
| | [Time of
Day](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Time_of_Day) |

**Taxonomic Coverage Vocabulary**

| [Taxon
Coverage](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Taxon_Coverage)
| | [Taxon
Name](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Taxon_Name) | |
[Identification
Qualifier](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Identification_Qualifier)
| | [Common
Name](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Common_Name) |
| [Name According
To](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Name_According_To)
| | [Scientific Name
ID](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Scientific_Name_ID)
| | [Other Scientific
Name](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Other_Scientific_Name)
| | [Identified
By](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Identified_By) |
| [Date
Identified](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Date_Identified)
| | [Taxon
Count](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Taxon_Count) |
| [Subject
Part](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Subject_Part) |
| [Subject
Sex](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Subject_Sex) | |
[Subject Life
Stage](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Subject_Life_Stage)
| | [Subject
Orientation](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Subject_Orientation)
|

**Resource Creation Vocabulary**

| [Location
Created](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Location_Created)
| | [Date and Time
Digitized](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Date_and_Time_Digitized)
| | [Capture
Device](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Capture_Device)
| | [Resource Creation
Technique](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Resource_Creation_Technique)
|

**Related Resources Vocabulary**

| [ID of Containing
Collection](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#ID_of_Containing_Collection)
| | [Related Resource
ID](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Related_Resource_ID)
| | [Provider
ID](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Provider_ID) | |
[Derived
From](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Derived_From) |
| [Associated Specimen
Reference](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Associated_Specimen_Reference)
| | [Associated Observation
Reference](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Associated_Observation_Reference)
|

**Service Access Point Vocabulary**

| [Access
URI](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Access_URI) | |
[Format](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Format) | |
[Variant](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Variant) |
| [Variant
Description](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Variant_Description)
| | [Further Information
URL](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Further_Information_URL)
| | [Licensing Exception
Statement](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Licensing_Exception_Statement)
| | [Service
Expectation](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Service_Expectation)
| | [Hash
Function](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Hash_Function)
| | [Hash](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Hash) | |
[Image
Width](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Image_Width) |
| [Image
Height](https://terms.tdwg.org/wiki/Audubon_Core_Term_List#Image_Height)
|



## <a id="Vocabularies">7 Vocabularies</a>

### <a id="Management_Vocabulary">7.1 Management Vocabulary</a>
| property | value |
|----------|-------|
| **Term Name:** | **ac:accessURI** |
| Normative URI: | http://rs.tdwg.org/ac/terms/accessURI |
| Label: | Access URI |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | A URI that uniquely identifies a service that provides a representation of the underlying resource. If this resource can be acquired by an http request, its http URL should be given. If not, but it has some URI in another URI scheme, that may be given here. |
| Notes: | Value might point to something offline, such as a published CD, etc. For example, the doi of an published CD would be a suitable value. |
| | |
| **Term Name:** | **ac:associatedObservationReference** |
| Normative URI: | http://rs.tdwg.org/ac/terms/associatedObservationReference |
| Label: | Associated Observation Reference |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A reference to an observation associated with this resource. |
| | |
| **Term Name:** | **ac:associatedSpecimenReference** |
| Normative URI: | http://rs.tdwg.org/ac/terms/associatedSpecimenReference |
| Label: | Associated Specimen Reference |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A reference to a specimen associated with this resource. |
| Notes: | Supports finding a specimen resource, where additional information is available. If several resources relate to the same specimen, these are implicitly related. Examples: for NHM "BM 23974324" for a barcoded or "BM Smith 32" for a non-barcoded specimen; for UNITS: "TSB 28637"; for PMSL: "PMSL-Lepidoptera-2534781". Ideally this may be a URI identifying a specimen record that is available online. |
| | |
| **Term Name:** | **ac:attributionLinkURL** |
| Normative URI: | http://rs.tdwg.org/ac/terms/attributionLinkURL |
| Label: | Attribution Link URL |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | The URL where information about ownership, attribution, etc. of the resource may be found. |
| Notes: | This URL may be used in creating a clickable logo. Providers should consider making this link as specific and useful to consumers as possible, e. g., linking to a metadata page of the specific image resource rather than to a generic page describing the owner or provider of a resource. |
| | |
| **Term Name:** | **ac:attributionLogoURL** |
| Normative URI: | http://rs.tdwg.org/ac/terms/attributionLogoURL |
| Label: | Attribution URL |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | The URL of the icon or logo image to appear in source attribution. |
| Notes: | Entering this URL into a browser should only result in the icon (not in a webpage including the icon). |
| | |
| **Term Name:** | **ac:caption** |
| Normative URI: | http://rs.tdwg.org/ac/terms/caption |
| Label: | Caption |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | As alternative or in addition to description, a caption is free-form text to be displayed together with (rather than instead of) a resource that is suitable for captions (especially images). |
| Notes: | If both description and caption are present in the metadata, a description is typically displayed instead of the resource, a caption together with the resource. Often only one of description or caption is present; choose the term most appropriate for your metadata. |
| | |
| **Term Name:** | **ac:captureDevice** |
| Normative URI: | http://rs.tdwg.org/ac/terms/captureDevice |
| Label: | Capture Device |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | Free form text describing the device or devices used to create the resource. |
| Notes: | It is best practice to record the device; this may include a combination such as camera plus lens, or camera plus microscope. Examples: "Canon Supershot 2000", "Makroscan Scanner 2000", "Zeiss Axioscope with Camera IIIu", "SEM (Scanning Electron Microscope)". |
| | |
| **Term Name:** | **ac:commenter** |
| Normative URI: | http://rs.tdwg.org/ac/terms/commenter |
| Label: | Commenter |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | A URI denoting a person, using some controlled vocabulary such as FOAF. Implementers and communities of practice may produce restrictions or recommendations on the choice of vocabularies. |
| Notes: | See also Reviewer Comments for the distinction between Comments and Reviewer Comments. |
| | |
| **Term Name:** | **ac:commenterLiteral** |
| Normative URI: | http://rs.tdwg.org/ac/terms/commenterLiteral |
| Label: | Commenter |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | A name or the literal "anonymous" (= anonymously commented). |
| Notes: | See also Reviewer Comments for the distinction between Comments and Reviewer Comments. See also See also the entry for ac:commenter in this document and the section Namespaces, Prefixes and Term Names for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| **Term Name:** | **ac:comments** |
| Normative URI: | http://rs.tdwg.org/ac/terms/comments |
| Label: | Comments |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Any comment provided on the media resource, as free-form text. Best practice would also identify the commenter. |
| Notes: | Comments may refer to the resource itself (e. g., asserting a taxon name or location of a biological subject in an image), or to the relation between resource and associated metadata (e. g., asserting that the taxon name given in the metadata is wrong, without asserting a positive identification). There is a separate item for Reviewer Comments, which is defined more as an expert-level review.Implementers or communities of practice might establish conventions about the meaning of the absence of a commenter, but this specification is silent on that matter. |
| | |
| **Term Name:** | **ac:derivedFrom** |
| Normative URI: | http://rs.tdwg.org/ac/terms/derivedFrom |
| Label: | Derived From |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A reference to an original resource from which the current one is derived. |
| Notes: | Derivation of one resource from another is of special interest for identification tools (e. g. a key from an unpublished data set, as in FRIDA, or a PDA key from a PC or web key) or web services (e. g. a name synonymization service being derived from a specific data set). It may very rarely also be known where one image or sound recording is derived from another (but compare the separate mechanism to be used for quality/resolution levels). ñ Human readable, or doi number, or URL. Simple name of parent for human readable. Can be repeated if a montage of images. |
| | |
| **Term Name:** | **ac:digitizationDate** |
| Normative URI: | http://rs.tdwg.org/ac/terms/digitizationDate |
| Label: | Date and Time Digitized |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | Date the first digital version was created, if different from Original Date and Time found in the Temporal Coverage Vocabulary. The date and time must comply with the World Wide Web Consortium (W3C) datetime practice, which requires that date and time representation correspond to ISO 8601:1998, but with year fields always comprising 4 digits. This makes datetime records compliant with 8601:2004. AC datetime values may also follow 8601:2004 for ranges by separating two IS0 8601 datetime fields by a solidus ("forward slash", '/'). See also the wikipedia IS0 8601 entry for further explanation and examples. |
| Notes: | This is often not the media creation or modification date. For example, if photographic prints have been scanned, the date of that scanning is what this term carries, but Original Date and Time is that depicted in the print. Use the international (ISO/xml) format yyyy-mm-ddThh:mm (e. g. "2007-12-31" or "2007-12-31T14:59"). Where available, timezone information should be added. In the case of digital images containing EXIF, whereas the EXIF capture date does not contain time zone information, but EXIF GPSDateStamp and GPSTimeStamp may be relevant as these include time-zone information. Compare also MWG (2010)[9], which has best practice advice on handling time-zone-less EXIF date/time data. See also the wikipedia IS0 8601 entry for further explanation and examples. |
| | |
| **Term Name:** | **ac:fundingAttribution** |
| Normative URI: | http://rs.tdwg.org/ac/terms/fundingAttribution |
| Label: | Funding |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Organizations or individuals who funded the creation of the resource. |
| | |
| **Term Name:** | **ac:furtherInformationURL** |
| Normative URI: | http://rs.tdwg.org/ac/terms/furtherInformationURL |
| Label: | Further Information URL |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | The URL of a Web site that provides additional information about the version of the media resource that is provided by the Service Access Point. |
| | |
| **Term Name:** | **ac:hashFunction** |
| Normative URI: | http://rs.tdwg.org/ac/terms/hashFunction |
| Label: | Hash Function |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | The cryptographic hash function used to compute the value given in the Hash Value. |
| Notes: | Recommended values include MD5, SHA-1, SHA-224,SHA-256, SHA-384, SHA-512, SHA-512/224 and SHA-512/256 |
| | |
| **Term Name:** | **ac:hashValue** |
| Normative URI: | http://rs.tdwg.org/ac/terms/hashValue |
| Label: | Hash |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | The value computed by a hash function applied to the media that will be delivered at the access point. |
| Notes: | Best practice is to also specify the hash function by supplying a value of the Hash Function term, using one of the standard literals from the Notes there. |
| | |
| **Term Name:** | **ac:hasServiceAccessPoint** |
| Normative URI: | http://rs.tdwg.org/ac/terms/hasServiceAccessPoint |
| Label: | Service Access Point |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | In a chosen serialization (RDF, XML Schema, etc.) the potentially multiple service access points (e.g., for different resolutions of an image) might be provided in a referenced or in a nested object. This property identifies one such access point. That is, each of potentially multiple values of hasServiceAccessPoint identifies a set of representation-dependent metadata using the properties defined under the section Service Access Point Vocabulary. |
| Notes: | Some serializations may flatten the model of service-access points by (a) dropping ac:hasServiceAccessPoint, ac:variant and ac:variantLiteral, (b) repeating properties from the Service Access Point Vocabulary and prefixing them with values of ac:variantLiteral. If such a flat serialization is necessary for services, we recommend to select from among term names of the form "AB" where "A" is one of thumbnail, trailer, lowerQuality, mediumQuality, goodQuality, bestQuality, offline and "B" is one of AccessURI, Format, Extent, FurtherInformationURL, LicensingException, ServiceExpectation (example: thumbnailAccessURI). Implementers in specific constraint languages such as XML Schema or RDF may wish to make Access URI and perhaps dcterms:format mandatory on instances of the service access point. |
| | |
| **Term Name:** | **ac:IDofContainingCollection** |
| Normative URI: | http://rs.tdwg.org/ac/terms/IDofContainingCollection |
| Label: | ID of Containing Collection |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | If the resource is contained in a Collection, this field identifies that Collection uniquely. Its form is not specified by this normative document, but is left to implementers of specific implementations. |
| Notes: | Repeatable: A media resource may be member of multiple collections |
| | |
| **Term Name:** | **ac:licenseLogoURL** |
| Normative URI: | http://rs.tdwg.org/ac/terms/licenseLogoURL |
| Label: | License Logo URL |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | A URL providing access to a logo that symbolizes the License. |
| Notes: | The originating metadata provider is strongly urged to choose a suitable logo as a graphical representation of the license. Failure to do so may leave downstream aggregators in a difficult position to supply a logo that adequately represents the professional, legal, or social aims of the licensors (license givers). Example: http://i.creativecommons.org/l/by-nc-sa/3.0/us/88x31.png provides access to a logo image. |
| | |
| **Term Name:** | **ac:licensingException** |
| Normative URI: | http://rs.tdwg.org/ac/terms/licensingException |
| Label: | Licensing Exception Statement |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | The licensing statement for this variant of the media resource if different from that given in the License Statement property of the resource. |
| Notes: | Required only if this version has different licensing than that of the media resource. For example, the highest resolution version may be more restricted than lower resolution versions. |
| | |
| **Term Name:** | **ac:metadataCreator** |
| Normative URI: | http://rs.tdwg.org/ac/terms/metadataCreator |
| Label: | Metadata Creator |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Person or organization originally creating the resource metadata record. |
| Notes: | See also the entry for ac:metadataCreatorLiteral in this document and the section Namespaces, Prefixes and Term Names for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| **Term Name:** | **ac:metadataCreatorLiteral** |
| Normative URI: | http://rs.tdwg.org/ac/terms/metadataCreatorLiteral |
| Label: | Metadata Creator |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Person or organization originally creating the resource metadata record. |
| Notes: | See also the entry for ac:metadataCreator in this document and the section Namespaces, Prefixes and Term Names for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| **Term Name:** | **ac:metadataLanguage** |
| Normative URI: | http://rs.tdwg.org/ac/terms/metadataLanguage |
| Label: | Metadata Language |
| | **Layer:** 1 -- **Required:** Yes -- **Repeatable:** No |
| Definition: | URI from the ISO639-2 list of URIs for ISO 3-letter language codes. |
| Notes: | This is NOT dcterms:language, which is about the resource, not the metadata. Metadata Language is deliberately single-valued, imposing on unstructured serializations a requirement that multi-lingual metadata be represented as separate, complete, metadata records. Audubon Core requires that each record also contains the language-neutral terms. In the absence of this requirement, metadata consumers would need to know which terms are language-neutral and merge these terms from all provided metadataLanguages into a single record. Metadata consumers may re-combine the information based on the dcterms:identifier that identifies the multimedia resource. At least one of ac:metadataLanguage and ac:metadataLanguageLiteral must be supplied but, when feasible, supplying both may make the metadata more widely useful. They must specify the same language. In case of ambiguity, ac:metadataLanguage prevails. Nothing in this document would, however, prevent an implementer, e. g. of an XML-Schema representation, from providing a fully hierarchical schema in which language neutral terms occur only a single time, and only the language-specific terms are repeated in a way that unambigously relates them to a metadata language. In RDF it may be a simple repetition of plain literals associated with a language (e.g., xml:lang attribute in RDF/XML). The language attribute would then be required in Audubon Core and would replace ac:metadataLanguage. |
| | |
| **Term Name:** | **ac:metadataLanguageLiteral** |
| Normative URI: | http://rs.tdwg.org/ac/terms/metadataLanguageLiteral |
| Label: | Metadata Language |
| | **Layer:** 1 -- **Required:** Yes -- **Repeatable:** No |
| Definition: | Language of description and other metadata (but not necessarily of the image itself) represented as an ISO639-2 three letter language code. ISO639-1 two-letter codes are permitted but deprecated. |
| Notes: | This is NOT dc:language, which is about the resource, not the metadata. Metadata Language is deliberately single-valued, imposing on unstructured serializations a requirement that multi-lingual metadata be represented as separate, complete, metadata records. Audubon Core requires that each record also contains the language-neutral terms. In the absence of this requirement, metadata consumers would need to know which terms are language-neutral and merge these terms from all provided metadataLanguages into a single record. Metadata consumers may re-combine the information based on the dcterms:identifier that identifies the multimedia resource. At least one of ac:metadataLanguage and ac:metadataLanguageLiteral must be supplied but, when feasible, supplying both may make the metadata more widely useful. They must specify the same language. In case of ambiguity, ac:metadataLanguage prevails. Nothing in this document would, however, prevent an implementer, e. g. of an XML-Schema representation, from providing a fully hierarchical schema in which language neutral terms occur only a single time, and only the language-specific terms are repeated in a way that unambigously relates them to a metadata language. In RDF it may be a simple repetition of plain literals associated with a language (e.g., xml:lang attribute in RDF/XML). The language attribute would then be required in Audubon Core and would replace ac:metadataLanguage. |
| | |
| **Term Name:** | **ac:metadataProvider** |
| Normative URI: | http://rs.tdwg.org/ac/terms/metadataProvider |
| Label: | Metadata Provider |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | URI of person or organization originally responsible for providing the resource metadata record. |
| Notes: | Media resources and their metadata may be served from different institutions, e. g. in the case of aggregators adding user annotations, taxon identifications, or ratings. Compare Provider. See also the entry for ac:metadataProviderLiteral in this document and the section Namespaces, Prefixes and Term Names for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| **Term Name:** | **ac:metadataProviderLiteral** |
| Normative URI: | http://rs.tdwg.org/ac/terms/metadataProviderLiteral |
| Label: | Metadata Provider |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Person or organization originally responsible for providing the resource metadata record. |
| Notes: | Media resources and their metadata may be served from different institutions, e. g. in the case of aggregators adding user annotations, taxon identifications, or ratings. Compare Provider. See also the entry for ac:metadataProvider in this document and the section Namespaces, Prefixes and Term Names for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| **Term Name:** | **ac:otherScientificName** |
| Normative URI: | http://rs.tdwg.org/ac/terms/otherScientificName |
| Label: | Other Scientific Name |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | One or several Scientific Taxon Names that are synonyms to the Scientific Taxon Name may be provided here. |
| Notes: | The primary purpose of this is in support of resource discovery, not developing a taxonomic synonymy. Misidentification or misspellings may thus be of interest. Where multiple taxa are present in a resource and multiple Scientific Taxon Names are given, the association between synonyms and names may not be deducible from the AC record alone. |
| | |
| **Term Name:** | **ac:physicalSetting** |
| Normative URI: | http://rs.tdwg.org/ac/terms/physicalSetting |
| Label: | Physical Setting |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The setting of the content represented in media such as images, sounds, and movies if the provider deems them relevant. Constrained vocabulary of: "Natural" = Object in its natural setting of the object (e. g. living organisms in their natural environment); "Artificial" = Object in an artificial environment (e. g. living organisms in an artificial environment such as a zoo, garden, greenhouse, or laboratory); "Edited" = Human media editing of a natural setting or media acquisition with a separate media background such as a photographic backdrop. |
| Notes: | Multiple values may be needed for movies or montages. See also ac:resourceCreationTechnique which should be used to describe any modifications to the resource itself. Communities of practice should form best practices for the use of these controlled terms. |
| | |
| **Term Name:** | **ac:provider** |
| Normative URI: | http://rs.tdwg.org/ac/terms/provider |
| Label: | Provider |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | URI for person or organization responsible for presenting the media resource. If no separate Metadata Provider is given, this also attributes the metadata. |
| Notes: | Media resources and their metadata may be served from different institutions, e. g. in the case of aggregators adding user annotations, taxon identifications, or ratings. See also the entry for ac:providerLiteral in this document and the section Namespaces, Prefixes and Term Names for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| **Term Name:** | **ac:providerID** |
| Normative URI: | http://rs.tdwg.org/ac/terms/providerID |
| Label: | Provider ID |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | A globally unique ID of the provider of the current AC metadata record. |
| Notes: | Only to be used if the annotated resource is not a provider itself - this item is for relating the resource to a provider, using an arbitrary code that is unique for a provider, contributing partner, or aggregator, or other roles (potentially defined by MARC, OAI) and by which the media resources are linked to the provider. |
| | |
| **Term Name:** | **ac:providerLiteral** |
| Normative URI: | http://rs.tdwg.org/ac/terms/providerLiteral |
| Label: | Provider |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | Person or organization responsible for presenting the media resource. If no separate Metadata Provider is given, this also attributes the metadata. |
| Notes: | Media resources and their metadata may be served from different institutions, e. g. in the case of aggregators adding user annotations, taxon identifications, or ratings. See also the entry for ac:provider in this document and the section Namespaces, Prefixes and Term Names for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| **Term Name:** | **ac:providerManagedID** |
| Normative URI: | http://rs.tdwg.org/ac/terms/providerManagedID |
| Label: | Provider-managed ID |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | A free-form identifier (a simple number, an alphanumeric code, a URL, etc.) that is unique and meaningful primarily for the data provider. |
| Notes: | Ideally, this would be a globally unique identifier (GUID), but the provider is encouraged to supply any form of identifier that simplifies communications on resources within their project and helps to locate individual data items in the provider's data repositories. It is the provider's decision whether to expose this value or not. |
| | |
| **Term Name:** | **ac:relatedResourceID** |
| Normative URI: | http://rs.tdwg.org/ac/terms/relatedResourceID |
| Label: | Related Resource ID |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Resource related in ways not specified through a collection, e.g., before-after images; time-lapse series; different orientations/angles of view |
| Notes: | The value references a related media item. Examples of relations are: Images taken in a sequence or defined time series, an exposure or focus series (e.g. for stacking), different framing or views (top, side, bottom) of the same subject, or an overview plus several details. The property makes such related media items discoverable, but does not indicate the nature of this relationship. More specific properties may be defined in a later version of AC. |
| | |
| **Term Name:** | **ac:resourceCreationTechnique** |
| Normative URI: | http://rs.tdwg.org/ac/terms/resourceCreationTechnique |
| Label: | Resource Creation Technique |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | Information about technical aspects of the creation and digitization process of the resource. This includes modification steps ("retouching") after the initial resource capture. |
| Notes: | Examples: Encoding method or settings, numbers of channels, lighting, audio sampling rate, frames per second, data rate, interlaced or progressive, multiflash lighting, remote control, automatic interval exposure.  Annotating whether and how a resource has been modified or edited significantly in ways that are not immediately obvious to, or expected by, consumers is of special significance. Examples for images are: Removing a distracting twig from a picture, moving an object to a different surrounding, changing the color in parts of the image, or blurring the background of an image. Modifications that are standard practice and expected or obvious are not necessary to document; examples of such practices include changing resolution, cropping, minor sharpening or overall color correction, and clearly perceptible modifications (e.g., addition of arrows or labels, or the placement of multiple pictures into a table.) If it is only known that significant modifications were made, but no details are known, a general statement like "Media may have been manipulated to improve appearance" may be appropriate. See also Subject Preparation Technique. |
| | |
| **Term Name:** | **ac:reviewer** |
| Normative URI: | http://rs.tdwg.org/ac/terms/reviewer |
| Label: | Reviewer |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | URI for a reviewer. If present, then resource is peer-reviewed, even if there are Reviewer Comments is absent or empty. Its presence tells whether an expert in the subject featured in the media has reviewed the media item or collection and approved its metadata description; must display a name or the literal "anonymous" (= anonymously reviewed). |
| Notes: | Provider is asserting they accept this review as competent. See also ac:reviewerLiteral in this document and the section Namespaces, Prefixes and Term Names for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| **Term Name:** | **ac:reviewerComments** |
| Normative URI: | http://rs.tdwg.org/ac/terms/reviewerComments |
| Label: | Reviewer Comments |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Any comment provided by a reviewer with expertise in the subject, as free-form text. |
| Notes: | Reviewer Comments may refer to the resource itself (e. g., asserting a taxon name or location of a biological subject in an image), or to the relation between resource and associated metadata (e. g., asserting that the taxon name given in the metadata is wrong, without asserting a positive identification). There is a separate item "Comments" for text from commenters of unrecorded expertise. |
| | |
| **Term Name:** | **ac:reviewerLiteral** |
| Normative URI: | http://rs.tdwg.org/ac/terms/reviewerLiteral |
| Label: | Reviewer |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | String providing the name of a reviewer. If present, then resource is peer-reviewed, even if Reviewer Comments is absent or empty. Its presence tells whether an expert in the subject featured in the media has reviewed the media item or collection and approved its metadata description; must display a name or the literal "anonymous" (= anonymously reviewed). |
| Notes: | Provider is asserting they accept this review as competent. See also ac:reviewer and the section Namespaces, Prefixes and Term Names for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| **Term Name:** | **ac:serviceExpectation** |
| Normative URI: | http://rs.tdwg.org/ac/terms/serviceExpectation |
| Label: | Service Expectation |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | A term that describes what service expectations users may have of the ac:accessURL. Recommended terms include online (denotes that the URL is expected to deliver the resource), authenticate (denotes that the URL delivers a login or other authentication interface requiring completion before delivery of the resource) published(non digital) (denotes that the URL is the identifier of a non-digital published work, for example a doi.) Communities should develop their own controlled vocabularies for Service Expectations. |
| | |
| **Term Name:** | **ac:subjectCategoryVocabulary** |
| Normative URI: | http://rs.tdwg.org/ac/terms/subjectCategoryVocabulary |
| Label: | Subject Category Vocabulary |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Any vocabulary or formal classification from which terms in the Subject Category have been drawn. |
| Notes: | The AC recommended vocabularies do not need to be cited here. There is no required linkage between individual Subject Category terms and the vocabulary; the mechanism is intended to support discovery of the normative URI for a term, but not guarantee it. |
| | |
| **Term Name:** | **ac:subjectOrientation** |
| Normative URI: | http://rs.tdwg.org/ac/terms/subjectOrientation |
| Label: | Subject Orientation |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Specific orientation (= direction, view angle) of the subject represented in the media resource with respect to the acquisition device. |
| Notes: | Examples: "dorsal", "ventral", "frontal", etc. No formal encoding scheme as yet exists. The term is repeatable e.g., in the case of a composite image, consisting of a combination of different view orientations. |
| | |
| **Term Name:** | **ac:subjectPart** |
| Normative URI: | http://rs.tdwg.org/ac/terms/subjectPart |
| Label: | Subject Part |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The portion or product of organism morphology, behaviour, environment, etc. that is either predominantly shown or particularly well exemplified by the media resource. |
| Notes: | No formal encoding scheme as yet exists. Examples are "whole body", "head", "flower", "leaf", "canopy" (of a rain forest stand). Several anatomical ontologies are emerging in http://www.obofoundry.org/ |
| | |
| **Term Name:** | **ac:subtype** |
| Normative URI: | http://rs.tdwg.org/ac/terms/subtype |
| Label: | Subtype |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Any URI may be used that provides for more specialization than the type. Possible values are community-defined. For exmamples see the non-normative page AC_Subtype_Examples. |
| Notes: | The subtype term may not be applied to Collection objects. However, the Description term in the Content Coverage Vocabulary may add further description to a Collection object. The subtype vocabulary may be extended by users provided they identify the term by a URI which is not in the ac namespace (for example, using "http://my.inst.org/namespace/metadata/subtype/repair-manual"). Conforming applications may choose to ignore these. See ac:subtypeLiteral for usage with strings. |
| | |
| **Term Name:** | **ac:subtypeLiteral** |
| Normative URI: | http://rs.tdwg.org/ac/terms/subtypeLiteral |
| Label: | Subtype |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The subtype should provide more specialization than the type. Possible values are community-defined. For exmamples see the non-normative page AC_Subtype_Examples. |
| Notes: | The subtypeLiteral term may not be applied to Collection objects. However, the Description term in the Content Coverage Vocabulary may add further description to a Collection object. |
| | |
| **Term Name:** | **ac:tag** |
| Normative URI: | http://rs.tdwg.org/ac/terms/tag |
| Label: | Tag |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | General keywords or tags. |
| Notes: | Tags may be multi-worded phrases. Where scientific names, common names, geographic locations, etc. are separable, those should go into the more specific coverage metadata items provided further below. Examples: "flower diagram". Character or part keywords like "leaf", or "flower color" are especially desirable. |
| | |
| **Term Name:** | **ac:taxonCount** |
| Normative URI: | http://rs.tdwg.org/ac/terms/taxonCount |
| Label: | Taxon Count |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | An exact or estimated number of taxa at the lowest applicable taxon rank (usually species or infraspecific) represented by the media resource (item or collection). |
| Notes: | Primarily intended for resource collections and singular resources dealing with sets of taxa (e. g., identification tools, videos). It is recommended to give an exact or estimated number of specific taxa when a complete list of taxa is not available or practical. The count should contain only the taxa covered fully or primarily by the resource. For a taxon page and most images this will be "1", i. e. other taxa mentioned on the side or in the background should not be counted. However, sometimes a resource may illustrate an ecological or behavioral entity with multiple species, e. g., a host-pathogen interaction; taxon count would then indicate the known number of species in this interaction. This should be a single integer number. Leave the field empty if you cannot estimate the information (do not enter 0). Additional taxon counts at higher levels (e. g. how many families are covered by a digital Fauna) should be given verbatim in the resource description, not here. |
| | |
| **Term Name:** | **ac:taxonCoverage** |
| Normative URI: | http://rs.tdwg.org/ac/terms/taxonCoverage |
| Label: | Taxon Coverage |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | A higher taxon (e. g., a genus, family, or order) at the level of the genus or higher, that covers all taxa that are the primary subject of the resource (which may be a media item or a collection). |
| Notes: | Example: Where the subject of an image is several species of ducks with trees visible in the background, Taxon Coverage would still be Anatidae (and not Biota). Example: "Aves" for a bird key or a bird image collection. Do not add a rank ("Class Aves") in this field. Note that this somewhat expands the usage of ncd:taxonCoverage which, however has not yet been adopted by TDWG, and which specifies at the Family level or higher. For collections it is recommended to follow ncd:taxonCoverage to avoid conflicts between an AC record and a record arising from use of the un-adopted NCD. If the resource contains a single taxon, this should be placed in Scientific Taxon Name. In this case Taxon Coverage may be left empty, but if not, care should be taken that the entries do not conflict. Example: If Scientific Taxon Name is Quercus alba then Taxon Coverage, if provided at all, should be Quercus. |
| | |
| **Term Name:** | **ac:timeOfDay** |
| Normative URI: | http://rs.tdwg.org/ac/terms/timeOfDay |
| Label: | Time of Day |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | Free text information beyond exact clock times. |
| Notes: | Examples in English: afternoon, twilight. |
| | |
| **Term Name:** | **ac:variant** |
| Normative URI: | http://rs.tdwg.org/ac/terms/variant |
| Label: | Variant |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A URI designating what this Service Access Point provides. Some suggested values are the URIs ac:Thumbnail, ac:Trailer, ac:LowerQuality, ac:MediumQuality, ac:GoodQuality, ac:BestQuality, and ac:Offline. Additional URIs from communities of practice may be introduced. |
| Notes: | A URI designating what this Service Access Point provides. Some suggested values are the URIs ac:Thumbnail, ac:Trailer, ac:LowerQuality, ac:MediumQuality, ac:GoodQuality, ac:BestQuality, and ac:Offline. Additional URIs from communities of practice may be introduced. |
| | |
| **Term Name:** | **ac:variantDescription** |
| Normative URI: | http://rs.tdwg.org/ac/terms/variantDescription |
| Label: | Variant Description |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | Text that describes this Service Access Point variant |
| Notes: | Most variants (thumb, low-res, high-res) are self-explanatory and it is best practice to leave this property empty if no special description is needed. It is provided for cases that require additional information (e.g., video shortened instead of simply quality reduced). |
| | |
| **Term Name:** | **ac:variantLiteral** |
| Normative URI: | http://rs.tdwg.org/ac/terms/variantLiteral |
| Label: | Variant |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Text that describes this Service Access Point variant. |
| Notes: | This is an alternative to ac:variant where using a string is preferred over a URI. It is best practice to use ac:variant instead of ac:variantLiteral wherever practical. Value may be free text, but it is suggested to consider including terminology based on the following: Thumbnail: Service Access Point provides a thumbnail image, short sound clip, or short movie clip that can be used in addition to the resource to represent the media object, typically at lower quality and higher compression than a preview object. A typical size for a tiny thumbnail image may be 50-100 pixels in the longer dimension. Trailer: Service Access Point provides video clip preview, in the form of a specifically authored "Trailer", which may provide somewhat different content than the original resource. Lower Quality: Service Access Point provides a lower quality version of the media resource, suitable e. g. for web sites. Medium Quality: Service Access Point provides a medium quality version of the media resource, e. g. shortened in duration, or reduced size, using lower resolution or higher compression causing moderate artifacts. Good Quality: Service Access Point provides a good quality version of the media resource intended for resources displayed as primary information; e. g. an image between 800 and 1600 px in width or height. Best Quality: Service Access Point provides the highest available quality of the media resource, whatever its resolution or quality level. Offline: Service Access Point provides data about an offline resource. |
| | |
| | |

## <a id="References">8 References</a>

1.  <a href='#cite_ref-1'></a>NASA Global Change Master Directory
    http://gcmd.nasa.gov/

2.  <a href='cite_note-2'></a>Subject Categories defined in Key to
    Nature http://www.keytonature.eu/wiki/Subject_Category

3.  <a href='cite_note-3'></a>BioComplexity Thesaurus
    http://thesaurus.nbii.gov

4.  <a href='cite_note-4'></a>GBIF Description Types
    http://rs.gbif.org/vocabulary/gbif/description_type.xml

5.  <a href='cite_note-5'></a>Species Profile Model
    http://rs.tdwg.org/ontology/voc/SPMInfoItems.rdf

6.  <a href='cite_note-6'></a>Plinian Core
    http://www.gbif.es/plinian/doku.php

7.  <a href='cite_note-7'></a>GEMET
    http://www.eionet.europa.eu/gemet

8.  <a href='cite_note-8'></a>LTER Controlled Vocabulary
    http://vocab.lternet.edu/

9.  <a href='cite_note-MWG2010-9'></a>Metadata Working Group
    Guidelines for Handling Image Metadata (MWG 2010), Version 2.0, November 2010
    http://www.metadataworkinggroup.org/pdf/mwg_guidance.pdf

-----------------
This document is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). ![http://creativecommons.org/licenses/by/4.0/](https://licensebuttons.net/l/by/4.0/88x31.png).

Copyright 2013 - Biodiversity Information Standards - TDWG - [Contact Us](http://www.tdwg.org/about-tdwg/contact-us/)
