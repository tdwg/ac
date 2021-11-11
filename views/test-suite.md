# Test suite - draft 2021-11-11

This document describes information to be collected from test implementers. 

# Implementer metadata

| field | description |
| ----- | ----------- |
| organization_name | The organization conducting the testing |
| organization_url | URL of the organization's home page |
| contact_name | The name of the person to be contacted about the report |
| contact_email | The email address of the contact person |
| taxonomic_coverage | Plain text description of the highest taxonomic level covered in the testing (e.g. "insects") |
| number_images | the approximate number of images used in the testing |
| type_images | "live organisms", "digitized specimens", or "both" |

# Test categories

These fields will have values of "x" (tested) or "o" (not tested)

| field | description |
| ----- | ----------- |
| manual_entry | Testers referred to controlled value string lists or spreadsheets and decided what to enter into a spreadsheet |
| machine_guided | Testers were presented with label choices by an application, which dermined the controlled value and entered it into content management system |
| machine_processed | Values were processed by an application. Possible uses: automatic conversion of existing data to controlled values, quality control on manually entered data |

# Feature utilization

These fields will have values of "x" (utilized) or "o" (not utilized) depending on whether or not a particular feature was utilized. Not all categories will apply to all implementers.

## General (all implementers)

| field | description |
| ----- | ----------- |
| subjectPart | provided values for ac:subjectPart or ac:subjectPartLiteral |
| subjectOrientation | provided values for ac:subjectOrientation or ac:subjectOrientationLiteral |
| strings | utilized controlled value strings for concepts |
| iri | utilized concept IRIs | 
| lists | used human-readable lists |
| csv | used CSV tables |
| json | used JSON files |

## Manual entry

| field | description | requirement |
| ----- | ----------- | ----------- |
| select_group | users selected a collection of part concepts appropriate for a particular organism group | 1-CATEGORIZE-1 |
| select_part | users selected a collection of orientation concepts appropriate for a particluar part | 1-CATEGORIZE-2 |
| broader | users had the option to select broader or narrower categories (e.g. male/female cones vs. "cone", left/right side vs. lateral view) | not coded |
| roi | users applied concepts to Regions of Interest (ROIs) as opposed to only whole images | 2-FILTER-1 |
| multiple | users sometimes applied concepts to more than one ROI per image | 7-CLARITY-2 |

## Machine-guided entry

| field | description | requirement |
| ----- | ----------- | ----------- |
| select_group | users selected a collection of part concepts appropriate for a particular organism group | 1-CATEGORIZE-1 |
| restrict_part | users were restricted to a collection of orientation concepts appropriate for a particluar part | 8-ORIENT-1 |
| ontology_link | users were directed to an ontology term to clarify a concept definition | 6-ANATOMY-1 |
| broader | users had the option to select broader or narrower categories (e.g. male/female cones vs. "cone", left/right side vs. lateral view) | not coded |
| roi | users applied concepts to Regions of Interest (ROIs) as opposed to only whole images | 2-FILTER-1 |
| multiple | users sometimes applied concepts to more than one ROI per image | 7-CLARITY-2 |


## Machine processing

| field | description |
| ----- | ----------- |
| machine_matching | concepts were determined without human intervention by matching to existing text view descriptions | 
| qc | possible errors were flagged by testing whether parts or orientations were present in collections appropriate for that concept scheme | 
| entailment | additional concepts were generated automatically by asserting broader concepts when narrower ones were selected |
| ml_part | used computer vision (machine learning) to automatically detect organism parts |

# General feedback

These are free response fields

1. Please provide information about any circumstances where human users had difficulty selecting an appropriate concept for a view.

2. Please describe any important concepts appropriate for a collection that were missing.

3. Please list any organism group collections that were insufficiently granualar to designate the relevant organism parts important to your work (e.g. need a collection for "hemiptera" rather than the generic "insects")

4. Please list any organism categories for which you have images with which you were unable to use the existing organism collections (i.e. there is no existing organism group collection that applies)


-----
Revised 2021-11-11
