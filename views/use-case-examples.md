# Use case examples

## Background

The [Views Controlled Vocabularies Task Group](https://github.com/tdwg/ac/tree/master/views) is collecting use cases to guide the development process of controlled vocabularies for the Audubon Core terms `ac:subjectOrientation` and `ac:subjectPart`.  For reference, here are the definitions of the two terms:

---

**Term Label:** Subject Orientation

**Definition:** Specific orientation (= direction, view angle) of the subject represented in the media resource with respect to the acquisition device.

**Notes:** Examples: "dorsal", "ventral", "frontal", etc. No formal encoding scheme as yet exists. The term is repeatable e.g., in the case of a composite image, consisting of a combination of different view orientations.

---

**Term Label:** Subject Part

**Definition:** The portion or product of organism morphology, behaviour, environment, etc. that is either predominantly shown or particularly well exemplified by the media resource.

**Notes:** No formal encoding scheme as yet exists. Examples are "whole body", "head", "flower", "leaf", "canopy" (of a rain forest stand). Several anatomical ontologies are emerging in http://www.obofoundry.org/

---

## Purpose

The purpose of use cases is to gather input from potential user communities in order to establish the requirements that must be met by the completed vocabularies.  The central part of the use case is a story describing how the vocabularies would be used.  

The requirements can include not only particular necessary values, but also how the values are structured hierarchically or grouped. 

# Examples

The following examples are actual use cases submitted by core members of the Task Group

## First example: categorization in an app

**Name of use case:** Categorization of images at acquisition

**Submitter:** Steve Baskauf

**Submitter's institution:** Vanderbilt University Libraries

**Goal:** Image creator is guided to photograph appropriate subject parts and orientations at time of image acquisition through interaction with software.

**Anticipated users:** bioblitz participant, image aggregator

**Scenario:**  Jo is participating in a bioblitz that is using an app to document organisms in a park.  She sees a tree that she would like to document.  Through a dropdown, she selects the general category of organisms she's observing (tree) and the app provides possible organism parts she should photograph.  She selects leaf and the app provides guidance on appropriate orientations and viewing angles for the leaf.  She selects the orientation she is using, then takes the image.  The app then suggests additional parts that she should document, graying out ones that she has fully documented.  When she has fully documented the tree, she indicates that she is done and the values for subject orientation and subject part are transmitted to the image aggregator.  

**Requirements:**
1. Subject part values are grouped appropriately for broad categories of organisms (e.g. trees, quadrapeds, etc.). 
2. Subject orientations are grouped appropriately for subject parts. 

## Second example: filtering images

**Name of use case:** Filtering images for desired views

**Submitter:** Matthew Nielsen

**Submitter’s institution:** University of Stockholm

**Goal:** Filter images for appropriate views for later morphometric analyses.

**Anticipated users:** ecologist/evolutionary biologist

**Scenario:** Carlos has access to a very large database of camera trap images of bobcats (Lynx rufus). He would like to test Allen’s rule in this species using these images (that limbs are proportionally shorter at higher latitudes/in colder environments). Most of these images won’t provide what he needs either because they don’t contain all of the limbs in question or are taken from an inappropriate angle. Fortunately for Carlos, all these images are already annotated using our ventral controlled views system thanks to a very clever imaging program (or, more likely, many undergrads). Because of this, he can specify what body parts he needs to be able to measure, from what sides, and automatically filter for the subset of images which meet those criteria. Once done, he has a subset of images that another very clever imaging program (or, more likely, even more undergrads) can take measurements from to get measures of relative limb length.

**Requirements:**
1. Allows specification of multiple parts in an image and/or inference of subparts from a larger whole
2. Allows specification of whether entire part is visible in image
3. Allows for description of orientations of live subjects which were not controlled by the photographer:
- Intermediate angles of photograph
- Different body parts at different angles (ideally)

## Third example: standardized insect collection images

**Name of Use Case:** Standardized insect images from a collection

**Submitter:** Neil Cobb

**Submitter's institution:** SCAN

**Goal:** Describe important gross morphological features in insects derived from images of pinned specimens

**Anticipated users:** Research users of insect specimens

**Scenario:** Benin would like to obtain reliable estimates of area, shape, length, width of entire body and major body parts including head, thorax, abdomen and wings and any obvious appendages. She would also like to assess the maculation and color of those parts.  Her team photographs the specimens following a best practice guide for imaging insect specimens, which includes guidance on systematically photographing dorsal, ventral, lateral, and frontal aspects of the whole specimen as well as additional images focusing on specific parts such as antennae and bristles.  The images are measured via processing software and the collected data is ingested into her database.  

**Requirements:** 
1. Best practice guide for controlling specimen position to obtain standardized image orientation.
2. Associate appropriate subject parts with different insect life stages.
3. Associate appropriate subject parts with different orders of insects.
4. Determine what orientations are appropriate for subject parts other than whole organism.



-----
Revised 2019-09-17