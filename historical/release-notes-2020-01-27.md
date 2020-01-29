# Release Notes for Audubon Core 2020-01-27 Version

**Date:** 2020-01-29

**Author:** Steve Baskauf - Audubon Core Maintenance Group convener

## Scope

The 2020-01-27 version of the [Audubon Core standard](https://www.tdwg.org/standards/ac/) updates the Audubon Core vocabulary and two documents: the [Audubon Core Term List](https://tdwg.github.io/ac/termlist/) and [Audubon Core Structure](https://tdwg.github.io/ac/structure/).

## Summary of changes

The changes made in this version represent the end of a two-year effort by the Maintenance Group to clean up the Audubon Core documentation, which had not been maintained for five years after its adoption. In this revision, there were no major semantic changes to the vocabulary. Nearly all of the changes were intended to clarify the metadata and documentation associated with the Audubon Core vocabulary without affecting stability and interoperability. The details of the changes are summarized in the following sections.

### Major changes to the vocabulary

1. [One new term has been added](https://github.com/tdwg/ac/issues/137) to the vocabulary: `ac:ServiceAccessPoint`, a class whose existence was implied but not explicitly defined in the previous version.

1. The [`tdwgutility:layers` property](https://tdwg.github.io/ac/termlist/2013-10-23#4-layers) has [been removed from the metadata of all terms](https://github.com/tdwg/ac/issues/143) in the vocabulary. It was unclear how this property would be used by communities in which terms would have varying importance and it was not generally used.

1. The usage guidelines for `dc:type` and `dcterms:type` underwent [major revisions](https://github.com/tdwg/ac/issues/144) in an attempt to clarify how they should be used.

These changes were [approved by the TDWG Executive Committee on 2019-12-01](https://github.com/tdwg/rs.tdwg.org/blob/master/decisions/decisions.csv) following a period of public comment.

### Minor changes to the vocabulary

A smaller number of changes were made to normative term definitions or usage guidelines. Those changes are summarized [here](https://github.com/tdwg/ac/blob/master/historical/minor-errata-definition-changes-2020-01-27-version.pdf). In an effort to maintain the stability of the vocabulary, the changes primarily affected the clarity of the metadata and not term meanings nor usage guidelines. Nevertheless, Audubon Core implementers should review these changes carefully to ensure conformance with the standard.

### Additional clarifications and corrections to term metadata

A large number of changes were made to non-normative term metadata, or to fix incorrect placement of text within the definitions, usage guidelines, and notes. In the determination of the Maintenance Group, these changes fell into the category of minor editorial errata not requiring notification, but the changes are documented in [this issue](https://github.com/tdwg/ac/issues/130) and [this document](https://docs.google.com/document/d/12Ck4t_x9LtG0BgPuBcNNqtYppNCP_Rj5F7bdgkmFvGY/edit?usp=sharing) for reference.

### Changes to documents

In addition to the changes above, which are reflected in the new version of the [Term List document](https://tdwg.github.io/ac/termlist/), there were two other significant changes to the two Audubon Core documents containing normative content: the [Term List](https://tdwg.github.io/ac/termlist/) and [Structure](https://tdwg.github.io/ac/structure/) documents.

1. **Conformance to RFC 2119 (use of keywords)**. To complete the process of bringing Audubon Core documents into conformance with the [TDWG Standards Documentation Specification](https://github.com/tdwg/vocab/blob/master/sds/documentation-specification.md), the guidelines of [RFC 2119](http://tools.ietf.org/html/rfc2119) were implemented in the Term List and Structure documents.

1. **Clarification of borrowed Darwin Core geography terms**. The introduction to [Section 7.5 of the Term List document](https://tdwg.github.io/ac/termlist/#75-geography-vocabulary) was edited to clarify the status of Darwin Core terms borrowed by Audubon Core. See [this issue](https://github.com/tdwg/ac/issues/134) for details.

A large number of other changes were made to these documents to correct typographical errors and fix formatting problems. To see the all of the changes, view [this diff](https://github.com/tdwg/ac/pull/155/files).

## Changes in maintenance workflow

The sections above detail the specific changes that were made to the standard. However, perhaps more significantly, there were several major changes made to the workflow for maintaining the standard. When the original standard was released, it was presented via [a wiki-based content management system](https://terms.tdwg.org/wiki/Audubon_Core). The problems associated with this system were:

1. It was difficult to easily track version changes.

1. The documents and vocabulary metadata were maintained manually. That was labor-intensive and meant that it was possible for the documentation to differ from machine-accessible metadata about vocabulary terms.

1. The content was stored in ideosyncratic wiki syntax.

The end result was that it was difficult to change and track the standard. That was particularly problematic given the complexities introduced by the large number of terms borrowed by Audubon Core from other vocabularies.

When the Audubon Core Maintenance Group was established in 2018, it began implementation of new procedures designed to overcome the deficiencies listed above and streamline the process of implementing term changes and additions.  

### Single point of entry for term metadata

Term additions and changes are made in a single CSV table that contains a line for every term whose metadata is being changed ([example](https://github.com/tdwg/rs.tdwg.org/blob/master/process/ac-revisions-2020-01-27/audubon-revisions.csv)). A [Python script](https://github.com/tdwg/rs.tdwg.org/blob/master/process/process_rs_tdwg_org.ipynb) is used to generate new versions of the terms and their containing term lists, the vocabulary, and the standard. The script also adds machine-generated metadata such as modification dateTime. When the script is run in a branch of the [rs.tdwg.org repository](https://github.com/tdwg/rs.tdwg.org) the [diff](https://github.com/tdwg/rs.tdwg.org/pull/32/files) can be used to verify that only the intended changes have been made prior to merging the branch. After the merge, the authoritative machine-accessible CSV files in the rs.tdwg.org repository fully document the changes involved in the new version.

### Generation of the Term List document by build script

The [term metadata section](https://tdwg.github.io/ac/termlist/#7-vocabularies) of the Term List document is generated by a [build script](https://github.com/tdwg/ac/blob/master/code/build_page.py) using the data in the rs.tdwg.org CSV files. This ensures that there are no differences in term metadata that might be caused by manual editing between the machine-accessible metadata and the human readable documents.

### Use of Markdown

The Audubon Core documents are now written in Markdown, making it possible to easily change their formatting by applying a different Jekyll template. That also makes them "future-proof" since Markdown is a simple and well-known text markup language that can easily be read in its raw form and would be simple to convert to other formats in the future.  Both the Markdown documents and term metadata CSV files are easily archived in GitHub, making it possible to track their changes over time using features built in to GitHub.

### Easy of maintenance

The changes described above has greatly simplified the process of maintaining the vocabulary and documents associated with Audubon Core, making it possible for the standard to evolve in response to the needs of the biodiversity informatics community in the future. It also enables robust tracking of the version history of the standard so that anyone can see how the standard has changed over time.
