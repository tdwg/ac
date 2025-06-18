# Audiovisual Core (AC)

This is the main entry point to the work of the Audiovisual Core Maintenance Group.  If you are looking for the landing page of the standard itself, go to <https://www.tdwg.org/standards/ac/>. To find the website containing the standards documents, go to <https://ac.tdwg.org/>.

The Audiovisual Core (AC), previously known as Audubon Core, is a set of vocabularies designed to represent metadata for biodiversity multimedia resources and collections. These vocabularies aim to represent information that will help to determine whether a particular resource or collection will be fit for some particular biodiversity science application before acquiring the media. Among others, the vocabularies address such concerns as the management of the media and collections, descriptions of their content, their taxonomic, geographic, and temporal coverage, and the appropriate ways to retrieve, attribute and reproduce them.

The current release (2022-02-23) is archived at <a href="https://doi.org/10.5281/zenodo.6590205"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.6590205.svg" alt="DOI"></a>

## The Audiovisual Core Maintenance Group

Audiovisual Core is maintained by a specialized [Interest Group](http://www.tdwg.org/about-tdwg/process/) whose [charter](audiovisual-core_maintenance-group_charter.md) was approved in January 2018.  The functions of the Audiovisual Core Maintenance Group are described in detail in [Section 2 of the TDWG Vocabulary Maintenance Specification](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md#2-administration).  In brief, the Maintenance Group manages vocabulary term additions and changes, and maintains the documentation that helps users to understand and apply the standard.  As an Interest Group, it may establish Task Groups to accomplish broader changes to the standard. The Maintenance Group generally meets on the third Wednesday of the month.

## Core Members of the AC Maintenance Group

Currently, core members of the group are:

Ed Baker - Natural History Museum, London, UK (Convener) - [edward.baker@nhm.ac.uk](mailto:edward.baker@nhm.ac.uk)

Vijay Barve - Natural History Museum of Los Angeles [vbarve@nhm.org](mailto:vbarve@nhm.org) 

Steve Baskauf - Vanderbilt University Jean & Alexander Heard Library (retired) - [steve.baskauf@gmail.com](mailto:steve.baskauf@gmail.com)

Douglas Boyer - Department of Evolutionary Anthropology, Duke University, Director of MorphoSource open access 3D repository - [douglasmb@gmail.com](mailto:douglasmb@gmail.com)

Niels Klazenga - Royal Botanic Gardens Victoria - [Niels.Klazenga@rbg.vic.gov.au](mailto:Niels.Klazenga@rbg.vic.gov.au)

Rebecca Snyder - Smithsonian Institution, National Museum of Natural History - [SNYDERR@si.edu](mailto:SNYDERR@si.edu)

Dan Stowell - Tilburg University and Naturalis Biodiversity Centre - [dstowell@tilburguniversity.edu](mailto:dstowell@tilburguniversity.edu)

Jocelyn Triplett - Duke University, MorphoSource.org - [jocelyn.triplett@duke.edu](mailto:jocelyn.triplett@duke.edu)

Kate Webbink - Field Museum of Natural History - [kwebbink@fieldmuseum.org](mailto:kwebbink@fieldmuseum.org)

To see all of the people who are paying attention to our work, see the list of ["watchers"](https://github.com/tdwg/ac/watchers).  The people on this list are effectively the "regular members" of the group.

The Maintenance Group would like to recognize Robert A. Morris who passed away in 2021. Bob can be considered the "father of Audiovisual Core" and led the task group through the development and process of ratifying of the standard. Thanks, Bob, for your vision and leadership!

## Task Groups

In the [TDWG Process](https://www.tdwg.org/about/process/) for creating and modifying standards, Task Groups are formed to create particular deliverables of interest to an Interest Group.  As an Interest Group, the Audiovisual Core Maintenance Group periodically establishes Task Groups.

We have chartered a 3D Imagery and Data Task Group (3DTG) to look at possible additions to Audiovisual Core for describing 3D images.  For more information, see the [Task Group's home page](3d/README.md).  If you are interested in the work of this group, contact its convener, [Doug Boyer](mailto:douglasmb@gmail.com).

We have also chartered a Views Controlled Vocabularies task group to create controlled vocabularies for `ac:subjectPart` and `ac:subjectOrientation`.  For more information, see the [Task Group's home page](views/README.md).  If you are interested in the work of this group, contact its convener, [Steve Baskauf](mailto:steve.baskauf@vanderbilt.edu).

## Participating in the Maintenance Group

If you would like to participate in this group, contact the convener or one of the core members.

To participate in the communication system of the group, "watch" the group's [Issues tracker](https://github.com/tdwg/ac/issues).  This issues tracker is the mechanism for suggesting specific changes to the standard as well as to raise issues for discussion by the group.

### Maintenance Group Meetings

The Maintenance Group meets via Zoom, usually at 17:00 UTC, on the third Wednesday of the month. These meetings are open to anyone interested in joining; please contact the convenor for the Zoom link. [Next meeting agenda](https://github.com/tdwg/ac/issues?q=is%3Aissue+is%3Aopen+label%3A%22next+meeting+agenda%22).

## Policies

Policies established by the Maintenance Group are listed [here](policies.md).  Please note that the policy document is not included with the Audiovisual Core Standard and is therefore not subject to any standards-related processes requiring public comment, Executive Committee approval, etc. Rather, the policies are established through consensus of the Maintenance Group, in consultation (when necessary) with the [Technical Architecture Group](https://github.com/tdwg/tag).

## Documentation

[Examples guide for Still Images](https://github.com/tdwg/ac/blob/master/image/examples.md)

[stub Examples guide for Sound](https://github.com/tdwg/ac/blob/master/sound/examples.md)

[Regions of Interest (ROI) recipes document](https://github.com/tdwg/ac/blob/master/roi-recipes.md)

To see what issues we are currently addressing, see our [Issue Tracker](https://github.com/tdwg/ac/issues).  

For notes of Maintenance group meetings and other historical documents, see [this page](historical/README.md).  To see what we've been working on in the past, see the [list of closed issues](https://github.com/tdwg/ac/issues?q=is%3Aissue+is%3Aclosed)

For the details of most of the documents in this repo, see the diagram below.

## Repo structure

The repository structure is described below.

```
├── README.md             : Description of this repository
├── license.md            : Repository license
├── policies.md           : Audiovisual Core maintenance policies
│
├── docs                  : Standards documents live here.  However, do not hyperlink to them here because they are rendered as HTML at https://tdwg.github.io/ac/.
│   ├── _config.yml       : Jekyll configuration file
│   ├── introduction.md   : Brief introduction to the standard
│   ├── structure.md      : Describes the structure of Audiovisual Core
│   ├── termlist.md       : AC Term List, including normative definitions. DO NOT EDIT MANUALLY!
│   ├── guide.md          : More detailed user guide
│   ├── 04_AudubonCore1.0NonNormative_docV1.95.doc     : version 1.95 of the reference guide
│   └── assets            : subdirectories contain stuff for Jekyll operation
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
│   ├── ac-20yy-annual-report.md       : 20yy report to the Executive Committee
│   └── [yyyy-mm-dd]-hangout-notes.pdf : Series of downloaded Google Docs notes from online Maintenance Group meetings
│
├── 3D                                 : Directory to store documents related to proposed 3D task group
│   ├── README.md                      : Homepage of the 3D Imagery and Data Task Group (3DTG)
│   ├── charter_3d_task_group_of_audubon_core_2019-06-11.docx   : Word version of submitted charter
│   ├── charter_3d_task_group_of_audubon_core_2019-06-11.pdf    : PDF version of submitted charter
│   └── proposed-3d-metadata-terms-from-dwc-hour.csv            : notes from Darwin Core hour
│
├── views                              : Directory to store documents related to proposed 3D task group
│   ├── README.md                      : Homepage of the Views Controlled Vocabularies Task Group
│   ├── views-tg-draft-charter-2019-06-25.docx                  : Word version of submitted charter
│   ├── views-tg-draft-charter-2019-06-25.docx.pdf              : PDF version of submitted charter
│   └── background.md                  : background notes
│
└── .gitignore                : Files and directories to be ignored by git
```

-----
Revised 2022-05-28
