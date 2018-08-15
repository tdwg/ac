# Audubon Core (AC)

This is the main entry point to the work of the Audubon Core Maintenance Group.  If you are looking for the landing page of the standard itself, go to https://www.tdwg.org/standards/ac/.

The Audubon Core (AC) is a set of vocabularies designed to represent metadata for biodiversity multimedia resources and collections. These vocabularies aim to represent information that will help to determine whether a particular resource or collection will be fit for some particular biodiversity science application before acquiring the media. Among others, the vocabularies address such concerns as the management of the media and collections, descriptions of their content, their taxonomic, geographic, and temporal coverage, and the appropriate ways to retrieve, attribute and reproduce them.

## The Audubon Core Maintenance Group

Audubon Core is maintained by a specialized [Interest Group](http://www.tdwg.org/about-tdwg/process/) whose [charter](audubon_core_maintenance_group_charter.pdf) was approved in January 2018.  The functions of the Audubon Core Maintenance Group are described in detail in [Section 2 of the TDWG Vocabulary Maintenance Specification](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md#2-administration).  In brief, the Maintenance Group manages vocabulary term additions and changes, and maintains the documentation that helps users to understand and apply the standard.  As an Interest Group, it may establish Task Groups to accomplish broader changes to the standard.  

## Core Members of the AC Maintenance Group

Currently, core members of the group are:

Steve Baskauf - Vanderbilt University Department of Biological Sciences (Convener) - [steve.baskauf@vanderbilt.edu](mailto:steve.baskauf@vanderbilt.edu)

Robert A. Morris - University of Massachusetts, Boston - [morris.bob@gmail.com](mailto:morris.bob@gmail.com)

Douglas Boyer -Department of Evolutionary Anthropology, Duke University, Director of MorphoSource open access 3D repository - [douglasmb@gmail.com](mailto:douglasmb@gmail.com)

Niels Klazenga - Royal Botanic Gardens Victoria - [Niels.Klazenga@rbg.vic.gov.au](mailto:Niels.Klazenga@rbg.vic.gov.au)

Rebecca Snyder - Smithsonian Institution, National Museum of Natural History - [SNYDERR@si.edu](mailto:SNYDERR@si.edu)

To see all of the people who are paying attention to our work, see the list of ["watchers"](https://github.com/tdwg/ac/watchers).  The people on this list are effectively the "regular members" of the group.

## Participating in the Group

If you would like to participate in this group, contact the convener or one of the core members.  

To participate in the communication system of the group, "watch" the group's [Issues tracker](https://github.com/tdwg/ac/issues).  This issues tracker is the mechanism for suggesting specific changes to the standard as well as to raise issues for discussion by the group.

## Documentation

To see what issues we are currently addressing, see our [Issue Tracker](https://github.com/tdwg/ac/issues).  

For notes of Maintenance group meetings and other historical documents, see [this page](historical/README.md).  To see what we've been working on in the past, see the [list of closed issues](https://github.com/tdwg/ac/issues?q=is%3Aissue+is%3Aclosed)

For the details of most of the documents in this repo, see the diagram below.

## Repo structure

The repository structure is described below.

```
├── README.md             : Description of this repository
├── license.md            : Repository license
│
├── docs                  : Standards documents live here.  However, do not hyperlink to them here because they are rendered as HTML at https://tdwg.github.io/ac/.
│   ├── introduction.md   : Brief introduction to the standard
│   ├── structure.md      : Describes the structure of Audubon Core
│   ├── termlist.md       : AC Term List, including normative definitions. DO NOT EDIT MANUALLY!
│   ├── guide.md          : More detailed user guide
│   └── assets            : subdirectories contain stuff for Jekyll operation
│       ├── styles.css    : CSS for generated Jekyll site
│       └── images        : directory for images used in the documents
│
├── code
│   ├── build_page.py               : Build script to generate termlist.md
│   ├── http_library.py             : Function library used by build_page.py
│   ├── termlist-header.md          : Manually-edited header section to which the generated term list is appended
│   ├── termlist-footer.md          : Manually-edited footer section (currently empty) to be appended to the generated term list
│   └── pandoc-conversion-notes.txt : Notes on conversion from mediawiki
│
├── historical                         : Documents of historical interest
│   ├── README.md                      : Contents of this directory
│   ├── RecordOfPublicReview.md        : Summary of public comment period during the adoption of the standard
│   └── [yyyy-mm-dd]-hangout-notes.pdf : Series of downloaded Google Docs notes from online Maintenance Group meetings
│
├── 3D                                               : Directory to store documents related to proposed 3D task group
│   └── proposed-3d-metadata-terms-from-dwc-hour.csv : notes from Darwin Core hour
│
└── .gitignore                : Files and directories to be ignored by git
```
