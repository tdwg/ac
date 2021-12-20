# Regions of Interest (ROI) Recipes

The complete draft is [here](https://docs.google.com/document/d/1oTbL_RdtlO288Ixw9vYK7DQgBH6UXfRadvD5s4CER6g/edit?usp=sharing).

This page will eventually hold the document, which is currently under construction.

## 1. Still image

This example involves a still image of a plant. The image was intended to illustrate the characteristics of fruit of the plant, but it unintentionally included evidence of a leaf-mining moth in one of the background leaves. The fruit and mine are designated within the image using regions of interest. 

### Tabular serialization of the data

**Table 1. Metadata about the abstract media item.**
<https://github.com/tdwg/ac/blob/master/fragments/transformation_examples/media.csv>

|| dcterms:identifier | dcterms:title | ac:metadataLanguage | dc:rights | dcterms:type ||
|| ---- | ---- | ---- | ---- | ---- ||
|| http://bioimages.vanderbilt.edu/hessd/e5384 | Tragia cordata (Euphorbiaceae) - fruit – juvenile | http://id.loc.gov/vocabulary/iso639-2/eng | (c) 2008 Darel Hess | http://purl.org/dc/dcmitype/StillImage

**Table 2. Metadata about service access points (SAP) for the media item.**
<https://github.com/tdwg/ac/blob/master/fragments/transformation_examples/sap.csv>

|| dcterms:identifier | ac:variantLiteral | dc:format | exif:PixelXDimension | exif:PixelYDimension | ac:accessURI ||
|| ---- | ---- | ---- | ----- | ----- | ---- ||
|| http://bioimages.vanderbilt.edu/hessd/e5384 | Best Quality | image/jpeg | 2112 | 2526 | https://iiif.library.vanderbilt.edu/iiif/3/bioimages%2Fhessd%2Ftrco--fr040529-17e5384.jpg/full/max/0/default.jpg ||
|| http://bioimages.vanderbilt.edu/hessd/e5384 | Good Quality | image/jpeg | 856 | 1024 | https://iiif.library.vanderbilt.edu/iiif/3/bioimages%2Fhessd%2Ftrco--fr040529-17e5384.jpg/full/856,/0/default.jpg ||

**Table 3. Metadata about regions of interest (ROI) within the media item**
<https://github.com/tdwg/ac/blob/master/fragments/transformation_examples/roi.csv>

|| dcterms:identifier | ac:isROIOf | ac:xFrac |ac:yFrac | ac:widthFrac | ac:heightFrac | dcterm:description | dwc:scientificName | dwc:identifiedBy | ac:associatedObservationReference ||
|| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- ||
|| http://bioimages.vanderbilt.edu/hessd/e538#roi1 | http://bioimages.vanderbilt.edu/hessd/e5384 | 0.28939 | 0.23674 | 0.09066 | 0.26373 | mine | Cyphacma tragiae | Terry Harrison | https://www.gbif.org/occurrence/930742101 ||
|| http://bioimages.vanderbilt.edu/hessd/e538#roi2 | http://bioimages.vanderbilt.edu/hessd/e5384 | 0.21892 | 0.44792 | 0.28147 | 0.34612 | fruit | Tragia cordata | Darel Hess | || 

### JSON-LD serialization of the data

**Serialization 1.**

<https://github.com/tdwg/ac/blob/master/fragments/transformation_examples/image_graph_hess.json>

```
{
    "@context": 
        {
            "ac": "http://rs.tdwg.org/ac/terms/",
            "dwc": "http://rs.tdwg.org/dwc/terms/",
            "dc": "http://purl.org/dc/elements/1.1/",
            "dcterms": "http://purl.org/dc/terms/",
            "exif": "http://ns.adobe.com/exif/1.0/",
            "ac:metadataLanguage": {"@type": "@id"},
            "ac:accessURI": {"@type": "@id"},
            "ac:associatedObservationReference": {"@type": "@id"},
            "dcterms:type": {"@type": "@id"},
            "dcterms:format": {"@type": "@id"}
        },
    "@graph": 
        [
            {
                "@id": "http://bioimages.vanderbilt.edu/hessd/e5384",
                "@type": "http://purl.org/dc/dcmitype/StillImage",
                "dcterms:title": "Tragia cordata (Euphorbiaceae) - fruit – juvenile",
                "dcterms:identifier": "http://bioimages.vanderbilt.edu/hessd/e5384",
                "dcterms:type": "http://purl.org/dc/dcmitype/StillImage",
                "ac:metadataLanguage": "http://id.loc.gov/vocabulary/iso639-2/eng",
                "dc:rights": "(c) 2008 Darel Hess",
                "ac:hasServiceAccessPoint": 
                    [
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
            "ac:hasROI": 
                [
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

Note that ac:xFrac was provided with sufficient precision to specify the exact pixel used to originally delineate the bounding box.

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


