# Content Description Recipes

**Title:** Content Description Recipes

**Date modified:** 2024-05-16

**Part of TDWG Standard:** Not part of any standard

**Abstract:** This document provides examples showing how to use Audiovisual Core terms `Iptc4xmpExt:CVterm` and `ac:CVterm` with the Content Description controlled vocabulary.  

**Contributors:** Steve Baskauf

**Creator:** Audiovisual Core Maintenance Group

**Bibliographic citation:** Audiovisual Core Maintenance Group. 2024. Content Description Recipes. Biodiversity Information Standards (TDWG). https://github.com/tdwg/ac/blob/master/content-description-recipes.md

## Notes

Either of `ac:CVtermLiteral` or `Iptc4xmpExt:CVterm` may be used (both are not required). IRIs have not yet been assigned for the content description controlled values, but they should be similar in form to the value of `Iptc4xmpExt:CVterm` shown in the example.

When the subjectPart and subjectOrientation terms are used either the literal or IRI forms can be used. The example shows both, but only one form is required for each of the properties.

## 1. An image showing a label

<img href="https://medialib.naturalis.nl/file/id/RMNH.INS.661199_LAB/format/large" width="500">

Metadata at <https://www.idigbio.org/portal/mediarecords/ede483c1-3cb6-45b7-a538-a3dceb2f272f>

Note: the metadata from this example comes from the published data, which does not contain all of the properties required by Audiovisual Core. Some errors in usage were corrected.

### JSON-LD serialization of the data

Additional JSON was added to make the example valid JSON-LD.

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


## 2. An image showing a part of an insect

<img href="https://images.collections.yale.edu/iiif/2/ypm:e246d7d1-bdc4-4a47-877e-07ca729bd917/full/!1920,1920/0/default.jpg" width="500">

Metadata at <https://www.idigbio.org/portal/mediarecords/dd468f12-0389-4299-87c1-cf1921974325>

Note: the metadata from this example comes from the published data. Some incorrectly used fields were removed. 

### JSON-LD serialization of the data

Additional JSON was added to make the example valid JSON-LD.

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

## 3. An image showing plants in their habitat

<img href="http://bioimages.vanderbilt.edu/lq/baskauf/wecte3-wpin-glade12735.jpg">

Metadata derived from <http://bioimages.vanderbilt.edu/baskauf/12735.rdf>

Note: the metadata from this example comes generally from the published data. Some fields were omitted for brevity.

### JSON-LD serialization of the data

Data were converted from RDF/XML to JSON-LD

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

## 4. A specimen image with multiple regions of interest

<img href="https://s.idigbio.org/idigbio-images-prod-webview/bf1abe6bcc595f295d50c84d422f00ab.jpg" width="500">

Metadata derived from <https://www.idigbio.org/portal/mediarecords/344d88c0-31c9-4067-9502-a310a0ab942b>

Note: this example flattens the record to include data on only a single ServiceAccessPoint, whose metadata are included with the image level metadata.

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
                    "@id": "https://collections.nmnh.si.edu/media/?i=10395311#roi1",
                    "dcterms:description": "scale bar with logo",
                    "ac:xFrac": 0.91386,
                    "ac:yFrac": 0.318,
                    "ac:widthFrac": 0.06244,
                    "ac:heightFrac": 0.3414,
                    "ac:CVtermLiteral": "scaleBar",
                    "Iptc4xmpExt:CVterm": "http://rs.tdwg.org/accontent/values/c002"
                },
                {
                    "@id": "https://collections.nmnh.si.edu/media/?i=10395311#roi1",
                    "dcterms:description": "determination label",
                    "ac:xFrac": 0.45617,
                    "ac:yFrac": 0.87431,
                    "ac:widthFrac": 0.26121,
                    "ac:heightFrac": 0.09536,
                    "ac:CVtermLiteral": "label",
                    "Iptc4xmpExt:CVterm": "http://rs.tdwg.org/accontent/values/c000"
                },
                {
                    "@id": "https://collections.nmnh.si.edu/media/?i=10395311#roi1",
                    "dcterms:description": "original collector's label",
                    "ac:xFrac": 0.11137,
                    "ac:yFrac": 0.87708,
                    "ac:widthFrac": 0.29613,
                    "ac:heightFrac": 0.10408,
                    "ac:CVtermLiteral": "label",
                    "Iptc4xmpExt:CVterm": "http://rs.tdwg.org/accontent/values/c000"
                },
                {
                    "@id": "https://collections.nmnh.si.edu/media/?i=10395311#roi1",
                    "dcterms:description": "bar code",
                    "ac:xFrac": 0.51631,
                    "ac:yFrac": 0.84794,
                    "ac:widthFrac": 0.12003,
                    "ac:heightFrac": 0.02815,
                    "ac:CVtermLiteral": "label",
                    "Iptc4xmpExt:CVterm": "http://rs.tdwg.org/accontent/values/c000"
                },
                {
                    "@id": "https://collections.nmnh.si.edu/media/?i=10395311#roi1",
                    "dcterms:description": "accession stamp",
                    "ac:xFrac": 0.77497,
                    "ac:yFrac": 0.83723,
                    "ac:widthFrac": 0.12385,
                    "ac:heightFrac": 0.068,
                    "ac:CVtermLiteral": "label",
                    "Iptc4xmpExt:CVterm": "http://rs.tdwg.org/accontent/values/c000"
                },
                {
                    "@id": "https://collections.nmnh.si.edu/media/?i=10395311#roi1",
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
                    "@id": "https://collections.nmnh.si.edu/media/?i=10395311#roi2",
                    "dcterms:description": "compound leaf",
                    "ac:xFrac": 0.26988,
                    "ac:yFrac": 0.14869,
                    "ac:widthFrac": 0.5976,
                    "ac:heightFrac": 0.70301,
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

<https://iiif.library.vanderbilt.edu/iiif/2/test%2FNMNH-01075361.jpg/pct:66.131,68.259,12.385,7.197/1280,/0/default.jpg>

Click to view:

[color and grayscale bar](https://iiif.library.vanderbilt.edu/iiif/2/test%2FNMNH-01075361.jpg/pct:0,3.985,10.499,94.33/1280,/0/default.jpg)

[scale bar with logo](https://iiif.library.vanderbilt.edu/iiif/2/test%2FNMNH-01075361.jpg/pct:91.386,31.8,6.244,34.14/1280,/0/default.jpg)

[determination label](https://iiif.library.vanderbilt.edu/iiif/2/test%2FNMNH-01075361.jpg/pct:45.617,87.431,26.121,9.536/1280,/0/default.jpg)

[original collector's label](https://iiif.library.vanderbilt.edu/iiif/2/test%2FNMNH-01075361.jpg/pct:11.137,87.708,29.613,10.408/1280,/0/default.jpg)

[bar code](https://iiif.library.vanderbilt.edu/iiif/2/test%2FNMNH-01075361.jpg/pct:51.631,84.794,12.003,2.815/1280,/0/default.jpg)

[accession stamp](https://iiif.library.vanderbilt.edu/iiif/2/test%2FNMNH-01075361.jpg/pct:77.497,83.723,12.385,6.8/1280,/0/default.jpg)

[winged fruits](https://iiif.library.vanderbilt.edu/iiif/2/test%2FNMNH-01075361.jpg/pct:66.131,68.259,12.385,7.197/1280,/0/default.jpg)

[compound leaf](https://iiif.library.vanderbilt.edu/iiif/2/test%2FNMNH-01075361.jpg/pct:26.988,14.869,59.76,70.301/1280,/0/default.jpg)

Under construction...

### Tabular serialization of the data

**Table 1. Metadata about the abstract media item.**
<https://github.com/tdwg/ac/blob/master/fragments/transformation_examples/media.csv>

| dcterms:identifier | dcterms:title | ac:metadataLanguage | dc:rights | dcterms:type |
| ---- | ---- | ---- | ---- | ---- |
| http://bioimages.vanderbilt.edu/hessd/e5384 | Tragia cordata (Euphorbiaceae) - fruit – juvenile | http://id.loc.gov/vocabulary/iso639-2/eng | (c) 2008 Darel Hess | http://purl.org/dc/dcmitype/StillImage |

**Table 2. Metadata about service access points (SAP) for the media item.**
<https://github.com/tdwg/ac/blob/master/fragments/transformation_examples/sap.csv>

| dcterms:identifier | ac:variantLiteral | dc:format | exif:PixelXDimension | exif:PixelYDimension | ac:accessURI |
| ---- | ---- | ---- | ----- | ----- | ---- |
| http://bioimages.vanderbilt.edu/hessd/e5384 | Best Quality | image/jpeg | 2112 | 2526 | https://iiif.library.vanderbilt.edu/iiif/3/bioimages%2Fhessd%2Ftrco--fr040529-17e5384.jpg/full/max/0/default.jpg |
| http://bioimages.vanderbilt.edu/hessd/e5384 | Good Quality | image/jpeg | 856 | 1024 | https://iiif.library.vanderbilt.edu/iiif/3/bioimages%2Fhessd%2Ftrco--fr040529-17e5384.jpg/full/856,/0/default.jpg |

**Table 3. Metadata about regions of interest (ROI) within the media item**
<https://github.com/tdwg/ac/blob/master/fragments/transformation_examples/roi.csv>

| dcterms:identifier | ac:isROIOf | ac:xFrac |ac:yFrac | ac:widthFrac | ac:heightFrac | dcterm:description | dwc:scientificName | dwc:identifiedBy | ac:associatedObservationReference |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| http://bioimages.vanderbilt.edu/hessd/e538#roi1 | http://bioimages.vanderbilt.edu/hessd/e5384 | 0.28939 | 0.23674 | 0.09066 | 0.26373 | mine | Cyphacma tragiae | Terry Harrison | https://www.gbif.org/occurrence/930742101 |
| http://bioimages.vanderbilt.edu/hessd/e538#roi2 | http://bioimages.vanderbilt.edu/hessd/e5384 | 0.21892 | 0.44792 | 0.28147 | 0.34612 | fruit | Tragia cordata | Darel Hess | |

