# Candidate Requirements

See <https://www.w3.org/TR/rdf-dawg-uc/> and <https://www.w3.org/TR/skos-ucr/> for example from W3C.

# Subject part

## 1 Categorization

1.1 Subject part values are grouped appropriately for broad categories of organisms (e.g. trees, quadrapeds, etc.). ([1-CATEGORIZE-1](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#1-categorize)) *Use [SKOS Collections](https://www.w3.org/TR/skos-primer/#seccollections) to create groups of concepts appropriate for categories of organisms.*

1.2 Links to trait ontologies would help standardize the labels, but the ontologies are not always accurate. There should be a way to take this into account. ([6-ANATOMY-1](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#6-anatomy)) *Do we want to be using trait ontologies or organism part ontologies for this? We need to curate a list of candidate ontologies. See [this list](https://github.com/tdwg/ac/blob/master/views/background.md#relevant-obo-foundry-ontologies) for a start.*

## 2 Factors influencing parts that are included

2.1 Associate appropriate subject parts with different developmental stages. ([3-MEASURE-2](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#3-measure)) *This is a broader issue beyond insects, (such as larval fishes where morphology changes dramatically, e.g. flounders) although it's probably the most apparent for that group because morphology changes so much between stages in insects.  Perhaps can be handled using SKOS collections as with broad organism categories.*

2.2 Semantics must distinguish between varying developmental stages. ([7-CLARITY-3](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#7-clarity)) *Is this actually different from the previous one?*

2.3 Associate appropriate subject parts with different orders of insects. ([3-MEASURE-3](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#3-measure)) *Similar to 2.2 .*

2.4 Semantics must distinguish between sexes. (added during discussion of 2.2)

## 3 Miscellaneous

*I'm thinking that 3.1 to 3.3 are ones that we should come back to after some more basic work roughing out the concept scheme.*

3.1 Allows specification of multiple parts in an image and/or inference of subparts from a larger whole ([2-FILTER-1](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#2-filter))

3.2 Semantics must distinguish between single and aggregate parts (e.g. one vs. several leaves). ([7-CLARITY-2](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#7-clarity))

3.3 Allows specification of whether entire part is visible in image ([2-FILTER-2](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#2-filter))

3.4 Semantics must distinguish between similar parts (flower bud vs. leaf bud). ([7-CLARITY-1](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#7-clarity)) *I think that this will go away with the use of SKOS since the concepts will be defined independently from the labels.  So there shouldn't be any label-based confusion about meaning (vs. simple text tags)*

# 4 Subject orientation

4.1 Allows for description of orientations of live subjects which were not controlled by the photographer: different body parts at different angles (ideally) (part of [2-FILTER-3](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#2-filter))

# 5 Relationship between part and viewing angle

*These items seem to be contingent on working out 3.1 to 3.3.*

5.1 Determine what orientations are appropriate for subject parts other than whole organism. ([3-MEASURE-4](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#3-measure))

5.2 Subject orientations are grouped appropriately for subject parts. ([1-CATEGORIZE-2](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#1-categorize))

5.3 For some organism groups, viewing angles must be related to particular morphological features so that selection of that angle would make the feature visible. ([8-ORIENT-1](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#8-orient))

5.4 Standardized image labels should indicate both the part of the plant photographed and, the view/orientation of the part (side view of the flower, top view etc.) ([5-KEYS-1](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#5-keys))

# 6 Best practice guides

*I think we tackle these at the end.*

6.1 Guidance for taking standardized images in the field. ([5-KEYS-2](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#5-keys))

6.2 Best practice guide for controlling specimen position to obtain standardized image orientation. ([3-MEASURE-1](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#3-measure))

6.3 Best practice guides for certain groups should suggest viewing angles and subject parts that illustrate the features most important for taxonomic identification. ([8-ORIENT-2](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#8-orient))

# Determined to be out of scope

X.1 Subject Part is hierarchical to nest appropriate terms under specimen vs. not-specimen (e.g. label). There might be a better term in AC for this, in which case, please disregard this use case here! ([4-ISLABEL-1](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#4-islabel)) *Is this out of scope for the vocabulary? Maybe there just needs to be an AC term for this?*

x.2 Allows for description of orientations of live subjects which were not controlled by the photographer:
- Intermediate angles of photograph (part of [2-FILTER-3](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#2-filter))

x.3 The view should contain the section "angle:" cross, longitudinal, oblique, tangential, radial/medial. ([6-ANATOMY-2](https://github.com/tdwg/ac/blob/master/views/submitted-use-cases.md#6-anatomy)) *This would be appropriate, but perhaps better to return to if there is more demand in the future. Also, need to distinguish between morphonlogy and anatomy.*

# Additional notes from discussion

A general term for the "usability" of a photo would be helpful, e.g. is it blurry?  There is the existing term `xmp:Rating`, but there is no scheme associatied with the rating numbers (from 1 to 5).  

It would also be useful to have some kind of term to indicate whether the organism was alive or dead (e.g. a specimen) when it was photographed.  There has been significant discussion about a similar term in Darwin Core (https://github.com/tdwg/dwc/issues/228), although that is probably related to Occurence status and not status when photographed.

-----
Revised 2020-01-21
