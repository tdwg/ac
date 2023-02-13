**Title:** Still image examples

**Date modified:** 2021-02-22

**Part of TDWG Standard:** Not part of any standard

**Abstract:** This document includes examples of Audiovisual Core still image records.  

**Contributors:** Kate Webbink

**Creator:** Audiovisual Core Maintenance Group

**Bibliographic citation:** Audiovisual Core Maintenance Group. 2021. Still image examples. Biodiversity Information Standards (TDWG). https://github.com/tdwg/ac/blob/master/image/examples.md

## 1 Introduction

This document is intended to provide the community with examples "from the wild" of how providers have successfully used Audiovisual Core terms to describe still images.


### 1.1 Status of the content of this document

All parts of this document are non-normative.  


### 1.2 RFC 2119 key words
[RFC 2119](https://tools.ietf.org/html/rfc2119) are not used in this document.


## 2 Audiovisual Core terms used with still images

Audiovisual Core terms (and values) for Image records include:

**Required Terms**:
  - [dcterms:identifier](https://tdwg.github.io/ac/termlist/#dcterms_identifier)
  - [dc:rights](https://tdwg.github.io/ac/termlist/#dc_rights) or [dcterms:rights](https://tdwg.github.io/ac/termlist/#dcterms_rights)
  - [dc:type](https://tdwg.github.io/ac/termlist/#dc_type) ("Image" or "StillImage") or [dcterms:type](https://tdwg.github.io/ac/termlist/#dcterms_type) ("http://purl.org/dc/dcmitype/StillImage")
  - [ac:metadataLanguage](https://tdwg.github.io/ac/termlist/#ac_metadataLanguage) or [ac:metadataLanguageLiteral](https://tdwg.github.io/ac/termlist/#ac_metadataLanguageLiteral)

**Recommended Terms**:
  - [ac:subtypeLiteral](https://tdwg.github.io/ac/termlist/#ac_subtypeLiteral) (e.g., "Photograph") or [ac:subtype](https://tdwg.github.io/ac/termlist/#ac_subtype)
  - [dc:creator](https://tdwg.github.io/ac/termlist/#dc_creator) (if known)

### 2.1 Example - Photographs ('StillImage')
*also viewable in [this google doc's 'Ex1' tab](https://docs.google.com/spreadsheets/d/1HeDwclaGgSh8L8FlVy0awbmgq-KRy0EyVWu-3gdFOqI/edit#gid=0)*

occurrenceId|identifier|type|subtypeLiteral|title|MetadataDate|metadataLanguageLiteral|providerManagedID|rights|Owner|WebStatement|Credit|creator|providerLiteral|description|tag|CreateDate|IDofContainingCollection|accessURI|format|hashFunction|hashValue|PixelXDimension|PixelYDimension
-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
84409e16-48ae-4994-8798-50a1294f6ef0|7d48b938-a946-47cd-abd7-c9cb1a62acea|StillImage|Photograph|NAMA 2011-026 - specimen image|2018-08-22|eng|1487473|[Copyright] Field Museum of Natural History - CC BY-NC|Field Museum of Natural History|https://www.fieldmuseum.org/field-museum-natural-history-conditions-and-suggested-norms-use-collections|Please cite this as: (c) The Field Museum (DATE) CC-BY-NC||Field Museum of Natural History|North American Mycological Association Foray 2011: specimen # NAMA 2011-026|Fungi||http://grbio.org/cool/90as-ki3a|https://fm-digital-assets.fieldmuseum.org/1487/473/NAMA2011-026a.JPG|jpeg|MD5|7e12851821d2342680492bb5f83f22cb|2048|1536
84409e16-48ae-4994-8798-50a1294f6ef0|fe806e66-e5c1-4fc1-9fba-ac6bbee07281|StillImage|Photograph|NAMA 2011-026 - specimen image|2018-08-22|eng|1487474|[Copyright] Field Museum of Natural History - CC BY-NC|Field Museum of Natural History|https://www.fieldmuseum.org/field-museum-natural-history-conditions-and-suggested-norms-use-collections|Please cite this as: (c) The Field Museum (DATE) CC-BY-NC||Field Museum of Natural History|North American Mycological Association Foray 2011: specimen # NAMA 2011-026|Fungi||http://grbio.org/cool/90as-ki3a|https://fm-digital-assets.fieldmuseum.org/1487/474/NAMA2011-026b.JPG|jpeg|MD5|83f73ea4d2c93a2e24e56e5ef400ba2e|2048|1536
f206a966-9506-4913-8f79-945e0fa5bd0e|0ce934a4-35e5-4a02-9cb0-babd5b9731b6|StillImage|Photograph|C0372592F|2019-09-18|eng|1989011|[Copyright] Field Museum of Natural History - CC BY-NC|Field Museum of Natural History|https://www.fieldmuseum.org/field-museum-natural-history-conditions-and-suggested-norms-use-collections|Please cite this as: (c) The Field Museum (DATE) CC-BY-NC|S. Russell|Field Museum of Natural History - Botany Department|Fresh specimen image of C0372592F|Fungi||http://grbio.org/cool/90as-ki3a|https://fm-digital-assets.fieldmuseum.org/1989/011/C0372592F.jpeg|jpeg|MD5|5e3456f17b5510d4f0ac84514a0ae872|768|1024

These three records are packaged with two corresponding occurrence records in the Darwin Core Archive here: https://doi.org/10.15468/x2hjnp


### 2.2 Example - Images available in multiple resolutions or versions
*also viewable in [this google doc's 'Ex2' tab](https://docs.google.com/spreadsheets/d/1HeDwclaGgSh8L8FlVy0awbmgq-KRy0EyVWu-3gdFOqI/edit#gid=1683326393&range=A1), and in the table below)*

occurrenceId|identifier|type|subtypeLiteral|title|MetadataDate|metadataLanguageLiteral|providerManagedID|hasServiceAccessPoint|rights|Owner|WebStatement|Credit|creator|providerLiteral|description|tag|CreateDate|IDofContainingCollection|accessURI|format|variantLiteral|hashFunction|hashValue|PixelXDimension|PixelYDimension
-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
04d9efc4-8b47-4545-b9d9-781508392b44|00a1388e-bc5c-46f2-ab3f-d5b7ce4d6655|StillImage||PP29675_image_1|2019-04-09|eng|744562|https://mm.fieldmuseum.org/00a1388e-bc5c-46f2-ab3f-d5b7ce4d6655|[Copyright] Field Museum of Natural History - CC BY-NC|Field Museum of Natural History|https://www.fieldmuseum.org/field-museum-natural-history-conditions-and-suggested-norms-use-collections|Please cite this as: (c) The Field Museum (DATE) CC-BY-NC|Field Museum of Natural History - Botany Department | Robert North : Field Museum of Natural History\|Field Museum of Natural History|PP 29675 A+B [HS, M] Pinnularia, Moscovian / Desmoinesian, Francis Creek Shale Member, United States of America, Illinois, Will, Mazon Creek Region|Fossil Ferns|22 Jul 2014|http://biocol.org/urn:lsid:biocol.org:col:34795|https://fm-digital-assets.fieldmuseum.org/744/562/PP29675_image_1.jpg|jpeg|mediumQualityFurtherInformationURL|MD5|9b7ad87adb8f5ada19e91a202f4339b1|1500|1908

The following Audiovisual Core terms are recommended for describing an image's alternate resolutions, formats, or other versions:
- [accessURI](https://tdwg.github.io/ac/termlist/#ac_accessURI)
- [ac:hasServiceAccessPoint](https://tdwg.github.io/ac/termlist/#ac_hasServiceAccessPoint)
- [ac:variantLiteral](https://tdwg.github.io/ac/termlist/#ac_variantLiteral) or [ac:variant](https://tdwg.github.io/ac/termlist/#ac_variant)

Further information on how to handle multiple versions is available in [section 3.2 of the Audiovisual Core Structure document](https://tdwg.github.io/ac/structure/#3-multiplicity-and-cardinality).

In the example-record:
- [ac:variant](https://tdwg.github.io/ac/termlist/#ac_variant) indicates that a "medium-Quality" version of the image is available with "Further-Information."
- [ac:hasServiceAccessPoint](https://tdwg.github.io/ac/termlist/#ac_hasServiceAccessPoint) provides the alternate version's URL.


## 3 Further Examples
See [the **ImageExamples** tab in this google doc](https://docs.google.com/spreadsheets/d/1HeDwclaGgSh8L8FlVy0awbmgq-KRy0EyVWu-3gdFOqI/edit#gid=1059134995&range=A2)


### 3.1 Images of Text or Sound?
Following the [Dublin Core recommendations for the Text type](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/dcmitype/Text), images of text (e.g., Catalog Cards) should be described as type **Text**.  
Similarly, visualizations of sound (e.g. Spectrograms) should be documented as type **Sound**.

### 3.2 Photographs of Living Organisms vs Museum Specimens
The differences between a photograph of a living organism and one of a museum specimen is mainly reflected in the related Darwin Core occurrence records.
If the photographs were both recorded with similar camera-setups, the recommended Audiovisual Core terms would be the same, with one distinction:

- [ac:associatedSpecimenReference](https://tdwg.github.io/ac/termlist/#ac_associatedSpecimenReference) to link related occurrences for specimens
- [ac:associatedObservationReference](https://tdwg.github.io/ac/termlist/#ac_associatedObservationReference) to link related occurrences for observations

### 3.3 Camera-traps
Note that photographs recorded with camera traps or other sequential or repeated image-recording methods can benefit from other detailed documentation.
(Consider https://www.mdpi.com/1424-8220/21/2/343/html)


## 4 Data Citations:
Example-records are from the following datasets:

*(accessed via GBIF.org on 2021-01-24)*

- Commonwealth Scientific and Industrial Research Organisation (2019). Australian National Insect Collection Image Library. Occurrence dataset https://doi.org/10.15468/y5eckg
- Gall L (2021). Invertebrate Paleontology Division, Yale Peabody Museum. Yale University Peabody Museum. Occurrence dataset https://doi.org/10.15468/nqheui
- Goud J, van der Bijl B, Creuwels J (2021). Naturalis Biodiversity Center (NL) - Mollusca. Naturalis Biodiversity Center. Occurrence dataset https://doi.org/10.15468/yefvnk
- Grant S, von Konrat M (2019). Field Museum of Natural History (Botany) Fungi Collection. Version 4.9. Field Museum. Occurrence dataset https://doi.org/10.15468/x2hjnp 
- Grant S, Webbink K, Jones J, Ferguson A (2020). Field Museum of Natural History (Zoology) Mammal Collection. Version 9.18. Field Museum. Occurrence dataset https://doi.org/10.15468/n4zgxw
- Grant S, Webbink K, Turcatel M, Shuman R (2020). Field Museum of Natural History (Zoology) Insect, Arachnid and Myriapod Collection. Version 12.31. Field Museum. Occurrence dataset https://doi.org/10.15468/0ywfpc
- Harvard University M, Morris P J (2021). Museum of Comparative Zoology, Harvard University. Version 162.246. Museum of Comparative Zoology, Harvard University. Occurrence dataset https://doi.org/10.15468/p5rupv
- Orrell T (2020). NMNH Paleobiology Specimen Records. Version 1.36. National Museum of Natural History, Smithsonian Institution. Occurrence dataset https://doi.org/10.15468/7m0fvd
- Ramirez J, Tulig M, Watson K, Thiers B (2020). The New York Botanical Garden Herbarium (NY). Version 1.29. The New York Botanical Garden. Occurrence dataset https://doi.org/10.15468/6e8nje

------

Content on this site, made open by [Biodiversity Information Standards (TDWG)](https://www.tdwg.org/) is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
