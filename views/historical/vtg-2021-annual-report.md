# Views Controlled Vocabuaries Task Group

## Task Group Annual Report

### Web Site:
https://github.com/tdwg/ac/tree/master/views

### Convener(s):
Steve Baskauf - [steve.baskauf@vanderbilt.edu](mailto:steve.baskauf@vanderbilt.edu)

### Submitted:
2021-11-09

## Phase of work:
The Views Controlled Vocabularies Task Group is chartered under the Audubon Core 
Maintenance Group. It is tasked with developing controlled vocabularies for the Audubon 
Core terms `ac:subjectPart` and `ac:subjectOrientation`, which are sometimes collectively 
referred to as a "view". 

The Task Group has completed work on developing draft vocabularies and is proceeding toward collecting implementation experience.

## Activities:
- The Task Group met five times during 2021 and will meet once more at a workshop associated with the TDWG Annual Meeting. The notes for those meetings can be viewed in the group's [historical documents directory](https://github.com/tdwg/ac/tree/master/views/historical) of its GitHub repository.
- The group's work this year revolved mainly around the details of developing the controlled vocabularies themselves, while taking into consideration the draft requirements. Key considerations were determining how the orientation terms would be related to each of the subject part terms and how the subject parts would be grouped by organism type. We also struggled with the appropriate level of granularity for organism groups and subjectPart (particularly with insects), but eventually reached a consensus.
- Links were made from each proposed term to one of the well-known OBO ontologies that define organism parts and spatial orientations.
- We considered how the subjectPart and subjectOrientation values would be linked to Regions of Interest within still images as that proposal developed. We did some experimenting with applying the draft values to composite fish images using the draft ROI terms. 


## Accomplishments:
- At our 2021-05-19 meeting, we finalized the requirements, which have been assembeled into a [draft final requirements document](https://github.com/tdwg/ac/blob/master/views/final-requirements.md), to meet in part the [Feature Report requirement](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md#421-feature-report) for vocabulary enhancements as required by the Vocabulary Maintenance Specification. The final requirements were scaled back considerably from the candidate requirements, which were far more ambitious that what was feasibly in scope for the Task Group to handle in this iteration. 
- A [draft `subjectPart` controlled vocabulary](https://github.com/tdwg/ac/blob/master/views/subjectPart.md) was assembled as a SKOS Concept Scheme. It is also available in [machine-readable JSON-LD form](https://tdwg.github.io/rs.tdwg.org/cvJson/acpart.json). 
- A [draft `subjectOrientation` controlled vocabulary](https://github.com/tdwg/ac/blob/master/views/subjectOrientation.md) was assembled as a SKOS Concept Scheme. It is also available in [machine-readable JSON-LD form](https://tdwg.github.io/rs.tdwg.org/cvJson/acorient.json). 
- To indicate which `subjectPart` values are appropriate for organism groups, a set of SKOS Collections were developed, with a collection for each organism group. Those collections can be used to generate a picklist appropriate for a group, or to carry out data validation. The collections are avaiable in [machine-readable JSON-LD form](https://tdwg.github.io/rs.tdwg.org/cvJson/acpart_collection.json).
- To indicate which `subjectOrientation` values are appropriate for each subject part, a set of SKOS Collections were developed, with a collection for each part. Those collections can be used to create picklists or for validation. The collections are avaiable in [machine-readable JSON-LD form](https://tdwg.github.io/rs.tdwg.org/cvJson/acorient_collection.json).

## Impediments to progress
The convener ran out of bandwidth to move things forward during part of the year.

## Changes in goals or scope
There are no anticipated major changes in goals or scope.

## Plans for next calendar year
The task group is currently soliciting test implementers and during the next year will acquire data on implementation experience from them. We hope to complete work and submit the vocabularies for ratification in 2022.
