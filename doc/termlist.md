# Audubon Core Term List

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
Chavan, Jos√© Cuadra, Chris Freeland, Gregor Hagedorn, Patrick Leary,
Dimitry Mozzherin, Annette Olson, Greg Riccardi, Ivan Teage

**Creator:** GBIF/TDWG Multimedia Resources Task Group

**Bibliographic citation:** Multimedia Resources Task Group. 2013. Audubon Core Term List. Biodiversity Information Standards (TDWG). http://rs.tdwg.org/ac/doc/termlist/

## Table of Contents

[1 Introduction](#1-introduction)

[1.1 Status of the content of this document](#11-status-of-the-content-of-this-document)

[1.2 Categories of terms](#12-categories-of-terms)

[2 Borrowed Vocabulary](#2-borrowed-vocabulary)

[3 Namespaces, Prefixes and Term Names](#3-namespaces-prefixes-and-term-names)

[4 Layers](#4-layers)

[5 Literal- vs. URI-valued Terms](#5-literal--vs-uri-valued-terms)

[6 Vocabulary Indices](#6-vocabulary-indices)

[6.1 Index By Term Name](#61-index-by-term-name)

[6.2 Index By Label](#62-index-by-label)

[7 Vocabularies](#7-vocabularies)

[7.1 Management Vocabulary](#71-management-vocabulary)

[7.2 Attribution Vocabulary](#72-attribution-vocabulary)

[7.3 Agents Vocabulary](#73-agents-vocabulary)

[7.4 Content Coverage Vocabulary](#74-content-coverage-vocabulary)

[7.5 Geography Vocabulary](#75-geography-vocabulary)

[7.6 Temporal Coverage Vocabulary](#76-temporal-coverage-vocabulary)

[7.7 Taxonomic Coverage Vocabulary](#77-taxonomic-coverage-vocabulary)

[7.8 Resource Creation Vocabulary](#78-resource-creation-vocabulary)

[7.9 Related Resources Vocabulary](#79-related-resources-vocabulary)

[7.10 Service Access Point Vocabulary](#710-service-access-point-vocabulary)


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
### 6.1 Index By Term Name

(See also [6.2 Index By Label](#62-index-by-label))

**Management Vocabulary**

| [dcterms:available](#dcterms_available) |
| [ac:commenter](#ac_commenter) |
| [ac:commenterLiteral](#ac_commenterLiteral) |
| [ac:comments](#ac_comments) |
| [ac:hasServiceAccessPoint](#ac_hasServiceAccessPoint) |
| [dcterms:identifier](#dcterms_identifier) |
| [xmp:MetadataDate](#xmp_MetadataDate) |
| [ac:metadataLanguage](#ac_metadataLanguage) |
| [ac:metadataLanguageLiteral](#ac_metadataLanguageLiteral) |
| [dcterms:modified](#dcterms_modified) |
| [ac:providerManagedID](#ac_providerManagedID) |
| [xmp:Rating](#xmp_Rating) |
| [ac:reviewer](#ac_reviewer) |
| [ac:reviewerComments](#ac_reviewerComments) |
| [ac:reviewerLiteral](#ac_reviewerLiteral) |
| [ac:subtype](#ac_subtype) |
| [ac:subtypeLiteral](#ac_subtypeLiteral) |
| [dcterms:title](#dcterms_title) |
| [dc:type](#dc_type) |
| [dcterms:type](#dcterms_type) |

**Attribution Vocabulary**

| [ac:attributionLinkURL](#ac_attributionLinkURL) |
| [ac:attributionLogoURL](#ac_attributionLogoURL) |
| [photoshop:Credit](#photoshop_Credit) |
| [ac:fundingAttribution](#ac_fundingAttribution) |
| [ac:licenseLogoURL](#ac_licenseLogoURL) |
| [xmpRights:Owner](#xmpRights_Owner) |
| [dc:rights](#dc_rights) |
| [dcterms:rights](#dcterms_rights) |
| [dc:source](#dc_source) |
| [dcterms:source](#dcterms_source) |
| [xmpRights:UsageTerms](#xmpRights_UsageTerms) |
| [xmpRights:WebStatement](#xmpRights_WebStatement) |

**Agents Vocabulary**

| [dc:creator](#dc_creator) |
| [dcterms:creator](#dcterms_creator) |
| [ac:metadataCreator](#ac_metadataCreator) |
| [ac:metadataCreatorLiteral](#ac_metadataCreatorLiteral) |
| [ac:metadataProvider](#ac_metadataProvider) |
| [ac:metadataProviderLiteral](#ac_metadataProviderLiteral) |
| [ac:provider](#ac_provider) |
| [ac:providerLiteral](#ac_providerLiteral) |

**Content Coverage Vocabulary**

| [ac:caption](#ac_caption) |
| [Iptc4xmpExt:CVterm](#Iptc4xmpExt_CVterm) |
| [dcterms:description](#dcterms_description) |
| [dc:language](#dc_language) |
| [dcterms:language](#dcterms_language) |
| [ac:physicalSetting](#ac_physicalSetting) |
| [ac:subjectCategoryVocabulary](#ac_subjectCategoryVocabulary) |
| [ac:tag](#ac_tag) |

**Geography Vocabulary**

| [Iptc4xmpExt:City](#Iptc4xmpExt_City) |
| [dwc:continent](#dwc_continent) |
| [dwc:coordinatePrecision](#dwc_coordinatePrecision) |
| [dwc:coordinateUncertaintyInMeters](#dwc_coordinateUncertaintyInMeters) |
| [dwc:country](#dwc_country) |
| [Iptc4xmpExt:CountryCode](#Iptc4xmpExt_CountryCode) |
| [dwc:countryCode](#dwc_countryCode) |
| [Iptc4xmpExt:CountryName](#Iptc4xmpExt_CountryName) |
| [dwc:county](#dwc_county) |
| [dwc:decimalLatitude](#dwc_decimalLatitude) |
| [dwc:decimalLongitude](#dwc_decimalLongitude) |
| [dwc:footprintSpatialFit](#dwc_footprintSpatialFit) |
| [dwc:footprintSRS](#dwc_footprintSRS) |
| [dwc:footprintWKT](#dwc_footprintWKT) |
| [dwc:geodeticDatum](#dwc_geodeticDatum) |
| [dwc:georeferencedBy](#dwc_georeferencedBy) |
| [dwc:georeferenceProtocol](#dwc_georeferenceProtocol) |
| [dwc:georeferenceRemarks](#dwc_georeferenceRemarks) |
| [dwc:georeferenceSources](#dwc_georeferenceSources) |
| [dwc:georeferenceVerificationStatus](#dwc_georeferenceVerificationStatus) |
| [dwc:higherGeography](#dwc_higherGeography) |
| [dwc:higherGeographyID](#dwc_higherGeographyID) |
| [dwc:island](#dwc_island) |
| [dwc:islandGroup](#dwc_islandGroup) |
| [dwc:locality](#dwc_locality) |
| [dwc:locationAccordingTo](#dwc_locationAccordingTo) |
| [dwc:locationID](#dwc_locationID) |
| [dwc:locationRemarks](#dwc_locationRemarks) |
| [Iptc4xmpExt:LocationShown](#Iptc4xmpExt_LocationShown) |
| [dwc:maximumDepthInMeters](#dwc_maximumDepthInMeters) |
| [dwc:maximumDistanceAboveSurfaceInMeters](#dwc_maximumDistanceAboveSurfaceInMeters) |
| [dwc:maximumElevationInMeters](#dwc_maximumElevationInMeters) |
| [dwc:minimumDepthInMeters](#dwc_minimumDepthInMeters) |
| [dwc:minimumDistanceAboveSurfaceInMeters](#dwc_minimumDistanceAboveSurfaceInMeters) |
| [dwc:minimumElevationInMeters](#dwc_minimumElevationInMeters) |
| [dwc:municipality](#dwc_municipality) |
| [dwc:pointRadiusSpatialFit](#dwc_pointRadiusSpatialFit) |
| [Iptc4xmpExt:ProvinceState](#Iptc4xmpExt_ProvinceState) |
| [dwc:stateProvince](#dwc_stateProvince) |
| [Iptc4xmpExt:Sublocation](#Iptc4xmpExt_Sublocation) |
| [dwc:verbatimCoordinates](#dwc_verbatimCoordinates) |
| [dwc:verbatimCoordinateSystem](#dwc_verbatimCoordinateSystem) |
| [dwc:verbatimDepth](#dwc_verbatimDepth) |
| [dwc:verbatimElevation](#dwc_verbatimElevation) |
| [dwc:verbatimLatitude](#dwc_verbatimLatitude) |
| [dwc:verbatimLocality](#dwc_verbatimLocality) |
| [dwc:verbatimLongitude](#dwc_verbatimLongitude) |
| [dwc:verbatimSRS](#dwc_verbatimSRS) |
| [dwc:waterBody](#dwc_waterBody) |
| [Iptc4xmpExt:WorldRegion](#Iptc4xmpExt_WorldRegion) |

**Temporal Coverage Vocabulary**

| [xmp:CreateDate](#xmp_CreateDate) |
| [dcterms:temporal](#dcterms_temporal) |
| [ac:timeOfDay](#ac_timeOfDay) |

**Taxonomic Coverage Vocabulary**

| [dwc:dateIdentified](#dwc_dateIdentified) |
| [dwc:identificationQualifier](#dwc_identificationQualifier) |
| [dwc:identifiedBy](#dwc_identifiedBy) |
| [dwc:lifeStage](#dwc_lifeStage) |
| [dwc:nameAccordingTo](#dwc_nameAccordingTo) |
| [ac:otherScientificName](#ac_otherScientificName) |
| [dwc:preparations](#dwc_preparations) |
| [dwc:scientificName](#dwc_scientificName) |
| [dwc:scientificNameID](#dwc_scientificNameID) |
| [dwc:sex](#dwc_sex) |
| [ac:subjectOrientation](#ac_subjectOrientation) |
| [ac:subjectPart](#ac_subjectPart) |
| [ac:taxonCount](#ac_taxonCount) |
| [ac:taxonCoverage](#ac_taxonCoverage) |
| [dwc:vernacularName](#dwc_vernacularName) |

**Resource Creation Vocabulary**

| [ac:captureDevice](#ac_captureDevice) |
| [ac:digitizationDate](#ac_digitizationDate) |
| [Iptc4xmpExt:LocationCreated](#Iptc4xmpExt_LocationCreated) |
| [ac:resourceCreationTechnique](#ac_resourceCreationTechnique) |

**Related Resources Vocabulary**

| [ac:associatedObservationReference](#ac_associatedObservationReference) |
| [ac:associatedSpecimenReference](#ac_associatedSpecimenReference) |
| [ac:derivedFrom](#ac_derivedFrom) |
| [ac:IDofContainingCollection](#ac_IDofContainingCollection) |
| [ac:providerID](#ac_providerID) |
| [ac:relatedResourceID](#ac_relatedResourceID) |

**Service Access Point Vocabulary**

| [ac:accessURI](#ac_accessURI) |
| [dc:format](#dc_format) |
| [dcterms:format](#dcterms_format) |
| [ac:furtherInformationURL](#ac_furtherInformationURL) |
| [ac:hashFunction](#ac_hashFunction) |
| [ac:hashValue](#ac_hashValue) |
| [ac:licensingException](#ac_licensingException) |
| [exif:PixelXDimension](#exif_PixelXDimension) |
| [exif:PixelYDimension](#exif_PixelYDimension) |
| [ac:serviceExpectation](#ac_serviceExpectation) |
| [ac:variant](#ac_variant) |
| [ac:variantDescription](#ac_variantDescription) |
| [ac:variantLiteral](#ac_variantLiteral) |

### 6.2 Index By Label

(See also [6.1 Index By Term Name](#61-index-by-term-name))

**Management Vocabulary**

| [Commenter](#ac_commenter) |
| [Comments](#ac_comments) |
| [Date Available](#dcterms_available) |
| [Identifier](#dcterms_identifier) |
| [Metadata Date](#xmp_MetadataDate) |
| [Metadata Language](#ac_metadataLanguage) |
| [Modified](#dcterms_modified) |
| [Provider-managed ID](#ac_providerManagedID) |
| [Rating](#xmp_Rating) |
| [Reviewer](#ac_reviewer) |
| [Reviewer Comments](#ac_reviewerComments) |
| [Service Access Point](#ac_hasServiceAccessPoint) |
| [Subtype](#ac_subtype) |
| [Title](#dcterms_title) |
| [Type](#dc_type) |

**Attribution Vocabulary**

| [Attribution Link URL](#ac_attributionLinkURL) |
| [Attribution URL](#ac_attributionLogoURL) |
| [Copyright Owner](#xmpRights_Owner) |
| [Copyright Statement](#dc_rights) |
| [Credit](#photoshop_Credit) |
| [Funding](#ac_fundingAttribution) |
| [License Logo URL](#ac_licenseLogoURL) |
| [License Terms](#xmpRights_UsageTerms) |
| [License URL](#xmpRights_WebStatement) |
| [Published Source](#dc_source) |

**Agents Vocabulary**

| [Creator](#dc_creator) |
| [Metadata Creator](#ac_metadataCreator) |
| [Metadata Provider](#ac_metadataProvider) |
| [Provider](#ac_provider) |

**Content Coverage Vocabulary**

| [Caption](#ac_caption) |
| [Description](#dcterms_description) |
| [Language](#dc_language) |
| [Physical Setting](#ac_physicalSetting) |
| [Subject Category](#Iptc4xmpExt_CVterm) |
| [Subject Category Vocabulary](#ac_subjectCategoryVocabulary) |
| [Tag](#ac_tag) |

**Geography Vocabulary**

| [City or Place Name](#Iptc4xmpExt_City) |
| [Continent](#dwc_continent) |
| [Coordinate Precision](#dwc_coordinatePrecision) |
| [Coordinate Uncertainty In Meters](#dwc_coordinateUncertaintyInMeters) |
| [Country](#dwc_country) |
| [Country Code](#Iptc4xmpExt_CountryCode) |
| [Country Name](#Iptc4xmpExt_CountryName) |
| [County](#dwc_county) |
| [Decimal Latitude](#dwc_decimalLatitude) |
| [Decimal Longitude](#dwc_decimalLongitude) |
| [Footprint Spatial Fit](#dwc_footprintSpatialFit) |
| [Footprint SRS](#dwc_footprintSRS) |
| [Footprint WKT](#dwc_footprintWKT) |
| [Geodetic Datum](#dwc_geodeticDatum) |
| [Georeference Protocol](#dwc_georeferenceProtocol) |
| [Georeference Remarks](#dwc_georeferenceRemarks) |
| [Georeference Sources](#dwc_georeferenceSources) |
| [Georeference Verification Status](#dwc_georeferenceVerificationStatus) |
| [Georeferenced By](#dwc_georeferencedBy) |
| [Higher Geography](#dwc_higherGeography) |
| [Higher Geography ID](#dwc_higherGeographyID) |
| [Island](#dwc_island) |
| [Island Group](#dwc_islandGroup) |
| [Locality](#dwc_locality) |
| [Location According To](#dwc_locationAccordingTo) |
| [Location ID](#dwc_locationID) |
| [Location Remarks](#dwc_locationRemarks) |
| [Location Shown](#Iptc4xmpExt_LocationShown) |
| [Maximum Depth In Meters](#dwc_maximumDepthInMeters) |
| [Maximum Distance Above Surface In Meters](#dwc_maximumDistanceAboveSurfaceInMeters) |
| [Maximum Elevation In Meters](#dwc_maximumElevationInMeters) |
| [Minimum Depth In Meters](#dwc_minimumDepthInMeters) |
| [Minimum Distance Above Surface In Meters](#dwc_minimumDistanceAboveSurfaceInMeters) |
| [Minimum Elevation In Meters](#dwc_minimumElevationInMeters) |
| [Municipality](#dwc_municipality) |
| [Point Radius Spatial Fit](#dwc_pointRadiusSpatialFit) |
| [Province or State](#Iptc4xmpExt_ProvinceState) |
| [State Province](#dwc_stateProvince) |
| [Sublocation](#Iptc4xmpExt_Sublocation) |
| [Verbatim Coordinate System](#dwc_verbatimCoordinateSystem) |
| [Verbatim Coordinates](#dwc_verbatimCoordinates) |
| [Verbatim Depth](#dwc_verbatimDepth) |
| [Verbatim Elevation](#dwc_verbatimElevation) |
| [Verbatim Latitude](#dwc_verbatimLatitude) |
| [Verbatim Locality](#dwc_verbatimLocality) |
| [Verbatim Longitude](#dwc_verbatimLongitude) |
| [Verbatim SRS](#dwc_verbatimSRS) |
| [Water Body](#dwc_waterBody) |
| [World Region](#Iptc4xmpExt_WorldRegion) |

**Temporal Coverage Vocabulary**

| [Original Date and Time](#xmp_CreateDate) |
| [Temporal Coverage](#dcterms_temporal) |
| [Time of Day](#ac_timeOfDay) |

**Taxonomic Coverage Vocabulary**

| [Common Name](#dwc_vernacularName) |
| [Date Identified](#dwc_dateIdentified) |
| [Identification Qualifier](#dwc_identificationQualifier) |
| [Identified By](#dwc_identifiedBy) |
| [Name According To](#dwc_nameAccordingTo) |
| [Other Scientific Name](#ac_otherScientificName) |
| [Scientific Name ID](#dwc_scientificNameID) |
| [Scientific Taxon Name](#dwc_scientificName) |
| [Subject Life Stage](#dwc_lifeStage) |
| [Subject Orientation](#ac_subjectOrientation) |
| [Subject Part](#ac_subjectPart) |
| [Subject Preparation Technique](#dwc_preparations) |
| [Subject Sex](#dwc_sex) |
| [Taxon Count](#ac_taxonCount) |
| [Taxon Coverage](#ac_taxonCoverage) |

**Resource Creation Vocabulary**

| [Capture Device](#ac_captureDevice) |
| [Date and Time Digitized](#ac_digitizationDate) |
| [Location Created](#Iptc4xmpExt_LocationCreated) |
| [Resource Creation Technique](#ac_resourceCreationTechnique) |

**Related Resources Vocabulary**

| [Associated Observation Reference](#ac_associatedObservationReference) |
| [Associated Specimen Reference](#ac_associatedSpecimenReference) |
| [Derived From](#ac_derivedFrom) |
| [ID of Containing Collection](#ac_IDofContainingCollection) |
| [Provider ID](#ac_providerID) |
| [Related Resource ID](#ac_relatedResourceID) |

**Service Access Point Vocabulary**

| [Access URI](#ac_accessURI) |
| [Format](#dc_format) |
| [Further Information URL](#ac_furtherInformationURL) |
| [Hash](#ac_hashValue) |
| [Hash Function](#ac_hashFunction) |
| [Image Height](#exif_PixelYDimension) |
| [Image Width](#exif_PixelXDimension) |
| [Licensing Exception Statement](#ac_licensingException) |
| [Service Expectation](#ac_serviceExpectation) |
| [Variant](#ac_variant) |
| [Variant Description](#ac_variantDescription) |

## 7 Vocabularies
### 7.1 Management Vocabulary

| property | value |
|----------|-------|
| <a id="dcterms_available"></a>**Term Name:** | **dcterms:available** |
| Normative URI: | http://purl.org/dc/terms/available |
| Label: | Date Available |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | The date (often a range) that the resource became or will become available. The date and time must comply with the World Wide Web Consortium (W3C) datetime practice, which requires that date and time representation correspond to ISO 8601:1998, but with year fields always comprising 4 digits. This makes datetime records compliant with 8601:2004. AC datetime values may also follow 8601:2004 for ranges by separating two IS0 8601 datetime fields by a solidus ("forward slash", '/'). See also the wikipedia IS0 8601 entry for further explanation and examples. |
| Notes: | A use case is the harvesting of metadata published before the media are available, which are pending a formal publication elsewhere. One important example is the case of metadata that documents an occurrence, which metadata harvesters might exploit without use of the media. See also the wikipedia IS0 8601 entry for further explanation and examples. |
| | |
| <a id="ac_commenter"></a>**Term Name:** | **ac:commenter** |
| Normative URI: | http://rs.tdwg.org/ac/terms/commenter |
| Label: | Commenter |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | A URI denoting a person, using some controlled vocabulary such as FOAF. Implementers and communities of practice may produce restrictions or recommendations on the choice of vocabularies. |
| Notes: | See also Reviewer Comments for the distinction between Comments and Reviewer Comments. |
| | |
| <a id="ac_commenterLiteral"></a>**Term Name:** | **ac:commenterLiteral** |
| Normative URI: | http://rs.tdwg.org/ac/terms/commenterLiteral |
| Label: | Commenter |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | A name or the literal "anonymous" (= anonymously commented). |
| Notes: | See also Reviewer Comments for the distinction between Comments and Reviewer Comments. See also See also the entry for ac:commenter in this document and the section Namespaces, Prefixes and Term Names for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| <a id="ac_comments"></a>**Term Name:** | **ac:comments** |
| Normative URI: | http://rs.tdwg.org/ac/terms/comments |
| Label: | Comments |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Any comment provided on the media resource, as free-form text. Best practice would also identify the commenter. |
| Notes: | Comments may refer to the resource itself (e. g., asserting a taxon name or location of a biological subject in an image), or to the relation between resource and associated metadata (e. g., asserting that the taxon name given in the metadata is wrong, without asserting a positive identification). There is a separate item for Reviewer Comments, which is defined more as an expert-level review.Implementers or communities of practice might establish conventions about the meaning of the absence of a commenter, but this specification is silent on that matter. |
| | |
| <a id="ac_hasServiceAccessPoint"></a>**Term Name:** | **ac:hasServiceAccessPoint** |
| Normative URI: | http://rs.tdwg.org/ac/terms/hasServiceAccessPoint |
| Label: | Service Access Point |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | In a chosen serialization (RDF, XML Schema, etc.) the potentially multiple service access points (e.g., for different resolutions of an image) might be provided in a referenced or in a nested object. This property identifies one such access point. That is, each of potentially multiple values of hasServiceAccessPoint identifies a set of representation-dependent metadata using the properties defined under the section Service Access Point Vocabulary. |
| Notes: | Some serializations may flatten the model of service-access points by (a) dropping ac:hasServiceAccessPoint, ac:variant and ac:variantLiteral, (b) repeating properties from the Service Access Point Vocabulary and prefixing them with values of ac:variantLiteral. If such a flat serialization is necessary for services, we recommend to select from among term names of the form "AB" where "A" is one of thumbnail, trailer, lowerQuality, mediumQuality, goodQuality, bestQuality, offline and "B" is one of AccessURI, Format, Extent, FurtherInformationURL, LicensingException, ServiceExpectation (example: thumbnailAccessURI). Implementers in specific constraint languages such as XML Schema or RDF may wish to make Access URI and perhaps dcterms:format mandatory on instances of the service access point. |
| | |
| <a id="dcterms_identifier"></a>**Term Name:** | **dcterms:identifier** |
| Normative URI: | http://purl.org/dc/terms/identifier |
| Label: | Identifier |
| | **Layer:** 1 -- **Required:** Yes/No -- **Repeatable:** Yes |
| Definition: | An arbitrary code that is unique for the resource, with the resource being either a provider, collection, or media item. |
| Notes: | Using multiple identifiers implies that they have a same-as relationship, i.e. they all identify the same object (e. g. an object may have all of an http-URL, an lsid-URI, and a UUID). |
| | |
| <a id="xmp_MetadataDate"></a>**Term Name:** | **xmp:MetadataDate** |
| Normative URI: | http://ns.adobe.com/xap/1.0/MetadataDate |
| Label: | Metadata Date |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | Point in time recording when the last modification to metadata (not necessarily the media object itself) occurred. The date and time must comply with the World Wide Web Consortium (W3C) datetime practice, which requires that date and time representation correspond to ISO 8601:1998, but with year fields always comprising 4 digits. This makes datetime records compliant with 8601:2004. AC datetime values may also follow 8601:2004 for ranges by separating two IS0 8601 datetime fields by a solidus ("forward slash", '/'). See also the wikipedia IS0 8601 entry for further explanation and examples. |
| Notes: | This is not dcterms:modified, which refers to the resource itself rather than its metadata. See also the wikipedia IS0 8601 entry for further explanation and examples. |
| | |
| <a id="ac_metadataLanguage"></a>**Term Name:** | **ac:metadataLanguage** |
| Normative URI: | http://rs.tdwg.org/ac/terms/metadataLanguage |
| Label: | Metadata Language |
| | **Layer:** 1 -- **Required:** Yes -- **Repeatable:** No |
| Definition: | URI from the ISO639-2 list of URIs for ISO 3-letter language codes. |
| Notes: | This is NOT dcterms:language, which is about the resource, not the metadata. Metadata Language is deliberately single-valued, imposing on unstructured serializations a requirement that multi-lingual metadata be represented as separate, complete, metadata records. Audubon Core requires that each record also contains the language-neutral terms. In the absence of this requirement, metadata consumers would need to know which terms are language-neutral and merge these terms from all provided metadataLanguages into a single record. Metadata consumers may re-combine the information based on the dcterms:identifier that identifies the multimedia resource. At least one of ac:metadataLanguage and ac:metadataLanguageLiteral must be supplied but, when feasible, supplying both may make the metadata more widely useful. They must specify the same language. In case of ambiguity, ac:metadataLanguage prevails. Nothing in this document would, however, prevent an implementer, e. g. of an XML-Schema representation, from providing a fully hierarchical schema in which language neutral terms occur only a single time, and only the language-specific terms are repeated in a way that unambigously relates them to a metadata language. In RDF it may be a simple repetition of plain literals associated with a language (e.g., xml:lang attribute in RDF/XML). The language attribute would then be required in Audubon Core and would replace ac:metadataLanguage. |
| | |
| <a id="ac_metadataLanguageLiteral"></a>**Term Name:** | **ac:metadataLanguageLiteral** |
| Normative URI: | http://rs.tdwg.org/ac/terms/metadataLanguageLiteral |
| Label: | Metadata Language |
| | **Layer:** 1 -- **Required:** Yes -- **Repeatable:** No |
| Definition: | Language of description and other metadata (but not necessarily of the image itself) represented as an ISO639-2 three letter language code. ISO639-1 two-letter codes are permitted but deprecated. |
| Notes: | This is NOT dc:language, which is about the resource, not the metadata. Metadata Language is deliberately single-valued, imposing on unstructured serializations a requirement that multi-lingual metadata be represented as separate, complete, metadata records. Audubon Core requires that each record also contains the language-neutral terms. In the absence of this requirement, metadata consumers would need to know which terms are language-neutral and merge these terms from all provided metadataLanguages into a single record. Metadata consumers may re-combine the information based on the dcterms:identifier that identifies the multimedia resource. At least one of ac:metadataLanguage and ac:metadataLanguageLiteral must be supplied but, when feasible, supplying both may make the metadata more widely useful. They must specify the same language. In case of ambiguity, ac:metadataLanguage prevails. Nothing in this document would, however, prevent an implementer, e. g. of an XML-Schema representation, from providing a fully hierarchical schema in which language neutral terms occur only a single time, and only the language-specific terms are repeated in a way that unambigously relates them to a metadata language. In RDF it may be a simple repetition of plain literals associated with a language (e.g., xml:lang attribute in RDF/XML). The language attribute would then be required in Audubon Core and would replace ac:metadataLanguage. |
| | |
| <a id="dcterms_modified"></a>**Term Name:** | **dcterms:modified** |
| Normative URI: | http://purl.org/dc/terms/modified |
| Label: | Modified |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Date that the media resource was altered. The date and time must comply with the World Wide Web Consortium (W3C) datetime practice, which requires that date and time representation correspond to ISO 8601:1998, but with year fields always comprising 4 digits. This makes datetime records compliant with 8601:2004. AC datetime values may also follow 8601:2004 for ranges by separating two IS0 8601 datetime fields by a solidus ("forward slash", '/'). See also the wikipedia IS0 8601 entry for further explanation and examples. |
| Notes: | dcterms:modified permits all modification dates to be recorded, or if only one is recorded, it is assumed to be the latest. See also the wikipedia IS0 8601 entry for further explanation and examples. |
| | |
| <a id="ac_providerManagedID"></a>**Term Name:** | **ac:providerManagedID** |
| Normative URI: | http://rs.tdwg.org/ac/terms/providerManagedID |
| Label: | Provider-managed ID |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | A free-form identifier (a simple number, an alphanumeric code, a URL, etc.) that is unique and meaningful primarily for the data provider. |
| Notes: | Ideally, this would be a globally unique identifier (GUID), but the provider is encouraged to supply any form of identifier that simplifies communications on resources within their project and helps to locate individual data items in the provider's data repositories. It is the provider's decision whether to expose this value or not. |
| | |
| <a id="xmp_Rating"></a>**Term Name:** | **xmp:Rating** |
| Normative URI: | http://ns.adobe.com/xap/1.0/Rating |
| Label: | Rating |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | A rating of the media resources, provided by record originators or editors, with "-1" defining "rejected", "0" defining "unrated", and "1" (worst) to "5" (best). |
| Notes: | The origin of the rating is not communicated. It may, e. g., be based on user feedback or on editorial ratings. If Rating is not present, a value of 0 may be assumed. By "user-assigned" is meant assigned by the originator or editor of the record using the term. |
| | |
| <a id="ac_reviewer"></a>**Term Name:** | **ac:reviewer** |
| Normative URI: | http://rs.tdwg.org/ac/terms/reviewer |
| Label: | Reviewer |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | URI for a reviewer. If present, then resource is peer-reviewed, even if there are Reviewer Comments is absent or empty. Its presence tells whether an expert in the subject featured in the media has reviewed the media item or collection and approved its metadata description; must display a name or the literal "anonymous" (= anonymously reviewed). |
| Notes: | Provider is asserting they accept this review as competent. See also ac:reviewerLiteral in this document and the section Namespaces, Prefixes and Term Names for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| <a id="ac_reviewerComments"></a>**Term Name:** | **ac:reviewerComments** |
| Normative URI: | http://rs.tdwg.org/ac/terms/reviewerComments |
| Label: | Reviewer Comments |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Any comment provided by a reviewer with expertise in the subject, as free-form text. |
| Notes: | Reviewer Comments may refer to the resource itself (e. g., asserting a taxon name or location of a biological subject in an image), or to the relation between resource and associated metadata (e. g., asserting that the taxon name given in the metadata is wrong, without asserting a positive identification). There is a separate item "Comments" for text from commenters of unrecorded expertise. |
| | |
| <a id="ac_reviewerLiteral"></a>**Term Name:** | **ac:reviewerLiteral** |
| Normative URI: | http://rs.tdwg.org/ac/terms/reviewerLiteral |
| Label: | Reviewer |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | String providing the name of a reviewer. If present, then resource is peer-reviewed, even if Reviewer Comments is absent or empty. Its presence tells whether an expert in the subject featured in the media has reviewed the media item or collection and approved its metadata description; must display a name or the literal "anonymous" (= anonymously reviewed). |
| Notes: | Provider is asserting they accept this review as competent. See also ac:reviewer and the section Namespaces, Prefixes and Term Names for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| <a id="ac_subtype"></a>**Term Name:** | **ac:subtype** |
| Normative URI: | http://rs.tdwg.org/ac/terms/subtype |
| Label: | Subtype |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Any URI may be used that provides for more specialization than the type. Possible values are community-defined. For exmamples see the non-normative page AC_Subtype_Examples. |
| Notes: | The subtype term may not be applied to Collection objects. However, the Description term in the Content Coverage Vocabulary may add further description to a Collection object. The subtype vocabulary may be extended by users provided they identify the term by a URI which is not in the ac namespace (for example, using "http://my.inst.org/namespace/metadata/subtype/repair-manual"). Conforming applications may choose to ignore these. See ac:subtypeLiteral for usage with strings. |
| | |
| <a id="ac_subtypeLiteral"></a>**Term Name:** | **ac:subtypeLiteral** |
| Normative URI: | http://rs.tdwg.org/ac/terms/subtypeLiteral |
| Label: | Subtype |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The subtype should provide more specialization than the type. Possible values are community-defined. For exmamples see the non-normative page AC_Subtype_Examples. |
| Notes: | The subtypeLiteral term may not be applied to Collection objects. However, the Description term in the Content Coverage Vocabulary may add further description to a Collection object. |
| | |
| <a id="dcterms_title"></a>**Term Name:** | **dcterms:title** |
| Normative URI: | http://purl.org/dc/terms/title |
| Label: | Title |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | Concise title, name, or brief descriptive label of institution, resource collection, or individual resource. This field should include the complete title with all the subtitles, if any. |
| Notes: | It is strongly suggested to provide a title. The title facilitates interactions with humans: e.g., it could be used as display text of hyperlinks or to provide a choice of images in a pick list. The title is therefore highly useful and an effort should be made to provide it where it is not already available. When the resource is a collection without an institutional or official name, but with a thematic content, a descriptive title, e. g. "Urban Ants of New England," would be suitable. In individual media resources depicting taxa, the scientific name or names of taxa often form a good title. Common names in addition to or instead of scientific names are also acceptable. Indications of action or roles captured by the media resource, such as predatory acts, are desirable ("Rattlesnake eating deer mouse", "Pollinators of California Native Plants"). |
| | |
| <a id="dc_type"></a>**Term Name:** | **dc:type** |
| Normative URI: | http://purl.org/dc/elements/1.1/type |
| Label: | Type |
| | **Layer:** 1 -- **Required:** Yes -- **Repeatable:** No |
| Definition: | dc:type may take as value any type term from the DCMI Type Vocabulary. Recommended terms are Collection, StillImage, Sound, MovingImage, InteractiveResource, Text. Values may be used either in their literal form, or with a full namespace (e. g. from a controlled vocabulary, but the best practice is to use the literal form when using dc:type and use dcterms:type when you can supply the URI from a controlled vocabulary and implementers may require this practice. At least one of dc:type and dcterms:type must be supplied but, when feasible, supplying both may make the metadata more widely useful. The values of each should designate the same type, but in case of ambiguity dcterms:type prevails. |
| Notes: | A Collection should be given type "Collection" when using dc:type. If the resource is a Collection, this item does not identify what types of objects it may contain. Following the DC recommendations for the Text type, images of text should be marked given as the string Text when provided as a string. See also the entry for dcterms:type in this document and see the DCMI FAQ on DC and DCTERMS Namespaces for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| <a id="dcterms_type"></a>**Term Name:** | **dcterms:type** |
| Normative URI: | http://purl.org/dc/terms/type |
| Label: | Type |
| | **Layer:** 1 -- **Required:** Yes -- **Repeatable:** No |
| Definition: | A full URI preferably from among the type URIs specified in the DCMI Type Vocabulary. Recommended terms are those URIs whose labels are Collection, StillImage, Sound, MovingImage, InteractiveResource, or Text (e.g. . Also recommended are the full URIs of ac:PanAndZoomImage, ac:3DStillImage, and ac: 3DMovingImage. Values MUST NOT be a string, but a URI with full namespace (e. g. from a controlled vocabulary. Implementers and communities of practice may determine whether specific controlled vocabularies must be used. If the resource is a Collection, this item does not identify what types of objects it may contain. Following the DC recommendations at http://purl.org/dc/dcmitype/Text, images of text should be with this URI. |
| Notes: | Following the DC recommendations for the Text type, images of text should be given as http://purl.org/dc/dcmitype/Text when given as a URI. See also the entry for dc:type in this document and see the DCMI FAQ on DC and DCTERMS Namespaces for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. At least one of dc:type and dcterms:type must be supplied but, when feasible, supplying both may make the metadata more widely useful. The values of each should designate the same type, but in case of ambiguity dcterms:type prevails. |
| | |

### 7.2 Attribution Vocabulary

| property | value |
|----------|-------|
| <a id="ac_attributionLinkURL"></a>**Term Name:** | **ac:attributionLinkURL** |
| Normative URI: | http://rs.tdwg.org/ac/terms/attributionLinkURL |
| Label: | Attribution Link URL |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | The URL where information about ownership, attribution, etc. of the resource may be found. |
| Notes: | This URL may be used in creating a clickable logo. Providers should consider making this link as specific and useful to consumers as possible, e. g., linking to a metadata page of the specific image resource rather than to a generic page describing the owner or provider of a resource. |
| | |
| <a id="ac_attributionLogoURL"></a>**Term Name:** | **ac:attributionLogoURL** |
| Normative URI: | http://rs.tdwg.org/ac/terms/attributionLogoURL |
| Label: | Attribution URL |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | The URL of the icon or logo image to appear in source attribution. |
| Notes: | Entering this URL into a browser should only result in the icon (not in a webpage including the icon). |
| | |
| <a id="photoshop_Credit"></a>**Term Name:** | **photoshop:Credit** |
| Normative URI: | http://ns.adobe.com/photoshop/1.0/Credit |
| Label: | Credit |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | free text for "Please cite this as ..." |
| Notes: | IPTC also refers to this generically as a "Credit Line" as it is frequently displayed with the media. |
| | |
| <a id="ac_fundingAttribution"></a>**Term Name:** | **ac:fundingAttribution** |
| Normative URI: | http://rs.tdwg.org/ac/terms/fundingAttribution |
| Label: | Funding |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Organizations or individuals who funded the creation of the resource. |
| | |
| <a id="ac_licenseLogoURL"></a>**Term Name:** | **ac:licenseLogoURL** |
| Normative URI: | http://rs.tdwg.org/ac/terms/licenseLogoURL |
| Label: | License Logo URL |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | A URL providing access to a logo that symbolizes the License. |
| Notes: | The originating metadata provider is strongly urged to choose a suitable logo as a graphical representation of the license. Failure to do so may leave downstream aggregators in a difficult position to supply a logo that adequately represents the professional, legal, or social aims of the licensors (license givers). Example: http://i.creativecommons.org/l/by-nc-sa/3.0/us/88x31.png provides access to a logo image. |
| | |
| <a id="xmpRights_Owner"></a>**Term Name:** | **xmpRights:Owner** |
| Normative URI: | http://ns.adobe.com/xap/1.0/rights/Owner |
| Label: | Copyright Owner |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | A list of the names of the owners of the copyright. 'Unknown' is an acceptable value, but 'Public Domain' is not. |
| Notes: | Some providers use dc:publisher for this purpose, but it seems doubtful that the publisher is by necessity the copyright owner. 'Public Domain' is not an appropriate value because it denotes something that is not under copyright. In this case, omit or leave empty xmpRights:Owner, and put 'Public Domain' in the Copyright Statement (dc:rights). Except for 'Public Domain' resources, it is strongly urged that this field be supplied. |
| | |
| <a id="dc_rights"></a>**Term Name:** | **dc:rights** |
| Normative URI: | http://purl.org/dc/elements/1.1/rights |
| Label: | Copyright Statement |
| | **Layer:** 1 -- **Required:** Yes -- **Repeatable:** No |
| Definition: | Information about rights held in and over the resource. A full-text, readable copyright statement, as required by the national legislation of the copyright holder. On collections, this applies to all contained objects, unless the object itself has a different statement. Examples: "Copyright XY 2008, all rights reserved", "© 2008 XY Museum", "Public Domain.", "Copyright unknown." Do not place just the name of the copyright holder(s) here! That belongs in a list in the xmpRights:Owner field, which should be supplied if dc:rights is not 'Public Domain', which is appropriate only if the resource is known to be not under copyright. |
| Notes: | This expresses rights over the media resource, not over the metadata text. At least one of dcterms:rights and dc:rights must be supplied but, when feasible, supplying both may make the metadata more widely useful. They must specify the same rights. In case of ambiguity, dcterms:rights prevails. |
| | |
| <a id="dcterms_rights"></a>**Term Name:** | **dcterms:rights** |
| Normative URI: | http://purl.org/dc/terms/rights |
| Label: | Copyright Statement |
| | **Layer:** 1 -- **Required:** Yes -- **Repeatable:** No |
| Definition: | A URI pointing to structured information about rights held in and over the resource. Examples include and . At least one of dcterms:rights and dc:rights must be supplied but, when feasible, supplying both may make the metadata more widely useful. They must specify the same rights. In case of ambiguity, dcterms:rights prevails. |
| Notes: | This expresses rights over the media resource, not over the metadata text. See also the entry for dc:rights in this document and see the DCMI FAQ on DC and DCTERMS Namespaces for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| <a id="dc_source"></a>**Term Name:** | **dc:source** |
| Normative URI: | http://purl.org/dc/elements/1.1/source |
| Label: | Published Source |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A string providing an identifiable source from which the described resources was derived. |
| Notes: | If the resource was digitized from a non-digital resource, or was also previously published in a digital or printed publication, this describes the original. Do not put generally "related" publications in here. This field normally contains a free-form text description. If a URI is available it should be provided in dcterms:source. Can be repeatable if a montage of images. Information about further provenance beyond the ultimate source should be put in the derivedFrom attribute. See also the entry for dcterms:source in this document and see the DCMI FAQ on DC and DCTERMS Namespaces for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions |
| | |
| <a id="dcterms_source"></a>**Term Name:** | **dcterms:source** |
| Normative URI: | http://purl.org/dc/terms/source |
| Label: | Published Source |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | URI for an identifiable source from which the described resources was derived. |
| Notes: | If the resource was digitized from a non-digital resource, or was also previously published in a digital or printed publication, this describes the original. If a string is required for this, use dc:source. Do not put generally "related" publications in here. A URI that can be resolved and dereferenced to provide a description of the source resource may also be used here. For example, "http://www.loc.gov/pictures/item/fsa1998021539/PP/" is the address of a web page that provides a description the original negative of a famous picture by the photographer Dorothea Lange and so would be an appropriate value of dcterms:source. The term may be repeatable if a montage of images. Information about further provenance beyond the ultimate source should be put in the derivedFrom attribute. See also the entry for dc:source in this document and see the DCMI FAQ on DC and DCTERMS Namespaces for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| <a id="xmpRights_UsageTerms"></a>**Term Name:** | **xmpRights:UsageTerms** |
| Normative URI: | http://ns.adobe.com/xap/1.0/rights/UsageTerms |
| Label: | License Terms |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | The license statement defining how resources may be used. Information on a collection applies to all contained objects unless the object has a different statement. |
| Notes: | Example: "Available under Creative Commons BY-SA 3.0 license". This also describes the commercial availability of items. Buying an identification tool or media resource is essentially the purchase of an individual license. Examples for such License statements: "Available through bookstores" for a commercially published CD, and "Individual licenses available for purchase" for a high-resolution image. Note that the medium or low resolution levels of the same image may be available under open access licenses. In general, this term determines the default licensing for the media. License terms specific to variants or representations of the media resource (e.g., different resolutions) are dealt within the section on Service Access Point Vocabulary |
| | |
| <a id="xmpRights_WebStatement"></a>**Term Name:** | **xmpRights:WebStatement** |
| Normative URI: | http://ns.adobe.com/xap/1.0/rights/WebStatement |
| Label: | License URL |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | A URL defining or further elaborating on the license statement (e. g., a web page explaining the precise terms of use). |
| Notes: | The value of this field may provide a complete definition of the terms of use. For Creative Commons, the appropriate value is the URL of the defining Web page for the license. Example: http://creativecommons.org/licenses/by-nc-sa/3.0/us/. Where different quality variants (e. g. different resolutions of images) are published under different licenses, the AC term "Licensing Exception Statement" supports variant-specific licenses. |
| | |

### 7.3 Agents Vocabulary

| property | value |
|----------|-------|
| <a id="dc_creator"></a>**Term Name:** | **dc:creator** |
| Normative URI: | http://purl.org/dc/elements/1.1/creator |
| Label: | Creator |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The person or organization responsible for creating the media resource. |
| Notes: | The value may be simple text including contact information. Note that the Creator need not be the Copyright Owner. See also the entry for dcterms:creator in this document and see the DCMI FAQ on DC and DCTERMS Namespaces for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| <a id="dcterms_creator"></a>**Term Name:** | **dcterms:creator** |
| Normative URI: | http://purl.org/dc/terms/creator |
| Label: | Creator |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A URI representing the person or organization responsible for creating the media resource. |
| Notes: | Note that the Creator need not be the Copyright Owner. See also the entry for dc:creator in this document and see the DCMI FAQ on DC and DCTERMS Namespaces for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| <a id="ac_metadataCreator"></a>**Term Name:** | **ac:metadataCreator** |
| Normative URI: | http://rs.tdwg.org/ac/terms/metadataCreator |
| Label: | Metadata Creator |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Person or organization originally creating the resource metadata record. |
| Notes: | See also the entry for ac:metadataCreatorLiteral in this document and the section Namespaces, Prefixes and Term Names for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| <a id="ac_metadataCreatorLiteral"></a>**Term Name:** | **ac:metadataCreatorLiteral** |
| Normative URI: | http://rs.tdwg.org/ac/terms/metadataCreatorLiteral |
| Label: | Metadata Creator |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Person or organization originally creating the resource metadata record. |
| Notes: | See also the entry for ac:metadataCreator in this document and the section Namespaces, Prefixes and Term Names for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| <a id="ac_metadataProvider"></a>**Term Name:** | **ac:metadataProvider** |
| Normative URI: | http://rs.tdwg.org/ac/terms/metadataProvider |
| Label: | Metadata Provider |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | URI of person or organization originally responsible for providing the resource metadata record. |
| Notes: | Media resources and their metadata may be served from different institutions, e. g. in the case of aggregators adding user annotations, taxon identifications, or ratings. Compare Provider. See also the entry for ac:metadataProviderLiteral in this document and the section Namespaces, Prefixes and Term Names for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| <a id="ac_metadataProviderLiteral"></a>**Term Name:** | **ac:metadataProviderLiteral** |
| Normative URI: | http://rs.tdwg.org/ac/terms/metadataProviderLiteral |
| Label: | Metadata Provider |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Person or organization originally responsible for providing the resource metadata record. |
| Notes: | Media resources and their metadata may be served from different institutions, e. g. in the case of aggregators adding user annotations, taxon identifications, or ratings. Compare Provider. See also the entry for ac:metadataProvider in this document and the section Namespaces, Prefixes and Term Names for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| <a id="ac_provider"></a>**Term Name:** | **ac:provider** |
| Normative URI: | http://rs.tdwg.org/ac/terms/provider |
| Label: | Provider |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | URI for person or organization responsible for presenting the media resource. If no separate Metadata Provider is given, this also attributes the metadata. |
| Notes: | Media resources and their metadata may be served from different institutions, e. g. in the case of aggregators adding user annotations, taxon identifications, or ratings. See also the entry for ac:providerLiteral in this document and the section Namespaces, Prefixes and Term Names for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| <a id="ac_providerLiteral"></a>**Term Name:** | **ac:providerLiteral** |
| Normative URI: | http://rs.tdwg.org/ac/terms/providerLiteral |
| Label: | Provider |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | Person or organization responsible for presenting the media resource. If no separate Metadata Provider is given, this also attributes the metadata. |
| Notes: | Media resources and their metadata may be served from different institutions, e. g. in the case of aggregators adding user annotations, taxon identifications, or ratings. See also the entry for ac:provider in this document and the section Namespaces, Prefixes and Term Names for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |

### 7.4 Content Coverage Vocabulary

| property | value |
|----------|-------|
| <a id="ac_caption"></a>**Term Name:** | **ac:caption** |
| Normative URI: | http://rs.tdwg.org/ac/terms/caption |
| Label: | Caption |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | As alternative or in addition to description, a caption is free-form text to be displayed together with (rather than instead of) a resource that is suitable for captions (especially images). |
| Notes: | If both description and caption are present in the metadata, a description is typically displayed instead of the resource, a caption together with the resource. Often only one of description or caption is present; choose the term most appropriate for your metadata. |
| | |
| <a id="Iptc4xmpExt_CVterm"></a>**Term Name:** | **Iptc4xmpExt:CVterm** |
| Normative URI: | http://iptc.org/std/Iptc4xmpExt/2008-02-29/CVterm |
| Label: | Subject Category |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Controlled vocabulary of subjects to support broad classification of media items. Terms from various controlled vocabularies may be used. AC-recommended vocabularies are preferred and may be unqualified literals (not a full URI). For terms from other vocabularies either a precise URI should be used, or, as long as all unqualified terms in all vocabularies are unique, metadata should provide the source vocabularies using the Subject Category Vocabulary term. |
| Notes: | Recommended sets include: the NASA Global Change Master Directory (GCMD; http://gcmd.nasa.gov/), Subject Categories defined in Key to Nature (K2N; http://www.keytonature.eu/wiki/Subject_Category), the BioComplexity Thesaurus (https://www2.usgs.gov/core_science_systems/csas/biocomplexity_thesaurus/), the Description Type GBIF Vocabulary (http://rs.gbif.org/vocabulary/gbif/description_type.xml), the TDWG Species Profile Model (http://rs.tdwg.org/ontology/voc/SPMInfoItems.rdf), the Plinian Core (https://github.com/PlinianCore/Documentation/wiki/About), the European Environmental Agency GEneral Multilingual Environmental Thesaurus (GEMET; http://www.eionet.europa.eu/gemet), and the LTER Controlled Vocabulary (http://vocab.lternet.edu/). The vocabulary may include major taxonomic groups (such as "vertebrates" or "fungi") or ecosystem terms ("savannah", "temperate rain forest", "forest fires", "aquatic vertebrates"). Other formal classifications (published in print or online) such as habitat, fuel, invasive species, agroproductivity, fisheries, migratory species etc. are also suitable. |
| | |
| <a id="dcterms_description"></a>**Term Name:** | **dcterms:description** |
| Normative URI: | http://purl.org/dc/terms/description |
| Label: | Description |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | Description of collection or individual resource, containing the Who, What, When, Where and Why as free-form text. This normative document is silent on the nature of formatting in the text. It is the role of implementers of an AC concrete representation (e.g., an XML Schema, an RDF representation, etc.) to decide and document how formatting advice will be represented in descriptions serialized according to such representations. |
| Notes: | It optionally allows the presentation of detailed information and will in most cases be shown together with the resource title. If both a description and a caption are present in the metadata, a description is typically displayed instead of the resource, whereas a caption is displayed together with the resource. The description should aim to be a good proxy for the underlying media resource in cases where only text can be shown, whereas the caption may only make sense when shown together with the media. Often only one of description or caption is present; choose the term most appropriate for your metadata. |
| | |
| <a id="dc_language"></a>**Term Name:** | **dc:language** |
| Normative URI: | http://purl.org/dc/elements/1.1/language |
| Label: | Language |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Language(s) of resource itself represented in the ISO639-2 three-letter language code. ISO639-1 two-letter codes are permitted but deprecated. |
| Notes: | An image may contain language such as superimposed labels. If an image is of a natural scene or organism, without any language included, the resource is language-neutral (ISO code "zxx"). Resources with present but unknown language are to be coded as undetermined (ISO code "und"). Regional dialects or other special cases should conform to the ISO639-5 Alpha-3 Code for Language Families and Groups where possible or the IETF Best Practices for Tags Identifying Languages where not. See also the entry for dcterms:language in this document and see the DCMI FAQ on DC and DCTERMS Namespaces for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| <a id="dcterms_language"></a>**Term Name:** | **dcterms:language** |
| Normative URI: | http://purl.org/dc/terms/language |
| Label: | Language |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | URI from the ISO639-2 list of URIs for ISO 3-letter language codes. |
| Notes: | An image may contain language such as superimposed labels. If an image is of a natural scene or organism, without any language included, the resource is language-neutral with URI http://id.loc.gov/vocabulary/iso639-2/zxx corresponding to ISO ISO639-2 code "zxx". Resources with present but unknown language are to be coded as undetermined, with URI http://id.loc.gov/vocabulary/iso639-2/und corresponding to ISO639-2 code "und". Regional dialects or other special cases should conform to the ISO639-5 Alpha-3 Code for Language Families and Groups where possible, or IETF Best Practices for Tags Identifying Languages where not. See also the entry for dc:language in this document and see the DCMI FAQ on DC and DCTERMS Namespaces for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| <a id="ac_physicalSetting"></a>**Term Name:** | **ac:physicalSetting** |
| Normative URI: | http://rs.tdwg.org/ac/terms/physicalSetting |
| Label: | Physical Setting |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The setting of the content represented in media such as images, sounds, and movies if the provider deems them relevant. Constrained vocabulary of: "Natural" = Object in its natural setting of the object (e. g. living organisms in their natural environment); "Artificial" = Object in an artificial environment (e. g. living organisms in an artificial environment such as a zoo, garden, greenhouse, or laboratory); "Edited" = Human media editing of a natural setting or media acquisition with a separate media background such as a photographic backdrop. |
| Notes: | Multiple values may be needed for movies or montages. See also ac:resourceCreationTechnique which should be used to describe any modifications to the resource itself. Communities of practice should form best practices for the use of these controlled terms. |
| | |
| <a id="ac_subjectCategoryVocabulary"></a>**Term Name:** | **ac:subjectCategoryVocabulary** |
| Normative URI: | http://rs.tdwg.org/ac/terms/subjectCategoryVocabulary |
| Label: | Subject Category Vocabulary |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Any vocabulary or formal classification from which terms in the Subject Category have been drawn. |
| Notes: | The AC recommended vocabularies do not need to be cited here. There is no required linkage between individual Subject Category terms and the vocabulary; the mechanism is intended to support discovery of the normative URI for a term, but not guarantee it. |
| | |
| <a id="ac_tag"></a>**Term Name:** | **ac:tag** |
| Normative URI: | http://rs.tdwg.org/ac/terms/tag |
| Label: | Tag |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | General keywords or tags. |
| Notes: | Tags may be multi-worded phrases. Where scientific names, common names, geographic locations, etc. are separable, those should go into the more specific coverage metadata items provided further below. Examples: "flower diagram". Character or part keywords like "leaf", or "flower color" are especially desirable. |
| | |

### 7.5 Geography Vocabulary

All geography terms from the Darwin Core version of 9 Dec 2009 are deemed included in the Core Layer. Specifically, this includes exactly those which are declared by Darwin Core to be in Darwin Core Class [dwc:Location](http://rs.tdwg.org/dwc/terms/Location). Note that [dwc:locality](http://rs.tdwg.org/dwc/terms/locality) may be used, but as applied to media this term may be ambiguous as to whether it applies to the location depicted or the location at which the media was created. When disambiguating information is available, it is better to use the terms Location Shown and Location Created. The latter is in the Resource Creation Vocabulary.

Location Created and Location Shown are separated in the current version of IPTC, and the metadata working group ([Metadata Working Group Guidelines for Handling Image Metadata, Version 2.0, November 2010](http://www.metadataworkinggroup.org/pdf/mwg_guidance.pdf)) also recommends this. We follow this below in order to support the expected future increase of automatic GPS-based coordinate recording. As a special case, the AC group recommends to change the semantics of Location Shown in the case of biodiversity specimens, where the original location may differ from the current location at which the specimen is held in a collection. In this case, Location Shown should exclusively refer to the location where a specimen was originally collected (gathering or sampling location). Use Location Created to express the location where the resource was created (a specimen was digitized).

| property | value |
|----------|-------|
| <a id="Iptc4xmpExt_City"></a>**Term Name:** | **Iptc4xmpExt:City** |
| Normative URI: | http://iptc.org/std/Iptc4xmpExt/2008-02-29/City |
| Label: | City or Place Name |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Optionally, the name of a city or place commonly found in gazetteers (such as a mountain or national park) in which the subjects (e. g., species, habitats, or events) were located. |
| | |
| <a id="dwc_continent"></a>**Term Name:** | **dwc:continent** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/continent |
| Label: | Continent |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The name of the continent in which the Location occurs. Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names. |
| | |
| <a id="dwc_coordinatePrecision"></a>**Term Name:** | **dwc:coordinatePrecision** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/coordinatePrecision |
| Label: | Coordinate Precision |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A decimal representation of the precision of the coordinates given in the decimalLatitude and decimalLongitude. |
| | |
| <a id="dwc_coordinateUncertaintyInMeters"></a>**Term Name:** | **dwc:coordinateUncertaintyInMeters** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/coordinateUncertaintyInMeters |
| Label: | Coordinate Uncertainty In Meters |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The horizontal distance (in meters) from the given decimalLatitude and decimalLongitude describing the smallest circle containing the whole of the Location. Leave the value empty if the uncertainty is unknown, cannot be estimated, or is not applicable (because there are no coordinates). Zero is not a valid value for this term. |
| | |
| <a id="dwc_country"></a>**Term Name:** | **dwc:country** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/country |
| Label: | Country |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The name of the country or major administrative unit in which the Location occurs. Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names. |
| | |
| <a id="Iptc4xmpExt_CountryCode"></a>**Term Name:** | **Iptc4xmpExt:CountryCode** |
| Normative URI: | http://iptc.org/std/Iptc4xmpExt/2008-02-29/CountryCode |
| Label: | Country Code |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The geographic location of the specific entity or entities documented by the media item, expressed through a constrained vocabulary of countries using 2-letter ISO country code (e. g. "it, si"). |
| Notes: | Accepted exceptions to be used instead of ISO codes are: "Global", "Marine", "Europe", "N-America", "C-America", "S-America", "Africa", "Asia", "Oceania", ATA = "Antarctica", XEU = "European Union", XAR = "Arctic", "ZZZ" = "Unknown country" (3 letter abbreviations from IPTC codes). This list may be extended as necessary. |
| | |
| <a id="dwc_countryCode"></a>**Term Name:** | **dwc:countryCode** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/countryCode |
| Label: | Country Code |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The standard code for the country in which the Location occurs. Recommended best practice is to use ISO 3166-1-alpha-2 country codes. |
| | |
| <a id="Iptc4xmpExt_CountryName"></a>**Term Name:** | **Iptc4xmpExt:CountryName** |
| Normative URI: | http://iptc.org/std/Iptc4xmpExt/2008-02-29/CountryName |
| Label: | Country Name |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | This field can be free text, but where possible, the use of http://iptc.org/std/Iptc4xmpExt/2008-02-29/CountryCode is preferred. |
| | |
| <a id="dwc_county"></a>**Term Name:** | **dwc:county** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/county |
| Label: | County |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The full, unabbreviated name of the next smaller administrative region than stateProvince (county, shire, department, etc.) in which the Location occurs. |
| | |
| <a id="dwc_decimalLatitude"></a>**Term Name:** | **dwc:decimalLatitude** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/decimalLatitude |
| Label: | Decimal Latitude |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The geographic latitude (in decimal degrees, using the spatial reference system given in geodeticDatum) of the geographic center of a Location. Positive values are north of the Equator, negative values are south of it. Legal values lie between -90 and 90, inclusive. |
| | |
| <a id="dwc_decimalLongitude"></a>**Term Name:** | **dwc:decimalLongitude** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/decimalLongitude |
| Label: | Decimal Longitude |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The geographic longitude (in decimal degrees, using the spatial reference system given in geodeticDatum) of the geographic center of a Location. Positive values are east of the Greenwich Meridian, negative values are west of it. Legal values lie between -180 and 180, inclusive. |
| | |
| <a id="dwc_footprintSpatialFit"></a>**Term Name:** | **dwc:footprintSpatialFit** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/footprintSpatialFit |
| Label: | Footprint Spatial Fit |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The ratio of the area of the footprint (footprintWKT) to the area of the true (original, or most specific) spatial representation of the Location. Legal values are 0, greater than or equal to 1, or undefined. A value of 1 is an exact match or 100% overlap. A value of 0 should be used if the given footprint does not completely contain the original representation. The footprintSpatialFit is undefined (and should be left blank) if the original representation is a point and the given georeference is not that same point. If both the original and the given georeference are the same point, the footprintSpatialFit is 1. |
| | |
| <a id="dwc_footprintSRS"></a>**Term Name:** | **dwc:footprintSRS** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/footprintSRS |
| Label: | Footprint SRS |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A Well-Known Text (WKT) representation of the Spatial Reference System (SRS) for the footprintWKT of the Location. Do not use this term to describe the SRS of the decimalLatitude and decimalLongitude, even if it is the same as for the footprintWKT - use the geodeticDatum instead. |
| | |
| <a id="dwc_footprintWKT"></a>**Term Name:** | **dwc:footprintWKT** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/footprintWKT |
| Label: | Footprint WKT |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A Well-Known Text (WKT) representation of the shape (footprint, geometry) that defines the Location. A Location may have both a point-radius representation (see decimalLatitude) and a footprint representation, and they may differ from each other. |
| | |
| <a id="dwc_geodeticDatum"></a>**Term Name:** | **dwc:geodeticDatum** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/geodeticDatum |
| Label: | Geodetic Datum |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The ellipsoid, geodetic datum, or spatial reference system (SRS) upon which the geographic coordinates given in decimalLatitude and decimalLongitude as based. Recommended best practice is use the EPSG code as a controlled vocabulary to provide an SRS, if known. Otherwise use a controlled vocabulary for the name or code of the geodetic datum, if known. Otherwise use a controlled vocabulary for the name or code of the ellipsoid, if known. If none of these is known, use the value "unknown". |
| | |
| <a id="dwc_georeferencedBy"></a>**Term Name:** | **dwc:georeferencedBy** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/georeferencedBy |
| Label: | Georeferenced By |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A list (concatenated and separated) of names of people, groups, or organizations who determined the georeference (spatial representation) for the Location. |
| | |
| <a id="dwc_georeferenceProtocol"></a>**Term Name:** | **dwc:georeferenceProtocol** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/georeferenceProtocol |
| Label: | Georeference Protocol |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A description or reference to the methods used to determine the spatial footprint, coordinates, and uncertainties. |
| | |
| <a id="dwc_georeferenceRemarks"></a>**Term Name:** | **dwc:georeferenceRemarks** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/georeferenceRemarks |
| Label: | Georeference Remarks |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Notes or comments about the spatial description determination, explaining assumptions made in addition or opposition to the those formalized in the method referred to in georeferenceProtocol. |
| | |
| <a id="dwc_georeferenceSources"></a>**Term Name:** | **dwc:georeferenceSources** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/georeferenceSources |
| Label: | Georeference Sources |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A list (concatenated and separated) of maps, gazetteers, or other resources used to georeference the Location, described specifically enough to allow anyone in the future to use the same resources. |
| | |
| <a id="dwc_georeferenceVerificationStatus"></a>**Term Name:** | **dwc:georeferenceVerificationStatus** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/georeferenceVerificationStatus |
| Label: | Georeference Verification Status |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A categorical description of the extent to which the georeference has been verified to represent the best possible spatial description. Recommended best practice is to use a controlled vocabulary. |
| | |
| <a id="dwc_higherGeography"></a>**Term Name:** | **dwc:higherGeography** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/higherGeography |
| Label: | Higher Geography |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A list (concatenated and separated) of geographic names less specific than the information captured in the locality term. |
| | |
| <a id="dwc_higherGeographyID"></a>**Term Name:** | **dwc:higherGeographyID** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/higherGeographyID |
| Label: | Higher Geography ID |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | An identifier for the geographic region within which the Location occurred. Recommended best practice is to use an persistent identifier from a controlled vocabulary such as the Getty Thesaurus of Geographic Names. |
| | |
| <a id="dwc_island"></a>**Term Name:** | **dwc:island** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/island |
| Label: | Island |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The name of the island on or near which the Location occurs. Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names. |
| | |
| <a id="dwc_islandGroup"></a>**Term Name:** | **dwc:islandGroup** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/islandGroup |
| Label: | Island Group |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The name of the island group in which the Location occurs. Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names. |
| | |
| <a id="dwc_locality"></a>**Term Name:** | **dwc:locality** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/locality |
| Label: | Locality |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The specific description of the place. Less specific geographic information can be provided in other geographic terms (higherGeography, continent, country, stateProvince, county, municipality, waterBody, island, islandGroup). This term may contain information modified from the original to correct perceived errors or standardize the description. |
| | |
| <a id="dwc_locationAccordingTo"></a>**Term Name:** | **dwc:locationAccordingTo** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/locationAccordingTo |
| Label: | Location According To |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Information about the source of this Location information. Could be a publication (gazetteer), institution, or team of individuals. |
| | |
| <a id="dwc_locationID"></a>**Term Name:** | **dwc:locationID** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/locationID |
| Label: | Location ID |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | An identifier for the set of location information (data associated with dcterms:Location). May be a global unique identifier or an identifier specific to the data set. |
| | |
| <a id="dwc_locationRemarks"></a>**Term Name:** | **dwc:locationRemarks** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/locationRemarks |
| Label: | Location Remarks |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Comments or notes about the Location. |
| | |
| <a id="Iptc4xmpExt_LocationShown"></a>**Term Name:** | **Iptc4xmpExt:LocationShown** |
| Normative URI: | http://iptc.org/std/Iptc4xmpExt/2008-02-29/LocationShown |
| Label: | Location Shown |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The location that is depicted the media content, irrespective of the location at which the resource has been created. |
| | |
| <a id="dwc_maximumDepthInMeters"></a>**Term Name:** | **dwc:maximumDepthInMeters** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/maximumDepthInMeters |
| Label: | Maximum Depth In Meters |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The greater depth of a range of depth below the local surface, in meters. |
| | |
| <a id="dwc_maximumDistanceAboveSurfaceInMeters"></a>**Term Name:** | **dwc:maximumDistanceAboveSurfaceInMeters** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/maximumDistanceAboveSurfaceInMeters |
| Label: | Maximum Distance Above Surface In Meters |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The greater distance in a range of distance from a reference surface in the vertical direction, in meters. Use positive values for locations above the surface, negative values for locations below. If depth measures are given, the reference surface is the location given by the depth, otherwise the reference surface is the location given by the elevation. |
| | |
| <a id="dwc_maximumElevationInMeters"></a>**Term Name:** | **dwc:maximumElevationInMeters** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/maximumElevationInMeters |
| Label: | Maximum Elevation In Meters |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The upper limit of the range of elevation (altitude, usually above sea level), in meters. |
| | |
| <a id="dwc_minimumDepthInMeters"></a>**Term Name:** | **dwc:minimumDepthInMeters** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/minimumDepthInMeters |
| Label: | Minimum Depth In Meters |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The lesser depth of a range of depth below the local surface, in meters. |
| | |
| <a id="dwc_minimumDistanceAboveSurfaceInMeters"></a>**Term Name:** | **dwc:minimumDistanceAboveSurfaceInMeters** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/minimumDistanceAboveSurfaceInMeters |
| Label: | Minimum Distance Above Surface In Meters |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The lesser distance in a range of distance from a reference surface in the vertical direction, in meters. Use positive values for locations above the surface, negative values for locations below. If depth measures are given, the reference surface is the location given by the depth, otherwise the reference surface is the location given by the elevation. |
| | |
| <a id="dwc_minimumElevationInMeters"></a>**Term Name:** | **dwc:minimumElevationInMeters** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/minimumElevationInMeters |
| Label: | Minimum Elevation In Meters |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The lower limit of the range of elevation (altitude, usually above sea level), in meters. |
| | |
| <a id="dwc_municipality"></a>**Term Name:** | **dwc:municipality** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/municipality |
| Label: | Municipality |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The full, unabbreviated name of the next smaller administrative region than county (city, municipality, etc.) in which the Location occurs. Do not use this term for a nearby named place that does not contain the actual location. |
| | |
| <a id="dwc_pointRadiusSpatialFit"></a>**Term Name:** | **dwc:pointRadiusSpatialFit** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/pointRadiusSpatialFit |
| Label: | Point Radius Spatial Fit |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The ratio of the area of the point-radius (decimalLatitude, decimalLongitude, coordinateUncertaintyInMeters) to the area of the true (original, or most specific) spatial representation of the Location. Legal values are 0, greater than or equal to 1, or undefined. A value of 1 is an exact match or 100% overlap. A value of 0 should be used if the given point-radius does not completely contain the original representation. The pointRadiusSpatialFit is undefined (and should be left blank) if the original representation is a point without uncertainty and the given georeference is not that same point (without uncertainty). If both the original and the given georeference are the same point, the pointRadiusSpatialFit is 1. |
| | |
| <a id="Iptc4xmpExt_ProvinceState"></a>**Term Name:** | **Iptc4xmpExt:ProvinceState** |
| Normative URI: | http://iptc.org/std/Iptc4xmpExt/2008-02-29/ProvinceState |
| Label: | Province or State |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Optionally, the geographic unit immediately below the country level (individual states in federal countries, provinces, or other administrative units) in which the subject of the media resource (e. g., species, habitats, or events) were located (if such information is available in separate fields). |
| | |
| <a id="dwc_stateProvince"></a>**Term Name:** | **dwc:stateProvince** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/stateProvince |
| Label: | State Province |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The name of the next smaller administrative region than country (state, province, canton, department, region, etc.) in which the Location occurs. |
| | |
| <a id="Iptc4xmpExt_Sublocation"></a>**Term Name:** | **Iptc4xmpExt:Sublocation** |
| Normative URI: | http://iptc.org/std/Iptc4xmpExt/2008-02-29/Sublocation |
| Label: | Sublocation |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Free-form text location details of the location of the subjects, down to the village, forest, or geographic feature etc., below the Iptc4xmpExt:City place name, especially information that could not be found in a gazetteer. |
| | |
| <a id="dwc_verbatimCoordinates"></a>**Term Name:** | **dwc:verbatimCoordinates** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/verbatimCoordinates |
| Label: | Verbatim Coordinates |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The verbatim original spatial coordinates of the Location. The coordinate ellipsoid, geodeticDatum, or full Spatial Reference System (SRS) for these coordinates should be stored in verbatimSRS and the coordinate system should be stored in verbatimCoordinateSystem. |
| | |
| <a id="dwc_verbatimCoordinateSystem"></a>**Term Name:** | **dwc:verbatimCoordinateSystem** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/verbatimCoordinateSystem |
| Label: | Verbatim Coordinate System |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The spatial coordinate system for the verbatimLatitude and verbatimLongitude or the verbatimCoordinates of the Location. Recommended best practice is to use a controlled vocabulary. |
| | |
| <a id="dwc_verbatimDepth"></a>**Term Name:** | **dwc:verbatimDepth** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/verbatimDepth |
| Label: | Verbatim Depth |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The original description of the depth below the local surface. |
| | |
| <a id="dwc_verbatimElevation"></a>**Term Name:** | **dwc:verbatimElevation** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/verbatimElevation |
| Label: | Verbatim Elevation |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The original description of the elevation (altitude, usually above sea level) of the Location. |
| | |
| <a id="dwc_verbatimLatitude"></a>**Term Name:** | **dwc:verbatimLatitude** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/verbatimLatitude |
| Label: | Verbatim Latitude |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The verbatim original latitude of the Location. The coordinate ellipsoid, geodeticDatum, or full Spatial Reference System (SRS) for these coordinates should be stored in verbatimSRS and the coordinate system should be stored in verbatimCoordinateSystem. |
| | |
| <a id="dwc_verbatimLocality"></a>**Term Name:** | **dwc:verbatimLocality** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/verbatimLocality |
| Label: | Verbatim Locality |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The original textual description of the place. |
| | |
| <a id="dwc_verbatimLongitude"></a>**Term Name:** | **dwc:verbatimLongitude** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/verbatimLongitude |
| Label: | Verbatim Longitude |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The verbatim original longitude of the Location. The coordinate ellipsoid, geodeticDatum, or full Spatial Reference System (SRS) for these coordinates should be stored in verbatimSRS and the coordinate system should be stored in verbatimCoordinateSystem. |
| | |
| <a id="dwc_verbatimSRS"></a>**Term Name:** | **dwc:verbatimSRS** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/verbatimSRS |
| Label: | Verbatim SRS |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The ellipsoid, geodetic datum, or spatial reference system (SRS) upon which coordinates given in verbatimLatitude and verbatimLongitude, or verbatimCoordinates are based. Recommended best practice is use the EPSG code as a controlled vocabulary to provide an SRS, if known. Otherwise use a controlled vocabulary for the name or code of the geodetic datum, if known. Otherwise use a controlled vocabulary for the name or code of the ellipsoid, if known. If none of these is known, use the value "unknown". |
| | |
| <a id="dwc_waterBody"></a>**Term Name:** | **dwc:waterBody** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/waterBody |
| Label: | Water Body |
| | **Layer:**  -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The name of the water body in which the Location occurs. Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names. |
| | |
| <a id="Iptc4xmpExt_WorldRegion"></a>**Term Name:** | **Iptc4xmpExt:WorldRegion** |
| Normative URI: | http://iptc.org/std/Iptc4xmpExt/2008-02-29/WorldRegion |
| Label: | World Region |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Name of a world region in some high level classification, such as names for continents, waterbodies, or island groups, whichever is most appropriate. The terms preferably are derived from a controlled vocabulary. |
| Notes: | The equivalent DarwinCore fields here forces primary metadata providers to classify world region terms into separate properties for "continent", "waterbody", "islandGroup". By contrast, the Iptc4xmpExt vocabulary only specifies that a World Region is something at the top of a hierarchy of locations. |
| | |

### 7.6 Temporal Coverage Vocabulary

| property | value |
|----------|-------|
| <a id="xmp_CreateDate"></a>**Term Name:** | **xmp:CreateDate** |
| Normative URI: | http://ns.adobe.com/xap/1.0/CreateDate |
| Label: | Original Date and Time |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | The date of the creation of the original resource from which the digital media was derived or created. The date and time must comply with the World Wide Web Consortium (W3C) datetime practice, which requires that date and time representation correspond to ISO 8601:1998, but with year fields always comprising 4 digits. This makes datetime records compliant with 8601:2004. AC datetime values may also follow 8601:2004 for ranges by separating two IS0 8601 datetime fields by a solidus ("forward slash", '/'). See also the wikipedia IS0 8601 entry for further explanation and examples. |
| Notes: | What constitutes "original" is determined by the metadata author. Example: Digitization of a photographic slide of a map would normally give the date at which the map was created; however a photographic work of art including the same map as its content may give the date of the original photographic exposure. Imprecise or unknown dates can be represented as ISO dates or ranges. Compare also Date and Time Digitized in the Resource Creation Vocabulary. See also the wikipedia IS0 8601 entry for further explanation and examples. |
| | |
| <a id="dcterms_temporal"></a>**Term Name:** | **dcterms:temporal** |
| Normative URI: | http://purl.org/dc/terms/temporal |
| Label: | Temporal Coverage |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | The coverage (extent or scope) of the content of the resource. Temporal coverage will typically include temporal period (a period label, date, or date range) to which the subjects of the media or media collection relate. If dates are mentioned, they should follow ISO 8601. When the resource is a Collection, this refers to the temporal coverage of the collection. Following dcterms:temporal, the value must be a URI. |
| Notes: | See the DCMI User Guide dcterms:temporal entry for an example. dc:coverage may be used for string values of temporal coverage, but use the Geography Vocabulary for geographic coverage. String examples for use with dc:coverage include "Jurassic", "Elizabethan", "Spring, 1957". 2008-01-01/2008-06-30. If the resource is video or audio, it refers to the time span, if any, depicted by the resource. For live-media this is closely related to Original Date and Time (Example: the time depicted by a time-lapse video file of organism development), but for media with fictional content it is not. |
| | |
| <a id="ac_timeOfDay"></a>**Term Name:** | **ac:timeOfDay** |
| Normative URI: | http://rs.tdwg.org/ac/terms/timeOfDay |
| Label: | Time of Day |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | Free text information beyond exact clock times. |
| Notes: | Examples in English: afternoon, twilight. |
| | |

### 7.7 Taxonomic Coverage Vocabulary

| property | value |
|----------|-------|
| <a id="dwc_dateIdentified"></a>**Term Name:** | **dwc:dateIdentified** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/dateIdentified |
| Label: | Date Identified |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | The date on which the person(s) given under Identfied By applied a Scientific Taxon Name to the resource. |
| | |
| <a id="dwc_identificationQualifier"></a>**Term Name:** | **dwc:identificationQualifier** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/identificationQualifier |
| Label: | Identification Qualifier |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A brief phrase or a standard abbreviation ("cf. genus", "cf. species", "cf. var.", "aff. species", etc.) to express the determiner's doubts with respect to a specified taxonomic rank about the identification given in Scientific Taxon Name. |
| Notes: | Splitting identification qualification and Scientific Taxon Name into separate fields is recommended practice in cases where only a single taxon name is available, or if the exchange format is able to keep relations between multiple names and identification qualifiers. Where the exchange format only supports simple multiplicities, a media item with multiple Scientific Taxon Names, some with, some without identification qualifiers, may have to be transferred with "cf." or "aff." qualifiers remaining embedded in the Scientific Taxon Name. For discussion of Darwin Core usage see here. Example: For the determinations "cf. Fusarium oxysporum f. sp. palmarum", "Fusarium cf. oxysporum f. sp. palmarum", "Fusarium oxysporum cf. f. sp. palmarum" the Scientific Taxon Name would always be "Fusarium oxysporum f. sp. palmarum", with Identification Qualifier "cf. genus", "cf. species" and "cf. f.sp.", respectively. In most cases only the lowest taxon is in doubt, but cases exist where good reasons exist to suspect a specific or even infraspecific determination, without having a save generic identification. |
| | |
| <a id="dwc_identifiedBy"></a>**Term Name:** | **dwc:identifiedBy** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/identifiedBy |
| Label: | Identified By |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The name(s) of the person(s) who applied the Scientific Taxon Name to the media item or the occurrence represented in the media item. |
| | |
| <a id="dwc_lifeStage"></a>**Term Name:** | **dwc:lifeStage** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/lifeStage |
| Label: | Subject Life Stage |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A description of the life-cycle stage of any organisms featured within the media, when relevant to the subject of the media, e. g., larvae, juvenile, adult. |
| | |
| <a id="dwc_nameAccordingTo"></a>**Term Name:** | **dwc:nameAccordingTo** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/nameAccordingTo |
| Label: | Name According To |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The taxonomic authority used to apply the name to the taxon, e. g., a person, book or web service. |
| Notes: | Examples are "Flora of North America", "Landrum 1981, Monograph of the Genus Myrceugenia (Myrtaceae)", "Peterson Field Guide to Birds of North America", or "Expert identification by J.Smith". The definition at dwc:nameAccordingTo is: 'The reference to the source in which the specific taxon concept circumscription is defined or implied - traditionally signified by the Latin "sensu" or "sec." (from secundum, meaning "according to"). For taxa that result from identifications, a reference to the keys, monographs, experts and other sources should be given.' |
| | |
| <a id="ac_otherScientificName"></a>**Term Name:** | **ac:otherScientificName** |
| Normative URI: | http://rs.tdwg.org/ac/terms/otherScientificName |
| Label: | Other Scientific Name |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | One or several Scientific Taxon Names that are synonyms to the Scientific Taxon Name may be provided here. |
| Notes: | The primary purpose of this is in support of resource discovery, not developing a taxonomic synonymy. Misidentification or misspellings may thus be of interest. Where multiple taxa are present in a resource and multiple Scientific Taxon Names are given, the association between synonyms and names may not be deducible from the AC record alone. |
| | |
| <a id="dwc_preparations"></a>**Term Name:** | **dwc:preparations** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/preparations |
| Label: | Subject Preparation Technique |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | Free form text describing the techniques used to prepare the subject of the media, prior to or while creating the media resource. |
| Notes: | Examples for such techniques are: Insect under CO2, cooled to immobility, preservation with ethanol or formaldehyde. See also Resource Creation Technique for technical aspects of digital media object creation. |
| | |
| <a id="dwc_scientificName"></a>**Term Name:** | **dwc:scientificName** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/scientificName |
| Label: | Scientific Taxon Name |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Scientific names of taxa represented in the media resource (with date and name authorship information if available) of the lowest level taxonomic rank that can be applied. |
| Notes: | The Scientific Taxon Name may possibly be of a higher rank, e.g., a genus or family name, if this is the most specific identification available. Where multiple taxa are the subject of the media item, multiple names may be given. If possible, add this information here even if the title or caption of the resource already contains scientific taxon names. Where the list of scientific taxon names is impractically large (e.g., media collections or identification tools), the number of taxa should be given in Taxon Count (see below). If possible, avoid repeating the Taxonomic Coverage here. Do not use abbreviated Genus names ("P. vulgaris"). It is recommended to provide author citation to scientific names, to avoid ambiguities in the presence of homonyms (the same name created by different authors for different taxa). Identifier qualifications should be supplied in the Identification Qualifier term rather than here (i. e. "Abies cf. alba" is deprecated, to be replaced with Scientific Taxon Name = "Abies alba" and Identification Qualifier = "cf. species"). |
| | |
| <a id="dwc_scientificNameID"></a>**Term Name:** | **dwc:scientificNameID** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/scientificNameID |
| Label: | Scientific Name ID |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | An identifier for the nomenclatural (not taxonomic) details of a scientific name. |
| Notes: | See dwc:scientificNameID and also the DwC Taxon attributes. |
| | |
| <a id="dwc_sex"></a>**Term Name:** | **dwc:sex** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/sex |
| Label: | Subject Sex |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A description of the sex of any organisms featured within the media, when relevant to the subject of the media, e. g., male, female, hermaphrodite, dioecious. |
| | |
| <a id="ac_subjectOrientation"></a>**Term Name:** | **ac:subjectOrientation** |
| Normative URI: | http://rs.tdwg.org/ac/terms/subjectOrientation |
| Label: | Subject Orientation |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Specific orientation (= direction, view angle) of the subject represented in the media resource with respect to the acquisition device. |
| Notes: | Examples: "dorsal", "ventral", "frontal", etc. No formal encoding scheme as yet exists. The term is repeatable e.g., in the case of a composite image, consisting of a combination of different view orientations. |
| | |
| <a id="ac_subjectPart"></a>**Term Name:** | **ac:subjectPart** |
| Normative URI: | http://rs.tdwg.org/ac/terms/subjectPart |
| Label: | Subject Part |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The portion or product of organism morphology, behaviour, environment, etc. that is either predominantly shown or particularly well exemplified by the media resource. |
| Notes: | No formal encoding scheme as yet exists. Examples are "whole body", "head", "flower", "leaf", "canopy" (of a rain forest stand). Several anatomical ontologies are emerging in http://www.obofoundry.org/ |
| | |
| <a id="ac_taxonCount"></a>**Term Name:** | **ac:taxonCount** |
| Normative URI: | http://rs.tdwg.org/ac/terms/taxonCount |
| Label: | Taxon Count |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | An exact or estimated number of taxa at the lowest applicable taxon rank (usually species or infraspecific) represented by the media resource (item or collection). |
| Notes: | Primarily intended for resource collections and singular resources dealing with sets of taxa (e. g., identification tools, videos). It is recommended to give an exact or estimated number of specific taxa when a complete list of taxa is not available or practical. The count should contain only the taxa covered fully or primarily by the resource. For a taxon page and most images this will be "1", i. e. other taxa mentioned on the side or in the background should not be counted. However, sometimes a resource may illustrate an ecological or behavioral entity with multiple species, e. g., a host-pathogen interaction; taxon count would then indicate the known number of species in this interaction. This should be a single integer number. Leave the field empty if you cannot estimate the information (do not enter 0). Additional taxon counts at higher levels (e. g. how many families are covered by a digital Fauna) should be given verbatim in the resource description, not here. |
| | |
| <a id="ac_taxonCoverage"></a>**Term Name:** | **ac:taxonCoverage** |
| Normative URI: | http://rs.tdwg.org/ac/terms/taxonCoverage |
| Label: | Taxon Coverage |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | A higher taxon (e. g., a genus, family, or order) at the level of the genus or higher, that covers all taxa that are the primary subject of the resource (which may be a media item or a collection). |
| Notes: | Example: Where the subject of an image is several species of ducks with trees visible in the background, Taxon Coverage would still be Anatidae (and not Biota). Example: "Aves" for a bird key or a bird image collection. Do not add a rank ("Class Aves") in this field. Note that this somewhat expands the usage of ncd:taxonCoverage which, however has not yet been adopted by TDWG, and which specifies at the Family level or higher. For collections it is recommended to follow ncd:taxonCoverage to avoid conflicts between an AC record and a record arising from use of the un-adopted NCD. If the resource contains a single taxon, this should be placed in Scientific Taxon Name. In this case Taxon Coverage may be left empty, but if not, care should be taken that the entries do not conflict. Example: If Scientific Taxon Name is Quercus alba then Taxon Coverage, if provided at all, should be Quercus. |
| | |
| <a id="dwc_vernacularName"></a>**Term Name:** | **dwc:vernacularName** |
| Normative URI: | http://rs.tdwg.org/dwc/terms/vernacularName |
| Label: | Common Name |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Common (= vernacular) names of the subject in one or several languages. The ISO language name should be given in parentheses after the name if not all names are given by values of the Metadata Language term. |
| Notes: | The ISO language code after the name should be formatted as in the following example: 'abete bianco (it); Tanne (de); White Fir (en)'. If names are known to be male- or female-specific, this may be specified as in: 'ewe (en-female); ram (en-male);'. |
| | |

### 7.8 Resource Creation Vocabulary

| property | value |
|----------|-------|
| <a id="ac_captureDevice"></a>**Term Name:** | **ac:captureDevice** |
| Normative URI: | http://rs.tdwg.org/ac/terms/captureDevice |
| Label: | Capture Device |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | Free form text describing the device or devices used to create the resource. |
| Notes: | It is best practice to record the device; this may include a combination such as camera plus lens, or camera plus microscope. Examples: "Canon Supershot 2000", "Makroscan Scanner 2000", "Zeiss Axioscope with Camera IIIu", "SEM (Scanning Electron Microscope)". |
| | |
| <a id="ac_digitizationDate"></a>**Term Name:** | **ac:digitizationDate** |
| Normative URI: | http://rs.tdwg.org/ac/terms/digitizationDate |
| Label: | Date and Time Digitized |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | Date the first digital version was created, if different from Original Date and Time found in the Temporal Coverage Vocabulary. The date and time must comply with the World Wide Web Consortium (W3C) datetime practice, which requires that date and time representation correspond to ISO 8601:1998, but with year fields always comprising 4 digits. This makes datetime records compliant with 8601:2004. AC datetime values may also follow 8601:2004 for ranges by separating two IS0 8601 datetime fields by a solidus ("forward slash", '/'). See also the wikipedia IS0 8601 entry for further explanation and examples. |
| Notes: | This is often not the media creation or modification date. For example, if photographic prints have been scanned, the date of that scanning is what this term carries, but Original Date and Time is that depicted in the print. Use the international (ISO/xml) format yyyy-mm-ddThh:mm (e. g. "2007-12-31" or "2007-12-31T14:59"). Where available, timezone information should be added. In the case of digital images containing EXIF, whereas the EXIF capture date does not contain time zone information, but EXIF GPSDateStamp and GPSTimeStamp may be relevant as these include time-zone information. Compare also MWG (2010)[9], which has best practice advice on handling time-zone-less EXIF date/time data. See also the wikipedia IS0 8601 entry for further explanation and examples. |
| | |
| <a id="Iptc4xmpExt_LocationCreated"></a>**Term Name:** | **Iptc4xmpExt:LocationCreated** |
| Normative URI: | http://iptc.org/std/Iptc4xmpExt/2008-02-29/LocationCreated |
| Label: | Location Created |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | The location at which the media recording instrument was placed when the media was created. |
| Notes: | The distinction between the location shown and created is often irrelevant, and metadata may be assumed to be referring to location shown. It is recommended that the Location Shown field above always be used when known. However, in the case of position data automatically recorded by the instrument (e. g. EXIF GPS data) Location Created should be used to maintain information accuracy. When one but not both of these locations are present, AC is silent about whether the provided one entails the other. A best practices document for a particular AC implementation might address this. |
| | |
| <a id="ac_resourceCreationTechnique"></a>**Term Name:** | **ac:resourceCreationTechnique** |
| Normative URI: | http://rs.tdwg.org/ac/terms/resourceCreationTechnique |
| Label: | Resource Creation Technique |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | Information about technical aspects of the creation and digitization process of the resource. This includes modification steps ("retouching") after the initial resource capture. |
| Notes: | Examples: Encoding method or settings, numbers of channels, lighting, audio sampling rate, frames per second, data rate, interlaced or progressive, multiflash lighting, remote control, automatic interval exposure.  Annotating whether and how a resource has been modified or edited significantly in ways that are not immediately obvious to, or expected by, consumers is of special significance. Examples for images are: Removing a distracting twig from a picture, moving an object to a different surrounding, changing the color in parts of the image, or blurring the background of an image. Modifications that are standard practice and expected or obvious are not necessary to document; examples of such practices include changing resolution, cropping, minor sharpening or overall color correction, and clearly perceptible modifications (e.g., addition of arrows or labels, or the placement of multiple pictures into a table.) If it is only known that significant modifications were made, but no details are known, a general statement like "Media may have been manipulated to improve appearance" may be appropriate. See also Subject Preparation Technique. |
| | |

### 7.9 Related Resources Vocabulary

| property | value |
|----------|-------|
| <a id="ac_associatedObservationReference"></a>**Term Name:** | **ac:associatedObservationReference** |
| Normative URI: | http://rs.tdwg.org/ac/terms/associatedObservationReference |
| Label: | Associated Observation Reference |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A reference to an observation associated with this resource. |
| | |
| <a id="ac_associatedSpecimenReference"></a>**Term Name:** | **ac:associatedSpecimenReference** |
| Normative URI: | http://rs.tdwg.org/ac/terms/associatedSpecimenReference |
| Label: | Associated Specimen Reference |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A reference to a specimen associated with this resource. |
| Notes: | Supports finding a specimen resource, where additional information is available. If several resources relate to the same specimen, these are implicitly related. Examples: for NHM "BM 23974324" for a barcoded or "BM Smith 32" for a non-barcoded specimen; for UNITS: "TSB 28637"; for PMSL: "PMSL-Lepidoptera-2534781". Ideally this may be a URI identifying a specimen record that is available online. |
| | |
| <a id="ac_derivedFrom"></a>**Term Name:** | **ac:derivedFrom** |
| Normative URI: | http://rs.tdwg.org/ac/terms/derivedFrom |
| Label: | Derived From |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A reference to an original resource from which the current one is derived. |
| Notes: | Derivation of one resource from another is of special interest for identification tools (e. g. a key from an unpublished data set, as in FRIDA, or a PDA key from a PC or web key) or web services (e. g. a name synonymization service being derived from a specific data set). It may very rarely also be known where one image or sound recording is derived from another (but compare the separate mechanism to be used for quality/resolution levels). Human readable, or doi number, or URL. Simple name of parent for human readable. Can be repeated if a montage of images. |
| | |
| <a id="ac_IDofContainingCollection"></a>**Term Name:** | **ac:IDofContainingCollection** |
| Normative URI: | http://rs.tdwg.org/ac/terms/IDofContainingCollection |
| Label: | ID of Containing Collection |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | If the resource is contained in a Collection, this field identifies that Collection uniquely. Its form is not specified by this normative document, but is left to implementers of specific implementations. |
| Notes: | Repeatable: A media resource may be member of multiple collections |
| | |
| <a id="ac_providerID"></a>**Term Name:** | **ac:providerID** |
| Normative URI: | http://rs.tdwg.org/ac/terms/providerID |
| Label: | Provider ID |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | A globally unique ID of the provider of the current AC metadata record. |
| Notes: | Only to be used if the annotated resource is not a provider itself - this item is for relating the resource to a provider, using an arbitrary code that is unique for a provider, contributing partner, or aggregator, or other roles (potentially defined by MARC, OAI) and by which the media resources are linked to the provider. |
| | |
| <a id="ac_relatedResourceID"></a>**Term Name:** | **ac:relatedResourceID** |
| Normative URI: | http://rs.tdwg.org/ac/terms/relatedResourceID |
| Label: | Related Resource ID |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Resource related in ways not specified through a collection, e.g., before-after images; time-lapse series; different orientations/angles of view |
| Notes: | The value references a related media item. Examples of relations are: Images taken in a sequence or defined time series, an exposure or focus series (e.g. for stacking), different framing or views (top, side, bottom) of the same subject, or an overview plus several details. The property makes such related media items discoverable, but does not indicate the nature of this relationship. More specific properties may be defined in a later version of AC. |
| | |

### 7.10 Service Access Point Vocabulary

These terms are representation-dependent metadata, referring to specific digital representations of a resource (e.g., a specific resolution, quality, or format). They are used within whatever a particular AC implementation assigns to the value of hasServiceAccessPoint, whose label is simply "Service Access Point." Note that it is possible for an implementation to use syntactic conventions that avoid direct use of hasServiceAccessPoint, as illustrated in the final example in the section [Multiplicity/Cardinality in the Audubon Core Structure document](structure.md#3-multiplicity-and-cardinality).

| property | value |
|----------|-------|
| <a id="ac_accessURI"></a>**Term Name:** | **ac:accessURI** |
| Normative URI: | http://rs.tdwg.org/ac/terms/accessURI |
| Label: | Access URI |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | A URI that uniquely identifies a service that provides a representation of the underlying resource. If this resource can be acquired by an http request, its http URL should be given. If not, but it has some URI in another URI scheme, that may be given here. |
| Notes: | Value might point to something offline, such as a published CD, etc. For example, the doi of an published CD would be a suitable value. |
| | |
| <a id="dc_format"></a>**Term Name:** | **dc:format** |
| Normative URI: | http://purl.org/dc/elements/1.1/format |
| Label: | Format |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | A string describing the technical format of the resource (file format or physical medium). |
| Notes: | Recommended best practice is to use a controlled vocabulary such as the list of Internet Media Types [MIME]. This term is recommended for offline digital content. In cases where the provided URL includes a standard file extension from which the format can be inferred, it is permissible to not provide this item. Three types of values are recommended: (a) any MIME type; (b) common file extensions like txt, doc, odf, jpg/jpeg, png, pdf; (c) the following special values: Data-CD, Audio-CD, Video-CD, Data-DVD, Audio-DVD, Video-DVD-PAL, Video-DVD-NTSC, photographic slide, photographic print. Compare Type for the content-type. See also the entry for dcterms:format in this document and see the DCMI FAQ on DC and DCTERMS Namespaces for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| <a id="dcterms_format"></a>**Term Name:** | **dcterms:format** |
| Normative URI: | http://purl.org/dc/terms/format |
| Label: | Format |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | URI referencing the technical format of the resource (file format or physical medium). |
| Notes: | See DCMI User_Guide for examples. See also the entry for dc:format in this document and see the DCMI FAQ on DC and DCTERMS Namespaces for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. |
| | |
| <a id="ac_furtherInformationURL"></a>**Term Name:** | **ac:furtherInformationURL** |
| Normative URI: | http://rs.tdwg.org/ac/terms/furtherInformationURL |
| Label: | Further Information URL |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | The URL of a Web site that provides additional information about the version of the media resource that is provided by the Service Access Point. |
| | |
| <a id="ac_hashFunction"></a>**Term Name:** | **ac:hashFunction** |
| Normative URI: | http://rs.tdwg.org/ac/terms/hashFunction |
| Label: | Hash Function |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | The cryptographic hash function used to compute the value given in the Hash Value. |
| Notes: | Recommended values include MD5, SHA-1, SHA-224,SHA-256, SHA-384, SHA-512, SHA-512/224 and SHA-512/256 |
| | |
| <a id="ac_hashValue"></a>**Term Name:** | **ac:hashValue** |
| Normative URI: | http://rs.tdwg.org/ac/terms/hashValue |
| Label: | Hash |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | The value computed by a hash function applied to the media that will be delivered at the access point. |
| Notes: | Best practice is to also specify the hash function by supplying a value of the Hash Function term, using one of the standard literals from the Notes there. |
| | |
| <a id="ac_licensingException"></a>**Term Name:** | **ac:licensingException** |
| Normative URI: | http://rs.tdwg.org/ac/terms/licensingException |
| Label: | Licensing Exception Statement |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | The licensing statement for this variant of the media resource if different from that given in the License Statement property of the resource. |
| Notes: | Required only if this version has different licensing than that of the media resource. For example, the highest resolution version may be more restricted than lower resolution versions. |
| | |
| <a id="exif_PixelXDimension"></a>**Term Name:** | **exif:PixelXDimension** |
| Normative URI: | http://ns.adobe.com/exif/1.0/PixelXDimension |
| Label: | Image Width |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | The width in pixels of the media specified by the access point. |
| | |
| <a id="exif_PixelYDimension"></a>**Term Name:** | **exif:PixelYDimension** |
| Normative URI: | http://ns.adobe.com/exif/1.0/PixelYDimension |
| Label: | Image Height |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** No |
| Definition: | The height in pixels of the media specified by the access point. |
| | |
| <a id="ac_serviceExpectation"></a>**Term Name:** | **ac:serviceExpectation** |
| Normative URI: | http://rs.tdwg.org/ac/terms/serviceExpectation |
| Label: | Service Expectation |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | A term that describes what service expectations users may have of the ac:accessURL. Recommended terms include online (denotes that the URL is expected to deliver the resource), authenticate (denotes that the URL delivers a login or other authentication interface requiring completion before delivery of the resource) published(non digital) (denotes that the URL is the identifier of a non-digital published work, for example a doi.) Communities should develop their own controlled vocabularies for Service Expectations. |
| | |
| <a id="ac_variant"></a>**Term Name:** | **ac:variant** |
| Normative URI: | http://rs.tdwg.org/ac/terms/variant |
| Label: | Variant |
| | **Layer:** 1 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | A URI designating what this Service Access Point provides. Some suggested values are the URIs ac:Thumbnail, ac:Trailer, ac:LowerQuality, ac:MediumQuality, ac:GoodQuality, ac:BestQuality, and ac:Offline. Additional URIs from communities of practice may be introduced. |
| Notes: | A URI designating what this Service Access Point provides. Some suggested values are the URIs ac:Thumbnail, ac:Trailer, ac:LowerQuality, ac:MediumQuality, ac:GoodQuality, ac:BestQuality, and ac:Offline. Additional URIs from communities of practice may be introduced. |
| | |
| <a id="ac_variantDescription"></a>**Term Name:** | **ac:variantDescription** |
| Normative URI: | http://rs.tdwg.org/ac/terms/variantDescription |
| Label: | Variant Description |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** No |
| Definition: | Text that describes this Service Access Point variant |
| Notes: | Most variants (thumb, low-res, high-res) are self-explanatory and it is best practice to leave this property empty if no special description is needed. It is provided for cases that require additional information (e.g., video shortened instead of simply quality reduced). |
| | |
| <a id="ac_variantLiteral"></a>**Term Name:** | **ac:variantLiteral** |
| Normative URI: | http://rs.tdwg.org/ac/terms/variantLiteral |
| Label: | Variant |
| | **Layer:** 2 -- **Required:** No -- **Repeatable:** Yes |
| Definition: | Text that describes this Service Access Point variant. |
| Notes: | This is an alternative to ac:variant where using a string is preferred over a URI. It is best practice to use ac:variant instead of ac:variantLiteral wherever practical. Value may be free text, but it is suggested to consider including terminology based on the following: Thumbnail: Service Access Point provides a thumbnail image, short sound clip, or short movie clip that can be used in addition to the resource to represent the media object, typically at lower quality and higher compression than a preview object. A typical size for a tiny thumbnail image may be 50-100 pixels in the longer dimension. Trailer: Service Access Point provides video clip preview, in the form of a specifically authored "Trailer", which may provide somewhat different content than the original resource. Lower Quality: Service Access Point provides a lower quality version of the media resource, suitable e. g. for web sites. Medium Quality: Service Access Point provides a medium quality version of the media resource, e. g. shortened in duration, or reduced size, using lower resolution or higher compression causing moderate artifacts. Good Quality: Service Access Point provides a good quality version of the media resource intended for resources displayed as primary information; e. g. an image between 800 and 1600 px in width or height. Best Quality: Service Access Point provides the highest available quality of the media resource, whatever its resolution or quality level. Offline: Service Access Point provides data about an offline resource. |
| | |


-----------------
This document is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). ![http://creativecommons.org/licenses/by/4.0/](https://licensebuttons.net/l/by/4.0/88x31.png).

Copyright 2013 - Biodiversity Information Standards - TDWG - [Contact Us](http://www.tdwg.org/about-tdwg/contact-us/)
