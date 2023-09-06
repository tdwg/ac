# Audiovisual Core Term List

Title
: Audiovisual Core Term List

Date version issued
: 2023-09-05

Date created
: 2013-10-23

Part of TDWG Standard
: <http://www.tdwg.org/standards/638>

This version
: <http://rs.tdwg.org/ac/doc/termlist/2023-09-05>

Latest version
: <http://rs.tdwg.org/ac/doc/termlist/>

Previous version
: <http://rs.tdwg.org/ac/doc/termlist/2023-02-24>

Abstract
: The Audiovisual Core is a set of vocabularies designed to represent metadata for biodiversity multimedia resources and collections. It aims to represent information that will help to determine whether a particular resource or collection will be fit for some particular biodiversity science application before acquiring the media. Among others, the vocabularies address such concerns as the management of the media and collections, descriptions of their content, their taxonomic, geographic, and temporal coverage, and the appropriate ways to retrieve, attribute and reproduce them. This document contains a list of attributes of each Audiovisual Core term, including a documentation name, a specified URI, a recommended English label for user interfaces, a definition, and some ancillary notes. This document contains normative content that may not be changed without due process.

Contributors
: [Robert A. Morris](https://orcid.org/0000-0002-6992-9446) ([University of Massachusetts at Boston, USA](http://www.wikidata.org/entity/Q15144)), [Gregor Hagedorn](https://orcid.org/0000-0001-7023-7386) ([JKI, Federal Research Institute for Cultivated Plants, Berlin, Germany](http://www.wikidata.org/entity/Q832099)), [Annette Olson](https://orcid.org/0000-0002-0772-0022) ([American Association for the Advancement of Science](http://www.wikidata.org/entity/Q40358)), [Steve Baskauf](https://orcid.org/0000-0003-4365-3135) ([Vanderbilt University, Nashville, TN, USA](http://www.wikidata.org/entity/Q29052)), [Vijay Barve](https://orcid.org/0000-0002-4852-2567), [Mihail Carausu](https://orcid.org/0000-0002-8234-0599) ([Danish Biodiversity Information Facility (DanBIF), Copenhagen, Denmark](http://www.wikidata.org/entity/Q1531570)), [Vishwas Chavan](https://orcid.org/0000-0002-3425-6499) ([Global Biodiversity Information Facility, Copenhagen, Denmark](http://www.wikidata.org/entity/Q1531570)), [José Cuadra](http://www.wikidata.org/entity/Q51883873), [Chris Freeland](https://orcid.org/0000-0002-2541-5822) ([Missouri Botanical Garden, St. Louis, USA](http://www.wikidata.org/entity/Q1852803)), [Patrick Leary](https://orcid.org/0000-0001-5172-8577), [Dimitry Mozzherin](https://orcid.org/0000-0003-1593-1417) ([Encyclopedia of Life, Woods Hole, USA](http://www.wikidata.org/entity/Q82486)), [Greg Riccardi](https://orcid.org/0000-0002-3850-9983) ([Florida State University, Tallahassee, USA](http://www.wikidata.org/entity/Q861548)), [Ivan Teage](https://orcid.org/0000-0003-4176-2274), [Dan Stowell](https://orcid.org/0000-0001-8068-3769) ([Queen Mary University of London](http://www.wikidata.org/entity/Q195668)), [Edward Baker](https://orcid.org/0000-0002-5887-9543) ([Natural History Museum, London](http://www.wikidata.org/entity/Q309388)), [Richard Pyle](https://orcid.org/0000-0003-0768-1286) ([Bernice P. Bishop Museum, Honolulu, HI, USA](http://www.wikidata.org/entity/Q826520)), [Steve Baskauf](https://orcid.org/0000-0003-4365-3135) ([Vanderbilt University, Nashville, TN, USA](http://www.wikidata.org/entity/Q29052), review manager)

Creator
: GBIF/TDWG Multimedia Resources Task Group and Audiovisual Core Maintenance Group

Bibliographic citation
: GBIF/TDWG Multimedia Resources Task Group and Audiovisual Core Maintenance Group. 2023. Audiovisual Core Term List. Biodiversity Information Standards (TDWG). <http://rs.tdwg.org/ac/doc/termlist/2023-09-05>

## 1 Introduction

There are a number of documents included in the Aububon Core Standard.  This document provides details about the terms included in the 2023-09-05 version of the Audiovisual Core vocabulary. The [Audiovisual Core Introduction](introduction.md) document provides a brief introduction to the Audiovisual Core Standard. For information about the structure of Audiovisual Core, see the [Audiovisual Core Structure](structure.md) document.  For a more detailed guide to the use of Audiovisual Core, see the [Audiovisual Core Guide](guide.md) document.


### 1.1 Status of the content of this document

Sections 1.3 through 5 are normative, except for Table 1.  In Section 7 and its subparts, the values of the Normative URI, Definition, Required, and Repeatable are normative. The value of Usage (if it exists for a given term) is normative in that it specifies how a borrowed term should be used as part of Audiovisual Core.  The values of Term Name is non-normative, although one can expect that the namespace abbreviation prefix is one commonly used for the term namespace.  Labels and the values of all other properties (such as notes) are non-normative.

### 1.2 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) and [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) when, and only when, they appear in all capitals, as shown here.

### 1.3 Categories of terms

An Audiovisual Core (AC) record is a description of a multimedia resource
using the AC vocabularies. Three kinds of terms are specified by this
document: those terms which describe representation-independent aspects
of the media, those which describe representation-dependent aspects, and those that designate specified parts of the media item.
Most terms are representation-independent, referring to an "abstract
multimedia resource". One such term, `ac:hasServiceAccessPoint`, refers to
or contains representation-dependent service access point metadata
describing a digital representation of the abstract multimedia resource (an instance of the `ac:ServiceAccessPoint` class).
These metadata describe such things as a web address at which a digital
representation can be retrieved, and the format, extent, or licenses
that describe a particular such representation. A multimedia resource
may provide several access points for different representations (e.g.,
different resolutions). The resource may also be linked to one or more Regions of Interest (ROI) that define parts within the media item (instances of the `ac:RegionOfInterest` class).


## 2 Borrowed Vocabulary

When terms are borrowed from other vocabularies, AC uses the URIs,
common abbreviations, and namespace prefixes in use in those
vocabularies. The URIs are normative, but abbreviations and namespace
prefixes have no impact except as an aid to reading the documentation.

Table 1. Vocabularies from which terms have been borrowed (non-normative)

Note: URIs for terms in most of these namespaces do not dereference to anything.  The authoritative documentation can be obtained by clicking on the vocabulary names in the table.

| Vocabulary | Abbreviation | Namespaces and abbreviations |
|------------|--------------|------------------------------|
| [Darwin Core](https://dwc.tdwg.org/terms/) | DwC         | `dwc: = http://rs.tdwg.org/dwc/terms/`
| [Dublin Core](http://dublincore.org/documents/dcmi-terms/) | DC          | `dc: = http://purl.org/dc/elements/1.1/, dcterms: = http://purl.org/dc/terms/` |
| [Adobe XMP Core Properties](https://wwwimages2.adobe.com/content/dam/acom/en/devnet/xmp/pdfs/XMP%20SDK%20Release%20cc-2016-08/XMPSpecificationPart1.pdf) | XMP | `xmp: = http://ns.adobe.com/xap/1.0/, xmpRights: = http://ns.adobe.com/xap/1.0/rights/` |
| [Adobe XMP Additional Properties](http://wwwimages.adobe.com/www.adobe.com/content/dam/acom/en/devnet/xmp/pdfs/XMP%20SDK%20Release%20cc-2014-12/XMPSpecificationPart2.pdf) | XMP | `photoshop: = http://ns.adobe.com/photoshop/1.0/` |
| [International Press and Telecommunications Council Photo Metadata Standard,Extension Schema 1.1](http://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-201007_1.pdf) | IPTC | `Iptc4xmpExt: = http://iptc.org/std/Iptc4xmpExt/2008-02-29/` |
| [Camera and Imaging Products Association Exchangeable Image File Format](http://www.cipa.jp/std/documents/e/DC-008-2012_E.pdf) | EXIF | `exif: = http://ns.adobe.com/exif/1.0/` |
| [Music Ontology](http://musicontology.com/specification/) | MO | `mo: = http://purl.org/ontology/mo/` |
| [TDWG Natural Collection Description LSID Ontology](https://github.com/tdwg/ontology/blob/master/ontology/voc/Collection.rdf) (referenced in metadata, but no terms borrowed) | NCD | `ncd: = http://rs.tdwg.org/ontology/voc/Collection#` |


## 3 Namespaces, Prefixes and Term Names

The namespace of terms borrowed from other vocabularies is that of the
original. The namespace of de novo AC terms is
`http://rs.tdwg.org/ac/terms/`. In the table of terms, each term entry has
a row with the term name. This term name is generally an "unqualified
name" preceded by a widely accepted prefix designating an abbreviation
for the namespace It is RECOMMENDED that implementers who need a
namespace prefix for the AC namespace use `ac`. In this web document,
hovering over a term in the [Index By Term Name](#index-by-term-name)
list below will reveal a complete URL that can be used in other web
documents to link to *this* document's treatment of that term, even if
it is from a borrowed vocabulary. It is very important to note that some
vocabularies, e.g those of the
[Dublin Core Metadata Initiative (DCMI)](http://dublincore.org/),
provide versions of the same term in two different namespaces, one
providing for string values and one providing for URIs, even where that
separation is simply a recommendation, not a mandate. See this
[DCMI wiki entry](https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md)
on this topic. For vocabularies where such a practice is in place, we
often follow it and signal a reference in the Notes of our term
descriptions to the sister version of the term. An example is the pair
[dc:type](#dc_type) and [dcterms:type](#dcterms_type). When such a pair allows repeated instances (e.g. as for [dc:source](#dc_source) and [dcterms:source](#dcterms_source)), particular care may be required in some
implementations of AC, because
some implementations may not provide enough structure to clearly state
the association between the members of a pair in the case of multiple
values of each. This is a special case of the issue treated in the
normative material on [Multiplicity and Cardinality](structure.md#3-multiplicity-and-cardinality) in the Audiovisual Core Structure document.


## 4 Layers

(The Audiovisual Core layer property has been deprecated as of 2020-01-27)


## 5 Literal- vs. URI-valued Terms

Some terms have two versions, one expecting a string literal value and
the other a URI. In these circumstances, the version expecting a string
is named with the suffix "Literal", e.g. `ac:metadataLanguageLiteral`. In
such cases, both forms MAY be provided, but care should be taken to
ensure that the uses reflect the same intent. In case of ambiguity, the
URI version prevails. All terms, including those whether or not with a
specific "Literal" suffix, specify in their definition whether the
required values are strings or URIs.



## 6 Vocabulary Indices (non-normative)
### 6.1 Index By Term Name

(See also [6.2 Index By Label](#62-index-by-label))

**Management Vocabulary**

[dcterms:available](#dcterms_available) |
[ac:commenter](#ac_commenter) |
[ac:commenterLiteral](#ac_commenterLiteral) |
[ac:comments](#ac_comments) |
[ac:hasServiceAccessPoint](#ac_hasServiceAccessPoint) |
[dcterms:identifier](#dcterms_identifier) |
[xmp:MetadataDate](#xmp_MetadataDate) |
[ac:metadataLanguage](#ac_metadataLanguage) |
[ac:metadataLanguageLiteral](#ac_metadataLanguageLiteral) |
[dcterms:modified](#dcterms_modified) |
[ac:providerManagedID](#ac_providerManagedID) |
[xmp:Rating](#xmp_Rating) |
[ac:reviewer](#ac_reviewer) |
[ac:reviewerComments](#ac_reviewerComments) |
[ac:reviewerLiteral](#ac_reviewerLiteral) |
[ac:subtype](#ac_subtype) |
[ac:subtypeLiteral](#ac_subtypeLiteral) |
[dcterms:title](#dcterms_title) |
[dc:type](#dc_type) |
[dcterms:type](#dcterms_type)

**Attribution Vocabulary**

[ac:attributionLinkURL](#ac_attributionLinkURL) |
[ac:attributionLogoURL](#ac_attributionLogoURL) |
[photoshop:Credit](#photoshop_Credit) |
[ac:fundingAttribution](#ac_fundingAttribution) |
[ac:licenseLogoURL](#ac_licenseLogoURL) |
[xmpRights:Owner](#xmpRights_Owner) |
[dc:rights](#dc_rights) |
[dcterms:rights](#dcterms_rights) |
[dc:source](#dc_source) |
[dcterms:source](#dcterms_source) |
[xmpRights:UsageTerms](#xmpRights_UsageTerms) |
[xmpRights:WebStatement](#xmpRights_WebStatement)

**Agents Vocabulary**

[dc:creator](#dc_creator) |
[dcterms:creator](#dcterms_creator) |
[ac:metadataCreator](#ac_metadataCreator) |
[ac:metadataCreatorLiteral](#ac_metadataCreatorLiteral) |
[ac:metadataProvider](#ac_metadataProvider) |
[ac:metadataProviderLiteral](#ac_metadataProviderLiteral) |
[ac:provider](#ac_provider) |
[ac:providerLiteral](#ac_providerLiteral)

**Content Coverage Vocabulary**

[ac:caption](#ac_caption) |
[Iptc4xmpExt:CVterm](#Iptc4xmpExt_CVterm) |
[dcterms:description](#dcterms_description) |
[ac:freqHigh](#ac_freqHigh) |
[ac:freqLow](#ac_freqLow) |
[dc:language](#dc_language) |
[dcterms:language](#dcterms_language) |
[ac:physicalSetting](#ac_physicalSetting) |
[ac:subjectCategoryVocabulary](#ac_subjectCategoryVocabulary) |
[ac:tag](#ac_tag)

**Geography Vocabulary**

[Iptc4xmpExt:City](#Iptc4xmpExt_City) |
[dwc:continent](#dwc_continent) |
[dwc:coordinatePrecision](#dwc_coordinatePrecision) |
[dwc:coordinateUncertaintyInMeters](#dwc_coordinateUncertaintyInMeters) |
[dwc:country](#dwc_country) |
[Iptc4xmpExt:CountryCode](#Iptc4xmpExt_CountryCode) |
[dwc:countryCode](#dwc_countryCode) |
[Iptc4xmpExt:CountryName](#Iptc4xmpExt_CountryName) |
[dwc:county](#dwc_county) |
[dwc:decimalLatitude](#dwc_decimalLatitude) |
[dwc:decimalLongitude](#dwc_decimalLongitude) |
[dwc:footprintSpatialFit](#dwc_footprintSpatialFit) |
[dwc:footprintSRS](#dwc_footprintSRS) |
[dwc:footprintWKT](#dwc_footprintWKT) |
[dwc:geodeticDatum](#dwc_geodeticDatum) |
[dwc:georeferencedBy](#dwc_georeferencedBy) |
[dwc:georeferenceProtocol](#dwc_georeferenceProtocol) |
[dwc:georeferenceRemarks](#dwc_georeferenceRemarks) |
[dwc:georeferenceSources](#dwc_georeferenceSources) |
[dwc:georeferenceVerificationStatus](#dwc_georeferenceVerificationStatus) |
[dwc:higherGeography](#dwc_higherGeography) |
[dwc:higherGeographyID](#dwc_higherGeographyID) |
[dwc:island](#dwc_island) |
[dwc:islandGroup](#dwc_islandGroup) |
[dwc:locality](#dwc_locality) |
[dwc:locationAccordingTo](#dwc_locationAccordingTo) |
[dwc:locationID](#dwc_locationID) |
[dwc:locationRemarks](#dwc_locationRemarks) |
[Iptc4xmpExt:LocationShown](#Iptc4xmpExt_LocationShown) |
[dwc:maximumDepthInMeters](#dwc_maximumDepthInMeters) |
[dwc:maximumDistanceAboveSurfaceInMeters](#dwc_maximumDistanceAboveSurfaceInMeters) |
[dwc:maximumElevationInMeters](#dwc_maximumElevationInMeters) |
[dwc:minimumDepthInMeters](#dwc_minimumDepthInMeters) |
[dwc:minimumDistanceAboveSurfaceInMeters](#dwc_minimumDistanceAboveSurfaceInMeters) |
[dwc:minimumElevationInMeters](#dwc_minimumElevationInMeters) |
[dwc:municipality](#dwc_municipality) |
[dwc:pointRadiusSpatialFit](#dwc_pointRadiusSpatialFit) |
[Iptc4xmpExt:ProvinceState](#Iptc4xmpExt_ProvinceState) |
[dwc:stateProvince](#dwc_stateProvince) |
[Iptc4xmpExt:Sublocation](#Iptc4xmpExt_Sublocation) |
[dwc:verbatimCoordinates](#dwc_verbatimCoordinates) |
[dwc:verbatimCoordinateSystem](#dwc_verbatimCoordinateSystem) |
[dwc:verbatimDepth](#dwc_verbatimDepth) |
[dwc:verbatimElevation](#dwc_verbatimElevation) |
[dwc:verbatimLatitude](#dwc_verbatimLatitude) |
[dwc:verbatimLocality](#dwc_verbatimLocality) |
[dwc:verbatimLongitude](#dwc_verbatimLongitude) |
[dwc:verbatimSRS](#dwc_verbatimSRS) |
[dwc:waterBody](#dwc_waterBody) |
[Iptc4xmpExt:WorldRegion](#Iptc4xmpExt_WorldRegion)

**Temporal Coverage Vocabulary**

[xmp:CreateDate](#xmp_CreateDate) |
[dcterms:temporal](#dcterms_temporal) |
[ac:timeOfDay](#ac_timeOfDay)

**Taxonomic Coverage Vocabulary**

[dwc:dateIdentified](#dwc_dateIdentified) |
[dwc:identificationQualifier](#dwc_identificationQualifier) |
[dwc:identifiedBy](#dwc_identifiedBy) |
[dwc:lifeStage](#dwc_lifeStage) |
[dwc:nameAccordingTo](#dwc_nameAccordingTo) |
[ac:otherScientificName](#ac_otherScientificName) |
[dwc:preparations](#dwc_preparations) |
[dwc:scientificName](#dwc_scientificName) |
[dwc:scientificNameID](#dwc_scientificNameID) |
[dwc:sex](#dwc_sex) |
[ac:subjectOrientation](#ac_subjectOrientation) |
[ac:subjectOrientationLiteral](#ac_subjectOrientationLiteral) |
[ac:subjectPart](#ac_subjectPart) |
[ac:subjectPartLiteral](#ac_subjectPartLiteral) |
[ac:taxonCount](#ac_taxonCount) |
[ac:taxonCoverage](#ac_taxonCoverage) |
[dwc:vernacularName](#dwc_vernacularName)

**Resource Creation Vocabulary**

[ac:captureDevice](#ac_captureDevice) |
[ac:digitizationDate](#ac_digitizationDate) |
[ac:frameRate](#ac_frameRate) |
[Iptc4xmpExt:LocationCreated](#Iptc4xmpExt_LocationCreated) |
[ac:resourceCreationTechnique](#ac_resourceCreationTechnique) |
[mo:sample_rate](#mo_sample_rate)

**Related Resources Vocabulary**

[ac:associatedObservationReference](#ac_associatedObservationReference) |
[ac:associatedSpecimenReference](#ac_associatedSpecimenReference) |
[ac:derivedFrom](#ac_derivedFrom) |
[ac:IDofContainingCollection](#ac_IDofContainingCollection) |
[ac:providerID](#ac_providerID) |
[ac:relatedResourceID](#ac_relatedResourceID)

**Service Access Point Vocabulary**

[ac:accessURI](#ac_accessURI) |
[dc:format](#dc_format) |
[dcterms:format](#dcterms_format) |
[ac:furtherInformationURL](#ac_furtherInformationURL) |
[ac:hashFunction](#ac_hashFunction) |
[ac:hashValue](#ac_hashValue) |
[ac:licensingException](#ac_licensingException) |
[exif:PixelXDimension](#exif_PixelXDimension) |
[exif:PixelYDimension](#exif_PixelYDimension) |
[ac:ServiceAccessPoint](#ac_ServiceAccessPoint) |
[ac:serviceExpectation](#ac_serviceExpectation) |
[ac:variant](#ac_variant) |
[ac:variantDescription](#ac_variantDescription) |
[ac:variantLiteral](#ac_variantLiteral)

**Region of Interest Vocabulary**

[ac:endTime](#ac_endTime) |
[ac:endTimestamp](#ac_endTimestamp) |
[ac:hasROI](#ac_hasROI) |
[ac:heightFrac](#ac_heightFrac) |
[ac:isROIOf](#ac_isROIOf) |
[ac:mediaDuration](#ac_mediaDuration) |
[ac:mediaSpeed](#ac_mediaSpeed) |
[ac:radius](#ac_radius) |
[ac:RegionOfInterest](#ac_RegionOfInterest) |
[ac:startTime](#ac_startTime) |
[ac:startTimestamp](#ac_startTimestamp) |
[ac:widthFrac](#ac_widthFrac) |
[ac:xFrac](#ac_xFrac) |
[ac:yFrac](#ac_yFrac)

### 6.2 Index By Label

(See also [6.1 Index By Term Name](#61-index-by-term-name))

**Management Vocabulary**

[Commenter](#ac_commenter) |
[Comments](#ac_comments) |
[Date Available](#dcterms_available) |
[Identifier](#dcterms_identifier) |
[Metadata Date](#xmp_MetadataDate) |
[Metadata Language](#ac_metadataLanguage) |
[Modified](#dcterms_modified) |
[Provider-managed ID](#ac_providerManagedID) |
[Rating](#xmp_Rating) |
[Reviewer](#ac_reviewer) |
[Reviewer Comments](#ac_reviewerComments) |
[Service Access Point](#ac_hasServiceAccessPoint) |
[Subtype (IRI)](#ac_subtype) |
[Subtype (literal)](#ac_subtypeLiteral) |
[Title](#dcterms_title) |
[Type](#dc_type)

**Attribution Vocabulary**

[Attribution Link URL](#ac_attributionLinkURL) |
[Attribution URL](#ac_attributionLogoURL) |
[Copyright Owner](#xmpRights_Owner) |
[Copyright Statement](#dc_rights) |
[Credit](#photoshop_Credit) |
[Funding](#ac_fundingAttribution) |
[License Logo URL](#ac_licenseLogoURL) |
[License Terms](#xmpRights_UsageTerms) |
[License URL](#xmpRights_WebStatement) |
[Published Source](#dc_source)

**Agents Vocabulary**

[Creator](#dc_creator) |
[Metadata Creator](#ac_metadataCreator) |
[Metadata Provider](#ac_metadataProvider) |
[Provider](#ac_provider)

**Content Coverage Vocabulary**

[Caption](#ac_caption) |
[Description](#dcterms_description) |
[Language](#dc_language) |
[Lower frequency bound](#ac_freqLow) |
[Physical Setting](#ac_physicalSetting) |
[Subject Category](#Iptc4xmpExt_CVterm) |
[Subject Category Vocabulary](#ac_subjectCategoryVocabulary) |
[Tag](#ac_tag) |
[Upper frequency bound](#ac_freqHigh)

**Geography Vocabulary**

[City or Place Name](#Iptc4xmpExt_City) |
[Continent](#dwc_continent) |
[Coordinate Precision](#dwc_coordinatePrecision) |
[Coordinate Uncertainty In Meters](#dwc_coordinateUncertaintyInMeters) |
[Country](#dwc_country) |
[Country Code](#Iptc4xmpExt_CountryCode) |
[Country Name](#Iptc4xmpExt_CountryName) |
[County](#dwc_county) |
[Decimal Latitude](#dwc_decimalLatitude) |
[Decimal Longitude](#dwc_decimalLongitude) |
[Footprint Spatial Fit](#dwc_footprintSpatialFit) |
[Footprint SRS](#dwc_footprintSRS) |
[Footprint WKT](#dwc_footprintWKT) |
[Geodetic Datum](#dwc_geodeticDatum) |
[Georeference Protocol](#dwc_georeferenceProtocol) |
[Georeference Remarks](#dwc_georeferenceRemarks) |
[Georeference Sources](#dwc_georeferenceSources) |
[Georeference Verification Status](#dwc_georeferenceVerificationStatus) |
[Georeferenced By](#dwc_georeferencedBy) |
[Higher Geography](#dwc_higherGeography) |
[Higher Geography ID](#dwc_higherGeographyID) |
[Island](#dwc_island) |
[Island Group](#dwc_islandGroup) |
[Locality](#dwc_locality) |
[Location According To](#dwc_locationAccordingTo) |
[Location ID](#dwc_locationID) |
[Location Remarks](#dwc_locationRemarks) |
[Location Shown](#Iptc4xmpExt_LocationShown) |
[Maximum Depth In Meters](#dwc_maximumDepthInMeters) |
[Maximum Distance Above Surface In Meters](#dwc_maximumDistanceAboveSurfaceInMeters) |
[Maximum Elevation In Meters](#dwc_maximumElevationInMeters) |
[Minimum Depth In Meters](#dwc_minimumDepthInMeters) |
[Minimum Distance Above Surface In Meters](#dwc_minimumDistanceAboveSurfaceInMeters) |
[Minimum Elevation In Meters](#dwc_minimumElevationInMeters) |
[Municipality](#dwc_municipality) |
[Point Radius Spatial Fit](#dwc_pointRadiusSpatialFit) |
[Province or State](#Iptc4xmpExt_ProvinceState) |
[State Province](#dwc_stateProvince) |
[Sublocation](#Iptc4xmpExt_Sublocation) |
[Verbatim Coordinate System](#dwc_verbatimCoordinateSystem) |
[Verbatim Coordinates](#dwc_verbatimCoordinates) |
[Verbatim Depth](#dwc_verbatimDepth) |
[Verbatim Elevation](#dwc_verbatimElevation) |
[Verbatim Latitude](#dwc_verbatimLatitude) |
[Verbatim Locality](#dwc_verbatimLocality) |
[Verbatim Longitude](#dwc_verbatimLongitude) |
[Verbatim SRS](#dwc_verbatimSRS) |
[Water Body](#dwc_waterBody) |
[World Region](#Iptc4xmpExt_WorldRegion)

**Temporal Coverage Vocabulary**

[Original Date and Time](#xmp_CreateDate) |
[Temporal Coverage](#dcterms_temporal) |
[Time of Day](#ac_timeOfDay)

**Taxonomic Coverage Vocabulary**

[Common Name](#dwc_vernacularName) |
[Date Identified](#dwc_dateIdentified) |
[Identification Qualifier](#dwc_identificationQualifier) |
[Identified By](#dwc_identifiedBy) |
[Name According To](#dwc_nameAccordingTo) |
[Other Scientific Name](#ac_otherScientificName) |
[Scientific Name ID](#dwc_scientificNameID) |
[Scientific Taxon Name](#dwc_scientificName) |
[Subject Life Stage](#dwc_lifeStage) |
[Subject Orientation](#ac_subjectOrientation) |
[Subject Orientation (literal)](#ac_subjectOrientationLiteral) |
[Subject Part](#ac_subjectPart) |
[Subject Part (literal)](#ac_subjectPartLiteral) |
[Subject Preparation Technique](#dwc_preparations) |
[Subject Sex](#dwc_sex) |
[Taxon Count](#ac_taxonCount) |
[Taxon Coverage](#ac_taxonCoverage)

**Resource Creation Vocabulary**

[Capture Device](#ac_captureDevice) |
[Date and Time Digitized](#ac_digitizationDate) |
[Frame Rate](#ac_frameRate) |
[Location Created](#Iptc4xmpExt_LocationCreated) |
[Resource Creation Technique](#ac_resourceCreationTechnique) |
[Sample Rate](#mo_sample_rate)

**Related Resources Vocabulary**

[Associated Observation Reference](#ac_associatedObservationReference) |
[Associated Specimen Reference](#ac_associatedSpecimenReference) |
[Derived From](#ac_derivedFrom) |
[ID of Containing Collection](#ac_IDofContainingCollection) |
[Provider ID](#ac_providerID) |
[Related Resource ID](#ac_relatedResourceID)

**Service Access Point Vocabulary**

[Access URI](#ac_accessURI) |
[Format (IRI)](#dcterms_format) |
[Format (literal)](#dc_format) |
[Further Information URL](#ac_furtherInformationURL) |
[Hash](#ac_hashValue) |
[Hash Function](#ac_hashFunction) |
[Image Height](#exif_PixelYDimension) |
[Image Width](#exif_PixelXDimension) |
[Licensing Exception Statement](#ac_licensingException) |
[Service Access Point Class](#ac_ServiceAccessPoint) |
[Service Expectation](#ac_serviceExpectation) |
[Variant (IRI)](#ac_variant) |
[Variant (literal)](#ac_variantLiteral) |
[Variant Description](#ac_variantDescription)

**Region of Interest Vocabulary**

[End Time in Seconds](#ac_endTime) |
[End Timestamp](#ac_endTimestamp) |
[Fractional Height](#ac_heightFrac) |
[Fractional Width](#ac_widthFrac) |
[Fractional X](#ac_xFrac) |
[Fractional Y](#ac_yFrac) |
[Has Region of Interest](#ac_hasROI) |
[Is Region of Interest of](#ac_isROIOf) |
[Media Duration](#ac_mediaDuration) |
[Media Speed](#ac_mediaSpeed) |
[Radius](#ac_radius) |
[Region of Interest Class](#ac_RegionOfInterest) |
[Start Time in Seconds](#ac_startTime) |
[Start Timestamp](#ac_startTimestamp)

## 7 Vocabularies
### 7.1 Management Vocabulary

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dcterms_available"></a>Term Name: dcterms:available</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://purl.org/dc/terms/available">http://purl.org/dc/terms/available</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://dublincore.org/usage/terms/history/#available-003">http://dublincore.org/usage/terms/history/#available-003</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Date Available</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Date (often a range) that the resource became or will become available. </td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The date (often a range) that the resource became or will become available. The date and time MUST comply with the World Wide Web Consortium (W3C) datetime practice, <a href="https://www.w3.org/TR/NOTE-datetime">https://www.w3.org/TR/NOTE-datetime</a>, which requires that date and time representation correspond to ISO 8601:1998, but with year fields always comprising 4 digits. This makes datetime records compliant with 8601:2004, <a href="https://www.iso.org/standard/40874.html">https://www.iso.org/standard/40874.html</a>. AC datetime values MAY also follow 8601:2004 for ranges by separating two IS0 8601 datetime fields by a solidus ("forward slash", '/').</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>A use case is the harvesting of metadata published before the media are available, which are pending a formal publication elsewhere. One important example is the case of metadata that documents an occurrence, which metadata harvesters might exploit without use of the media. See also the wikipedia IS0 8601 entry, <a href="https://en.wikipedia.org/wiki/ISO_8601">https://en.wikipedia.org/wiki/ISO_8601</a>, for further explanation and examples.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_commenter"></a>Term Name: ac:commenter</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/commenter">http://rs.tdwg.org/ac/terms/commenter</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/commenter-2023-09-05">http://rs.tdwg.org/ac/terms/version/commenter-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Commenter</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A URI denoting a person who created a comment.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Implementers and communities of practice MAY produce restrictions or recommendations on the choice of vocabularies.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>See also Reviewer Comments for the distinction between Comments and Reviewer Comments. See also the entry for ac:commenterLiteral and the section Namespaces, Prefixes and Term Names in the Audiovisual Core Term List document for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_commenterLiteral"></a>Term Name: ac:commenterLiteral</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/commenterLiteral">http://rs.tdwg.org/ac/terms/commenterLiteral</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/commenterLiteral-2023-09-05">http://rs.tdwg.org/ac/terms/version/commenterLiteral-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Commenter</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The name of a person who created a comment, or the literal "anonymous" (= anonymously commented).</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>See also Reviewer Comments for the distinction between Comments and Reviewer Comments. See also the entry for ac:commenter and the section Namespaces, Prefixes and Term Names in the Audiovisual Core Term List document for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_comments"></a>Term Name: ac:comments</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/comments">http://rs.tdwg.org/ac/terms/comments</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/comments-2020-01-27">http://rs.tdwg.org/ac/terms/version/comments-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Comments</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Any comment provided on the media resource, as free-form text.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Best practice would also identify the commenter.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Comments may refer to the resource itself (e. g., asserting a taxon name or location of a biological subject in an image), or to the relation between resource and associated metadata (e. g., asserting that the taxon name given in the metadata is wrong, without asserting a positive identification). There is a separate item for Reviewer Comments, which is defined more as an expert-level review. Implementers or communities of practice might establish conventions about the meaning of the absence of a commenter, but this specification is silent on that matter.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_hasServiceAccessPoint"></a>Term Name: ac:hasServiceAccessPoint</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/hasServiceAccessPoint">http://rs.tdwg.org/ac/terms/hasServiceAccessPoint</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/hasServiceAccessPoint-2023-09-05">http://rs.tdwg.org/ac/terms/version/hasServiceAccessPoint-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Service Access Point</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>In a chosen serialization (RDF, XML Schema, etc.) the potentially multiple service access points (e.g., for different resolutions of an image) might be provided in a referenced or in a nested object. This property identifies one such access point. That is, each of potentially multiple values of hasServiceAccessPoint identifies a set of representation-dependent metadata using the properties defined under the Service Access Point Vocabulary section of the Audiovisual Core Term List document.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Some serializations may flatten the model of service-access points by (a) dropping ac:hasServiceAccessPoint, ac:variant and ac:variantLiteral, (b) repeating properties from the Service Access Point Vocabulary and prefixing them with values of ac:variantLiteral. If such a flat serialization is necessary for services, we recommend to select from among term names of the form "AB" where "A" is one of thumbnail, trailer, lowerQuality, mediumQuality, goodQuality, bestQuality, offline and "B" is one of AccessURI, Format, Extent, FurtherInformationURL, LicensingException, ServiceExpectation (example: thumbnailAccessURI). Implementers in specific constraint languages such as XML Schema or RDF may wish to make Access URI and perhaps dcterms:format mandatory on instances of the service access point.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dcterms_identifier"></a>Term Name: dcterms:identifier</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://purl.org/dc/terms/identifier">http://purl.org/dc/terms/identifier</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://dublincore.org/usage/terms/history/#identifierT-001">http://dublincore.org/usage/terms/history/#identifierT-001</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Identifier</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> Yes for media collections, No for media resources (but preferred if available) -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An unambiguous reference to the resource within a given context. </td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>An arbitrary code that is unique for the resource, with the resource being either a provider, collection, or media item.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Using multiple identifiers implies that they have a same-as relationship, i.e. they all identify the same object (e. g. an object may have all of an http-URL, an lsid-URI, and a UUID).</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="xmp_MetadataDate"></a>Term Name: xmp:MetadataDate</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://ns.adobe.com/xap/1.0/MetadataDate">http://ns.adobe.com/xap/1.0/MetadataDate</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Metadata Date</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The date and time that any metadata for this resource was last changed. It should be the same as or more recent than xmp:ModifyDate.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Point in time recording when the last modification to metadata (not necessarily the media object itself) occurred. The date and time MUST comply with the World Wide Web Consortium (W3C) datetime practice, <a href="https://www.w3.org/TR/NOTE-datetime">https://www.w3.org/TR/NOTE-datetime</a>, which requires that date and time representation correspond to ISO 8601:1998, but with year fields always comprising 4 digits. This makes datetime records compliant with 8601:2004, <a href="https://www.iso.org/standard/40874.html">https://www.iso.org/standard/40874.html</a>. AC datetime values MAY also follow 8601:2004 for ranges by separating two IS0 8601 datetime fields by a solidus ("forward slash", '/').</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This is not dcterms:modified, which refers to the resource itself rather than its metadata. See also the wikipedia IS0 8601 entry, <a href="https://en.wikipedia.org/wiki/ISO_8601">https://en.wikipedia.org/wiki/ISO_8601</a>, for further explanation and examples.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_metadataLanguage"></a>Term Name: ac:metadataLanguage</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/metadataLanguage">http://rs.tdwg.org/ac/terms/metadataLanguage</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/metadataLanguage-2023-09-05">http://rs.tdwg.org/ac/terms/version/metadataLanguage-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Metadata Language</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> Yes -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The URI of the language of description and other metadata (but not necessarily of the image itself) , from the ISO639-2 list of URIs for ISO 3-letter language codes, http://id.loc.gov/vocabulary/iso639-2.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>At least one of ac:metadataLanguage and ac:metadataLanguageLiteral MUST be supplied but, when feasible, supplying both might make the metadata more widely useful. They must specify the same language. In case of ambiguity, ac:metadataLanguage prevails.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This is NOT dcterms:language, which is about the resource, not the metadata. Metadata Language is deliberately single-valued, imposing on unstructured serializations a requirement that multi-lingual metadata be represented as separate, complete, metadata records. Audiovisual Core requires that each record also contains the language-neutral terms. In the absence of this requirement, metadata consumers would need to know which terms are language-neutral and merge these terms from all provided metadataLanguages into a single record. Metadata consumers may re-combine the information based on the dcterms:identifier that identifies the multimedia resource. Nothing in this document would, however, prevent an implementer, e. g. of an XML-Schema representation, from providing a fully hierarchical schema in which language neutral terms occur only a single time, and only the language-specific terms are repeated in a way that unambigously relates them to a metadata language. In RDF it may be a simple repetition of plain literals associated with a language (e.g., xml:lang attribute in RDF/XML). The language attribute would then be required in Audiovisual Core and would replace ac:metadataLanguage.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_metadataLanguageLiteral"></a>Term Name: ac:metadataLanguageLiteral</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/metadataLanguageLiteral">http://rs.tdwg.org/ac/terms/metadataLanguageLiteral</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/metadataLanguageLiteral-2023-09-05">http://rs.tdwg.org/ac/terms/version/metadataLanguageLiteral-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Metadata Language</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> Yes -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Language of description and other metadata (but not necessarily of the image itself) represented as an ISO639-2 three letter language code.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>ISO639-1 two-letter codes are permitted but deprecated. At least one of ac:metadataLanguage and ac:metadataLanguageLiteral MUST be supplied but, when feasible, supplying both might make the metadata more widely useful. They MUST specify the same language. In case of ambiguity, ac:metadataLanguage prevails. </td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This is NOT dc:language, which is about the resource, not the metadata. Metadata Language is deliberately single-valued, imposing on unstructured serializations a requirement that multi-lingual metadata be represented as separate, complete, metadata records. Audiovisual Core requires that each record also contains the language-neutral terms. In the absence of this requirement, metadata consumers would need to know which terms are language-neutral and merge these terms from all provided metadataLanguages into a single record. Metadata consumers may re-combine the information based on the dcterms:identifier that identifies the multimedia resource. Nothing in this document would, however, prevent an implementer, e. g. of an XML-Schema representation, from providing a fully hierarchical schema in which language neutral terms occur only a single time, and only the language-specific terms are repeated in a way that unambigously relates them to a metadata language. In RDF it may be a simple repetition of plain literals associated with a language (e.g., xml:lang attribute in RDF/XML). The language attribute would then be required in Audiovisual Core and would replace ac:metadataLanguage.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dcterms_modified"></a>Term Name: dcterms:modified</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://purl.org/dc/terms/modified">http://purl.org/dc/terms/modified</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://dublincore.org/usage/terms/history/#modified-003">http://dublincore.org/usage/terms/history/#modified-003</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Modified</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Date on which the resource was changed. </td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Date that the media resource was altered. The date and time MUST comply with the World Wide Web Consortium (W3C) datetime practice, <a href="https://www.w3.org/TR/NOTE-datetime">https://www.w3.org/TR/NOTE-datetime</a>, which requires that date and time representation correspond to ISO 8601:1998, <a href="https://www.iso.org/standard/40874.html">https://www.iso.org/standard/40874.html</a>, but with year fields always comprising 4 digits. This makes datetime records compliant with 8601:2004. AC datetime values MAY also follow 8601:2004 for ranges by separating two IS0 8601 datetime fields by a solidus ("forward slash", '/').</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>dcterms:modified permits all modification dates to be recorded, or if only one is recorded, it is assumed to be the latest. See also the wikipedia IS0 8601 entry, <a href="https://en.wikipedia.org/wiki/ISO_8601">https://en.wikipedia.org/wiki/ISO_8601</a>, for further explanation and examples.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_providerManagedID"></a>Term Name: ac:providerManagedID</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/providerManagedID">http://rs.tdwg.org/ac/terms/providerManagedID</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/providerManagedID-2020-01-27">http://rs.tdwg.org/ac/terms/version/providerManagedID-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Provider-managed ID</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A free-form identifier (a simple number, an alphanumeric code, a URL, etc.) for the resource that is unique and meaningful primarily for the data provider.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Ideally, this would be a globally unique identifier (GUID), but the provider is encouraged to supply any form of identifier that simplifies communications on resources within their project and helps to locate individual data items in the provider's data repositories. It is the provider's decision whether to expose this value or not.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="xmp_Rating"></a>Term Name: xmp:Rating</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://ns.adobe.com/xap/1.0/Rating">http://ns.adobe.com/xap/1.0/Rating</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Rating</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A user-assigned rating for this file. The value shall be -1 or in the range [0..5], where -1 indicates "rejected" and 0 indicates "unrated".  If xmp:Rating is not present, a value of 0 should be assumed.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>A rating of the media resources, provided by record originators or editors, with '1' (worst) to '5' (best). Anticipated usage is for a typical 'star rating' UI, with the addition of a notion of rejection. Values MAY be decimal numbers in the permitted range.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The origin of the rating is not communicated. It may, e. g., be based on user feedback or on editorial ratings. By "user-assigned" is meant assigned by the originator or editor of the record using the term.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_reviewer"></a>Term Name: ac:reviewer</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/reviewer">http://rs.tdwg.org/ac/terms/reviewer</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/reviewer-2023-09-05">http://rs.tdwg.org/ac/terms/version/reviewer-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Reviewer</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>URI for a reviewer.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>If present, then resource is peer-reviewed, even if Reviewer Comments is absent or empty. Its presence tells whether an expert in the subject featured in the media has reviewed the media item or collection and approved its metadata description; MUST display a name or the literal "anonymous" (= anonymously reviewed).</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Provider is asserting they accept this review as competent. See also ac:reviewerLiteral and the section Namespaces, Prefixes and Term Names in the Audiovisual Core Term List document for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_reviewerComments"></a>Term Name: ac:reviewerComments</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/reviewerComments">http://rs.tdwg.org/ac/terms/reviewerComments</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/reviewerComments-2020-01-27">http://rs.tdwg.org/ac/terms/version/reviewerComments-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Reviewer Comments</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Any comment provided by a reviewer with expertise in the subject, as free-form text.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Reviewer Comments may refer to the resource itself (e. g., asserting a taxon name or location of a biological subject in an image), or to the relation between resource and associated metadata (e. g., asserting that the taxon name given in the metadata is wrong, without asserting a positive identification). There is a separate item "Comments" for text from commenters of unrecorded expertise.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_reviewerLiteral"></a>Term Name: ac:reviewerLiteral</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/reviewerLiteral">http://rs.tdwg.org/ac/terms/reviewerLiteral</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/reviewerLiteral-2023-09-05">http://rs.tdwg.org/ac/terms/version/reviewerLiteral-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Reviewer</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>String providing the name of a reviewer.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>If present, then resource is peer-reviewed, even if Reviewer Comments is absent or empty. Its presence tells whether an expert in the subject featured in the media has reviewed the media item or collection and approved its metadata description; MUST display a name or the literal "anonymous" (= anonymously reviewed).</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Provider is asserting they accept this review as competent. See also ac:reviewer and the section Namespaces, Prefixes and Term Names in the Audiovisual Core Term List document for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_subtype"></a>Term Name: ac:subtype</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/subtype">http://rs.tdwg.org/ac/terms/subtype</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/subtype-2023-09-05">http://rs.tdwg.org/ac/terms/version/subtype-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Subtype (IRI)</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A class, represented by an IRI, that provides for more specialization of the media item type than dcterms:type.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The subtype term MUST NOT be applied to Collection objects. However, the Description term in the Content Coverage Vocabulary might add further description to a Collection object. IRI values SHOULD be selected from the Controlled Vocabulary for Audiovisual Core subtype. Human-readable information about the Controlled Vocabulary for subtype is at <a href="http://rs.tdwg.org/ac/doc/subtype/">http://rs.tdwg.org/ac/doc/subtype/</a> . In text-based systems such as tables, IRI values MUST be in unabbreviated form. When an appropriate subtype is not available in the Audiovisual Core controlled vocabulary, a term IRI that is not in a TDWG namespace MAY be used. Conforming applications MAY choose to ignore controlled values not issued by Audiovisual Core.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>See ac:subtypeLiteral for usage with strings.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_subtypeLiteral"></a>Term Name: ac:subtypeLiteral</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/subtypeLiteral">http://rs.tdwg.org/ac/terms/subtypeLiteral</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/subtypeLiteral-2023-09-05">http://rs.tdwg.org/ac/terms/version/subtypeLiteral-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Subtype (literal)</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A class, represented by a controlled value string, that provides for more specialization of the media item type than dc:type.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The subtypeLiteral term MUST NOT be applied to Collection objects. However, the Description term in the Content Coverage Vocabulary might add further description to a Collection object. Controlled string values SHOULD be selected from the Controlled Vocabulary for Audiovisual Core subtype. Human-readable information about the Controlled Vocabulary for subtype is at <a href="http://rs.tdwg.org/ac/doc/subtype/">http://rs.tdwg.org/ac/doc/subtype/</a> . It is best practice to use ac:subtype instead of ac:subytpeLiteral whenever practical.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dcterms_title"></a>Term Name: dcterms:title</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://purl.org/dc/terms/title">http://purl.org/dc/terms/title</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://dublincore.org/usage/terms/history/#titleT-002">http://dublincore.org/usage/terms/history/#titleT-002</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Title</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A name given to the resource.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Concise title, name, or brief descriptive label of institution, resource collection, or individual resource. This field SHOULD include the complete title with all the subtitles, if any.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>It is strongly suggested to provide a title. The title facilitates interactions with humans: e.g., it could be used as display text of hyperlinks or to provide a choice of images in a pick list. The title is therefore highly useful and an effort should be made to provide it where it is not already available. When the resource is a collection without an institutional or official name, but with a thematic content, a descriptive title, e. g. "Urban Ants of New England," would be suitable. In individual media resources depicting taxa, the scientific name or names of taxa often form a good title. Common names in addition to or instead of scientific names are also acceptable. Indications of action or roles captured by the media resource, such as predatory acts, are desirable ("Rattlesnake eating deer mouse", "Pollinators of California Native Plants").</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dc_type"></a>Term Name: dc:type</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://purl.org/dc/elements/1.1/type">http://purl.org/dc/elements/1.1/type</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://dublincore.org/usage/terms/history/#type-006">http://dublincore.org/usage/terms/history/#type-006</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Type</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> Yes -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The nature or genre of the resource.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The value of dc:type SHOULD be a term name of any term from the DCMI Type Vocabulary, <a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#section-7">https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#section-7</a> RECOMMENDED term names for media items are "Collection", "StillImage", "Sound", "MovingImage", "InteractiveResource", and "Text". A Collection MUST be given a value of "Collection". Following the DC recommendations at <a href="http://purl.org/dc/dcmitype/Text">http://purl.org/dc/dcmitype/Text</a>, images of text SHOULD be given a value of "Text" for dc:type. A value for at least one of dc:type and dcterms:type MUST be supplied in an Audiovisual Core record but when feasible, supplying both can make the metadata more widely useful. The values of dc:type and dcterms:type SHOULD designate the same type, but in case of ambiguity dcterms:type prevails.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If the resource is a Collection, this term does not identify what types of objects it may contain. See also the entry for dcterms:type in the Audiovisual Core term list document and see the DCMI FAQ on DC and DCTERMS Namespaces, <a href="https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md">https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md</a>, for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dcterms_type"></a>Term Name: dcterms:type</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://purl.org/dc/terms/type">http://purl.org/dc/terms/type</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://dublincore.org/usage/terms/history/#typeT-001">http://dublincore.org/usage/terms/history/#typeT-001</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Type</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> Yes -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The nature or genre of the resource. </td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The value of dcterms:type SHOULD be an IRI of any term from the DCMI Type Vocabulary, <a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#section-7">https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#section-7</a> . In text-based systems (e.g. spreadsheets) the value MUST be an IRI with an unabbreviated namespace. Machine-readable systems MAY use any form of the IRI (e.g. compact URIs; CURIEs) that can be determined to be equivalent to the unabbreviated IRI. RECOMMENDED values for media items are those IRIs whose term names are "Collection", "StillImage", "Sound", "MovingImage", "InteractiveResource", and "Text". A Collection MUST be given a value of <a href="http://purl.org/dc/dcmitype/Collection">http://purl.org/dc/dcmitype/Collection</a>. Following the DC recommendations at <a href="http://purl.org/dc/dcmitype/Text">http://purl.org/dc/dcmitype/Text</a>, images of text SHOULD be given a value of <a href="http://purl.org/dc/dcmitype/Text">http://purl.org/dc/dcmitype/Text</a> for dcterms:type. A value for at least one of dc:type and dcterms:type MUST be supplied in an Audiovisual Core record but when feasible, supplying both can make the metadata more widely useful. The values of dc:type and dcterms:type SHOULD designate the same type, but in case of ambiguity dcterms:type prevails.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If the resource is a Collection, this term does not identify what types of objects it may contain. See also the entry for dc:type in the Audiovisual Core term list document and see the DCMI FAQ on DC and DCTERMS Namespaces, <a href="https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md">https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md</a>, for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions.</td>
		</tr>
	</tbody>
</table>


### 7.2 Attribution Vocabulary

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_attributionLinkURL"></a>Term Name: ac:attributionLinkURL</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/attributionLinkURL">http://rs.tdwg.org/ac/terms/attributionLinkURL</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/attributionLinkURL-2020-01-27">http://rs.tdwg.org/ac/terms/version/attributionLinkURL-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Attribution Link URL</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The URL where information about ownership, attribution, etc. of the resource may be found.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This URL may be used in creating a clickable logo. Providers should consider making this link as specific and useful to consumers as possible, e. g., linking to a metadata page of the specific image resource rather than to a generic page describing the owner or provider of a resource.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_attributionLogoURL"></a>Term Name: ac:attributionLogoURL</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/attributionLogoURL">http://rs.tdwg.org/ac/terms/attributionLogoURL</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/attributionLogoURL-2020-01-27">http://rs.tdwg.org/ac/terms/version/attributionLogoURL-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Attribution URL</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The URL of the icon or logo image to appear in source attribution.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Entering this URL into a browser should only result in the icon (not in a webpage including the icon).</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="photoshop_Credit"></a>Term Name: photoshop:Credit</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://ns.adobe.com/photoshop/1.0/Credit">http://ns.adobe.com/photoshop/1.0/Credit</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Credit</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The credit to person(s) and/or organisation(s) required by the supplier of the item to be used when published. This is a free-text field.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>free text for "Please cite this as ..."</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>IPTC also refers to this generically as a "Credit Line" as it is frequently displayed with the media.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_fundingAttribution"></a>Term Name: ac:fundingAttribution</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/fundingAttribution">http://rs.tdwg.org/ac/terms/fundingAttribution</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/fundingAttribution-2020-01-27">http://rs.tdwg.org/ac/terms/version/fundingAttribution-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Funding</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Text description of organizations or individuals who funded the creation of the resource.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_licenseLogoURL"></a>Term Name: ac:licenseLogoURL</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/licenseLogoURL">http://rs.tdwg.org/ac/terms/licenseLogoURL</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/licenseLogoURL-2020-01-27">http://rs.tdwg.org/ac/terms/version/licenseLogoURL-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>License Logo URL</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A URL providing access to a logo that symbolizes the License.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The originating metadata provider is strongly urged to choose a suitable logo as a graphical representation of the license. Failure to do so may leave downstream aggregators in a difficult position to supply a logo that adequately represents the professional, legal, or social aims of the licensors (license givers). Example: <a href="http://i.creativecommons.org/l/by-nc-sa/3.0/us/88x31.png">http://i.creativecommons.org/l/by-nc-sa/3.0/us/88x31.png</a> provides access to a logo image.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="xmpRights_Owner"></a>Term Name: xmpRights:Owner</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://ns.adobe.com/xap/1.0/rights/Owner">http://ns.adobe.com/xap/1.0/rights/Owner</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Copyright Owner</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A list of legal owners of the resource.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>A list of the names of the owners of the copyright. 'Unknown' is an acceptable value, but 'Public Domain' is not. In that case, omit or leave empty xmpRights:Owner, and put 'Public Domain' in the Copyright Statement (dc:rights). Note: Audiovisual Core guidelines on value format are less restrictive than is specified in the IPTC guidelines.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Some providers use dc:publisher for this purpose, but it seems doubtful that the publisher is by necessity the copyright owner. 'Public Domain' is not an appropriate value because it denotes something that is not under copyright. Except for 'Public Domain' resources, it is strongly urged that this field be supplied.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dc_rights"></a>Term Name: dc:rights</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://purl.org/dc/elements/1.1/rights">http://purl.org/dc/elements/1.1/rights</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://dublincore.org/usage/terms/history/#rights-006">http://dublincore.org/usage/terms/history/#rights-006</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Copyright Statement</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> Yes -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Information about rights held in and over the resource.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>A full-text, readable copyright statement, as required by the national legislation of the copyright holder. On collections, this applies to all contained objects, unless the object itself has a different statement. Do not place just the name of the copyright holder(s) here! That belongs in a list in the xmpRights:Owner field, which SHOULD be supplied if dc:rights is not 'Public Domain', which is appropriate only if the resource is known to be not under copyright. At least one of dcterms:rights and dc:rights MUST be supplied but, when feasible, supplying both might make the metadata more widely useful. They MUST specify the same rights. </td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This expresses rights over the media resource, not over the metadata text. In case of ambiguity, dcterms:rights prevails. See also the entry for dcterms:rights in the Audiovisual Core Term List document and see the DCMI FAQ on DC and DCTERMS Namespaces, <a href="https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md">https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md</a>, for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. Examples: "Copyright XY 2008, all rights reserved", "© 2008 XY Museum", "Public Domain.", "Copyright unknown."</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dcterms_rights"></a>Term Name: dcterms:rights</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://purl.org/dc/terms/rights">http://purl.org/dc/terms/rights</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://dublincore.org/usage/terms/history/#rightsT-001">http://dublincore.org/usage/terms/history/#rightsT-001</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Copyright Statement</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> Yes -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Information about rights held in and over the resource.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>A URI pointing to structured information about rights held in and over the resource. At least one of dcterms:rights and dc:rights MUST be supplied but, when feasible, supplying both might make the metadata more widely useful. They MUST specify the same rights. In case of ambiguity, dcterms:rights prevails.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This expresses rights over the media resource, not over the metadata text. See also the entry for dc:rights in the Audiovisual Core Term List document and see the DCMI FAQ on DC and DCTERMS Namespaces, <a href="https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md">https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md</a>, for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions. Examples include <a href="http://creativecommons.org/licenses/by/3.0/legalcode">http://creativecommons.org/licenses/by/3.0/legalcode</a> and <a href="http://creativecommons.org/publicdomain/zero/1.0/">http://creativecommons.org/publicdomain/zero/1.0/</a>.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dc_source"></a>Term Name: dc:source</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://purl.org/dc/elements/1.1/source">http://purl.org/dc/elements/1.1/source</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://dublincore.org/usage/terms/history/#source-006">http://dublincore.org/usage/terms/history/#source-006</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Published Source</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A related resource from which the described resource is derived. </td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>A string providing an identifiable source from which the described resources was derived.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If the resource was digitized from a non-digital resource, or was also previously published in a digital or printed publication, this describes the original. Do not put generally "related" publications in here. This field normally contains a free-form text description. If a URI is available it should be provided in dcterms:source. Can be repeatable if a montage of images. Information about further provenance beyond the ultimate source should be put in the derivedFrom attribute. See also the entry for dcterms:source in the Audiovisual Core term list document and see the DCMI FAQ on DC and DCTERMS Namespaces, <a href="https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md">https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md</a>, for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dcterms_source"></a>Term Name: dcterms:source</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://purl.org/dc/terms/source">http://purl.org/dc/terms/source</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://dublincore.org/usage/terms/history/#sourceT-001">http://dublincore.org/usage/terms/history/#sourceT-001</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Published Source</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A related resource from which the described resource is derived. </td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>URI for an identifiable source from which the described resources was derived.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If the resource was digitized from a non-digital resource, or was also previously published in a digital or printed publication, this describes the original. If a string is required for this, use dc:source. Do not put generally "related" publications in here. A URI that can be resolved and dereferenced to provide a description of the source resource may also be used here. For example, "<a href="http://www.loc.gov/pictures/item/fsa1998021539/PP/">http://www.loc.gov/pictures/item/fsa1998021539/PP/</a>" is the address of a web page that provides a description the original negative of a famous picture by the photographer Dorothea Lange and so would be an appropriate value of dcterms:source. The term may be repeatable if a montage of images. Information about further provenance beyond the ultimate source should be put in the derivedFrom attribute. See also the entry for dc:source in the Audiovisual Core term list document and see the DCMI FAQ on DC and DCTERMS Namespaces, <a href="https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md">https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md</a>, for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="xmpRights_UsageTerms"></a>Term Name: xmpRights:UsageTerms</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://ns.adobe.com/xap/1.0/rights/UsageTerms">http://ns.adobe.com/xap/1.0/rights/UsageTerms</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>License Terms</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A collection of text instructions on how a resource can be legally used, given in a variety of languages.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The license statement defining how resources might be used. Information on a collection applies to all contained objects unless the object has a different statement. Where different quality variants (e. g. different resolutions of images) are published under different licenses, the AC term "Licensing Exception Statement" supports variant-specific licenses. Note that the medium or low resolution levels of the same image might be available under open access licenses.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Example: "Available under Creative Commons BY-SA 3.0 license". This also describes the commercial availability of items. Buying an identification tool or media resource is essentially the purchase of an individual license. Examples for such License statements: "Available through bookstores" for a commercially published CD, and "Individual licenses available for purchase" for a high-resolution image. In general, this term determines the default licensing for the media. License terms specific to variants or representations of the media resource (e.g., different resolutions) are dealt within the section on Service Access Point Vocabulary</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="xmpRights_WebStatement"></a>Term Name: xmpRights:WebStatement</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://ns.adobe.com/xap/1.0/rights/WebStatement">http://ns.adobe.com/xap/1.0/rights/WebStatement</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>License URL</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A Web URL for a statement of the ownership and usage rights for this resource.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>A URL defining or further elaborating on the license statement (e. g., a web page explaining the precise terms of use).  Where different quality variants (e. g. different resolutions of images) are published under different licenses, the AC term "Licensing Exception Statement" supports variant-specific licenses</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The value of this field may provide a complete definition of the terms of use. For Creative Commons, the appropriate value is the URL of the defining Web page for the license. Example: <a href="http://creativecommons.org/licenses/by-nc-sa/3.0/us/">http://creativecommons.org/licenses/by-nc-sa/3.0/us/</a></td>
		</tr>
	</tbody>
</table>


### 7.3 Agents Vocabulary

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dc_creator"></a>Term Name: dc:creator</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://purl.org/dc/elements/1.1/creator">http://purl.org/dc/elements/1.1/creator</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://dublincore.org/usage/terms/history/#creator-006">http://dublincore.org/usage/terms/history/#creator-006</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Creator</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An entity primarily responsible for making the resource.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The person or organization responsible for creating the media resource. The value MAY be simple text including contact information.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Note that the Creator need not be the Copyright Owner. See also the entry for dcterms:creator in the Audiovisual Core term list document and see the DCMI FAQ on DC and DCTERMS Namespaces, <a href="https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md">https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md</a>, for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dcterms_creator"></a>Term Name: dcterms:creator</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://purl.org/dc/terms/creator">http://purl.org/dc/terms/creator</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://dublincore.org/usage/terms/history/#creatorT-002">http://dublincore.org/usage/terms/history/#creatorT-002</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Creator</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An entity primarily responsible for making the resource. </td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>A URI representing the person or organization responsible for creating the media resource.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Note that the Creator need not be the Copyright Owner. See also the entry for dc:creator in the Audiovisual Core term list document and see the DCMI FAQ on DC and DCTERMS Namespaces, <a href="https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md">https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md</a>, for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_metadataCreator"></a>Term Name: ac:metadataCreator</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/metadataCreator">http://rs.tdwg.org/ac/terms/metadataCreator</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/metadataCreator-2023-09-05">http://rs.tdwg.org/ac/terms/version/metadataCreator-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Metadata Creator</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A URI representing a person or organization originally creating the resource metadata record.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>See also the entry for ac:metadataCreatorLiteral and the section Namespaces, Prefixes and Term Names in the Audiovisual Core Term List document for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_metadataCreatorLiteral"></a>Term Name: ac:metadataCreatorLiteral</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/metadataCreatorLiteral">http://rs.tdwg.org/ac/terms/metadataCreatorLiteral</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/metadataCreatorLiteral-2023-09-05">http://rs.tdwg.org/ac/terms/version/metadataCreatorLiteral-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Metadata Creator</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Name of the person or organization originally creating the resource metadata record.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>See also the entry for ac:metadataCreator and the section Namespaces, Prefixes and Term Names in the Audiovisual Core Term List document for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_metadataProvider"></a>Term Name: ac:metadataProvider</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/metadataProvider">http://rs.tdwg.org/ac/terms/metadataProvider</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/metadataProvider-2023-09-05">http://rs.tdwg.org/ac/terms/version/metadataProvider-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Metadata Provider</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>URI of person or organization originally responsible for providing the resource metadata record.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Media resources and their metadata may be served from different institutions, e. g. in the case of aggregators adding user annotations, taxon identifications, or ratings. Compare Provider. See also the entry for ac:metadataProviderLiteral and the section Namespaces, Prefixes and Term Names in the Audiovisual Core Term List document for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_metadataProviderLiteral"></a>Term Name: ac:metadataProviderLiteral</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/metadataProviderLiteral">http://rs.tdwg.org/ac/terms/metadataProviderLiteral</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/metadataProviderLiteral-2020-01-27">http://rs.tdwg.org/ac/terms/version/metadataProviderLiteral-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Metadata Provider</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Name of the person or organization originally responsible for providing the resource metadata record.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Media resources and their metadata may be served from different institutions, e. g. in the case of aggregators adding user annotations, taxon identifications, or ratings. Compare Provider. See also the entry for ac:metadataProvider in this document and the section Namespaces, Prefixes and Term Names for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_provider"></a>Term Name: ac:provider</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/provider">http://rs.tdwg.org/ac/terms/provider</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/provider-2023-09-05">http://rs.tdwg.org/ac/terms/version/provider-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Provider</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>URI for person or organization responsible for presenting the media resource.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>If no separate Metadata Provider is given, this also attributes the metadata.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Media resources and their metadata may be served from different institutions, e. g. in the case of aggregators adding user annotations, taxon identifications, or ratings. See also the entry for ac:providerLiteral and the section Namespaces, Prefixes and Term Names in the Audiovisual Core Term List document for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_providerLiteral"></a>Term Name: ac:providerLiteral</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/providerLiteral">http://rs.tdwg.org/ac/terms/providerLiteral</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/providerLiteral-2023-09-05">http://rs.tdwg.org/ac/terms/version/providerLiteral-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Provider</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Name of the person or organization responsible for presenting the media resource.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>If no separate Metadata Provider is given, this also attributes the metadata.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Media resources and their metadata may be served from different institutions, e. g. in the case of aggregators adding user annotations, taxon identifications, or ratings. See also the entry for ac:provider and the section Namespaces, Prefixes and Term Names in the Audiovisual Core Term List document for discussion of the rationale for separate terms taking URI values from those taking Literal values where both are possible. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions.</td>
		</tr>
	</tbody>
</table>


### 7.4 Content Coverage Vocabulary

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_caption"></a>Term Name: ac:caption</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/caption">http://rs.tdwg.org/ac/terms/caption</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/caption-2021-10-05">http://rs.tdwg.org/ac/terms/version/caption-2021-10-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Caption</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>As alternative or in addition to description, a caption is free-form text to be displayed together with (rather than instead of) a resource that is suitable for captions (especially images).</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>If both description and caption are present in the metadata, a description is typically displayed instead of the resource, a caption together with the resource. Thus, in HTML it would be appropriate to use ac:caption values in figcaption elements. Often only one of description or caption is present; choose the term most appropriate for your metadata.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="Iptc4xmpExt_CVterm"></a>Term Name: Iptc4xmpExt:CVterm</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://iptc.org/std/Iptc4xmpExt/2008-02-29/CVterm">http://iptc.org/std/Iptc4xmpExt/2008-02-29/CVterm</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Subject Category</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A term to describe the content of the image by a value from a Controlled Vocabulary. </td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Controlled vocabulary of subjects to support broad classification of media items. Terms from various controlled vocabularies may be used. AC-recommended vocabularies are preferred and MAY be unqualified literals (not a full URI). For terms from other vocabularies either a precise URI SHOULD be used, or, as long as all unqualified terms in all vocabularies are unique, metadata SHOULD provide the source vocabularies using the Subject Category Vocabulary term. The value SHOULD be a string, whose text can also be in the form of a URL.  These guidelines on value format are less restrictive than is specified by the IPTC guidelines.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended sets include: the NASA Global Change Master Directory (GCMD; <a href="http://gcmd.nasa.gov/">http://gcmd.nasa.gov/</a>), Subject Categories defined in Key to Nature (K2N; <a href="http://www.keytonature.eu/wiki/Subject_Category">http://www.keytonature.eu/wiki/Subject_Category</a>), the BioComplexity Thesaurus; <a href="https://www2.usgs.gov/core_science_systems/csas/biocomplexity_thesaurus/">https://www2.usgs.gov/core_science_systems/csas/biocomplexity_thesaurus/</a>, the Description Type GBIF Vocabulary; <a href="http://rs.gbif.org/vocabulary/gbif/description_type.xml">http://rs.gbif.org/vocabulary/gbif/description_type.xml</a>, the TDWG Species Profile Model; <a href="http://rs.tdwg.org/ontology/voc/SPMInfoItems.rdf">http://rs.tdwg.org/ontology/voc/SPMInfoItems.rdf</a>, the Plinian Core; <a href="https://github.com/tdwg/PlinianCore/wiki">https://github.com/tdwg/PlinianCore/wiki</a>, the European Environmental Agency GEneral Multilingual Environmental Thesaurus (GEMET; <a href="http://www.eionet.europa.eu/gemet">http://www.eionet.europa.eu/gemet</a>), and the Long Term Ecological Research Network Controlled Vocabulary (LTER; <a href="http://vocab.lternet.edu/">http://vocab.lternet.edu/</a>). The vocabulary may include major taxonomic groups (such as "vertebrates" or "fungi") or ecosystem terms ("savannah", "temperate rain forest", "forest fires", "aquatic vertebrates"). Other formal classifications (published in print or online) such as habitat, fuel, invasive species, agroproductivity, fisheries, migratory species etc. are also suitable.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dcterms_description"></a>Term Name: dcterms:description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://purl.org/dc/terms/description">http://purl.org/dc/terms/description</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://dublincore.org/usage/terms/history/#descriptionT-001">http://dublincore.org/usage/terms/history/#descriptionT-001</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Description</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An account of the resource. </td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Description of collection or individual resource, containing the Who, What, When, Where and Why as free-form text.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This property optionally allows the presentation of detailed information and will in most cases be shown together with the resource title. If both a description and a caption are present in the metadata, a description is typically displayed instead of the resource, whereas a caption is displayed together with the resource. The description should aim to be a good proxy for the underlying media resource in cases where only text can be shown, whereas the caption may only make sense when shown together with the media. Thus, in HTML it would be appropriate to use dcterms:description values for alt attributes in img elements. Often only one of description or caption is present; choose the term most appropriate for your metadata. It is the role of implementers of an AC concrete representation (e.g., an XML Schema, an RDF representation, etc.) to decide and document how formatting advice will be represented in descriptions serialized according to such representations.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_freqHigh"></a>Term Name: ac:freqHigh</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/freqHigh">http://rs.tdwg.org/ac/terms/freqHigh</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/freqHigh-2021-10-05">http://rs.tdwg.org/ac/terms/version/freqHigh-2021-10-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Upper frequency bound</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The highest frequency of the phenomena reflected in the multimedia item or Region of Interest.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Numeric value in hertz (Hz)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This term refers to the sound events depicted and not to the constraints of the recording medium, so are in principle independent from sampleRate. If dwc:scientificName is specified and if applied to the entire multimedia item, these frequency bounds refer to the sounds of the species given in the dwc:scientificName throughout the whole recording. Although many users will specify both freqLow and freqHigh, it is permitted to specify just one or the other, for example if only one of the bounds is discernible.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_freqLow"></a>Term Name: ac:freqLow</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/freqLow">http://rs.tdwg.org/ac/terms/freqLow</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/freqLow-2021-10-05">http://rs.tdwg.org/ac/terms/version/freqLow-2021-10-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Lower frequency bound</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The lowest frequency of the phenomena reflected in the multimedia item or Region of Interest.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Numeric value in hertz (Hz)</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This term refers to the sound events depicted and not to the constraints of the recording medium, so are in principle independent from sampleRate. If dwc:scientificName is specified and if applied to the entire multimedia item, these frequency bounds refer to the sounds of the species given in the dwc:scientificName throughout the whole recording. Although many users will specify both freqLow and freqHigh, it is permitted to specify just one or the other, for example if only one of the bounds is discernible.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dc_language"></a>Term Name: dc:language</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://purl.org/dc/elements/1.1/language">http://purl.org/dc/elements/1.1/language</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://dublincore.org/usage/terms/history/#language-007">http://dublincore.org/usage/terms/history/#language-007</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Language</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A language of the resource.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Language(s) of resource itself represented in the ISO639-2 three-letter language code. ISO639-1 two-letter codes are permitted but deprecated.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>An image may contain language such as superimposed labels. If an image is of a natural scene or organism, without any language included, the resource is language-neutral (ISO code "zxx"). Resources with present but unknown language are to be coded as undetermined (ISO code "und"). Regional dialects or other special cases should conform to the ISO639-5 Alpha-3 Code for Language Families and Groups, <a href="http://id.loc.gov/vocabulary/iso639-5.html">http://id.loc.gov/vocabulary/iso639-5.html</a>, where possible or the IETF Best Practices for Tags Identifying Languages, <a href="https://tools.ietf.org/html/rfc5646">https://tools.ietf.org/html/rfc5646</a>, where not. See also the entry for dcterms:language in the Audiovisual Core term list document and see the DCMI FAQ on DC and DCTERMS Namespaces, <a href="https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md">https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md</a>, for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dcterms_language"></a>Term Name: dcterms:language</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://purl.org/dc/terms/language">http://purl.org/dc/terms/language</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://dublincore.org/usage/terms/history/#languageT-001">http://dublincore.org/usage/terms/history/#languageT-001</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Language</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A language of the resource. </td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>URI from the ISO639-2 list of URIs for ISO 3-letter language codes, <a href="http://id.loc.gov/vocabulary/iso639-2">http://id.loc.gov/vocabulary/iso639-2</a>.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>An image may contain language such as superimposed labels. If an image is of a natural scene or organism, without any language included, the resource is language-neutral with URI <a href="http://id.loc.gov/vocabulary/iso639-2/zxx">http://id.loc.gov/vocabulary/iso639-2/zxx</a> corresponding to ISO ISO639-2 code "zxx". Resources with present but unknown language are to be coded as undetermined, with URI <a href="http://id.loc.gov/vocabulary/iso639-2/und">http://id.loc.gov/vocabulary/iso639-2/und</a> corresponding to ISO639-2 code "und". Regional dialects or other special cases should conform to the ISO639-5 Alpha-3 Code for Language Families and Groups, <a href="http://id.loc.gov/vocabulary/iso639-5.html">http://id.loc.gov/vocabulary/iso639-5.html</a>, where possible or the IETF Best Practices for Tags Identifying Languages, <a href="https://tools.ietf.org/html/rfc5646">https://tools.ietf.org/html/rfc5646</a>, where not. See also the entry for dc:language in the Audiovisual Core term list document and see the DCMI FAQ on DC and DCTERMS Namespaces, <a href="https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md">https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md</a>, for discussion of the rationale for terms in two namespaces. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_physicalSetting"></a>Term Name: ac:physicalSetting</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/physicalSetting">http://rs.tdwg.org/ac/terms/physicalSetting</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/physicalSetting-2020-01-27">http://rs.tdwg.org/ac/terms/version/physicalSetting-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Physical Setting</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The setting of the content represented in media such as images, sounds, and movies if the provider deems them relevant.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Constrained vocabulary of: "Natural" = Object in its natural setting of the object (e. g. living organisms in their natural environment); "Artificial" = Object in an artificial environment (e. g. living organisms in an artificial environment such as a zoo, garden, greenhouse, or laboratory); "Edited" = Human media editing of a natural setting or media acquisition with a separate media background such as a photographic backdrop.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Multiple values may be needed for movies or montages. See also ac:resourceCreationTechnique which should be used to describe any modifications to the resource itself. Communities of practice should form best practices for the use of these controlled terms.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_subjectCategoryVocabulary"></a>Term Name: ac:subjectCategoryVocabulary</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/subjectCategoryVocabulary">http://rs.tdwg.org/ac/terms/subjectCategoryVocabulary</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/subjectCategoryVocabulary-2020-01-27">http://rs.tdwg.org/ac/terms/version/subjectCategoryVocabulary-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Subject Category Vocabulary</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Any vocabulary or formal classification from which terms in the Subject Category have been drawn.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The AC recommended vocabularies do not need to be cited here. There is no required linkage between individual Subject Category terms and the vocabulary; the mechanism is intended to support discovery of the normative URI for a term, but not guarantee it.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_tag"></a>Term Name: ac:tag</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/tag">http://rs.tdwg.org/ac/terms/tag</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/tag-2020-01-27">http://rs.tdwg.org/ac/terms/version/tag-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Tag</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>General keywords or tags.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Tags may be multi-worded phrases. Where scientific names, common names, geographic locations, etc. are separable, those should go into the more specific coverage metadata items provided further below. Examples: "flower diagram". Character or part keywords like "leaf", or "flower color" are especially desirable.</td>
		</tr>
	</tbody>
</table>


### 7.5 Geography Vocabulary

Note that [dwc:locality](http://rs.tdwg.org/dwc/terms/locality) may be used, but as applied to media this term may be ambiguous as to whether it applies to the location depicted or the location at which the media was created. When disambiguating information is available, it is better to use the terms Location Shown and Location Created. The latter is in the Resource Creation Vocabulary.

Location Created and Location Shown are separated in the current version of IPTC, and the Metadata Working Group ([Metadata Working Group Guidelines for Handling Image Metadata, Version 2.0, November 2010](https://web.archive.org/web/20180919181934/http://www.metadataworkinggroup.org/pdf/mwg_guidance.pdf)) also recommends this. We follow this below in order to support the expected future increase of automatic GPS-based coordinate recording. As a special case, the AC group recommends to change the semantics of Location Shown in the case of biodiversity specimens, where the original location may differ from the current location at which the specimen is held in a collection. In this case, Location Shown should exclusively refer to the location where a specimen was originally collected (gathering or sampling location). Use Location Created to express the location where the resource was created (a specimen was digitized).

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="Iptc4xmpExt_City"></a>Term Name: Iptc4xmpExt:City</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://iptc.org/std/Iptc4xmpExt/2008-02-29/City">http://iptc.org/std/Iptc4xmpExt/2008-02-29/City</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>City or Place Name</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Name of the city of a location. This element is at the fourth level of a top-down geographical hierarchy.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Optionally, the name of a city or place commonly found in gazetteers (such as a mountain or national park) in which the subjects (e. g., species, habitats, or events) were located.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_continent"></a>Term Name: dwc:continent</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/continent">http://rs.tdwg.org/dwc/terms/continent</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/continent-2017-10-06">http://rs.tdwg.org/dwc/terms/version/continent-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Continent</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The name of the continent in which the Location occurs.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>Africa</code>, <code>Antarctica</code>, <code>Asia</code>, <code>Europe</code>, <code>North America</code>, <code>Oceania</code>, <code>South America</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_coordinatePrecision"></a>Term Name: dwc:coordinatePrecision</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/coordinatePrecision">http://rs.tdwg.org/dwc/terms/coordinatePrecision</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/coordinatePrecision-2017-10-06">http://rs.tdwg.org/dwc/terms/version/coordinatePrecision-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Coordinate Precision</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A decimal representation of the precision of the coordinates given in the decimalLatitude and decimalLongitude.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>0.00001</code> (normal GPS limit for decimal degrees). <code>0.000278</code> (nearest second). <code>0.01667</code> (nearest minute). <code>1.0</code> (nearest degree).</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_coordinateUncertaintyInMeters"></a>Term Name: dwc:coordinateUncertaintyInMeters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/coordinateUncertaintyInMeters">http://rs.tdwg.org/dwc/terms/coordinateUncertaintyInMeters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/coordinateUncertaintyInMeters-2017-10-06">http://rs.tdwg.org/dwc/terms/version/coordinateUncertaintyInMeters-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Coordinate Uncertainty In Meters</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The horizontal distance (in meters) from the given decimalLatitude and decimalLongitude describing the smallest circle containing the whole of the Location. Leave the value empty if the uncertainty is unknown, cannot be estimated, or is not applicable (because there are no coordinates). Zero is not a valid value for this term.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>30</code> (reasonable lower limit of a GPS reading under good conditions if the actual precision was not recorded at the time). <code>71</code> (uncertainty for a UTM coordinate having 100 meter precision and a known spatial reference system).</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_country"></a>Term Name: dwc:country</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/country">http://rs.tdwg.org/dwc/terms/country</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/country-2017-10-06">http://rs.tdwg.org/dwc/terms/version/country-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Country</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The name of the country or major administrative unit in which the Location occurs.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>Denmark</code>, <code>Colombia</code>, <code>España</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="Iptc4xmpExt_CountryCode"></a>Term Name: Iptc4xmpExt:CountryCode</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://iptc.org/std/Iptc4xmpExt/2008-02-29/CountryCode">http://iptc.org/std/Iptc4xmpExt/2008-02-29/CountryCode</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Country Code</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The ISO code of a country of a location. This element is at the second level of a top-down geographical hierarchy.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The geographic location of the specific entity or entities documented by the media item, expressed through a constrained vocabulary of countries using 2-letter ISO 3166-1 country code (e. g. "IT, SI").</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Accepted exceptions to be used instead of ISO codes are: "Global", "Marine", "Europe", "N-America", "C-America", "S-America", "Africa", "Asia", "Oceania", ATA = "Antarctica", XEU = "European Union", XAR = "Arctic", "ZZZ" = "Unknown country" (3 letter abbreviations from IPTC codes).</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_countryCode"></a>Term Name: dwc:countryCode</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/countryCode">http://rs.tdwg.org/dwc/terms/countryCode</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/countryCode-2017-10-06">http://rs.tdwg.org/dwc/terms/version/countryCode-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Country Code</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The standard code for the country in which the Location occurs.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use an ISO 3166-1-alpha-2 country code.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>AR</code>, <code>SV</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="Iptc4xmpExt_CountryName"></a>Term Name: Iptc4xmpExt:CountryName</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://iptc.org/std/Iptc4xmpExt/2008-02-29/CountryName">http://iptc.org/std/Iptc4xmpExt/2008-02-29/CountryName</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Country Name</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The name of a country of a location. This element is at the second level of a top-down geographical hierarchy.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>This field can be free text, but where possible, the use of <a href="http://iptc.org/std/Iptc4xmpExt/2008-02-29/CountryCode">http://iptc.org/std/Iptc4xmpExt/2008-02-29/CountryCode</a> is preferred.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_county"></a>Term Name: dwc:county</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/county">http://rs.tdwg.org/dwc/terms/county</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/county-2017-10-06">http://rs.tdwg.org/dwc/terms/version/county-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>County</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The full, unabbreviated name of the next smaller administrative region than stateProvince (county, shire, department, etc.) in which the Location occurs.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>Missoula</code>, <code>Los Lagos</code>, <code>Mataró</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_decimalLatitude"></a>Term Name: dwc:decimalLatitude</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/decimalLatitude">http://rs.tdwg.org/dwc/terms/decimalLatitude</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/decimalLatitude-2017-10-06">http://rs.tdwg.org/dwc/terms/version/decimalLatitude-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Decimal Latitude</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The geographic latitude (in decimal degrees, using the spatial reference system given in geodeticDatum) of the geographic center of a Location. Positive values are north of the Equator, negative values are south of it. Legal values lie between -90 and 90, inclusive.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>-41.0983423</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_decimalLongitude"></a>Term Name: dwc:decimalLongitude</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/decimalLongitude">http://rs.tdwg.org/dwc/terms/decimalLongitude</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/decimalLongitude-2017-10-06">http://rs.tdwg.org/dwc/terms/version/decimalLongitude-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Decimal Longitude</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The geographic longitude (in decimal degrees, using the spatial reference system given in geodeticDatum) of the geographic center of a Location. Positive values are east of the Greenwich Meridian, negative values are west of it. Legal values lie between -180 and 180, inclusive.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>-121.1761111</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_footprintSpatialFit"></a>Term Name: dwc:footprintSpatialFit</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/footprintSpatialFit">http://rs.tdwg.org/dwc/terms/footprintSpatialFit</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/footprintSpatialFit-2020-08-20">http://rs.tdwg.org/dwc/terms/version/footprintSpatialFit-2020-08-20</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Footprint Spatial Fit</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The ratio of the area of the footprint (footprintWKT) to the area of the true (original, or most specific) spatial representation of the Location. Legal values are 0, greater than or equal to 1, or undefined. A value of 1 is an exact match or 100% overlap. A value of 0 should be used if the given footprint does not completely contain the original representation. The footprintSpatialFit is undefined (and should be left empty) if the original representation is a point without uncertainty and the given georeference is not that same point (without uncertainty). If both the original and the given georeference are the same point, the footprintSpatialFit is 1.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Detailed explanations with graphical examples can be found in the Georeferencing Best Practices, Chapman and Wieczorek, 2020 (<a href="https://doi.org/10.15468/doc-gg7h-s853">https://doi.org/10.15468/doc-gg7h-s853</a>).</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>0</code>, <code>1</code>, <code>1.5708</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_footprintSRS"></a>Term Name: dwc:footprintSRS</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/footprintSRS">http://rs.tdwg.org/dwc/terms/footprintSRS</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Footprint SRS</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A Well-Known Text (WKT) representation of the Spatial Reference System (SRS) for the footprintWKT of the Location. Do not use this term to describe the SRS of the decimalLatitude and decimalLongitude, even if it is the same as for the footprintWKT - use the geodeticDatum instead.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>GEOGCS["GCS_WGS_1984", DATUM["D_WGS_1984", SPHEROID["WGS_1984",6378137,298.257223563]], PRIMEM["Greenwich",0], UNIT["Degree",0.0174532925199433]]</code> (WKT for the standard WGS84 Spatial Reference System EPSG:4326).</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_footprintWKT"></a>Term Name: dwc:footprintWKT</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/footprintWKT">http://rs.tdwg.org/dwc/terms/footprintWKT</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/footprintWKT-2017-10-06">http://rs.tdwg.org/dwc/terms/version/footprintWKT-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Footprint WKT</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A Well-Known Text (WKT) representation of the shape (footprint, geometry) that defines the Location. A Location may have both a point-radius representation (see decimalLatitude) and a footprint representation, and they may differ from each other.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>POLYGON ((10 20, 11 20, 11 21, 10 21, 10 20))</code> (the one-degree bounding box with opposite corners at longitude=10, latitude=20 and longitude=11, latitude=21)</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_geodeticDatum"></a>Term Name: dwc:geodeticDatum</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/geodeticDatum">http://rs.tdwg.org/dwc/terms/geodeticDatum</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/geodeticDatum-2017-10-06">http://rs.tdwg.org/dwc/terms/version/geodeticDatum-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Geodetic Datum</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The ellipsoid, geodetic datum, or spatial reference system (SRS) upon which the geographic coordinates given in decimalLatitude and decimalLongitude as based.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use the EPSG code of the SRS, if known. Otherwise use a controlled vocabulary for the name or code of the geodetic datum, if known. Otherwise use a controlled vocabulary for the name or code of the ellipsoid, if known. If none of these is known, use the value <code>unknown</code>.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>EPSG:4326</code>, <code>WGS84</code>, <code>NAD27</code>, <code>Campo Inchauspe</code>, <code>European 1950</code>, <code>Clarke 1866</code>, <code>unknown</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_georeferencedBy"></a>Term Name: dwc:georeferencedBy</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/georeferencedBy">http://rs.tdwg.org/dwc/terms/georeferencedBy</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/georeferencedBy-2017-10-06">http://rs.tdwg.org/dwc/terms/version/georeferencedBy-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Georeferenced By</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A list (concatenated and separated) of names of people, groups, or organizations who determined the georeference (spatial representation) for the Location.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to separate the values in a list with space vertical bar space (<code> | </code>).</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>Brad Millen (ROM)</code>, <code>Kristina Yamamoto | Janet Fang</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_georeferenceProtocol"></a>Term Name: dwc:georeferenceProtocol</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/georeferenceProtocol">http://rs.tdwg.org/dwc/terms/georeferenceProtocol</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/georeferenceProtocol-2020-08-20">http://rs.tdwg.org/dwc/terms/version/georeferenceProtocol-2020-08-20</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Georeference Protocol</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A description or reference to the methods used to determine the spatial footprint, coordinates, and uncertainties.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>Georeferencing Quick Reference Guide (Zermoglio et al. 2020, <a href="https://doi.org/10.35035/e09p-h128">https://doi.org/10.35035/e09p-h128</a>)</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_georeferenceRemarks"></a>Term Name: dwc:georeferenceRemarks</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/georeferenceRemarks">http://rs.tdwg.org/dwc/terms/georeferenceRemarks</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/georeferenceRemarks-2017-10-06">http://rs.tdwg.org/dwc/terms/version/georeferenceRemarks-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Georeference Remarks</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Notes or comments about the spatial description determination, explaining assumptions made in addition or opposition to the those formalized in the method referred to in georeferenceProtocol.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>Assumed distance by road (Hwy. 101)</code>.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_georeferenceSources"></a>Term Name: dwc:georeferenceSources</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/georeferenceSources">http://rs.tdwg.org/dwc/terms/georeferenceSources</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-10-28</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/georeferenceSources-2020-10-28">http://rs.tdwg.org/dwc/terms/version/georeferenceSources-2020-10-28</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Georeference Sources</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A list (concatenated and separated) of maps, gazetteers, or other resources used to georeference the Location, described specifically enough to allow anyone in the future to use the same resources.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to separate the values in a list with space vertical bar space (<code> | </code>).</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code><a href="https://www.geonames.org/">https://www.geonames.org/</a></code>, <code>USGS 1:24000 Florence Montana Quad 1967 | Terrametrics 2008 on Google Earth</code>, <code>GeoLocate</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_georeferenceVerificationStatus"></a>Term Name: dwc:georeferenceVerificationStatus</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/georeferenceVerificationStatus">http://rs.tdwg.org/dwc/terms/georeferenceVerificationStatus</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/georeferenceVerificationStatus-2017-10-06">http://rs.tdwg.org/dwc/terms/version/georeferenceVerificationStatus-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Georeference Verification Status</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A categorical description of the extent to which the georeference has been verified to represent the best possible spatial description.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>requires verification</code>, <code>verified by collector</code>, <code>verified by curator</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_higherGeography"></a>Term Name: dwc:higherGeography</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/higherGeography">http://rs.tdwg.org/dwc/terms/higherGeography</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/higherGeography-2017-10-06">http://rs.tdwg.org/dwc/terms/version/higherGeography-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Higher Geography</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A list (concatenated and separated) of geographic names less specific than the information captured in the locality term.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to separate the values in a list with space vertical bar space (<code> | </code>), with terms in order from least specific to most specific.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>North Atlantic Ocean</code>. <code>South America | Argentina | Patagonia | Parque Nacional Nahuel Huapi | Neuquén | Los Lagos</code> (with accompanying values <code>South America</code> in continent, <code>Argentina</code> in country, <code>Neuquén</code> in stateProvince, and <code>Los Lagos</code> in county.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_higherGeographyID"></a>Term Name: dwc:higherGeographyID</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/higherGeographyID">http://rs.tdwg.org/dwc/terms/higherGeographyID</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/higherGeographyID-2017-10-06">http://rs.tdwg.org/dwc/terms/version/higherGeographyID-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Higher Geography ID</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An identifier for the geographic region within which the Location occurred.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a persistent identifier from a controlled vocabulary such as the Getty Thesaurus of Geographic Names.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code><a href="http://vocab.getty.edu/tgn/1002002">http://vocab.getty.edu/tgn/1002002</a></code> (Antártida e Islas del Atlántico Sur, Territorio Nacional de la Tierra del Fuego, Argentina).</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_island"></a>Term Name: dwc:island</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/island">http://rs.tdwg.org/dwc/terms/island</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/island-2017-10-06">http://rs.tdwg.org/dwc/terms/version/island-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Island</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The name of the island on or near which the Location occurs.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>Nosy Be</code>, <code>Bikini Atoll</code>, <code>Vancouver</code>, <code>Viti Levu</code>, <code>Zanzibar</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_islandGroup"></a>Term Name: dwc:islandGroup</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/islandGroup">http://rs.tdwg.org/dwc/terms/islandGroup</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/islandGroup-2017-10-06">http://rs.tdwg.org/dwc/terms/version/islandGroup-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Island Group</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The name of the island group in which the Location occurs.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>Alexander Archipelago</code>, <code>Archipiélago Diego Ramírez</code>, <code>Seychelles</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_locality"></a>Term Name: dwc:locality</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/locality">http://rs.tdwg.org/dwc/terms/locality</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/locality-2017-10-06">http://rs.tdwg.org/dwc/terms/version/locality-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Locality</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The specific description of the place. Less specific geographic information can be provided in other geographic terms (higherGeography, continent, country, stateProvince, county, municipality, waterBody, island, islandGroup). This term may contain information modified from the original to correct perceived errors or standardize the description.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>Bariloche, 25 km NNE via Ruta Nacional 40 (=Ruta 237)</code>.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_locationAccordingTo"></a>Term Name: dwc:locationAccordingTo</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/locationAccordingTo">http://rs.tdwg.org/dwc/terms/locationAccordingTo</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/locationAccordingTo-2017-10-06">http://rs.tdwg.org/dwc/terms/version/locationAccordingTo-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Location According To</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Information about the source of this Location information. Could be a publication (gazetteer), institution, or team of individuals.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>Getty Thesaurus of Geographic Names</code>, <code>GADM</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_locationID"></a>Term Name: dwc:locationID</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/locationID">http://rs.tdwg.org/dwc/terms/locationID</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/locationID-2017-10-06">http://rs.tdwg.org/dwc/terms/version/locationID-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Location ID</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An identifier for the set of location information (data associated with dcterms:Location). May be a global unique identifier or an identifier specific to the data set.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code><a href="https://opencontext.org/subjects/768A875F-E205-4D0B-DE55-BAB7598D0FD1">https://opencontext.org/subjects/768A875F-E205-4D0B-DE55-BAB7598D0FD1</a></code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_locationRemarks"></a>Term Name: dwc:locationRemarks</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/locationRemarks">http://rs.tdwg.org/dwc/terms/locationRemarks</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/locationRemarks-2017-10-06">http://rs.tdwg.org/dwc/terms/version/locationRemarks-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Location Remarks</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Comments or notes about the Location.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>under water since 2005</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="Iptc4xmpExt_LocationShown"></a>Term Name: Iptc4xmpExt:LocationShown</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://iptc.org/std/Iptc4xmpExt/2008-02-29/LocationShown">http://iptc.org/std/Iptc4xmpExt/2008-02-29/LocationShown</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Location Shown</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A location the content of the item is about. For photos that is a location shown in the image.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The location that is depicted the media content, irrespective of the location at which the resource has been created.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_maximumDepthInMeters"></a>Term Name: dwc:maximumDepthInMeters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/maximumDepthInMeters">http://rs.tdwg.org/dwc/terms/maximumDepthInMeters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/maximumDepthInMeters-2017-10-06">http://rs.tdwg.org/dwc/terms/version/maximumDepthInMeters-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Maximum Depth In Meters</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The greater depth of a range of depth below the local surface, in meters.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>0</code>, <code>200</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_maximumDistanceAboveSurfaceInMeters"></a>Term Name: dwc:maximumDistanceAboveSurfaceInMeters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/maximumDistanceAboveSurfaceInMeters">http://rs.tdwg.org/dwc/terms/maximumDistanceAboveSurfaceInMeters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/maximumDistanceAboveSurfaceInMeters-2017-10-06">http://rs.tdwg.org/dwc/terms/version/maximumDistanceAboveSurfaceInMeters-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Maximum Distance Above Surface In Meters</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The greater distance in a range of distance from a reference surface in the vertical direction, in meters. Use positive values for locations above the surface, negative values for locations below. If depth measures are given, the reference surface is the location given by the depth, otherwise the reference surface is the location given by the elevation.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>-1.5</code> (below the surface). <code>4.2</code> (above the surface). For a 1.5 meter sediment core from the bottom of a lake (at depth 20m) at 300m elevation: verbatimElevation: <code>300m</code> minimumElevationInMeters: <code>300</code>, maximumElevationInMeters: <code>300</code>, verbatimDepth: <code>20m</code>, minimumDepthInMeters: <code>20</code>, maximumDepthInMeters: <code>20</code>, minimumDistanceAboveSurfaceInMeters: <code>0</code>, maximumDistanceAboveSurfaceInMeters: <code>-1.5</code>.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_maximumElevationInMeters"></a>Term Name: dwc:maximumElevationInMeters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/maximumElevationInMeters">http://rs.tdwg.org/dwc/terms/maximumElevationInMeters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/maximumElevationInMeters-2017-10-06">http://rs.tdwg.org/dwc/terms/version/maximumElevationInMeters-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Maximum Elevation In Meters</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The upper limit of the range of elevation (altitude, usually above sea level), in meters.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>-205</code>, <code>1236</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_minimumDepthInMeters"></a>Term Name: dwc:minimumDepthInMeters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/minimumDepthInMeters">http://rs.tdwg.org/dwc/terms/minimumDepthInMeters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/minimumDepthInMeters-2017-10-06">http://rs.tdwg.org/dwc/terms/version/minimumDepthInMeters-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Minimum Depth In Meters</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The lesser depth of a range of depth below the local surface, in meters.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>0</code>, <code>100</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_minimumDistanceAboveSurfaceInMeters"></a>Term Name: dwc:minimumDistanceAboveSurfaceInMeters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/minimumDistanceAboveSurfaceInMeters">http://rs.tdwg.org/dwc/terms/minimumDistanceAboveSurfaceInMeters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/minimumDistanceAboveSurfaceInMeters-2017-10-06">http://rs.tdwg.org/dwc/terms/version/minimumDistanceAboveSurfaceInMeters-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Minimum Distance Above Surface In Meters</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The lesser distance in a range of distance from a reference surface in the vertical direction, in meters. Use positive values for locations above the surface, negative values for locations below. If depth measures are given, the reference surface is the location given by the depth, otherwise the reference surface is the location given by the elevation.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>-1.5</code> (below the surface). <code>4.2</code> (above the surface). For a 1.5 meter sediment core from the bottom of a lake (at depth 20m) at 300m elevation: verbatimElevation: <code>300m</code> minimumElevationInMeters: <code>300</code>, maximumElevationInMeters: <code>300</code>, verbatimDepth: <code>20m</code>, minimumDepthInMeters: <code>20</code>, maximumDepthInMeters: <code>20</code>, minimumDistanceAboveSurfaceInMeters: <code>0</code>, maximumDistanceAboveSurfaceInMeters: <code>-1.5</code>.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_minimumElevationInMeters"></a>Term Name: dwc:minimumElevationInMeters</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/minimumElevationInMeters">http://rs.tdwg.org/dwc/terms/minimumElevationInMeters</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/minimumElevationInMeters-2017-10-06">http://rs.tdwg.org/dwc/terms/version/minimumElevationInMeters-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Minimum Elevation In Meters</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The lower limit of the range of elevation (altitude, usually above sea level), in meters.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>-100</code>, <code>802</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_municipality"></a>Term Name: dwc:municipality</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/municipality">http://rs.tdwg.org/dwc/terms/municipality</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/municipality-2017-10-06">http://rs.tdwg.org/dwc/terms/version/municipality-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Municipality</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The full, unabbreviated name of the next smaller administrative region than county (city, municipality, etc.) in which the Location occurs. Do not use this term for a nearby named place that does not contain the actual location.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>Holzminden</code>, <code>Araçatuba</code>, <code>Ga-Segonyana</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_pointRadiusSpatialFit"></a>Term Name: dwc:pointRadiusSpatialFit</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/pointRadiusSpatialFit">http://rs.tdwg.org/dwc/terms/pointRadiusSpatialFit</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/pointRadiusSpatialFit-2020-08-20">http://rs.tdwg.org/dwc/terms/version/pointRadiusSpatialFit-2020-08-20</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Point Radius Spatial Fit</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The ratio of the area of the point-radius (decimalLatitude, decimalLongitude, coordinateUncertaintyInMeters) to the area of the true (original, or most specific) spatial representation of the Location. Legal values are 0, greater than or equal to 1, or undefined. A value of 1 is an exact match or 100% overlap. A value of 0 should be used if the given point-radius does not completely contain the original representation. The pointRadiusSpatialFit is undefined (and should be left empty) if the original representation is a point without uncertainty and the given georeference is not that same point (without uncertainty). If both the original and the given georeference are the same point, the pointRadiusSpatialFit is 1.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Detailed explanations with graphical examples can be found in the Georeferencing Best Practices, Chapman and Wieczorek, 2020 (<a href="https://doi.org/10.15468/doc-gg7h-s853">https://doi.org/10.15468/doc-gg7h-s853</a>).</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>0</code>, <code>1</code>, <code>1.5708</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="Iptc4xmpExt_ProvinceState"></a>Term Name: Iptc4xmpExt:ProvinceState</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://iptc.org/std/Iptc4xmpExt/2008-02-29/ProvinceState">http://iptc.org/std/Iptc4xmpExt/2008-02-29/ProvinceState</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Province or State</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The name of a subregion of a country - a province or state - of a location. This element is at the third level of a top-down geographical hierarchy.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>OPTIONALLY, the geographic unit immediately below the country level (individual states in federal countries, provinces, or other administrative units) in which the subject of the media resource (e. g., species, habitats, or events) were located (if such information is available in separate fields).</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_stateProvince"></a>Term Name: dwc:stateProvince</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/stateProvince">http://rs.tdwg.org/dwc/terms/stateProvince</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/stateProvince-2017-10-06">http://rs.tdwg.org/dwc/terms/version/stateProvince-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>State Province</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The name of the next smaller administrative region than country (state, province, canton, department, region, etc.) in which the Location occurs.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>Montana</code>, <code>Minas Gerais</code>, <code>Córdoba</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="Iptc4xmpExt_Sublocation"></a>Term Name: Iptc4xmpExt:Sublocation</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://iptc.org/std/Iptc4xmpExt/2008-02-29/Sublocation">http://iptc.org/std/Iptc4xmpExt/2008-02-29/Sublocation</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Sublocation</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Name of a sublocation. This sublocation name could either be the name of a sublocation to a city or the name of a well known location or (natural) monument outside a city. In the sense of a sublocation to a city this element is at the fifth level of a top-down geographical hierarchy.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Free-form text location details of the location of the subjects, down to the village, forest, or geographic feature etc., below the Iptc4xmpExt:City place name, especially information that could not be found in a gazetteer.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_verbatimCoordinates"></a>Term Name: dwc:verbatimCoordinates</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/verbatimCoordinates">http://rs.tdwg.org/dwc/terms/verbatimCoordinates</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/verbatimCoordinates-2017-10-06">http://rs.tdwg.org/dwc/terms/version/verbatimCoordinates-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Verbatim Coordinates</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The verbatim original spatial coordinates of the Location. The coordinate ellipsoid, geodeticDatum, or full Spatial Reference System (SRS) for these coordinates should be stored in verbatimSRS and the coordinate system should be stored in verbatimCoordinateSystem.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>41 05 54S 121 05 34W</code>, <code>17T 630000 4833400</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_verbatimCoordinateSystem"></a>Term Name: dwc:verbatimCoordinateSystem</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/verbatimCoordinateSystem">http://rs.tdwg.org/dwc/terms/verbatimCoordinateSystem</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/verbatimCoordinateSystem-2020-08-20">http://rs.tdwg.org/dwc/terms/version/verbatimCoordinateSystem-2020-08-20</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Verbatim Coordinate System</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The coordinate format for the verbatimLatitude and verbatimLongitude or the verbatimCoordinates of the Location.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>decimal degrees</code>, <code>degrees decimal minutes</code>, <code>degrees minutes seconds</code>, <code>UTM</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_verbatimDepth"></a>Term Name: dwc:verbatimDepth</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/verbatimDepth">http://rs.tdwg.org/dwc/terms/verbatimDepth</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/verbatimDepth-2017-10-06">http://rs.tdwg.org/dwc/terms/version/verbatimDepth-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Verbatim Depth</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The original description of the depth below the local surface.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>100-200 m</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_verbatimElevation"></a>Term Name: dwc:verbatimElevation</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/verbatimElevation">http://rs.tdwg.org/dwc/terms/verbatimElevation</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/verbatimElevation-2017-10-06">http://rs.tdwg.org/dwc/terms/version/verbatimElevation-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Verbatim Elevation</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The original description of the elevation (altitude, usually above sea level) of the Location.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>100-200 m</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_verbatimLatitude"></a>Term Name: dwc:verbatimLatitude</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/verbatimLatitude">http://rs.tdwg.org/dwc/terms/verbatimLatitude</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/verbatimLatitude-2017-10-06">http://rs.tdwg.org/dwc/terms/version/verbatimLatitude-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Verbatim Latitude</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The verbatim original latitude of the Location. The coordinate ellipsoid, geodeticDatum, or full Spatial Reference System (SRS) for these coordinates should be stored in verbatimSRS and the coordinate system should be stored in verbatimCoordinateSystem.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>41 05 54.03S</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_verbatimLocality"></a>Term Name: dwc:verbatimLocality</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/verbatimLocality">http://rs.tdwg.org/dwc/terms/verbatimLocality</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/verbatimLocality-2017-10-06">http://rs.tdwg.org/dwc/terms/version/verbatimLocality-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Verbatim Locality</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The original textual description of the place.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>25 km NNE Bariloche por R. Nac. 237</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_verbatimLongitude"></a>Term Name: dwc:verbatimLongitude</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/verbatimLongitude">http://rs.tdwg.org/dwc/terms/verbatimLongitude</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/verbatimLongitude-2017-10-06">http://rs.tdwg.org/dwc/terms/version/verbatimLongitude-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Verbatim Longitude</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The verbatim original longitude of the Location. The coordinate ellipsoid, geodeticDatum, or full Spatial Reference System (SRS) for these coordinates should be stored in verbatimSRS and the coordinate system should be stored in verbatimCoordinateSystem.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>121d 10' 34" W</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_verbatimSRS"></a>Term Name: dwc:verbatimSRS</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/verbatimSRS">http://rs.tdwg.org/dwc/terms/verbatimSRS</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/verbatimSRS-2017-10-06">http://rs.tdwg.org/dwc/terms/version/verbatimSRS-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Verbatim SRS</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The ellipsoid, geodetic datum, or spatial reference system (SRS) upon which coordinates given in verbatimLatitude and verbatimLongitude, or verbatimCoordinates are based.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use the EPSG code of the SRS, if known. Otherwise use a controlled vocabulary for the name or code of the geodetic datum, if known. Otherwise use a controlled vocabulary for the name or code of the ellipsoid, if known. If none of these is known, use the value <code>unknown</code>.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>unknown</code>, <code>EPSG:4326</code>, <code>WGS84</code>, <code>NAD27</code>, <code>Campo Inchauspe</code>, <code>European 1950</code>, <code>Clarke 1866</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_waterBody"></a>Term Name: dwc:waterBody</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/waterBody">http://rs.tdwg.org/dwc/terms/waterBody</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/waterBody-2017-10-06">http://rs.tdwg.org/dwc/terms/version/waterBody-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Water Body</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The name of the water body in which the Location occurs. Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>Indian Ocean</code>, <code>Baltic Sea</code>, <code>Hudson River</code>, <code>Lago Nahuel Huapi</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="Iptc4xmpExt_WorldRegion"></a>Term Name: Iptc4xmpExt:WorldRegion</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://iptc.org/std/Iptc4xmpExt/2008-02-29/WorldRegion">http://iptc.org/std/Iptc4xmpExt/2008-02-29/WorldRegion</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>World Region</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The name of a world region of a location. This element is at the first (topI) level of a topdown geographical hierarchy.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Name of a world region in some high level classification, such as names for continents, waterbodies, or island groups, whichever is most appropriate. The terms preferably are derived from a controlled vocabulary.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The equivalent DarwinCore fields here forces primary metadata providers to classify world region terms into separate properties for "continent", "waterbody", "islandGroup". By contrast, the Iptc4xmpExt vocabulary only specifies that a World Region is something at the top of a hierarchy of locations.</td>
		</tr>
	</tbody>
</table>


### 7.6 Temporal Coverage Vocabulary

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="xmp_CreateDate"></a>Term Name: xmp:CreateDate</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://ns.adobe.com/xap/1.0/CreateDate">http://ns.adobe.com/xap/1.0/CreateDate</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Original Date and Time</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The date and time the resource was created. For a digital file, this need not match a file-system creation time.  For a freshly created resource, it should be close to that time, modulo the time taken to write the file.  Later file transfer, copying, and so on, can make the file-system time arbitrarily different.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The date of the creation of the original resource from which the digital media was derived or created. The date and time MUST comply with the World Wide Web Consortium (W3C) datetime practice, <a href="https://www.w3.org/TR/NOTE-datetime">https://www.w3.org/TR/NOTE-datetime</a>, which requires that date and time representation correspond to ISO 8601:1998, but with year fields always comprising 4 digits. This makes datetime records compliant with 8601:2004, <a href="https://www.iso.org/standard/40874.html">https://www.iso.org/standard/40874.html</a>. AC datetime values MAY also follow 8601:2004 for ranges by separating two IS0 8601 datetime fields by a solidus ("forward slash", '/'). When applied to a media resource with temporal extent such as audio or video, this property indicates the startTime of the recording.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>What constitutes "original" is determined by the metadata author. Example: Digitization of a photographic slide of a map would normally give the date at which the map was created; however a photographic work of art including the same map as its content may give the date of the original photographic exposure. Imprecise or unknown dates can be represented as ISO dates or ranges. Compare also Date and Time Digitized in the Resource Creation Vocabulary. See also the wikipedia IS0 8601 entry, <a href="https://en.wikipedia.org/wiki/ISO_8601">https://en.wikipedia.org/wiki/ISO_8601</a>, for further explanation and examples.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dcterms_temporal"></a>Term Name: dcterms:temporal</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://purl.org/dc/terms/temporal">http://purl.org/dc/terms/temporal</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://dublincore.org/usage/terms/history/#temporal-003">http://dublincore.org/usage/terms/history/#temporal-003</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Temporal Coverage</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Temporal characteristics of the resource. </td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The coverage (extent or scope) of the content of the resource. Temporal coverage will typically include temporal period (a period label, date, or date range) to which the subjects of the media or media collection relate. If dates are mentioned, they SHOULD follow ISO 8601. When the resource is a Collection, this refers to the temporal coverage of the collection. Following dcterms:temporal, the value MUST be a URI.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>See the DCMI User Guide dcterms:temporal entry, <a href="https://github.com/dcmi/repository/blob/master/mediawiki_wiki/User_Guide/Publishing_Metadata.md#dctermstemporal">https://github.com/dcmi/repository/blob/master/mediawiki_wiki/User_Guide/Publishing_Metadata.md#dctermstemporal</a>, for an example. dc:coverage may be used for string values of temporal coverage, but use the Geography Vocabulary for geographic coverage. String examples for use with dc:coverage include "Jurassic", "Elizabethan", "Spring, 1957". 2008-01-01/2008-06-30. If the resource is video or audio, it refers to the time span, if any, depicted by the resource. For live-media this is closely related to Original Date and Time (Example: the time depicted by a time-lapse video file of organism development), but for media with fictional content it is not.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_timeOfDay"></a>Term Name: ac:timeOfDay</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/timeOfDay">http://rs.tdwg.org/ac/terms/timeOfDay</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/timeOfDay-2020-01-27">http://rs.tdwg.org/ac/terms/version/timeOfDay-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Time of Day</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Free text information beyond exact clock times.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Examples in English: afternoon, twilight.</td>
		</tr>
	</tbody>
</table>


### 7.7 Taxonomic Coverage Vocabulary

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_dateIdentified"></a>Term Name: dwc:dateIdentified</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/dateIdentified">http://rs.tdwg.org/dwc/terms/dateIdentified</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/dateIdentified-2020-08-12">http://rs.tdwg.org/dwc/terms/version/dateIdentified-2020-08-12</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Date Identified</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The date on which the subject was determined as representing the Taxon.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The date on which the person(s) given under Identified By applied a Scientific Taxon Name to the resource.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a date that conforms to ISO 8601-1:2019.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>1963-03-08T14:07-0600</code> (8 Mar 1963 at 2:07pm in the time zone six hours earlier than UTC). <code>2009-02-20T08:40Z</code> (20 February 2009 8:40am UTC). <code>2018-08-29T15:19</code> (3:19pm local time on 29 August 2018). <code>1809-02-12</code> (some time during 12 February 1809). <code>1906-06</code> (some time in June 1906). <code>1971</code> (some time in the year 1971). <code>2007-03-01T13:00:00Z/2008-05-11T15:30:00Z</code> (some time during the interval between 1 March 2007 1pm UTC and 11 May 2008 3:30pm UTC). <code>1900/1909</code> (some time during the interval between the beginning of the year 1900 and the end of the year 1909). <code>2007-11-13/15</code> (some time in the interval between 13 November 2007 and 15 November 2007).</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_identificationQualifier"></a>Term Name: dwc:identificationQualifier</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/identificationQualifier">http://rs.tdwg.org/dwc/terms/identificationQualifier</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/identificationQualifier-2017-10-06">http://rs.tdwg.org/dwc/terms/version/identificationQualifier-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Identification Qualifier</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A brief phrase or a standard term ("cf.", "aff.") to express the determiner's doubts about the Identification.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>A brief phrase or a standard abbreviation ("cf. genus", "cf. species", "cf. var.", "aff. species", etc.) to express the determiner's doubts with respect to a specified taxonomic rank about the identification given in Scientific Taxon Name.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Splitting identification qualification and Scientific Taxon Name into separate fields is recommended practice in cases where only a single taxon name is available, or if the exchange format is able to keep relations between multiple names and identification qualifiers. Where the exchange format only supports simple multiplicities, a media item with multiple Scientific Taxon Names, some with, some without identification qualifiers, may have to be transferred with "cf." or "aff." qualifiers remaining embedded in the Scientific Taxon Name. Example: For the determinations "cf. Fusarium oxysporum f. sp. palmarum", "Fusarium cf. oxysporum f. sp. palmarum", "Fusarium oxysporum cf. f. sp. palmarum" the Scientific Taxon Name would always be "Fusarium oxysporum f. sp. palmarum", with Identification Qualifier "cf. genus", "cf. species" and "cf. f.sp.", respectively. In most cases only the lowest taxon is in doubt, but cases exist where good reasons exist to suspect a specific or even infraspecific determination, without having a save generic identification.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>aff. agrifolia var. oxyadenia</code> (for <code>Quercus aff. agrifolia var. oxyadenia</code> with accompanying values <code>Quercus</code> in genus, <code>agrifolia</code>  in specificEpithet, <code>oxyadenia</code>  in infraspecificEpithet, and <code>var.</code> in taxonRank. <code>cf. var. oxyadenia</code> for <code>Quercus agrifolia cf. var. oxyadenia</code> with accompanying values <code>Quercus</code> in genus, <code>agrifolia</code> in specificEpithet, <code>oxyadenia</code> in infraspecificEpithet, and <code>var.</code> in taxonRank.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_identifiedBy"></a>Term Name: dwc:identifiedBy</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/identifiedBy">http://rs.tdwg.org/dwc/terms/identifiedBy</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/identifiedBy-2017-10-06">http://rs.tdwg.org/dwc/terms/version/identifiedBy-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Identified By</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A list (concatenated and separated) of names of people, groups, or organizations who assigned the Taxon to the subject.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The name(s) of the person(s) who applied the Scientific Taxon Name to the media item or the occurrence represented in the media item.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to separate the values in a list with space vertical bar space (<code> | </code>).</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>James L. Patton</code>, <code>Theodore Pappenfuss | Robert Macey</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_lifeStage"></a>Term Name: dwc:lifeStage</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/lifeStage">http://rs.tdwg.org/dwc/terms/lifeStage</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/lifeStage-2017-10-06">http://rs.tdwg.org/dwc/terms/version/lifeStage-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Subject Life Stage</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The age class or life stage of the biological individual(s) at the time the Occurrence was recorded.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>A description of the life-cycle stage of any organisms featured within the media, when relevant to the subject of the media, e. g., larvae, juvenile, adult.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>egg</code>, <code>eft</code>, <code>juvenile</code>, <code>adult</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_nameAccordingTo"></a>Term Name: dwc:nameAccordingTo</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/nameAccordingTo">http://rs.tdwg.org/dwc/terms/nameAccordingTo</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/nameAccordingTo-2017-10-06">http://rs.tdwg.org/dwc/terms/version/nameAccordingTo-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Name According To</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The reference to the source in which the specific taxon concept circumscription is defined or implied - traditionally signified by the Latin "sensu" or "sec." (from secundum, meaning "according to"). For taxa that result from identifications, a reference to the keys, monographs, experts and other sources should be given.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The taxonomic authority used to apply the name to the taxon, e. g., a person, book or web service.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Examples are "Flora of North America", "Landrum 1981, Monograph of the Genus Myrceugenia (Myrtaceae)", "Peterson Field Guide to Birds of North America", or "Expert identification by J.Smith".</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>McCranie, J. R., D. B. Wake, and L. D. Wilson. 1996. The taxonomic status of Bolitoglossa schmidti, with comments on the biology of the Mesoamerican salamander Bolitoglossa dofleini (Caudata: Plethodontidae). Carib. J. Sci. 32:395-398.</code>, <code>Werner Greuter 2008</code>. <code>Lilljeborg 1861, Upsala Univ. Arsskrift, Math. Naturvet., pp. 4, 5</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_otherScientificName"></a>Term Name: ac:otherScientificName</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/otherScientificName">http://rs.tdwg.org/ac/terms/otherScientificName</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/otherScientificName-2020-01-27">http://rs.tdwg.org/ac/terms/version/otherScientificName-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Other Scientific Name</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>One or several Scientific Taxon Names that are synonyms to the Scientific Taxon Name may be provided here.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The primary purpose of this is in support of resource discovery, not developing a taxonomic synonymy. Misidentification or misspellings may thus be of interest. Where multiple taxa are present in a resource and multiple Scientific Taxon Names are given, the association between synonyms and names may not be deducible from the AC record alone.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_preparations"></a>Term Name: dwc:preparations</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/preparations">http://rs.tdwg.org/dwc/terms/preparations</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/preparations-2017-10-06">http://rs.tdwg.org/dwc/terms/version/preparations-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Subject Preparation Technique</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A list (concatenated and separated) of preparations and preservation methods for a specimen.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Free form text describing the techniques used to prepare the subject of the media, prior to or while creating the media resource.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Examples for such techniques are: Insect under CO2, cooled to immobility, preservation with ethanol or formaldehyde. See also Resource Creation Technique for technical aspects of digital media object creation.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_scientificName"></a>Term Name: dwc:scientificName</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/scientificName">http://rs.tdwg.org/dwc/terms/scientificName</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/scientificName-2017-10-06">http://rs.tdwg.org/dwc/terms/version/scientificName-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Scientific Taxon Name</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The full scientific name, with authorship and date information if known. When forming part of an Identification, this should be the name in lowest level taxonomic rank that can be determined. This term should not contain identification qualifications, which should instead be supplied in the IdentificationQualifier term.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Scientific names of taxa represented in the media resource (with date and name authorship information if available) of the lowest level taxonomic rank that can be applied.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The Scientific Taxon Name may possibly be of a higher rank, e.g., a genus or family name, if this is the most specific identification available. Where multiple taxa are the subject of the media item, multiple names may be given. If possible, add this information here even if the title or caption of the resource already contains scientific taxon names. Where the list of scientific taxon names is impractically large (e.g., media collections or identification tools), the number of taxa should be given in Taxon Count (see below). If possible, avoid repeating the Taxonomic Coverage here. Do not use abbreviated Genus names ("P. vulgaris"). It is recommended to provide author citation to scientific names, to avoid ambiguities in the presence of homonyms (the same name created by different authors for different taxa). Identifier qualifications should be supplied in the Identification Qualifier term rather than here (i. e. "Abies cf. alba" is deprecated, to be replaced with Scientific Taxon Name = "Abies alba" and Identification Qualifier = "cf. species").</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>Coleoptera</code> (order). <code>Vespertilionidae</code> (family). <code>Manis</code> (genus). <code>Ctenomys sociabilis</code> (genus + specificEpithet). <code>Ambystoma tigrinum diaboli</code> (genus + specificEpithet + infraspecificEpithet). <code>Roptrocerus typographi (Györfi, 1952)</code> (genus + specificEpithet + scientificNameAuthorship), <code>Quercus agrifolia var. oxyadenia (Torr.) J.T. Howell</code> (genus + specificEpithet + taxonRank + infraspecificEpithet + scientificNameAuthorship).</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_scientificNameID"></a>Term Name: dwc:scientificNameID</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/scientificNameID">http://rs.tdwg.org/dwc/terms/scientificNameID</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/scientificNameID-2017-10-06">http://rs.tdwg.org/dwc/terms/version/scientificNameID-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Scientific Name ID</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An identifier for the nomenclatural (not taxonomic) details of a scientific name.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>See dwc:scientificName.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>urn:lsid:ipni.org:names:37829-1:1.3</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_sex"></a>Term Name: dwc:sex</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/sex">http://rs.tdwg.org/dwc/terms/sex</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/sex-2017-10-06">http://rs.tdwg.org/dwc/terms/version/sex-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Subject Sex</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The sex of the biological individual(s) represented in the Occurrence.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>A description of the sex of any organisms featured within the media, when relevant to the subject of the media, e. g., male, female, hermaphrodite, dioecious.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended best practice is to use a controlled vocabulary.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>female</code>, <code>male</code>, <code>hermaphrodite</code></td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_subjectOrientation"></a>Term Name: ac:subjectOrientation</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/subjectOrientation">http://rs.tdwg.org/ac/terms/subjectOrientation</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/subjectOrientation-2023-09-05">http://rs.tdwg.org/ac/terms/version/subjectOrientation-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Subject Orientation</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Specific orientation (= direction, view angle) of the subject represented in the media resource with respect to the acquisition device, denoted by an IRI.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Values SHOULD be selected from the Controlled Vocabulary for Audiovisual Core subjectOrientation. In text-based systems such as tables, IRI values MUST be in unabbreviated form.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_subjectOrientationLiteral"></a>Term Name: ac:subjectOrientationLiteral</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/subjectOrientationLiteral">http://rs.tdwg.org/ac/terms/subjectOrientationLiteral</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/subjectOrientationLiteral-2023-09-05">http://rs.tdwg.org/ac/terms/version/subjectOrientationLiteral-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Subject Orientation (literal)</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Specific orientation (= direction, view angle) of the subject represented in the media resource with respect to the acquisition device, denoted by a controlled value string.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Values SHOULD be selected from the Controlled Vocabulary for Audiovisual Core subjectOrientation. It is best practice to use ac:subjectOrientation instead of ac:subjectOrientationLiteral whenever practical.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_subjectPart"></a>Term Name: ac:subjectPart</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/subjectPart">http://rs.tdwg.org/ac/terms/subjectPart</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/subjectPart-2023-09-05">http://rs.tdwg.org/ac/terms/version/subjectPart-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Subject Part</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The portion or product of organism morphology, behaviour, environment, etc. that is either predominantly shown or particularly well exemplified by the media resource, denoted by an IRI.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Values SHOULD be selected from the Controlled Vocabulary for Audiovisual Core subjectPart. In text-based systems such as tables, IRI values MUST be in unabbreviated form.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_subjectPartLiteral"></a>Term Name: ac:subjectPartLiteral</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/subjectPartLiteral">http://rs.tdwg.org/ac/terms/subjectPartLiteral</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/subjectPartLiteral-2023-09-05">http://rs.tdwg.org/ac/terms/version/subjectPartLiteral-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Subject Part (literal)</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The portion or product of organism morphology, behaviour, environment, etc. that is either predominantly shown or particularly well exemplified by the media resource, denoted by a controlled value string.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Values SHOULD be selected from the Controlled Vocabulary for Audiovisual Core subjectPart. It is best practice to use ac:subjectPart instead of ac:subjectPartLiteral whenever practical.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_taxonCount"></a>Term Name: ac:taxonCount</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/taxonCount">http://rs.tdwg.org/ac/terms/taxonCount</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/taxonCount-2020-01-27">http://rs.tdwg.org/ac/terms/version/taxonCount-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Taxon Count</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>An exact or estimated number of taxa at the lowest applicable taxon rank (usually species or infraspecific) represented by the media resource (item or collection).</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The count SHOULD contain only the taxa covered fully or primarily by the resource. This SHOULD be a single integer number. </td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Primarily intended for resource collections and singular resources dealing with sets of taxa (e. g., identification tools, videos). It is recommended to give an exact or estimated number of specific taxa when a complete list of taxa is not available or practical. For a taxon page and most images this will be "1", i. e. other taxa mentioned on the side or in the background should not be counted. However, sometimes a resource may illustrate an ecological or behavioral entity with multiple species, e. g., a host-pathogen interaction; taxon count would then indicate the known number of species in this interaction. Leave the field empty if you cannot estimate the information (do not enter 0). Additional taxon counts at higher levels (e. g. how many families are covered by a digital Fauna) should be given verbatim in the resource description, not here.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_taxonCoverage"></a>Term Name: ac:taxonCoverage</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/taxonCoverage">http://rs.tdwg.org/ac/terms/taxonCoverage</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/taxonCoverage-2020-01-27">http://rs.tdwg.org/ac/terms/version/taxonCoverage-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Taxon Coverage</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A higher taxon (e. g., a genus, family, or order) at the level of the genus or higher, that covers all taxa that are the primary subject of the resource (which may be a media item or a collection).</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Example: Where the subject of an image is several species of ducks with trees visible in the background, Taxon Coverage would still be Anatidae (and not Biota). Example: "Aves" for a bird key or a bird image collection. Do not add a rank ("Class Aves") in this field. Note that this somewhat expands the usage of ncd:taxonCoverage which, however has not yet been adopted by TDWG, and which specifies at the Family level or higher. For collections it is recommended to follow ncd:taxonCoverage to avoid conflicts between an AC record and a record arising from use of the un-adopted NCD. If the resource contains a single taxon, this should be placed in Scientific Taxon Name. In this case Taxon Coverage may be left empty, but if not, care should be taken that the entries do not conflict. Example: If Scientific Taxon Name is Quercus alba then Taxon Coverage, if provided at all, should be Quercus.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dwc_vernacularName"></a>Term Name: dwc:vernacularName</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/vernacularName">http://rs.tdwg.org/dwc/terms/vernacularName</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-08-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/dwc/terms/version/vernacularName-2017-10-06">http://rs.tdwg.org/dwc/terms/version/vernacularName-2017-10-06</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Common Name</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A common or vernacular name.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Common (= vernacular) names of the subject in one or several languages. The ISO 639-1 language code SHOULD be given in parentheses after the name if not all names are given by values of the Metadata Language term.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The ISO language code after the name should be formatted as in the following example: 'abete bianco (it); Tanne (de); White Fir (en)'. If names are known to be male- or female-specific, this may be specified as in: 'ewe (en-female); ram (en-male);'.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td><code>Andean Condor</code>, <code>Condor Andino</code>, <code>American Eagle</code>, <code>Gänsegeier</code></td>
		</tr>
	</tbody>
</table>


### 7.8 Resource Creation Vocabulary

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_captureDevice"></a>Term Name: ac:captureDevice</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/captureDevice">http://rs.tdwg.org/ac/terms/captureDevice</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/captureDevice-2020-01-27">http://rs.tdwg.org/ac/terms/version/captureDevice-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Capture Device</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Free form text describing the device or devices used to create the resource.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>It is best practice to record the device; this may include a combination such as camera plus lens, or camera plus microscope. Examples: "Canon Supershot 2000", "Makroscan Scanner 2000", "Zeiss Axioscope with Camera IIIu", "SEM (Scanning Electron Microscope)".</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_digitizationDate"></a>Term Name: ac:digitizationDate</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/digitizationDate">http://rs.tdwg.org/ac/terms/digitizationDate</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/digitizationDate-2020-01-27">http://rs.tdwg.org/ac/terms/version/digitizationDate-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Date and Time Digitized</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Date the first digital version was created, if different from Original Date and Time found in the Temporal Coverage Vocabulary.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The date and time MUST comply with the World Wide Web Consortium (W3C) datetime practice, <a href="https://www.w3.org/TR/NOTE-datetime">https://www.w3.org/TR/NOTE-datetime</a>, which requires that date and time representation correspond to ISO 8601:1998, but with year fields always comprising 4 digits. This makes datetime records compliant with 8601:2004, <a href="https://www.iso.org/standard/40874.html">https://www.iso.org/standard/40874.html</a>. AC datetime values MAY also follow 8601:2004 for ranges by separating two IS0 8601 datetime fields by a solidus ("forward slash", '/'). Use the international (ISO/xml) format yyyy-mm-ddThh:mm (e. g. "2007-12-31" or "2007-12-31T14:59"). Where available, timezone information SHOULD be added. </td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This is often not the media creation or modification date. For example, if photographic prints have been scanned, the date of that scanning is what this term carries, but Original Date and Time is that depicted in the print. In the case of digital images containing EXIF, whereas the EXIF capture date does not contain time zone information, but EXIF GPSDateStamp and GPSTimeStamp may be relevant as these include time-zone information. See also Metadata Working Group Guidelines for Handling Image Metadata, Version 2.0 (November 2010), <a href="https://web.archive.org/web/20180919181934/http://www.metadataworkinggroup.org/pdf/mwg_guidance.pdf">https://web.archive.org/web/20180919181934/http://www.metadataworkinggroup.org/pdf/mwg_guidance.pdf</a>, which has best practice advice on handling time-zone-less EXIF date/time data. See also the Wikipedia IS0 8601 entry, <a href="https://en.wikipedia.org/wiki/ISO_8601">https://en.wikipedia.org/wiki/ISO_8601</a>, for further explanation and examples.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_frameRate"></a>Term Name: ac:frameRate</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/frameRate">http://rs.tdwg.org/ac/terms/frameRate</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2022-02-23</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/frameRate-2022-02-23">http://rs.tdwg.org/ac/terms/version/frameRate-2022-02-23</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Frame Rate</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The decimal fraction representing the frequency (rate) at which consecutive images (frames) were captured in real time for a moving image, expressed as the number of frames per second.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>This term represents the rate at which consecutive images were captured in real time, not the rate at which the media is encoded to play back the recording.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For example, in a recording where 60 consecutive images (frames) are captured for each second of the real-time recording, this would be 60. In a time-lapse recording where one image (frame) is recorded every 5 seconds of recording, this would be 0.2.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="Iptc4xmpExt_LocationCreated"></a>Term Name: Iptc4xmpExt:LocationCreated</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://iptc.org/std/Iptc4xmpExt/2008-02-29/LocationCreated">http://iptc.org/std/Iptc4xmpExt/2008-02-29/LocationCreated</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Location Created</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The location the content of the item was created </td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The location at which the media recording instrument was placed when the media was created.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The distinction between the location shown and created is often irrelevant, and metadata may be assumed to be referring to location shown. It is recommended that the Location Shown field above always be used when known. However, in the case of position data automatically recorded by the instrument (e. g. EXIF GPS data) Location Created should be used to maintain information accuracy. When one but not both of these locations are present, AC is silent about whether the provided one entails the other. A best practices document for a particular AC implementation might address this.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_resourceCreationTechnique"></a>Term Name: ac:resourceCreationTechnique</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/resourceCreationTechnique">http://rs.tdwg.org/ac/terms/resourceCreationTechnique</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-10-13</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/resourceCreationTechnique-2020-10-13">http://rs.tdwg.org/ac/terms/version/resourceCreationTechnique-2020-10-13</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Resource Creation Technique</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Information about technical aspects of the creation and digitization process of the resource. This includes modification steps ("retouching") after the initial resource capture.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Annotating whether and how a resource has been modified or edited significantly in ways that are not immediately obvious to, or expected by, consumers is of special significance. Examples for images are: Removing a distracting twig from a picture, moving an object to a different surrounding, changing the color in parts of the image, or blurring the background of an image. Modifications that are standard practice and expected or obvious are not necessary to document; examples of such practices include changing resolution, cropping, minor sharpening or overall color correction, and clearly perceptible modifications (e.g., addition of arrows or labels, or the placement of multiple pictures into a table.) If it is only known that significant modifications were made, but no details are known, a general statement like "Media may have been manipulated to improve appearance" may be appropriate. See also Subject Preparation Technique.</td>
		</tr>
		<tr>
			<td>Examples</td>
			<td>Encoding method or settings, numbers of channels, lighting, frames per second, data rate, interlaced or progressive, multiflash lighting, remote control, automatic interval exposure.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="mo_sample_rate"></a>Term Name: mo:sample_rate</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://purl.org/ontology/mo/sample_rate">http://purl.org/ontology/mo/sample_rate</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-10-13</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Sample Rate</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Associates a digital signal to its sample rate.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Numeric value in hertz (Hz).</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For example, a Service Access Point may have a specific resolution, quality, or format. “Sample rate” is distinct from the related concept of “bit rate” for compressed files such as MP3, and is applicable to both uncompressed and compressed files. See <a href="http://musicontology.com/specification/#term-sample_rate">http://musicontology.com/specification/#term-sample_rate</a> for additional information.</td>
		</tr>
	</tbody>
</table>


### 7.9 Related Resources Vocabulary

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_associatedObservationReference"></a>Term Name: ac:associatedObservationReference</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/associatedObservationReference">http://rs.tdwg.org/ac/terms/associatedObservationReference</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/associatedObservationReference-2020-01-27">http://rs.tdwg.org/ac/terms/version/associatedObservationReference-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Associated Observation Reference</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A reference to an observation associated with this resource.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_associatedSpecimenReference"></a>Term Name: ac:associatedSpecimenReference</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/associatedSpecimenReference">http://rs.tdwg.org/ac/terms/associatedSpecimenReference</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/associatedSpecimenReference-2020-01-27">http://rs.tdwg.org/ac/terms/version/associatedSpecimenReference-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Associated Specimen Reference</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A reference to a specimen associated with this resource.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Supports finding a specimen resource, where additional information is available. If several resources relate to the same specimen, these are implicitly related. Examples: for NHM "BM 23974324" for a barcoded or "BM Smith 32" for a non-barcoded specimen; for UNITS: "TSB 28637"; for PMSL: "PMSL-Lepidoptera-2534781". Ideally this may be a URI identifying a specimen record that is available online.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_derivedFrom"></a>Term Name: ac:derivedFrom</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/derivedFrom">http://rs.tdwg.org/ac/terms/derivedFrom</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/derivedFrom-2020-01-27">http://rs.tdwg.org/ac/terms/version/derivedFrom-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Derived From</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A reference to an original resource from which the current one is derived.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Human readable, or doi number, or URL. Simple name of parent for human readable.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Derivation of one resource from another is of special interest for identification tools (e. g. a key from an unpublished data set, as in FRIDA, or a PDA key from a PC or web key) or web services (e. g. a name synonymization service being derived from a specific data set). It may very rarely also be known where one image or sound recording is derived from another (but compare the separate mechanism to be used for quality/resolution levels). Can be repeated if a montage of images.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_IDofContainingCollection"></a>Term Name: ac:IDofContainingCollection</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/IDofContainingCollection">http://rs.tdwg.org/ac/terms/IDofContainingCollection</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/IDofContainingCollection-2020-01-27">http://rs.tdwg.org/ac/terms/version/IDofContainingCollection-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>ID of Containing Collection</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>If the resource is contained in a Collection, this field identifies that Collection uniquely.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Repeatable: A media resource may be member of multiple collections. The form of the identifier is left to implementers of specific implementations.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_providerID"></a>Term Name: ac:providerID</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/providerID">http://rs.tdwg.org/ac/terms/providerID</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/providerID-2020-01-27">http://rs.tdwg.org/ac/terms/version/providerID-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Provider ID</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A globally unique ID of the provider of the current AC metadata record.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Only to be used if the annotated resource is not a provider itself - this item is for relating the resource to a provider, using an arbitrary code that is unique for a provider, contributing partner, or aggregator, or other roles (potentially defined by MARC, OAI) and by which the media resources are linked to the provider.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_relatedResourceID"></a>Term Name: ac:relatedResourceID</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/relatedResourceID">http://rs.tdwg.org/ac/terms/relatedResourceID</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/relatedResourceID-2020-01-27">http://rs.tdwg.org/ac/terms/version/relatedResourceID-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Related Resource ID</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Resource related in ways not specified through a collection, e.g., before-after images; time-lapse series; different orientations/angles of view</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>The value references a related media item. Examples of relations are: Images taken in a sequence or defined time series, an exposure or focus series (e.g. for stacking), different framing or views (top, side, bottom) of the same subject, or an overview plus several details. The property makes such related media items discoverable, but does not indicate the nature of this relationship. More specific properties may be defined in a later version of AC.</td>
		</tr>
	</tbody>
</table>


### 7.10 Service Access Point Vocabulary

These terms are representation-dependent metadata, referring to specific digital representations of a resource (e.g., a specific resolution, quality, or format). They are used within whatever a particular AC implementation assigns to the value of `ac:hasServiceAccessPoint`, whose label is simply "Service Access Point." Note that it is possible for an implementation to use syntactic conventions that avoid direct use of `ac:hasServiceAccessPoint`, as illustrated in the final example in the section [Multiplicity/Cardinality in the Audiovisual Core Structure document](structure.md#3-multiplicity-and-cardinality).

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_accessURI"></a>Term Name: ac:accessURI</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/accessURI">http://rs.tdwg.org/ac/terms/accessURI</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/accessURI-2020-01-27">http://rs.tdwg.org/ac/terms/version/accessURI-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Access URI</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A URI that uniquely identifies a service that provides a representation of the underlying resource.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>If this resource can be acquired by an http request, its http URL SHOULD be given. If not, but it has some URI in another URI scheme, that MAY be given here.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Value might point to something offline, such as a published CD, etc. For example, the doi of a published CD would be a suitable value.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dc_format"></a>Term Name: dc:format</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://purl.org/dc/elements/1.1/format">http://purl.org/dc/elements/1.1/format</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://dublincore.org/usage/terms/history/#format-007">http://dublincore.org/usage/terms/history/#format-007</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Format (literal)</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The file format, physical medium, or dimensions of the resource.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>A controlled value string describing the technical format of the resource (file format or physical medium). The string SHOULD be a controlled value from the Audiovisual Core Controlled Vocabulary for Dublin Core format, although it MAY be any Media Type (MIME type) value from the IANA list of Media Types (<a href="https://www.iana.org/assignments/media-types/media-types.xhtml">https://www.iana.org/assignments/media-types/media-types.xhtml</a>) or any commonly used file extension string. Human-readable information about the Controlled Vocabulary for format is at <a href="http://rs.tdwg.org/ac/doc/format/">http://rs.tdwg.org/ac/doc/format/</a> .</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This term can be used to describe offline digital content. In cases where the provided Service Access Point URL includes a standard file extension from which the format can be inferred, it is permissible to not provide a value for this property. See also the entry for dcterms:format in the Audiovisual Core term list document and see the DCMI FAQ on DC and DCTERMS Namespaces, <a href="https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md">https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md</a>, for discussion of the rationale for terms in two namespaces. It is best practice to use dcterms:format instead of dc:format whenever practical. Normal practice is to use the same Label if both are provided. Labels have no effect on information discovery and are only suggestions.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="dcterms_format"></a>Term Name: dcterms:format</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://purl.org/dc/terms/format">http://purl.org/dc/terms/format</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://dublincore.org/usage/terms/history/#formatT-001">http://dublincore.org/usage/terms/history/#formatT-001</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Format (IRI)</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The file format, physical medium, or dimensions of the resource. </td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>An IRI denoting the technical format of the resource (file format or physical medium). The IRI SHOULD be from the Audiovisual Core Controlled Vocabulary for Dublin Core format. Human-readable information about the Controlled Vocabulary for format is at <a href="http://rs.tdwg.org/ac/doc/format/">http://rs.tdwg.org/ac/doc/format/</a> .</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>In cases where an IRI for the format does not exist in the controlled vocabulary, a provider can omit this property and provide a media type or file extension value for dc:format. See the DCMI FAQ on DC and DCTERMS Namespaces, <a href="https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md">https://web.archive.org/web/20171126043657/https://github.com/dcmi/repository/blob/master/mediawiki_wiki/FAQ/DC_and_DCTERMS_Namespaces.md</a>, for discussion of the rationale for terms in two namespaces. Labels have no effect on information discovery and are only suggestions.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_furtherInformationURL"></a>Term Name: ac:furtherInformationURL</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/furtherInformationURL">http://rs.tdwg.org/ac/terms/furtherInformationURL</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/furtherInformationURL-2020-01-27">http://rs.tdwg.org/ac/terms/version/furtherInformationURL-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Further Information URL</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The URL of a Web site that provides additional information about the version of the media resource that is provided by the Service Access Point.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_hashFunction"></a>Term Name: ac:hashFunction</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/hashFunction">http://rs.tdwg.org/ac/terms/hashFunction</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/hashFunction-2020-01-27">http://rs.tdwg.org/ac/terms/version/hashFunction-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Hash Function</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The cryptographic hash function used to compute the value given in the Hash Value.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended values include MD5, SHA-1, SHA-224,SHA-256, SHA-384, SHA-512, SHA-512/224 and SHA-512/256</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_hashValue"></a>Term Name: ac:hashValue</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/hashValue">http://rs.tdwg.org/ac/terms/hashValue</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/hashValue-2020-01-27">http://rs.tdwg.org/ac/terms/version/hashValue-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Hash</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The value computed by a hash function applied to the media that will be delivered at the access point.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Best practice is to also specify the hash function by supplying a value of the Hash Function term, using one of the standard literals from the Notes there.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_licensingException"></a>Term Name: ac:licensingException</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/licensingException">http://rs.tdwg.org/ac/terms/licensingException</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/licensingException-2020-01-27">http://rs.tdwg.org/ac/terms/version/licensingException-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Licensing Exception Statement</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The licensing statement for this variant of the media resource if different from that given in the License Statement property of the resource.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Required only if this version has different licensing than that of the media resource. For example, the highest resolution version may be more restricted than lower resolution versions.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="exif_PixelXDimension"></a>Term Name: exif:PixelXDimension</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://ns.adobe.com/exif/1.0/PixelXDimension">http://ns.adobe.com/exif/1.0/PixelXDimension</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Image Width</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Information specific to compressed data. When a compressed file is recorded, the valid width of the meaningful image shall be recorded in this tag, whether or not there is padding data or a restart marker.  This tag shall not exist in an uncompressed file.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The width in pixels of the media specified by the access point. Contrary to the definition, in Audiovisual Core, this term MAY be used with uncompressed files.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Audiovisual Core uses this term for any image type, including those to which EXIF does not apply and those that are not a compressed file type like JPEG.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="exif_PixelYDimension"></a>Term Name: exif:PixelYDimension</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://ns.adobe.com/exif/1.0/PixelYDimension">http://ns.adobe.com/exif/1.0/PixelYDimension</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Image Height</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Information specific to compressed data. When a compressed file is recorded, the valid height of the meaningful image shall be recorded in this tag, whether or not there is padding data or a restart marker.  This tag shall not exist in an uncompressed file.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The height in pixels of the media specified by the access point. Contrary to the definition, in Audiovisual Core, this term MAY be used with uncompressed files.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Audiovisual Core uses this term for any image type, including those to which EXIF does not apply and those that are not a compressed file type like JPEG.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_ServiceAccessPoint"></a>Term Name: ac:ServiceAccessPoint</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/ServiceAccessPoint">http://rs.tdwg.org/ac/terms/ServiceAccessPoint</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/ServiceAccessPoint-2020-01-27">http://rs.tdwg.org/ac/terms/version/ServiceAccessPoint-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Service Access Point Class</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> </td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A specific digital representation of a media resource.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>This term serves as a type for values of the ac:hasServiceAccessPoint property.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For example, a Service Access Point may have a specific resolution, quality, or format.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_serviceExpectation"></a>Term Name: ac:serviceExpectation</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/serviceExpectation">http://rs.tdwg.org/ac/terms/serviceExpectation</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/serviceExpectation-2023-09-05">http://rs.tdwg.org/ac/terms/version/serviceExpectation-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Service Expectation</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A term that describes what service expectations users may have of the ac:accessURI.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Recommended terms include online (denotes that the URL is expected to deliver the resource), authenticate (denotes that the URL delivers a login or other authentication interface requiring completion before delivery of the resource) published(non digital) (denotes that the URL is the identifier of a non-digital published work, for example a doi.) Communities should develop their own controlled vocabularies for Service Expectations.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_variant"></a>Term Name: ac:variant</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/variant">http://rs.tdwg.org/ac/terms/variant</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/variant-2023-09-05">http://rs.tdwg.org/ac/terms/version/variant-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Variant (IRI)</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The category describing this Service Access Point variant, denoted by an IRI.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Values SHOULD be selected from the Controlled Vocabulary for Audiovisual Core variant. Human-readable information about the Controlled Vocabulary for variant is at <a href="http://rs.tdwg.org/ac/doc/variant/">http://rs.tdwg.org/ac/doc/variant/</a> . In text-based systems such as tables, IRI values MUST be in unabbreviated form.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_variantDescription"></a>Term Name: ac:variantDescription</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/variantDescription">http://rs.tdwg.org/ac/terms/variantDescription</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2020-01-27</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/variantDescription-2020-01-27">http://rs.tdwg.org/ac/terms/version/variantDescription-2020-01-27</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Variant Description</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>Text that describes this Service Access Point variant</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Most variants (thumb, low-res, high-res) are self-explanatory and it is best practice to leave this property empty if no special description is needed. It is provided for cases that require additional information (e.g., video shortened instead of simply quality reduced).</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_variantLiteral"></a>Term Name: ac:variantLiteral</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/variantLiteral">http://rs.tdwg.org/ac/terms/variantLiteral</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2023-09-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/variantLiteral-2023-09-05">http://rs.tdwg.org/ac/terms/version/variantLiteral-2023-09-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Variant (literal)</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The category describing this Service Access Point variant, denoted by a controlled value string.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>Values SHOULD be selected from the Controlled Vocabulary for Audiovisual Core variant. Human-readable information about the Controlled Vocabulary for variant is at <a href="http://rs.tdwg.org/ac/doc/variant/">http://rs.tdwg.org/ac/doc/variant/</a> . It is best practice to use ac:variant instead of ac:variantLiteral whenever practical.</td>
		</tr>
	</tbody>
</table>


### 7.11 Region of Interest Vocabulary

Regions of Interest (ROI) designate specific parts of media items. Features within these regions can be taxonomically identified or linked to occurrence records. ROI metadata may also be used to generate annotations of the media item or to facilitate display or highlighting of specific parts. 

Currently spatial ROIs are limited to two dimensions and can only be defined by rectangles or arcs (including circles). The terms in this group are not repeatable within a single ROI instance, although a media item may be linked to more than one ROI by the `ac:hasROI` property.

 For examples showing how to use these terms, see the <a href="https://github.com/tdwg/ac/blob/master/roi-recipes.md">ROI Recipes</a> page.

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_endTime"></a>Term Name: ac:endTime</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/endTime">http://rs.tdwg.org/ac/terms/endTime</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/endTime-2021-10-05">http://rs.tdwg.org/ac/terms/version/endTime-2021-10-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>End Time in Seconds</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The end of a temporal region, specified as an absolute offset relative to the beginning of the media item (this corresponds to Normal Play Time RFC 2326), specified as seconds, with an optional fractional part to indicate milliseconds or finer.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>This term MUST only be applied to a region of interest.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_endTimestamp"></a>Term Name: ac:endTimestamp</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/endTimestamp">http://rs.tdwg.org/ac/terms/endTimestamp</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/endTimestamp-2021-10-05">http://rs.tdwg.org/ac/terms/version/endTimestamp-2021-10-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>End Timestamp</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The end of a temporal region, specified as real-world clock time ISO 8601 timestamps, using UTC timezone, with an optional fractional part to indicate milliseconds or finer. There is no limit on the number of decimal places for the decimal fraction.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>This term MAY be applied to a region of interest or an entire media item.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_hasROI"></a>Term Name: ac:hasROI</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/hasROI">http://rs.tdwg.org/ac/terms/hasROI</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/hasROI-2021-10-05">http://rs.tdwg.org/ac/terms/version/hasROI-2021-10-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Has Region of Interest</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> Yes</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A region of interest located within the subject media item.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>ac:hasROI is the inverse property of ac:isROIOf.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Used to link a subject media item to an object region of interest.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_heightFrac"></a>Term Name: ac:heightFrac</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/heightFrac">http://rs.tdwg.org/ac/terms/heightFrac</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/heightFrac-2021-10-05">http://rs.tdwg.org/ac/terms/version/heightFrac-2021-10-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Fractional Height</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The height of the bounding rectangle, expressed as a decimal fraction of the height of the media item.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The sum of a valid value plus ac:yFrac MUST be greater than zero and less than or equal to one. The precision of this value SHOULD be great enough that when ac:heightFrac and ac:yFrac are used with the exif:PixelYDimension of the Best Quality variant of the Service Access point to calculate the lower right corner of the rectangle, rounding to the nearest integer results in the same vertical pixel originally used to define the point. This term MUST NOT be used with ac:radius to define a region of interest.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Zero-sized bounding rectangles are not allowed. To designate a point, use the radius option with a zero value.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_isROIOf"></a>Term Name: ac:isROIOf</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/isROIOf">http://rs.tdwg.org/ac/terms/isROIOf</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/isROIOf-2021-10-05">http://rs.tdwg.org/ac/terms/version/isROIOf-2021-10-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Is Region of Interest of</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The media item within which a region of interest is located.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>ac:isROIOf is the inverse property of ac:hasROI.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Used to link a subject region of interest to an object media item.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_mediaDuration"></a>Term Name: ac:mediaDuration</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/mediaDuration">http://rs.tdwg.org/ac/terms/mediaDuration</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/mediaDuration-2021-10-05">http://rs.tdwg.org/ac/terms/version/mediaDuration-2021-10-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Media Duration</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The playback duration of an audio or video file in seconds.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This might be different from the time in seconds calculated as the difference of ac:endTimestamp and ac:startTimestamp if ac:mediaSpeed is not equal to 1.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_mediaSpeed"></a>Term Name: ac:mediaSpeed</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/mediaSpeed">http://rs.tdwg.org/ac/terms/mediaSpeed</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/mediaSpeed-2021-10-05">http://rs.tdwg.org/ac/terms/version/mediaSpeed-2021-10-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Media Speed</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The decimal fraction representing the natural speed over the encoded speed.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>If a value for ac:mediaSpeed is not provided, applications SHOULD assume that 1.0 is the value.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>For example, in a time-lapse recording where 60 seconds of natural time is represented in 1 second of media this would be 60. In a time-expanded recording where 1 second of recording is represented in 5 seconds of media, this would be 0.2.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_radius"></a>Term Name: ac:radius</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/radius">http://rs.tdwg.org/ac/terms/radius</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/radius-2021-10-05">http://rs.tdwg.org/ac/terms/version/radius-2021-10-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Radius</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The radius of a bounding circle or arc, expressed as a fraction of the width of the media item.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>A valid value MUST be greater than or equal to zero. A valid value MAY cause the designated circle to extend beyond the bounds of the media item. In that case, the arc within the media item plus the bounds of the media item specify the region of interest. This term MUST NOT be used with ac:widthFrac or ac:heightFrac to define a region of interest.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This term may be used with ac:xFrac and ac:yFrac to define a point. In that case, the implication is that the point falls on some object of interest within the media item, but nothing more can be assumed about the bounds of that object.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_RegionOfInterest"></a>Term Name: ac:RegionOfInterest</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/RegionOfInterest">http://rs.tdwg.org/ac/terms/RegionOfInterest</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/RegionOfInterest-2021-10-05">http://rs.tdwg.org/ac/terms/version/RegionOfInterest-2021-10-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Region of Interest Class</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> </td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>A designated region of a media item bounded in dimensions appropriate for the media type.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Dimensions may include spatial, temporal, or frequency bounds.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_startTime"></a>Term Name: ac:startTime</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/startTime">http://rs.tdwg.org/ac/terms/startTime</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/startTime-2021-10-05">http://rs.tdwg.org/ac/terms/version/startTime-2021-10-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Start Time in Seconds</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The beginning of a temporal region, specified as an absolute offset relative to the beginning of the media item (this corresponds to Normal Play Time RFC 2326), specified as seconds, with an optional fractional part to indicate milliseconds or finer.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>This term MUST only be applied to a region of interest.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_startTimestamp"></a>Term Name: ac:startTimestamp</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/startTimestamp">http://rs.tdwg.org/ac/terms/startTimestamp</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/startTimestamp-2021-10-05">http://rs.tdwg.org/ac/terms/version/startTimestamp-2021-10-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Start Timestamp</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The beginning of a temporal region, specified as real-world clock time ISO 8601 timestamps, using UTC timezone, with an optional fractional part to indicate milliseconds or finer. There is no limit on the number of decimal places for the decimal fraction.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>This term MAY be applied to a region of interest or an entire media item.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_widthFrac"></a>Term Name: ac:widthFrac</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/widthFrac">http://rs.tdwg.org/ac/terms/widthFrac</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/widthFrac-2021-10-05">http://rs.tdwg.org/ac/terms/version/widthFrac-2021-10-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Fractional Width</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The width of the bounding rectangle, expressed as a decimal fraction of the width of the media item.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>The sum of a valid value plus ac:xFrac MUST be greater than zero and less than or equal to one. The precision of this value SHOULD be great enough that when ac:widthFrac and ac:xFrac are used with the exif:PixelXDimension of the Best Quality variant of the Service Access point to calculate the lower right corner of the rectangle, rounding to the nearest integer results in the same horizontal pixel originally used to define the point. This term MUST NOT be used with ac:radius to define a region of interest.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>Zero-sized bounding rectangles are not allowed. To designate a point, use the radius option with a zero value.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_xFrac"></a>Term Name: ac:xFrac</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/xFrac">http://rs.tdwg.org/ac/terms/xFrac</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/xFrac-2021-10-05">http://rs.tdwg.org/ac/terms/version/xFrac-2021-10-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Fractional X</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The horizontal position of a reference point, measured from the left side of the media item and expressed as a decimal fraction of the width of the media item.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>A valid value MUST be greater than or equal to zero and less than or equal to one. The precision of this value SHOULD be great enough that when the ac:xFrac value is multiplied by the exif:PixelXDimension of the Best Quality variant of the Service Access point, rounding to the nearest integer results in the same horizontal pixel location originally used to define the point.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This point can serve as the horizontal position of the upper left corner of a bounding rectangle, or as the center of a circle.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2"><a id="ac_yFrac"></a>Term Name: ac:yFrac</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Normative URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/yFrac">http://rs.tdwg.org/ac/terms/yFrac</a></td>
		</tr>
		<tr>
			<td>Modified</td>
			<td>2021-10-05</td>
		</tr>
		<tr>
			<td>Term version URI</td>
			<td><a href="http://rs.tdwg.org/ac/terms/version/yFrac-2021-10-05">http://rs.tdwg.org/ac/terms/version/yFrac-2021-10-05</a></td>
		</tr>
		<tr>
			<td>Label</td>
			<td>Fractional Y</td>
		</tr>
		<tr>
			<td></td>
			<td><b>Required:</b> No -- <b>Repeatable:</b> No</td>
		</tr>
		<tr>
			<td>Definition</td>
			<td>The vertical position of a reference point, measured from the top of the media item and expressed as a decimal fraction of the height of the media item.</td>
		</tr>
		<tr>
			<td>Usage</td>
			<td>A valid value MUST be greater than or equal to zero and less than or equal to one. The precision of this value SHOULD be great enough that when the ac:yFrac value is multiplied by the exif:PixelYDimension of the Best Quality variant of the Service Access point, rounding to the nearest integer results in the same vertical pixel originally used to define the point.</td>
		</tr>
		<tr>
			<td>Notes</td>
			<td>This point can serve as the vertical position of the upper left corner of a bounding rectangle, or as the center of a circle.</td>
		</tr>
	</tbody>
</table>


