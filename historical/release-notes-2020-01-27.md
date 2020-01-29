# Release Notes for Audubon Core 2020-01-27 Version

**Date:** 2020-01-29

**Author:** Steve Baskauf - Audubon Core Maintenance Group convener

## Scope

The 2020-01-27 version of Audubon Core updates two documents: the [Audubon Core Term List](https://tdwg.github.io/ac/termlist/) and [Audubon Core Structure](https://tdwg.github.io/ac/structure/), and the Audubon Core vocabulary itself.

## Summary of changes

The changes made in this version represent the end of a two-year effort by the Maintenance Group to clean up the Audubon Core documentation, which had not been maintained for five years.

### Major changes to the vocabulary

1. [One new term has been added](https://github.com/tdwg/ac/issues/137) to the vocabulary: `ac:ServiceAccessPoint`, a class whose existence was implied but not explicitly defined in the previous version.

1. The [`tdwgutility:layers` property](https://tdwg.github.io/ac/termlist/2013-10-23#4-layers) has [been removed from the metadata of all terms](https://github.com/tdwg/ac/issues/143) in the vocabulary. It was unclear how this property would be used by communities in which terms would have varying importance and it was not generally used.

1. The usage guidelines for `dc:type` and `dcterms:type` underwent [major revisions](https://github.com/tdwg/ac/issues/144) in an attempt to clarify how they should be used.

These changes were [approved by the TDWG Executive Committee on 2019-12-01](https://github.com/tdwg/rs.tdwg.org/blob/master/decisions/decisions.csv) following a period of public comment.

### Minor changes to the vocabulary

A smaller number of changes were made to normative term definitions or usage guidelines. Those changes are summarized [here](https://github.com/tdwg/ac/blob/master/historical/minor-errata-definition-changes-2020-01-27-version.pdf). In an effort to maintain the stability of the vocabulary, these changes primarily affected the clarity of the metadata and not term meanings nor usage guidelines. Nevertheless, Audubon Core implementers should review these changes carefully to ensure conformance.

### Additional clarifications and corrections to term metadata

A large number of changes were made to non-normative term metadata, or to fix incorrect placement of text within the definitions, usage guidelines, and notes. In the determination of the Maintenance Group, these changes fell into the category of minor editorial errata not requiring notification, but the changes are documented in [this issue](https://github.com/tdwg/ac/issues/130) and [this document](https://docs.google.com/document/d/12Ck4t_x9LtG0BgPuBcNNqtYppNCP_Rj5F7bdgkmFvGY/edit?usp=sharing) for reference.

### Changes to documents

1. Conformance to RFC 2119 (use of keywords). 