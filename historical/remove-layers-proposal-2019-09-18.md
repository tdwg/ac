# Proposal to remove layers from Audubon Core

## Background

When the Audubon Core standard was adopted on 2013-10-23, Section 2 of the [Structure document](https://tdwg.github.io/ac/structure/) defined a "layer" property as follows:

> AC terms are divided into two Layers. Those characterized as in Layer 1, including the four mandatory terms, should be meaningfully handled by all consuming client applications. Only wholly complete consuming applications need handle those in the Layer 2. What is meant by “meaningfully handle” is up to implementers of this normative specification. It could be as simple as “gracefully ignore”.

In the [Term List document](https://tdwg.github.io/ac/termlist/), each term had an attribute telling whether it was in Layer 1 or 2.

## Rationale for the change

When the [TDWG Vocabulary Maintenance Specification](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md) came out in 2017, it embraced the idea that TDWG vocabularies would include a basic layer of terms.  Vocabularies could be enhanced by communities of interest that built upon the basic layer by applying constraints to the basic layer.  There could be multiple enhancements to serve the purposes of those communities (Section 1.4).  Working groups can establish enhancements as coordinated additions to vocabularies based on need (Section 4.1).  

Given this outlook on vocabulary development, dividing vocabulary terms into general Layer 1 and 2 categories does not seem to belong as part of the general definition of terms.  Rather, specific communities would be likely to designate which terms are most important for uses in their community.  Those sets of terms are likely to be different if the media items are still images, audio, video, or 3D images.  In essence, communities could establish application profiles based on Audubon Core in order to meet the specific needs of their community.

Another complicating factor is that currently, none of the borrowed Darwin Core terms organized under the Location class have assigned layers.  If this proposal is adopted, that problem becomes moot.

## Proposed changes

In Section 2 of the Structure document, strike the following paragraph:

> AC terms are divided into two Layers. Those characterized as in Layer 1, including the four mandatory terms, should be meaningfully handled by all consuming client applications. Only wholly complete consuming applications need handle those in the Layer 2. What is meant by “meaningfully handle” is up to implementers of this normative specification. It could be as simple as “gracefully ignore”.

In the next paragraph change the text:

> In addition, a term has an attribute telling whether it is mandatory, one telling whether it is repeatable, and one telling whether it is in Layer 1 or 2. Layer 2 comprises terms likely to only occur for certain media. For example, the term DateAvailable will apply only to media that are embargoed, but for which the provider is prepared to make the metadata immediately available.

to:

> In addition, a term has an attribute telling whether it is mandatory and one telling whether it is repeatable.

In the Term List document, delete Section 4 (Layers).  In the metadata for each term, remove the Layer designation.  The corresponding layer metadata will also be removed from the machine-readable metadata.

## Possible implications for interoperability and stability of the vocabulary

Since the proposed changes will make Audubon Core less constrained than originally defined, they are not likely to have negative implications on interoperability and stability.  This change will free up communities of practice to establish guidelines that are more narrowly applicable to their needs rather than requiring them to follow a one-size-fits all approach.

# History of this proposal

2019-07-30 Drafted by Steve Baskauf

2019-08-29 Discussed during [Audubon Core Maintenance Group call](https://github.com/tdwg/ac/blob/master/historical/2019-08-29-meeting-notes.pdf) and approval given to proceed with change.

2019-09-18 Thirty day public comment period announced on tdwg-content
