# Final Requirements - draft 2021-11-07

These requirements were filtered from an [original list of candidate requirements](https://github.com/tdwg/ac/blob/master/views/candidate-requirements.md) at the 2021-05-19 Task Group meeting. The links following a requirement lead to the [submitted use cases](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md) that generated that requirement.

# Subject part

## 1 Categorization

1.1 Subject part values are grouped appropriately for broad categories of organisms (e.g. woody angiosperms, insects, etc.). Selecting a [SKOS Collection](https://www.w3.org/TR/skos-primer/#seccollections) will allow a user to find a group of part concepts appropriate for a particular category of organisms. ([1-CATEGORIZE-1](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#1-categorize)) 

1.2 Concepts are linked to well-known ontologies to clarify definitions and standardized labels. However, the actual concepts are TDWG-adopted terms, providing stability that might not exist in the source ontologies. ([6-ANATOMY-1](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#6-anatomy)) Ontologies used were the Biological Spatial Ontology (BSPO, http://www.ontobee.org/ontology/BSPO), Phenotype and Trait Ontology (PATO, http://www.ontobee.org/ontology/PATO), Common Anatomy Reference Ontology (CARO, http://www.ontobee.org/ontology/CARO), Plant Ontology (PO, http://www.ontobee.org/ontology/PO), Uber-anatomy Ontology (UBERON, https://www.ebi.ac.uk/ols/ontologies/uberon), Drosophila gross anatomy Ontology (FBBT, http://www.ontobee.org/ontology/FBBT), and Ontology for the Anatomy of the Insect SkeletoMuscular system (AISM, https://www.ebi.ac.uk/ols/ontologies/aism).

1.3 Concepts allow for distinguishing between sexes (if multimorphic) by selecting narrower categories of subjectPart.  (added during discussion)

1.4 Specify multiple parts in an image by applying subjectPart concepts to Regions of Interest within an image. ([2-FILTER-1](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#2-filter))

1.5 Distinguish between single and aggregate parts (e.g. one vs. several leaves) by applying multiple subjectPart concepts of the same type to Regions of Interest within a single image. ([7-CLARITY-2](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#7-clarity))

# 2 Relationship between part and orientation

2.1 Determine what orientations are appropriate for subject parts other than whole organism. ([3-MEASURE-4](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#3-measure) [1-CATEGORIZE-2](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#1-categorize))

2.2 For some organism groups, filter orientations so that selection is only possible if the feature is visible for a particular subject part. ([8-ORIENT-1](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#8-orient))

-----
Revised 2021-11-07
