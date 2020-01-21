# Submitted use cases and comments

# 1-CATEGORIZE

**Name of use case:** Categorization of images at acquisition

**Submitter:** Steve Baskauf

**Submitter's institution:** Vanderbilt University Libraries

**Goal:** Image creator is guided to photograph appropriate subject parts and orientations at time of image acquisition through interaction with software.

**Anticipated users:** bioblitz participant, image aggregator

**Scenario:**  Jo is participating in a bioblitz that is using an app to document organisms in a park.  She sees a tree that she would like to document.  Through a dropdown, she selects the general category of organisms she's observing (tree) and the app provides possible organism parts she should photograph.  She selects leaf and the app provides guidance on appropriate orientations and viewing angles for the leaf.  She selects the orientation she is using, then takes the image.  The app then suggests additional parts that she should document, graying out ones that she has fully documented.  When she has fully documented the tree, she indicates that she is done and the values for subject orientation and subject part are transmitted to the image aggregator.  

**Requirements:**

1. Subject part values are grouped appropriately for broad categories of organisms (e.g. trees, quadrapeds, etc.). (1-CATEGORIZE-1)
2. Subject orientations are grouped appropriately for subject parts. (1-CATEGORIZE-2)

# 2-FILTER

**Name of use case:** Filtering images for desired views

**Submitter:** Matthew Nielsen

**Submitter’s institution:** University of Stockholm

**Goal:** Filter images for appropriate views for later morphometric analyses.

**Anticipated users:** ecologist/evolutionary biologist

**Scenario:** Carlos has access to a very large database of camera trap images of bobcats (Lynx rufus). He would like to test Allen’s rule in this species using these images (that limbs are proportionally shorter at higher latitudes/in colder environments). Most of these images won’t provide what he needs either because they don’t contain all of the limbs in question or are taken from an inappropriate angle. Fortunately for Carlos, all these images are already annotated using our ventral controlled views system thanks to a very clever imaging program (or, more likely, many undergrads). Because of this, he can specify what body parts he needs to be able to measure, from what sides, and automatically filter for the subset of images which meet those criteria. Once done, he has a subset of images that another very clever imaging program (or, more likely, even more undergrads) can take measurements from to get measures of relative limb length.

**Requirements:**

1. Allows specification of multiple parts in an image and/or inference of subparts from a larger whole (2-FILTER-1)
2. Allows specification of whether entire part is visible in image (2-FILTER-2)
3. Allows for description of orientations of live subjects which were not controlled by the photographer:
- Intermediate angles of photograph
- Different body parts at different angles (ideally) (2-FILTER-3)

# 3-MEASURE

**Name of Use Case:** Standardized insect images from a collection

**Submitter:** Neil Cobb

**Submitter's institution:** SCAN

**Goal:** Describe important gross morphological features in insects derived from images of pinned specimens

**Anticipated users:** Research users of insect specimens

**Scenario:** Benin would like to obtain reliable estimates of area, shape, length, width of entire body and major body parts including head, thorax, abdomen and wings and any obvious appendages. She would also like to assess the maculation and color of those parts.  Her team photographs the specimens following a best practice guide for imaging insect specimens, which includes guidance on systematically photographing dorsal, ventral, lateral, and frontal aspects of the whole specimen as well as additional images focusing on specific parts such as antennae and bristles.  The images are measured via processing software and the collected data is ingested into her database.  

**Requirements:** 

1. Best practice guide for controlling specimen position to obtain standardized image orientation. (3-MEASURE-1)
2. Associate appropriate subject parts with different insect life stages. (3-MEASURE-2)
3. Associate appropriate subject parts with different orders of insects. (3-MEASURE-3)
4. Determine what orientations are appropriate for subject parts other than whole organism. (3-MEASURE-4)

# 4-ISLABEL

**Name of Use Case:** Filtering media showing specimen vs. label

**Submitter:** Erica Krimmel

**Submitter's institution:** iDigBio

**Goal:** Filter images based on whether the subject is specimen or label

**Anticipated users:** Individual users of digitized specimen media; third-party media aggregators

**Scenario:** The Paleobiology Database (<https://paleobiodb.org>) would like to be able to display specimen images representing the taxon *Alectryonella plicatula*. They are able to pull images from iDigBio via the ePANDDA API but they do not want to include images of specimen labels, only the specimens themselves. See <https://paleobiodb.org/classic/basicTaxonInfo?taxon_no=309883> for live example. Media should be able to use controlled vocabulary for Subject Part that is more specific than "specimen," e.g. "right valve."

**Requirements:** 

1. Subject Part is hierarchical to nest appropriate terms under specimen vs. not-specimen (e.g. label). There might be a better term in AC for this, in which case, please disregard this use case here! (4-ISLABEL-1)


# 5-KEYS

**Name of Use Case:** Online keys

**Submitter:** Bruce Kirchoff

**Submitter's institution:** University of North Carolina at Greenboro

**Goal:** To create online, visually rich keys and identification guides to plants

**Anticipated users:** image aggregator, herbaria, botanical gardens, taxonomists

**Scenario:** Taxonomists and field biologists regularly take photographs plants in the field and upload them to various websites. Image aggregator's like botanical gardens, herbaria and the USDA (plants.gov) would like to use these images to illustrate taxonomic treatments and create identification guides. For this they need images labeled with the part of the plant that they show, and the view of that part. With this information they can automatically crate plates/tables that show comparable parts of different species in comparable ways.

**Requirements:** 

1. Standardized image labels should indicate both the part of the plant photographed and, the view/orientation of the part (side view of the flower, top view etc.) (5-KEYS-1)
2. Guidance for taking standardized images in the field. (5-KEYS-2)


# 6-ANATOMY

**Name of Use Case:** Anatomical image collection

**Submitter:** Bruce Kirchoff

**Submitter's institution:** University of North Carolina at Greensboro

**Goal:** Labels for plant anatomical images such as those at the Cornell Plant Anatomy site (<http://cupac.bh.cornell.edu/cgi-bin/cupac/cupac_keyword_search.pl?keyword=ovary>) are needed.

**Anticipated users:** image aggregators, plant anatomists and morphologists

**Scenario:** A plant anatomist, morphologist or taxonomists collects micrographs of plant parts from sectioned material. She wants to label the parts so that comparisons can be made. Image aggregators like Cornell want to draw high quality microscopic images into their collections. For this they need to know not only the taxonimic identity of the image but also whether it is a cross or longitudinal section, and what part of the plant it is from. A cross section of a plant ovary, for instance. In cases where the organ has a complex structure, it is necessary to label the part of the organ where the section was taken - mid-locular region of the ovary, for instance.

**Requirements:** 

1. Links to trait ontologies would help standardize the labels, but the ontologies are not always accurate. There should be a way to take this into account. (6-ANATOMY-1)
2. The view should contain the section "angle:" cross, longitudinal, oblique, tangential, radial/medial. (6-ANATOMY-2)



# 7-CLARITY

**Comment regarding clear semantics**

**Submitter:** Ken-ichi Ueda

**Submitter's institution:** iNaturalist

**Note:** Specifically regarding ac:subjectPart, ac:subjectOrientation, we don't currently have data like this that pertains to individual photos, but we could certainly develop tools that allow our users to annotate photos with such values. I suspect the most important factors for us would clear semantics (if a photo is of a bud, is that a flower bud or a leaf bud?) and values that encompass all possible states (if the values are "leaf" and "flower" what are people supposed to do with a photo of a bud, or 10 leaves, or roots; an "other" category?). These are the kinds of problems we've run into with our existing annotation functionality (which applies to observations, not photos).

**Requirements:** 

1. Semantics must distinguish between similar parts (flower bud vs. leaf bud). (7-CLARITY-1)
2. Semantics must distinguish between single and aggregate parts (e.g. one vs. several leaves). (7-CLARITY-2)
3. Semantics must distinguish between varying developmental stages. (7-CLARITY-3)

# 8-ORIENT

**Comments regarding viewing angle**

**Submitter:** Tim Robertson

**Submitter's institution:** GBIF

The obvious use case would be to allow an image gallery of e.g. pinned insects of species X to all be oriented to show the frons/vertex or so, which could help someone pull up a reference to compare with as they're looking down their microscope. We have ideas to do that on <https://www.gbif.org/occurrence/gallery?q=antweb> at some point.

I can only guess, but imagine it may be useful for iNaturalist users to be informed that a better identification (human or machine) may be possible if they take a photo at an alternative angle - e.g. the underside of the mushroom fruit which the casual observer may not know about. Knowing the orientation and using it as a prior when training an MV model might be an area for someone in the AI space to research (but I'd assume we've got better gains to make with improvement in location/season priors).

**Requirements:** 

1. For some organism groups, viewing angles must be related to particular morphological features so that selection of that angle would make the feature visible. (8-ORIENT-1)
2. Best practice guides for certain groups should suggest viewing angles and subject parts that illustrate the features most important for taxonomic identification. (8-ORIENT-2)

-----
Revised 2020-01-20