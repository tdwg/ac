# Audubon Core Maintenance Group

## Interest Group Annual Report

### Web Site:
https://github.com/tdwg/ac

### Convener(s):
Steve Baskauf - steve.baskauf@vanderbilt.edu

### Submitted:
2018-08-20

## Phase of work:
The Audubon Core Maintenance Group (ACMG) was chartered in 2018.  As a vocabulary maintenance interest group, it's permanent task as laid out in the [Vocabulary Maintenance Specification](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md#21-vocabulary-maintenance-interest-groups) is to manage vocabulary term additions and changes, and maintain the documentation that helps users to understand and apply the standard.  Since relatively little maintenance has been done on the vocabulary since its adoption in 2013, much of the focus of the group this year has been to review the open issues in the [Audubon Core issue tracker](https://github.com/tdwg/ac/issues).  

## Activities:
The primary activity of the ACMG took place through a series of Google Hangouts between May and July.  Although open to the public, they were generally attended by only the core members.  The notes from those meetings can be viewed in the [historical documents section](https://github.com/tdwg/ac/tree/master/historical) of the group's Github repo. Additional communication took place through the group's issue tracker and occasional direct emails.

We spent some time looking at categories of issues in the tracker.  There were some issues that had been rendered moot by the passage of time. For example, some RDF-related questions had been resolved by the adoption of the [Standards Documentation Specification](https://github.com/tdwg/vocab/blob/master/sds/documentation-specification.md) (SDS) and were closed.

There were a number of issues in the tracker related to the creation of best-practices documents. In most cases, action on those issues were deferred pending the upcoming Audubon Core workshop at the annual meeting. One of the goals of that meeting is to determine by soliciting community input the focus of enhancements to the standard in the next year. Depending on the outcome of that workshop, the ACMG will set priorities for the types of best-practices documents that are most needed.

There were two areas of focus since the first meeting in May.  One was an effort to bring the Audubon Core documents into compliance with the SDS. Some of the necessary revisions simply required formatting the metadata into the required form. However, a major part of the effort was to increase the ease of access by converting to Markdown all four of the documents that are included in the standard. In particular, the user guide was only available as a Microsoft Word document and was therefore not directly viewable via a browser.  The other three documents were part of a mediaWiki system that is no longer the preferred method of maintaining TDWG documents.  After the conversion to Markdown, the documents were set up to be rendered at github.io by Jekyll as regular HTML web pages that were formatted to match the style of the new TDWG website.  Throughout the conversion process, we were careful to make sure that the resulting documents contained substantively the same information as in the original documents that were adopted as part of the the standard.

The [term list document](https://tdwg.github.io/ac/termlist) required the most complex conversion process. Although the introduction was hard-coded as Markdown, the term indices and the term list itself were generated via a [Python script](https://github.com/tdwg/ac/blob/master/code/build_page.py) from tabular metadata in the [rs.tdwg.org Github repo](https://github.com/tdwg/rs.tdwg.org). This is an important change because those same tables will eventually be used to generate the machine-readable metadata for the terms, so using the same source tables will ensure that the human- and machine-readable representations are identical in content.  It will also simplify maintenance because a single change to the metadata table will automatically be reflected in all available representations of the vocabulary.  

Another major part of the process of bringing the documentation into conformance with the SDS was to clarify what parts of the documents were normative. This was particularly complicated where the "borrowed" terms were concerned. The "definitions" given in the original documentation were not the definitions of the organizations that minted the terms, so we opted to present the original definitions and demarcate the Audubon Core "definitions" as normative usage guidelines. The other notes were considered non-normative.  

Finally, the original term list document included by reference all of the terms organized within the dwc:Location class. In the converted document, for clarity we explicitly listed all of those terms with their definitions.

The second major area of focus was laying the groundwork for chartering a Task Group charged with developing the set of terms necessary to describe 3D images. Two of the core members are also involved in the Community Standards for 3D Data Preservation (CS3DP) group, so the work of the proposed task group will be aligned with that effort.  Doug Boyer presented a poster about the proposed task group at the CS3DP forum in August and received useful feedback there.


## Accomplishments:
The four revised documents can be accessed via links in the "Parts of the Standard" section of the [Audubon Core landing page](https://www.tdwg.org/standards/ac/) on the TDWG website.

## Impediments to progress
The main impediments were lack of time to address all of the open issues in the tracker, and lack of input from the community about priority goals for improving the vocabulary.  We plan to address these two items at the Audubon Core workshop and ACMG interest group meeting at the annual conference in Dunedin.

## Changes in goals or scope
There are no anticipated major changes in goals or scope.

## Plans for next calendar year
A major goal is to charter the 3D Data Task Group that will propose term additions related to 3D images.

The other goal is make progress on developing one or more best-practices documents. We will probably start by focusing on documenting the practices for still images already in use in places like GBIF and iDigBio. Other potential areas of interest are audio and video, neither of which were dealt with in detail in the original adoption.

We will probably continue the monthly Google Hangouts to ensure that we maintain momentum.
