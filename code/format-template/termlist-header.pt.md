# Controlled Vocabulary for Dublin Core format: List of Terms

Title
: Controlled Vocabulary for Dublin Core format: List of Terms

Namespace IRI
: <http://rs.tdwg.org/acformat/values/>

Preferred namespace abbreviation
: acformat:

Date version issued
: {ratification_date}

Date created
: {created_date}

Part of TDWG Standard
: <{standard_iri}>

This version
: <{current_iri}{ratification_date}>

Latest version
: <{current_iri}>

{previous_version_slot}

Abstract
: Audiovisual Core borrows the Dublin Core terms dc:format and dcterms:format to provide information about the physical or electronic format of a media item. This controlled vocabulary provides values for those two terms.

Contributors
: {contributors}

Creator
: {creator}

Bibliographic citation
: {creator}. {year}. {document_title}. {publisher}. <{current_iri}{ratification_date}>

## 1 Introduction (informative)

This document includes terms intended to be used as a controlled value for Dublin Core terms `dc:format` and `dcterms:format`, which are borrowed by Audiovisual Core.

### 1.1 Status of the content of this document

Section 1 is informative (non-normative).

Section 2 is normative except as noted.

Section 3 is informative.

In Section 4, the values of the `Term IRI`, `Definition`, and `Controlled value` are normative. The value of `Usage` (if it exists for a given term) is normative.  The values of `Has broader concept` and `Has exact match` are normative. The values of `Term Name` are non-normative, although one can expect that the namespace abbreviation prefix is one commonly used for the term namespace.  `Label` and the values of all other properties are non-normative.

### 1.2 RFC 2119 key words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [\[RFC 2119\]](https://datatracker.ietf.org/doc/html/rfc2119) and [\[RFC 8174\]](https://datatracker.ietf.org/doc/html/rfc8174) when, and only when, they appear in all capitals, as shown here.

## 2 Use of Terms

### 2.1 Relationship of value types to property terms

In accordance with [the Audiovisual Core Term List document](http://rs.tdwg.org/ac/doc/termlist/), unabbreviated term IRIs MUST be used as values of the property `dcterms:format`. Controlled value strings SHOULD be used as values of the property `dc:format`.

### 2.2 Relationship between concepts and concept schemes

The entry for the property `dc:format` in the [Audiovisual Core term list document](http://rs.tdwg.org/ac/doc/termlist/#dc_format) specifies that three kinds of string values are RECOMMENDED: Internet Media Types (MIME types), special string values for physical media, or commonly used file extensions. This controlled vocabulary defines two SKOS concept schemes, a concept scheme for media types and physical media (the first two kinds of values specified for `dc:type`) and a concept scheme for file extensions (the last recommended kind of value). Because the Internet Assigned Numbers Authority (IANA) maintains a [registry of media types](https://www.iana.org/assignments/media-types/media-types.xhtml) and Audiovisual Core maintains a controlled list of physical media types, using values from the media types and physical media concept scheme is RECOMMENDED over the file extensions concept scheme. 

The concept scheme for media types and physical media defines a `skos:broader` relation between each specific media type or physical medium and one of the six [Top-level Media Types defined by RFC 2046](https://tools.ietf.org/html/rfc2046#page-4V) that are related to multimedia: application, audio, image, model, text, and video. This relation MAY be used by clients to infer the general category of the media item format.

The concept scheme for file extensions defines concepts for many common file extensions used for digital media files. These concepts are usually related to one of the media types and physical media by a `skos:exactMatch` relation. Metadata creators MAY use a controlled value from the file extensions concept scheme, but because of the asserted `skos:exactMatch` relation aggregators MAY substitute the equivalent value from the media types and physical media concept scheme.

### 2.3 Example workflows (non-normative)

Workflow 1: A data provider uses spreadsheets containing a column for literal values for `dc:format`. The spreadsheets are populated with file extensions that are controlled string values from the concept scheme for file extensions. The spreadsheets are provided to an aggregator whose software "looks up" the controlled string values in the concept scheme for file extensions and determines the equivalent concepts from the concept scheme for media types and physical media. The IRIs from the concept scheme for media types and physical media are used as standardized values for `dcterms:format` in the aggregator's database.

Workflow 2: A data aggregator acquires data about multimedia items that includes file names or URLs, but no format information. The aggregator extracts the file extensions from the files or URLs and uses the concept schemes to assign a `dcterms:format` IRI value from the concept scheme for media types and physical media to each item. In cases where an item has a file extension that does not correspond to one of the controlled value strings in the concept scheme for file extensions, the aggregator uses a community-maintained table of alternate file extension values to determine the appropriate format concept for the media item.

Workflow 3: A data aggregator harvests media items from an open data repository. The remote server provides the media type via a `Content-Type` header and the file extension is determined from the file name. The aggregator cross-checks the media type value against the file extension value and uses the `skos:exactMatch` relations in the SKOS concept schemes to determine whether the values are consistent. Inconsistent pairs of values are flagged for manual checking. Previously unknown file extensions are flagged for additional research and possible inclusion in the community-maintained table of alternate file extension values.

## 3 Term index
