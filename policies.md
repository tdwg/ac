# Audubon Core Maintenance Group Policies

**Title:** Audubon Core Maintenance Group Policies

**Last modified:** 2019-09-29

**Status:** This document is not included within the Audubon Core standard.

**Abstract:** This document records decisions made by the Audubon Core Maintenance Group regarding general policies related to management of the Audubon Core vocabulary. 

**Creator:** TDWG Audubon Core Maintenance Group

# 1 Introduction

This is a record of decisions reached by the Maintenance Group regarding the management of the Audubon Core vocabulary, Audubon Core standards documents, and other ancillary documents or data related to the Audubon Core standard.  

## 1.1 Conflicts

In cases where the policies outlined here are in conflict with either the [TDWG Vocabulary Maintenance Specification](https://github.com/tdwg/vocab/blob/master/vms/maintenance-specification.md) (SDS) or TDWG-wide policies articulated by the Technical Architecture Group (TAG), the SDS or TAG policies prevail.

## 1.2 RFC 2119 keywords

[RFC 2119](https://tools.ietf.org/html/rfc2119) keywords are NOT used in this document since its purpose is to describe policies rather than to specify requirements.

# 2 Decisions

## 2.1 Versioning of terms borrowed from other vocabularies

**Date:** 2019-09-26

**Decision:** The version of an Audubon Core term borrowed from another TDWG vocabulary will automatically be updated within Audubon Core whenever a new version of the borrowed term is issued by the source vocabulary.  The version of an Audubon Core term borrowed from a non-TDWG vocabulary will NOT be automatically updated.  The Maintenance Group may decide to advance the non-TDWG term version used in Audubon Core after assessing the likely effect of the change on stability and interoperability.  The Maintenance Group may solicit public comment or advice from the Technical Architecture Group (TAG) if the effect is unclear.

**Background:** This decision was adopted after discussion and feedback from the TAG about the meaning of the text "All geography terms from the Darwin Core version of 9 Dec 2009 are deemed included in the Core Layer." included in the http://rs.tdwg.org/ac/doc/termlist/2013-10-23 version of the Term List document. The Maintenance Group concluded that the intent of this text was to indicate what current terms Darwin Core terms were to be included in Audubon Core rather than to indicate that the specific term versions in use in Darwin Core on 2009-12-09 were to be "frozen" into Audubon Core. Based on feedback from the TAG and discussion within the group, the Maintenance Group considered it to be a best practice to keep Audubon Core in synch with source TDWG vocabularies, and to make it clear what versions were intended for non-TDWG terms. 

**References:** [Audubon Core Issue 134](https://github.com/tdwg/ac/issues/134),  [TDWG TAG Issue 23](https://github.com/tdwg/tag/issues/23), [2019-08-29 Maintenance Group meeting notes](historical/2019-08-29-meeting-notes.pdf), [2019-09-26 Maintenance Group meeting notes](historical/2019-09-26-meeting-notes.pdf).  

[Audubon Core Maintenance Group home](../)