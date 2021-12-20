# Regions of Interest (ROI) Recipes

**Title:** Regions of Interest (ROI) Recipes

**Date modified:** 2021-12-20

**Part of TDWG Standard:** Not part of any standard

**Abstract:** This document provides examples showing how to use terms related to Regions of Interest (ROIs).  

**Contributors:** Steve Baskauf

**Creator:** Audubon Core Maintenance Group

**Bibliographic citation:** Audubon Core Maintenance Group. 2021. Regions of Interest (ROI) Recipes. Biodiversity Information Standards (TDWG). https://github.com/tdwg/ac/blob/master/roi-recipes.md

## 1. Still image

This example involves a still image of a plant. The image was intended to illustrate the characteristics of fruit of the plant, but it unintentionally included evidence of a leaf-mining moth in one of the background leaves. The fruit and mine are designated within the image using regions of interest. 

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

### JSON-LD serialization of the data

**Serialization 1.**

<https://github.com/tdwg/ac/blob/master/fragments/transformation_examples/image_graph_hess.json>

```
{
    "@context": {
        "ac": "http://rs.tdwg.org/ac/terms/",
        "dwc": "http://rs.tdwg.org/dwc/terms/",
        "dc": "http://purl.org/dc/elements/1.1/",
        "dcterms": "http://purl.org/dc/terms/",
        "exif": "http://ns.adobe.com/exif/1.0/",
        "ac:metadataLanguage": {
            "@type": "@id"
        },
        "ac:accessURI": {
            "@type": "@id"
        },
        "ac:associatedObservationReference": {
            "@type": "@id"
        },
        "dcterms:type": {
            "@type": "@id"
        },
        "dcterms:format": {
            "@type": "@id"
        }
    },
    "@graph": [
        {
            "@id": "http://bioimages.vanderbilt.edu/hessd/e5384",
            "@type": "http://purl.org/dc/dcmitype/StillImage",
            "dcterms:title": "Tragia cordata (Euphorbiaceae) - fruit – juvenile",
            "dcterms:identifier": "http://bioimages.vanderbilt.edu/hessd/e5384",
            "dcterms:type": "http://purl.org/dc/dcmitype/StillImage",
            "ac:metadataLanguage": "http://id.loc.gov/vocabulary/iso639-2/eng",
            "dc:rights": "(c) 2008 Darel Hess",
            "ac:hasServiceAccessPoint": [
                {
                    "ac:accessURI": "https://iiif.library.vanderbilt.edu/iiif/3/bioimages%2Fhessd%2Ftrco--fr040529-17e5384.jpg/full/max/0/default.jpg",
                    "dc:format": "image/jpeg",
                    "dcterms:format": "http://rs.tdwg.org/format/values/m008",
                    "ac:variant": "http://rs.tdwg.org/acvariant/values/v006",
                    "ac:variantLiteral": "Best Quality",
                    "exif:PixelYDimension": 2112,
                    "exif:PixelXDimension": 2526
                },
                {
                    "ac:accessURI": "https://iiif.library.vanderbilt.edu/iiif/3/bioimages%2Fhessd%2Ftrco--fr040529-17e5384.jpg/full/856,/0/default.jpg",
                    "dc:format": "image/jpeg",
                    "dcterms:format": "http://rs.tdwg.org/format/values/m008",
                    "ac:variant": "http://rs.tdwg.org/acvariant/values/v005",
                    "ac:variantLiteral": "Good Quality",
                    "exif:PixelYDimension": 856,
                    "exif:PixelXDimension": 1024
                }
            ],
            "ac:hasROI": [
                {
                    "@id": "http://bioimages.vanderbilt.edu/hessd/e5384#roi1",
                    "dwc:scientificName": "Cyphacma tragiae",
                    "dwc:identifiedBy": "Terry Harrison",
                    "dcterms:description": "mine",
                    "ac:xFrac": 0.28939,
                    "ac:yFrac": 0.23674,
                    "ac:widthFrac": 0.09066,
                    "ac:heightFrac": 0.26373
                },
                {
                    "@id": "http://bioimages.vanderbilt.edu/hessd/e5384#roi2",
                    "dwc:scientificName": "Tragia cordata",
                    "dwc:identifiedBy": "Darel Hess",
                    "ac:associatedObservationReference": "https://www.gbif.org/occurrence/930742101",
                    "dcterms:description": "fruit",
                    "ac:xFrac": 0.21892,
                    "ac:yFrac": 0.44792,
                    "ac:widthFrac": 0.28147,
                    "ac:heightFrac": 0.34612
                }
            ]
        }
    ]
}
```

### Recipes

**Recipe 1.1 Convert ROI relative values to absolute pixel values for a particular SAP**

Calculate bounding box for mine on Best Quality SAP: <https://iiif.library.vanderbilt.edu/iiif/3/bioimages%2Fhessd%2Ftrco--fr040529-17e5384.jpg/full/max/0/default.jpg>

`round()` function rounds to nearest whole number.

```
x = round(ac:xFrac * exif:PixelXDimension)
x = round(0.28939 * 2526)
x = round(730.99914)
x = 731
```

Note that `ac:xFrac` was provided with sufficient precision to specify the exact pixel used to originally delineate the bounding box.

```
y = round(ac:yFrac * exif:PixelYDimension)
y = round(0.23674 * 2112)
y = round(499.99488)
y = 500

w = round(ac:widthFrac * exif:PixelXDimension)
w = round(0.09066 * 2526)
w = round(229.00716)
w = 229

h = round(ac:heightFrac * exif:PixelYDimension)
h = round(0.26373 * 2112)
h = round(556.99776)
h = 557
```

**Recipe 1.2 Convert ROI values to W3C Media Fragments**

`str()` function converts an integer into a string.
Strings are enclosed in double quotes.

```
bounding_box = str(x) + "," + str(y) + "," + str(w) + "," + str(h)
bounding_box = "731,500,229,557"

media fragment = "xywh=pixel:" + bounding_box
media fragment = "xywh=pixel:731,500,229,557"
```

**Recipe 1.3 Convert ROI values to IIIF Image API formats**

IIIF 2 URL for ROI within full image

```
endpoint_url = "https://iiif.library.vanderbilt.edu/iiif/2/"
identifier = "bioimages%2Fhessd%2Ftrco--fr040529-17e5384.jpg"
roi_url = endpoint_url + identifier + "/" + bounding_box + "/full/0/default.jpg"
roi_url = https://iiif.library.vanderbilt.edu/iiif/2/bioimages%2Fhessd%2Ftrco--fr040529-17e5384.jpg/731,500,229,557/full/0/default.jpg
```

IIIF 3 URL for ROI within full image

```
endpoint_url = "https://iiif.library.vanderbilt.edu/iiif/3/"
identifier = "bioimages%2Fhessd%2Ftrco--fr040529-17e5384.jpg"
roi_url = endpoint_url + identifier + "/" + bounding_box + "/max/0/default.jpg"
roi_url = https://iiif.library.vanderbilt.edu/iiif/3/bioimages%2Fhessd%2Ftrco--fr040529-17e5384.jpg/731,500,229,557/max/0/default.jpg
```

### Code examples

**Sample Python code** (Jupyter notebook)

<https://github.com/tdwg/ac/blob/master/fragments/transformation_examples/transformations.ipynb>

## 2. Sound recording (audio file SAP not available)

This example is from the Cornell Lab of Ornithology Macaulay Library: <https://macaulaylibrary.org/asset/245266991>. The recording can be streamed using an embedded player, but the original recording cannot be downloaded without making a special request. Thus we do not have direct access to any service access point of the recording. In the recording there are several flight songs of a broad-tailed hawk (*Buteo platypterus*), the focal species of the recording. However, the recording also includes singing of a red-eyed vireo (*Vireo olivaceus*), at some times overlapping with the *B. platypterus* song. The available metadata do not include timestamps, so the ROIs must be designated relative to the start time of the media.


### Tabular serialization of the data
                             
**Table 4. Metadata about the abstract media item.** 
<https://github.com/tdwg/ac/blob/master/fragments/sound/media.csv>

| dcterms:identifier | dcterms:title | ac:metadataLanguage | dc:rights | dcterms:type |
| ---- | ---- | ---- | ---- | ---- |
| https://macaulaylibrary.org/asset/245266991 | ML245266991 Broad-winged Hawk Macaulay Library | http://id.loc.gov/vocabulary/iso639-2/eng | (c) 2020 Daniel Jauvin | http://purl.org/dc/dcmitype/Sound |

**Table 5. Metadata about regions of interest (ROI) within the media item.** Note that the frequency range was not specified for the first two ROIs since there was only one sound occurring at those times. In the last two lines, the frequency range was used to distinguish between the sounds made by the two birds, which were occurring at the same time.
<https://github.com/tdwg/ac/blob/master/fragments/sound/roi.csv>
                             
| dcterms:identifier | ac:isROIOf | ac:startTime | ac:endTime | ac:freqLow | ac:freqHigh | dcterm:description | dwc:scientificName | dwc:identifiedBy | dwc:dateIdentified |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| https://macaulaylibrary.org/asset/245266991#bp1 | https://macaulaylibrary.org/asset/245266991 | 11.2 | 11.9 |  |  | flight song of red-winged hawk | Buteo platypterus | Daniel Jauvin | 2020-06-18 |
| https://macaulaylibrary.org/asset/245266991#vo1 | https://macaulaylibrary.org/asset/245266991 | 3.0 | 3.6 |  |  | song of red-eyed vireo | Vireo olivaceus | Steven J. Baskauf | 2021-06-14 |
| https://macaulaylibrary.org/asset/245266991#bp2 | https://macaulaylibrary.org/asset/245266991 | 0.2 | 1.2 | 2000 | 4200 | flight song of red-winged hawk | Buteo platypterus | Daniel Jauvin | 2020-06-18 |
| https://macaulaylibrary.org/asset/245266991#vo2 | https://macaulaylibrary.org/asset/245266991 | 0.4 | 1.2 | 4200 | 5000 | song of red-eyed vireo | Vireo olivaceus | Steven J. Baskauf | 2021-06-14 |

### JSON-LD serialization of the data

**Serialization 2.**
<https://github.com/tdwg/ac/blob/master/fragments/sound/bird_songs.json>

```
{
    "@context": {
        "ac": "http://rs.tdwg.org/ac/terms/",
        "dwc": "http://rs.tdwg.org/dwc/terms/",
        "dc": "http://purl.org/dc/elements/1.1/",
        "dcterms": "http://purl.org/dc/terms/",
        "ac:metadataLanguage": {
            "@type": "@id"
        },
        "dcterms:type": {
            "@type": "@id"
        },
        "dwc:dateIdentified": {
            "@type": "http://www.w3.org/2001/XMLSchema#date"
        }
    },
    "@graph": [
        {
            "@id": "https://macaulaylibrary.org/asset/245266991",
            "@type": "http://purl.org/dc/dcmitype/Sound",
            "dcterms:title": "ML245266991 Broad-winged Hawk Macaulay Library",
            "dcterms:identifier": "https://macaulaylibrary.org/asset/245266991",
            "dcterms:type": "http://purl.org/dc/dcmitype/Sound",
            "ac:metadataLanguage": "http://id.loc.gov/vocabulary/iso639-2/eng",
            "dc:rights": "(c) 2020 Daniel Jauvin",
            "ac:hasROI": [
                {
                    "@id": "https://macaulaylibrary.org/asset/245266991#bp1",
                    "dwc:scientificName": "Buteo platypterus",
                    "dwc:identifiedBy": "Daniel Jauvin",
                    "dwc:dateIdentified": "2020-06-18",
                    "dcterms:description": "flight song of red-winged hawk",
                    "ac:startTime": 11.2,
                    "ac:endTime": 11.9
                },
                {
                    "@id": "https://macaulaylibrary.org/asset/245266991#vo1",
                    "dwc:scientificName": "Vireo olivaceus",
                    "dwc:dateIdentified": "2021-06-14",
                    "dwc:identifiedBy": "Steven J. Baskauf",
                    "dcterms:description": "song of red-eyed vireo",
                    "ac:startTime": 3.0,
                    "ac:endTime": 3.6
                },
                {
                    "@id": "https://macaulaylibrary.org/asset/245266991#bp2",
                    "dwc:scientificName": "Buteo platypterus",
                    "dwc:identifiedBy": "Daniel Jauvin",
                    "dwc:dateIdentified": "2020-06-18",
                    "dcterms:description": "flight song of red-winged hawk",
                    "ac:startTime": 0.2,
                    "ac:endTime": 1.2,
                    "ac:freqLow": 2000,
                    "ac:freqHigh": 4200
                },
                {
                    "@id": "https://macaulaylibrary.org/asset/245266991#vo2",
                    "dwc:scientificName": "Vireo olivaceus",
                    "dwc:identifiedBy": "Steven J. Baskauf",
                    "dwc:dateIdentified": "2021-06-14",
                    "dcterms:description": "song of red-eyed vireo",
                    "ac:startTime": 0.4,
                    "ac:endTime": 1.2,
                    "ac:freqLow": 4200,
                    "ac:freqHigh": 5000
                }
            ]
        }
    ]
}
```

## 3. Sound recording (audio file SAP available)

This example involves a real recording from iNaturalist. However, the timestamp information is artificially created for this example. The cicada identification is also fanciful. The associated observation for the cicada at GBIF is made up, the cardinal occurrence identifier from GBIF is real. 

In this example, there are two SAPs from which MP4 audio files can be retrieved (one real and one fake). 

The recording from iNaturalist includes three regions of interest in which a Northern Cardinal sings. Between the first and second cardinal song, a cicada can be heard singing. This is noted by the submitter, but it does not get picked up by the iNaturalist AI. The metadata describe the region of interest of the cicada as a fourth ROI. Since the same cardinal is singing in the three ROIs, all three ROIs have been given the same value for `ac:associatedObservationReference`.

### Tabular serialization of the data
                             
**Table 6. Metadata about the abstract media item.**
<https://github.com/tdwg/ac/blob/master/fragments/inat/media.csv>
                             
| dcterms:identifier | dcterms:title | ac:metadataLanguage | dc:rights | dcterms:type | xmp:CreateDate |
| ---- | ---- | ---- | ---- | ---- | ---- |
| https://www.inaturalist.org/observations/82716069 | Northern Cardinal (Cardinalis cardinalis) on June 12, 2021 at 02:08 PM by cecildev8n5 | http://id.loc.gov/vocabulary/iso639-2/eng | (c) 2021 cecildev8n5 | http://purl.org/dc/dcmitype/Sound | 2021-06-12T14:08:10.3-04:00 |
 
**Table 7. Metadata about service access points (SAP) available for the media item.**
<https://github.com/tdwg/ac/blob/master/fragments/inat/sap.csv>
                             
| dcterms:identifier | dc:format | ac:mediaSpeed | ac:mediaDuration | ac:accessURI |
| ---- | ---- | ---- | ---- | ---- |
| https://www.inaturalist.org/observations/82716069 | audio/mp4 | 1 | 30.186 | https://static.inaturalist.org/sounds/251609.m4a?1623521443 | https://www.inaturalist.org/observations/82716069 | audio/mp4 | 0.2 | 150.93 | https://example.org/slomo/001 |

**Table 8. Metadata about regions of interest (ROI) within the media item.**
<https://github.com/tdwg/ac/blob/master/fragments/inat/roi.csv>

| dcterms:identifier | ac:isROIOf | ac:startTimestamp | ac:endTimestamp | dcterm:description | dwc:scientificName | dwc:identifiedBy | dwc:dateIdentified | ac:associatedObservationReference |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| https://www.inaturalist.org/observations/82716069#cc1 | https://www.inaturalist.org/observations/82716069 | 2021-06-12T14:08:12.1-04:00 | 2021-06-12T14:08:15.4-04:00 | song of Northern Cardinal | Cardinalis cardinalis | cecildev8n5 \| Caleb Helsel | 2021-06-12| https://www.gbif.org/occurrence/3307164054 |
| https://www.inaturalist.org/observations/82716069#nl | https://www.inaturalist.org/observations/82716069 | 2021-06-12T14:08:16.5-04:00 | 2021-06-12T14:08:20.2-04:00 | cicada song | Neotibicen linnei | Steven J. Baskauf | 2021-06-14 | https://www.gbif.org/occurrence/987654321 |
| https://www.inaturalist.org/observations/82716069#cc2 | https://www.inaturalist.org/observations/82716069 |2021-06-12T14:08:21.2-04:00 | 2021-06-12T14:08:24.1-04:00 | song of Northern Cardinal | Cardinalis cardinalis | cecildev8n5 \| Caleb Helsel | 2021-06-12 | https://www.gbif.org/occurrence/3307164054 |
| https://www.inaturalist.org/observations/82716069#cc3 | https://www.inaturalist.org/observations/82716069 | 2021-06-12T14:08:32.8-04:00 | 2021-06-12T14:08:36.4-04:00 | song of Northern Cardinal | Cardinalis cardinalis | cecildev8n5 \| Caleb Helsel | 2021-06-12 | https://www.gbif.org/occurrence/3307164054

### JSON-LD serialization of the data

**Serialization 3.**
<https://github.com/tdwg/ac/blob/master/fragments/inat/inat.json>

```
{
    "@context": {
        "ac": "http://rs.tdwg.org/ac/terms/",
        "dwc": "http://rs.tdwg.org/dwc/terms/",
        "dc": "http://purl.org/dc/elements/1.1/",
        "dcterms": "http://purl.org/dc/terms/",
        "xmp": "http://ns.adobe.com/xap/1.0/",
        "ac:metadataLanguage": {
            "@type": "@id"
        },
        "ac:accessURI": {
            "@type": "@id"
        },
        "ac:associatedObservationReference": {
            "@type": "@id"
        },
        "ac:startTimestamp": {
            "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
        },
        "ac:endTimestamp": {
            "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
        },
        "dcterms:type": {
            "@type": "@id"
        },
        "dcterms:format": {
            "@type": "@id"
        },
        "xmp:CreateDate": {
            "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
        },
        "dwc:dateIdentified": {
            "@type": "http://www.w3.org/2001/XMLSchema#date"
        }
    },
    "@graph": [
        {
            "@id": "https://www.inaturalist.org/observations/82716069",
            "@type": "http://purl.org/dc/dcmitype/Sound",
            "dcterms:title": "Northern Cardinal (Cardinalis cardinalis) on June 12, 2021 at 02:08 PM by cecildev8n5",
            "dcterms:identifier": "https://www.inaturalist.org/observations/82716069",
            "dcterms:type": "http://purl.org/dc/dcmitype/Sound",
            "ac:metadataLanguage": "http://id.loc.gov/vocabulary/iso639-2/eng",
            "dc:rights": "(c) 2021 cecildev8n5",
            "xmp:CreateDate": "2021-06-12T14:08:10.3-04:00",
            "ac:hasServiceAccessPoint": [
                {
                    "ac:accessURI": "https://static.inaturalist.org/sounds/251609.m4a?1623521443",
                    "dc:format": "audio/mp4",
                    "dcterms:format": "http://rs.tdwg.org/format/values/m015",
                    "ac:mediaDuration": 30.186,
                    "ac:mediaSpeed": 1.0
                },
                {
                    "ac:accessURI": "https://example.org/slomo/001",
                    "dc:format": "audio/mp4",
                    "dcterms:format": "http://rs.tdwg.org/format/values/m015",
                    "ac:mediaDuration": 150.93,
                    "ac:mediaSpeed": 0.2
                }
            ],
            "ac:hasROI": [
                {
                    "@id": "https://www.inaturalist.org/observations/82716069#cc1",
                    "dwc:scientificName": "Cardinalis cardinalis",
                    "dwc:identifiedBy": "cecildev8n5 | Caleb Helsel",
                    "dwc:dateIdentified": "2021-06-12",
                    "ac:associatedObservationReference": "https://www.gbif.org/occurrence/123456789",
                    "dcterms:description": "song of Northern Cardinal",
                    "ac:startTimestamp": "2021-06-12T14:08:12.1-04:00",
                    "ac:endTimestamp": "2021-06-12T14:08:15.4-04:00"
                },
                {
                    "@id": "https://www.inaturalist.org/observations/82716069#m",
                    "dwc:scientificName": "Neotibicen linnei",
                    "dwc:identifiedBy": "Steven J. Baskauf",
                    "dwc:dateIdentified": "2021-06-14",
                    "ac:associatedObservationReference": "https://www.gbif.org/occurrence/987654321",
                    "dcterms:description": "cicada song",
                    "ac:startTimestamp": "2021-06-12T14:08:16.5-04:00",
                    "ac:endTimestamp": "2021-06-12T14:08:20.2-04:00"
                },
                {
                    "@id": "https://www.inaturalist.org/observations/82716069#cc2",
                    "dwc:scientificName": "Cardinalis cardinalis",
                    "dwc:identifiedBy": "cecildev8n5 | Caleb Helsel",
                    "dwc:dateIdentified": "2021-06-12",
                    "ac:associatedObservationReference": "https://www.gbif.org/occurrence/123456789",
                    "dcterms:description": "song of Northern Cardinal",
                    "ac:startTimestamp": "2021-06-12T14:08:21.2-04:00",
                    "ac:endTimestamp": "2021-06-12T14:08:24.1-04:00"
                },
                {
                    "@id": "https://www.inaturalist.org/observations/82716069#cc3",
                    "dwc:scientificName": "Cardinalis cardinalis",
                    "dwc:identifiedBy": "cecildev8n5 | Caleb Helsel",
                    "dwc:dateIdentified": "2021-06-12",
                    "ac:associatedObservationReference": "https://www.gbif.org/occurrence/123456789",
                    "dcterms:description": "song of Northern Cardinal",
                    "ac:startTimestamp": "2021-06-12T14:08:32.8-04:00",
                    "ac:endTimestamp": "2021-06-12T14:08:36.4-04:00"
                }
            ]
        }
    ]
}
```

### Recipes

**Recipe 3.1 Calculate bounds of cicada ROI expressed as `ac:startTime` and `ac:endTime`**

```
ac:startTime = ac:startTimestamp - xmp:CreateDate
ac:startTime = 2021-06-12T14:08:16.5-04:00 - 2021-06-12T14:08:10.3-04:00
ac:startTime = 6.2
ac:endTime = ac:endTimestamp - xmp:CreateDate
ac:endTime = 2021-06-12T14:08:20.2-04:00 - 2021-06-12T14:08:10.3-04:00
ac:endTime = 9.9
```
