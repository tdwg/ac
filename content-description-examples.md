# Content Description Examples

**Title:** Content Description Examples

**Date modified:** 2024-05-16

**Part of TDWG Standard:** Not part of any standard

**Abstract:** This document provides examples showing how to use Audiovisual Core terms `Iptc4xmpExt:CVterm` and `ac:CVterm` with the Content Description controlled vocabulary.  

**Contributors:** Steve Baskauf

**Creator:** Audiovisual Core Maintenance Group

**Bibliographic citation:** Audiovisual Core Maintenance Group. 2024. Content Description examples. Biodiversity Information Standards (TDWG). https://github.com/tdwg/ac/blob/master/content-description-examples.md

## Notes

Either of `ac:CVtermLiteral` or `Iptc4xmpExt:CVterm` may be used (both are not required). IRIs have not yet been assigned for the content description controlled values, but they should be similar in form to the values of `Iptc4xmpExt:CVterm` shown in the examples.

When the subjectPart and subjectOrientation terms are used, either the literal or IRI forms can be used. The examples show both, but only one form is required for each of the properties.

## Example 1. An image depicting labels

<img src="https://medialib.naturalis.nl/file/id/RMNH.INS.661199_LAB/format/large" width="500">

Metadata at <https://www.idigbio.org/portal/mediarecords/ede483c1-3cb6-45b7-a538-a3dceb2f272f>

Note: the metadata from this example came from the published data, which did not contain all of the properties required by Audiovisual Core. Some errors in usage were corrected.

### Tabular serialization of the data

**Table 1. Metadata about the media item.**

| xmpRights:Owner | dc:type | dc:format | dcterms:identifier | ac:caption | dc:rights | ac:accessURI | ac:variantLiteral | ac:CVtermLiteral | Iptc4xmpExt:CVterm |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Naturalis Biodiversity Center | StillImage | image/jpeg | https://medialib.naturalis.nl/file/id/RMNH.INS.661199_LAB/format/large | RMNH.INS.661199_0 | CC0 1.0 | https://medialib.naturalis.nl/file/id/RMNH.INS.661199_LAB/format/large | Good Quality | label | http://rs.tdwg.org/accontent/values/c000 |

### JSON-LD serialization of the data

Additional JSON was added to make the example valid JSON-LD.

**Serialization 1**

```
{
    "@context": {
        "ac": "http://rs.tdwg.org/ac/terms/",
        "dc": "http://purl.org/dc/elements/1.1/",
        "dcterms": "http://purl.org/dc/terms/",
        "Iptc4xmpExt": "http://iptc.org/std/Iptc4xmpExt/2008-02-29/",
        "xmpRights": "http://ns.adobe.com/xap/1.0/rights/",
        "ac:accessURI": {
            "@type": "@id"
        },
        "Iptc4xmpExt:CVterm": {
            "@type": "@id"
        }
    },
    "@graph": [
        {
            "xmpRights:Owner": "Naturalis Biodiversity Center",
            "dc:type": "StillImage",
            "dc:format": "image/jpeg",
            "dcterms:identifier": "https://medialib.naturalis.nl/file/id/RMNH.INS.661199_LAB/format/large",
            "ac:caption": "RMNH.INS.661199_0",
            "dc:rights": "CC0 1.0",
            "ac:accessURI": "https://medialib.naturalis.nl/file/id/RMNH.INS.661199_LAB/format/large",
            "ac:variantLiteral": "Good Quality",
            "ac:CVtermLiteral": "label",
            "Iptc4xmpExt:CVterm": "http://rs.tdwg.org/accontent/values/c000"
        }
    ]
}
```


## Example 2. An image showing a part of an insect

<img src="https://images.collections.yale.edu/iiif/2/ypm:e246d7d1-bdc4-4a47-877e-07ca729bd917/full/!1920,1920/0/default.jpg" width="500">

Metadata at <https://www.idigbio.org/portal/mediarecords/dd468f12-0389-4299-87c1-cf1921974325>

Note: the metadata in this example came from the published data. Some incorrectly used fields were removed. 

### Tabular serialization of the data

**Table 2. Metadata about the media item.**

Abbreviated. See JSON-LD serialization for more complete metadata

| ac:providerManagedID | dc:creator | dc:type | dcterms:title | ac:comments | ac:digitizationDate | dc:format | dcterms:identifier | ac:CVtermLiteral | Iptc4xmpExt:CVterm | ac:subjectPartLiteral | ac:subjectPart | ac:subjectOrientationLiteral | ac:subjectOrientation |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| urn:uuid:e246d7d1-bdc4-4a47-877e-07ca729bd917 | Sikander Kiani | StillImage | Apis (YPM IZ 098672). Digital Image: Yale Peabody Museum; photo by Sikander Kiani 2018-04-11 | irn:657676 | 2018-04-11 | image/jpeg | urn:uuid:e246d7d1-bdc4-4a47-877e-07ca729bd917 | organismPart | http://rs.tdwg.org/accontent/values/c005 | leg | http://rs.tdwg.org/acpart/values/p0016 | lateral | http://rs.tdwg.org/acorient/values/r0003 |

### JSON-LD serialization of the data

Additional JSON was added to make the example valid JSON-LD.

**Serialization 2**

```
{
    "@context": {
        "ac": "http://rs.tdwg.org/ac/terms/",
        "dc": "http://purl.org/dc/elements/1.1/",
        "dcterms": "http://purl.org/dc/terms/",
        "Iptc4xmpExt": "http://iptc.org/std/Iptc4xmpExt/2008-02-29/",
        "xmp": "http://ns.adobe.com/xap/1.0/",
        "xmpRights": "http://ns.adobe.com/xap/1.0/rights/",
        "ac:accessURI": {
            "@type": "@id"
        },
        "Iptc4xmpExt:CVterm": {
            "@type": "@id"
        },
        "xmpRights:WebStatement": {
            "@type": "@id"
        },
        "ac:subjectPart": {
            "@type": "@id"
        },
        "ac:accessURI": {
            "@type": "@id"
        }
    },
    "@graph": [
        {
            "ac:providerManagedID": "urn:uuid:e246d7d1-bdc4-4a47-877e-07ca729bd917",
            "dc:creator": "Sikander Kiani",
            "dc:type": "StillImage",
            "dcterms:title": "Apis (YPM IZ 098672). Digital Image: Yale Peabody Museum; photo by Sikander Kiani 2018-04-11",
            "ac:comments": "irn:657676",
            "ac:digitizationDate": "2018-04-11",
            "dc:format": "image/jpeg",
            "dcterms:identifier": "urn:uuid:e246d7d1-bdc4-4a47-877e-07ca729bd917",
            "ac:metadataLanguageLiteral": "en",
            "xmpRights:WebStatement": "http://hdl.handle.net/10079/8931zqj/",
            "ac:accessURI": "https://images.collections.yale.edu/iiif/2/ypm:e246d7d1-bdc4-4a47-877e-07ca729bd917/full/!1920,1920/0/default.jpg",
            "xmp:MetadataDate": "2020-03-21T18:05:55Z",
            "dc:rights": "CC0",
            "ac:CVtermLiteral": "organismPart",
            "Iptc4xmpExt:CVterm": "http://rs.tdwg.org/accontent/values/c005",
            "ac:subjectPartLiteral": "leg",
            "ac:subjectPart": "http://rs.tdwg.org/acpart/values/p0016",
            "ac:subjectOrientationLiteral": "lateral",
            "ac:subjectOrientation": "http://rs.tdwg.org/acorient/values/r0003"
        }
    ]
}
```

## Example 3. An image showing plants in their habitat

<img src="http://bioimages.vanderbilt.edu/lq/baskauf/wecte3-wpin-glade12735.jpg">

Metadata derived from <http://bioimages.vanderbilt.edu/baskauf/12735.rdf>

Note: the metadata in this example came generally from the published data. Some fields were omitted for brevity.

### Tabular serialization of the data

**Table 3. Metadata about the media item.**

Abbreviated. See JSON-LD serialization for more complete metadata.

| dc:type | dcterms:type | dcterms:identifier | ac:metadataLanguageLiteral | ac:metadataLanguage | dc:rights | xmpRights:UsageTerms | xmpRights:WebStatement | ac:CVtermLiteral | Iptc4xmpExt:CVterm |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| StillImage | http://purl.org/dc/dcmitype/StillImage | http://bioimages.vanderbilt.edu/baskauf/12735 | en | http://id.loc.gov/vocabulary/iso639-2/eng | (c) 2002 Steven J. Baskauf | Available under Creative Commons Attribution 4.0 International License. | http://creativecommons.org/licenses/by/4.0/ | context | http://rs.tdwg.org/accontent/values/c001 |

### JSON-LD serialization of the data

Data were converted from RDF/XML to JSON-LD

**Serialization 3**

```
{
    "@context": {
        "ac": "http://rs.tdwg.org/ac/terms/",
        "dc": "http://purl.org/dc/elements/1.1/",
        "dcterms": "http://purl.org/dc/terms/",
        "Iptc4xmpExt": "http://iptc.org/std/Iptc4xmpExt/2008-02-29/",
        "xmp": "http://ns.adobe.com/xap/1.0/",
        "xmpRights": "http://ns.adobe.com/xap/1.0/rights/",
        "dcterms:type": {
            "@type": "@id"
        },
        "Iptc4xmpExt:CVterm": {
            "@type": "@id"
        },
        "xmpRights:WebStatement": {
            "@type": "@id"
        },
        "ac:metadataLanguage": {
            "@type": "@id"
        },
        "ac:hasServiceAccessPoint": {
            "@type": "@id"
        }
    },
    "@graph": [
        {
            "dc:type": "StillImage",
            "dcterms:type": "http://purl.org/dc/dcmitype/StillImage",
            "dcterms:identifier": "http://bioimages.vanderbilt.edu/baskauf/12735",
            "ac:metadataLanguageLiteral": "en",
            "ac:metadataLanguage": "http://id.loc.gov/vocabulary/iso639-2/eng",
            "dc:rights": "(c) 2002 Steven J. Baskauf",
            "xmpRights:UsageTerms": "Available under Creative Commons Attribution 4.0 International License.",
            "xmpRights:WebStatement": "http://creativecommons.org/licenses/by/4.0/",
            "dcterms:title": "Echinacea tennesseensis (Asteraceae) - whole plant - in flower - general view",
            "dc:creator": "Steven J. Baskauf",
            "xmp:MetadataDate": "2017-11-14T21:34:56-06:00",
            "xmp:CreateDate": "2002-06-18T10:08:05-05:00",
            "ac:hasServiceAccessPoint": "http://bioimages.vanderbilt.edu/baskauf/12735#lq",
            "ac:CVtermLiteral": "context",
            "Iptc4xmpExt:CVterm": "http://rs.tdwg.org/accontent/values/c001"
        }
    ]
}
```

## Example 4. A specimen image with multiple regions of interest

<img src="https://s.idigbio.org/idigbio-images-prod-webview/bf1abe6bcc595f295d50c84d422f00ab.jpg" width="500">

Metadata derived from <https://www.idigbio.org/portal/mediarecords/344d88c0-31c9-4067-9502-a310a0ab942b>

Note: this example flattens the record to include data on only a single ServiceAccessPoint, whose metadata are included with the image level metadata. For an example of normalized records with multiple ServiceAccessPoints, see the [Regions of Interest Recipes](https://github.com/tdwg/ac/blob/master/roi-recipes.md) document.

### Tabular serialization of the data

**Table 4. Metadata about the media item.**

Abbreviated. See JSON-LD serialization for more complete metadata.

| dc:source | xmpRights:WebStatement | dc:creator | ac:providerLiteral | dwc:scientificName | dc:rights | dc:type | dcterms:title | dc:format| dcterms:identifier |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| US National Herbarium, Department of Botany, NMNH, Smithsonian Institution | https://naturalhistory.si.edu/research/nmnh-collections/museum-collections-policies | Ingrid P. Lin | Smithsonian Institution, NMNH, Botany | Fraxinus americana | CC0 | image | 01075361.tif | image/jpeg | https://collections.nmnh.si.edu/media/?i=10395311 |

**Table 5. Metadata about regions of interest (ROI) within the media item**

Some ROIs omitted for brevity. See the JSON-LD for more complete metadata.

| dcterms:identifier | dcterm:description | ac:isROIOf | ac:xFrac |ac:yFrac | ac:widthFrac | ac:heightFrac | ac:CVtermLiteral | Iptc4xmpExt:CVterm | ac:subjectPartLiteral | ac:subjectPart | ac:subjectOrientationLiteral | ac:subjectOrientation |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| https://collections.nmnh.si.edu/media/?i=10395311#roi1 | color and grayscale bar | https://collections.nmnh.si.edu/media/?i=10395311 | 0 | 0.03985 | 0.10499 | 0.9433 | colorBar | http://rs.tdwg.org/accontent/values/c003 | | | | |
| https://collections.nmnh.si.edu/media/?i=10395311#roi2 | scale bar with logo | https://collections.nmnh.si.edu/media/?i=10395311 | 0.91386 | 0.318 | 0.06244 | 0.3414 | scaleBar | http://rs.tdwg.org/accontent/values/c002 | | | | |
| https://collections.nmnh.si.edu/media/?i=10395311#roi3 | determination label | https://collections.nmnh.si.edu/media/?i=10395311 | 0.45617 | 0.87431 | 0.26121 | 0.09536 | label | http://rs.tdwg.org/accontent/values/c000 | | | | |
| https://collections.nmnh.si.edu/media/?i=10395311#roi7 | winged fruits | https://collections.nmnh.si.edu/media/?i=10395311 | 0.66131 | 0.68259 | 0.12385 | 0.07197 | organismPart | http://rs.tdwg.org/accontent/values/c00 | fruit | http://rs.tdwg.org/acpart/values/p0008 | lateral | http://rs.tdwg.org/acorient/values/r0003 |
| https://collections.nmnh.si.edu/media/?i=10395311#roi8 | compound leaf | https://collections.nmnh.si.edu/media/?i=10395311 | 0.26988 | 0.14869 | 0.5976 | 0.70301 | organismPart | http://rs.tdwg.org/accontent/values/c00 | leaf | http://rs.tdwg.org/acpart/values/p0005 | upper | http://rs.tdwg.org/acorient/values/r0008 |

### JSON-LD serialization of the data

Note: the metadata in the media item part of this example came generally from the published data.

**Serialization 4**

```
{
    "@context": {
        "ac": "http://rs.tdwg.org/ac/terms/",
        "dc": "http://purl.org/dc/elements/1.1/",
        "dwc": "http://rs.tdwg.org/dwc/terms/",
        "dcterms": "http://purl.org/dc/terms/",
        "Iptc4xmpExt": "http://iptc.org/std/Iptc4xmpExt/2008-02-29/",
        "Iptc4xmpExt:CVterm": {
            "@type": "@id"
        },
        "xmpRights:WebStatement": {
            "@type": "@id"
        },
        "ac:accessURI": {
            "@type": "@id"
        }
    },
    "@graph": [
        {
            "dc:source": "US National Herbarium, Department of Botany, NMNH, Smithsonian Institution",
            "xmpRights:WebStatement": "https://naturalhistory.si.edu/research/nmnh-collections/museum-collections-policies",
            "dc:creator": "Ingrid P. Lin",
            "ac:providerLiteral": "Smithsonian Institution, NMNH, Botany",
            "dwc:scientificName": "Fraxinus americana",
            "dc:rights": "CC0",
            "dc:type": "image",
            "dcterms:title": "01075361.tif",
            "dc:format": "image/jpeg",
            "dcterms:identifier": "https://collections.nmnh.si.edu/media/?i=10395311",
            "dcterms:description": "Bigelow, J. M. s.n., US National Herbarium Sheet 61280, Barcode 01075361",
            "ac:accessURI": "http://n2t.net/ark:/65665/m382548833-2d4f-4a8f-b29e-96981f2193b8",
            "exif:PixelXDimension": "3924",
            "exif:PixelYDimension": "5044",
            "ac:hasROI": [
                {
                    "@id": "https://collections.nmnh.si.edu/media/?i=10395311#roi1",
                    "dcterms:description": "color and grayscale bar",
                    "ac:xFrac": 0,
                    "ac:yFrac": 0.03985,
                    "ac:widthFrac": 0.10499,
                    "ac:heightFrac": 0.9433,
                    "ac:CVtermLiteral": "colorBar",
                    "Iptc4xmpExt:CVterm": "http://rs.tdwg.org/accontent/values/c003"
                },
                {
                    "@id": "https://collections.nmnh.si.edu/media/?i=10395311#roi2",
                    "dcterms:description": "scale bar with logo",
                    "ac:xFrac": 0.91386,
                    "ac:yFrac": 0.318,
                    "ac:widthFrac": 0.06244,
                    "ac:heightFrac": 0.3414,
                    "ac:CVtermLiteral": "scaleBar",
                    "Iptc4xmpExt:CVterm": "http://rs.tdwg.org/accontent/values/c002"
                },
                {
                    "@id": "https://collections.nmnh.si.edu/media/?i=10395311#roi3",
                    "dcterms:description": "determination label",
                    "ac:xFrac": 0.45617,
                    "ac:yFrac": 0.87431,
                    "ac:widthFrac": 0.26121,
                    "ac:heightFrac": 0.09536,
                    "ac:CVtermLiteral": "label",
                    "Iptc4xmpExt:CVterm": "http://rs.tdwg.org/accontent/values/c000"
                },
                {
                    "@id": "https://collections.nmnh.si.edu/media/?i=10395311#roi4",
                    "dcterms:description": "original collector's label",
                    "ac:xFrac": 0.11137,
                    "ac:yFrac": 0.87708,
                    "ac:widthFrac": 0.29613,
                    "ac:heightFrac": 0.10408,
                    "ac:CVtermLiteral": "label",
                    "Iptc4xmpExt:CVterm": "http://rs.tdwg.org/accontent/values/c000"
                },
                {
                    "@id": "https://collections.nmnh.si.edu/media/?i=10395311#roi5",
                    "dcterms:description": "bar code",
                    "ac:xFrac": 0.51631,
                    "ac:yFrac": 0.84794,
                    "ac:widthFrac": 0.12003,
                    "ac:heightFrac": 0.02815,
                    "ac:CVtermLiteral": "label",
                    "Iptc4xmpExt:CVterm": "http://rs.tdwg.org/accontent/values/c000"
                },
                {
                    "@id": "https://collections.nmnh.si.edu/media/?i=10395311#roi6",
                    "dcterms:description": "accession stamp",
                    "ac:xFrac": 0.77497,
                    "ac:yFrac": 0.83723,
                    "ac:widthFrac": 0.12385,
                    "ac:heightFrac": 0.068,
                    "ac:CVtermLiteral": "label",
                    "Iptc4xmpExt:CVterm": "http://rs.tdwg.org/accontent/values/c000"
                },
                {
                    "@id": "https://collections.nmnh.si.edu/media/?i=10395311#roi7",
                    "dcterms:description": "winged fruits",
                    "ac:xFrac": 0.66131,
                    "ac:yFrac": 0.68259,
                    "ac:widthFrac": 0.12385,
                    "ac:heightFrac": 0.07197,
                    "ac:CVtermLiteral": "organismPart",
                    "Iptc4xmpExt:CVterm": "http://rs.tdwg.org/accontent/values/c005",
                    "ac:subjectPartLiteral": "fruit",
                    "ac:subjectPart": "http://rs.tdwg.org/acpart/values/p0008",
                    "ac:subjectOrientationLiteral": "lateral",
                    "ac:subjectOrientation": "http://rs.tdwg.org/acorient/values/r0003"

                },
                {
                    "@id": "https://collections.nmnh.si.edu/media/?i=10395311#roi8",
                    "dcterms:description": "compound leaf",
                    "ac:xFrac": 0.26988,
                    "ac:yFrac": 0.14869,
                    "ac:widthFrac": 0.5976,
                    "ac:heightFrac": 0.70301,
                    "ac:CVtermLiteral": "organismPart",
                    "Iptc4xmpExt:CVterm": "http://rs.tdwg.org/accontent/values/c005",
                    "ac:subjectPartLiteral": "leaf",
                    "ac:subjectPart": "http://rs.tdwg.org/acpart/values/p0005",
                    "ac:subjectOrientationLiteral": "upper",
                    "ac:subjectOrientation": "http://rs.tdwg.org/acorient/values/r0008"
                }
            ]
        }
    ]
}
```

The regions of interest metadata can be easily used to construct IIIF Image API (v2) URLs that display the focal content. The fractional values can be multiplied by 100 to generate a `pct:` region description, e.g. for the fruits:

ac:xFrac: 0.66131<br/>
ac:yFrac: 0.68259<br/>
ac:widthFrac: 0.12385<br/>
ac:heightFrac: 0.07197<br/>

<https://iiif.library.vanderbilt.edu/iiif/2/test%2FNMNH-01075361.jpg/pct:66.131,68.259,12.385,7.197/!500,500/0/default.jpg>

Region of Interest displayed:

<img src="https://iiif.library.vanderbilt.edu/iiif/2/test%2FNMNH-01075361.jpg/pct:66.131,68.259,12.385,7.197/!500,500/0/default.jpg">

Click to view the regions of interest described in the example (via IIIF Image API URLs constructed as above):

[color and grayscale bar](https://iiif.library.vanderbilt.edu/iiif/2/test%2FNMNH-01075361.jpg/pct:0,3.985,10.499,94.33/!500,500/0/default.jpg)

[scale bar with logo](https://iiif.library.vanderbilt.edu/iiif/2/test%2FNMNH-01075361.jpg/pct:91.386,31.8,6.244,34.14/!500,500/0/default.jpg)

[determination label](https://iiif.library.vanderbilt.edu/iiif/2/test%2FNMNH-01075361.jpg/pct:45.617,87.431,26.121,9.536/!500,500/0/default.jpg)

[original collector's label](https://iiif.library.vanderbilt.edu/iiif/2/test%2FNMNH-01075361.jpg/pct:11.137,87.708,29.613,10.408/!500,500/0/default.jpg)

[bar code](https://iiif.library.vanderbilt.edu/iiif/2/test%2FNMNH-01075361.jpg/pct:51.631,84.794,12.003,2.815/!500,500/0/default.jpg)

[accession stamp](https://iiif.library.vanderbilt.edu/iiif/2/test%2FNMNH-01075361.jpg/pct:77.497,83.723,12.385,6.8/!500,500/0/default.jpg)

[winged fruits](https://iiif.library.vanderbilt.edu/iiif/2/test%2FNMNH-01075361.jpg/pct:66.131,68.259,12.385,7.197/!500,500/0/default.jpg)

[compound leaf](https://iiif.library.vanderbilt.edu/iiif/2/test%2FNMNH-01075361.jpg/pct:26.988,14.869,59.76,70.301/!500,500/0/default.jpg)

