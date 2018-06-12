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
Chavan, José Cuadra, Chris Freeland, Gregor Hagedorn, Patrick Leary,
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
