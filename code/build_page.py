# Script to build the Audubon Core term list page using Markdown.
# Steve Baskauf 2018-06-20
# This script merges static Markdown header and footer documents with term information tables (in Markdown) generated from data in the rs.tdwg.org repo from the TDWG Github site

# Note: this script calls a function from http_library.py, which requires importing the requests, csv, and json modules
import http_library

# ---------------------------------------------------------------------------
# retrieve vocabularies members metadata from Github
def retrieveVocabularyInfo(githubBaseUri):
    dataUrl = githubBaseUri + 'vocabularies/vocabularies-members.csv'
    table = http_library.retrieveData(dataUrl, 'csv', ',')
    header = table[0]

    # determine which column contains the vocab and term list ids
    for column in range(len(header)):
        if header[column] == 'termList':
            termListColumn = column
        if header[column] == 'vocabulary':
            vocabularyColumn = column

    # store the identifiers of the term lists
    termLists = []
    for row in range(1,len(table)):    #skip the header row
        if table[row][vocabularyColumn] == 'http://rs.tdwg.org/ac/':
            termLists.append(table[row][termListColumn])
    return termLists

# ---------------------------------------------------------------------------
# create dictionaries of metadata about term lists
def retrieveTermListMetadata(githubBaseUri):
    # retrieve term list metadata from Github
    dataUrl = githubBaseUri + 'term-lists/term-lists.csv'
    table = http_library.retrieveData(dataUrl, 'csv', ',')
    header = table[0]

    # determine which columns contain the namespace info
    for column in range(len(header)):
        if header[column] == 'list':
            listColumn = column
        if header[column] == 'vann_preferredNamespacePrefix':
            prefixColumn = column
        if header[column] == 'vann_preferredNamespaceUri':
            uriColumn = column

    listFilename = {}
    listNamespace = {}
    listUri = {}

    for row in range(1,len(table)):    #skip the header row
        for termList in termLists:
            if termList == table[row][listColumn]:
                listNamespace[termList] = table[row][prefixColumn] # make a dictionary of namespaces
                listUri[termList] = table[row][uriColumn] # make a dictionary of URIs
                if table[row][prefixColumn] == 'ac':
                    listFilename[termList] = 'audubon'
                else:
                    listFilename[termList] = table[row][prefixColumn] + '-for-ac' # make a dictionary of filenames
    return [listFilename, listNamespace, listUri]

# ---------------------------------------------------------------------------
# create a single table that combines all relevant metadata from the various term list metadata tables
def createMasterMetadataTable(termLists, listMetadata):
    fileNameDict = listMetadata[0]
    namespaceDict = listMetadata[1]
    uriDict = listMetadata[2]
    masterTable = []

    for termList in termLists:
        # retrieve term metadata for a particular list from Github
        dataUrl = githubBaseUri + fileNameDict[termList] + '/' + fileNameDict[termList] + '.csv'
        table = http_library.retrieveData(dataUrl, 'csv', ',')
        header = table[0]

        # determine which columns contain specified metadata fields
        for column in range(len(header)):
            if header[column] == 'term_localName':
                localNameColumn = column
            if header[column] == 'label':
                labelColumn = column
            if header[column] == 'tdwgutility_layer':
                layerColumn = column
            if header[column] == 'tdwgutility_required':
                requiredColumn = column
            if header[column] == 'tdwgutility_repeatable':
                repeatableColumn = column
            if header[column] == 'rdfs_comment':
                definitionColumn = column
            if header[column] == 'dcterms_description':
                notesColumn = column
            if header[column] == 'tdwgutility_organizedInClass':
                organizedColumn = column

        for row in range(1,len(table)):    #skip the header row
            masterTable.append([ namespaceDict[termList], uriDict[termList], table[row][localNameColumn], table[row][labelColumn], table[row][layerColumn], table[row][requiredColumn], table[row][repeatableColumn], table[row][definitionColumn], table[row][notesColumn], table[row][organizedColumn] ])

    return masterTable

# ---------------------------------------------------------------------------
# generate the index of terms grouped by category and sorted alphabetically by lowercase term local name
def buildIndexByTermName(table, displayOrder, displayLabel, displayId):

    text = '### 6.1 Index By Term Name\n\n'
    text += '(See also [6.2 Index By Label](#62-index-by-label))\n\n'
    for category in range(0,len(displayOrder)):
        text += '**' + displayLabel[category] + '**\n'
        text += '\n'
        for row in range(0,len(table)):    #no header row
            if displayOrder[category] == table[row][9]:
                curie = table[row][0] + ":" + table[row][2]
                curieAnchor = curie.replace(':','_')
                text += '| [' + curie + '](#' + curieAnchor + ') |\n'
        text += '\n'
    return text
    
# ---------------------------------------------------------------------------
# generate the index of terms grouped by category and sorted alphabetically by the term label
def buildIndexByTermLabel(table, displayOrder, displayLabel, displayId):

    text = '### 6.2 Index By Label\n\n'
    text += '(See also [6.1 Index By Term Name](#61-index-by-term-name))\n\n'
    for category in range(0,len(displayOrder)):
        text += '**' + displayLabel[category] + '**\n'
        text += '\n'
        for row in range(0,len(table)):    #no header row
            if displayOrder[category] == table[row][9]:
                if row == 0 or (row != 0 and table[row][3] != table[row-1][3]): # this is a hack to prevent duplicate labels
                    curieAnchor = table[row][0] + "_" + table[row][2]
                    text += '| [' + table[row][3] + '](#' + curieAnchor + ') |\n'
        text += '\n'
    return text
    
# ---------------------------------------------------------------------------
# generate a table for each term, with terms grouped by category
def buildMarkdown(table, displayOrder, displayLabel, displayComments, displayId):

    # generate the Markdown for the terms table
    text = '## 7 Vocabularies\n'
    for category in range(0,len(displayOrder)):
        text += '### 7.' + str(category + 1) + ' ' + displayLabel[category] + '\n'
        text += '\n'
        text += displayComments[category] # insert the comments for the category, if any.
        text += '| property | value |\n'
        text += '|----------|-------|\n'
        for row in range(0,len(table)):    #no header row
            if displayOrder[category] == table[row][9]:
                curie = table[row][0] + ":" + table[row][2]
                curieAnchor = curie.replace(':','_')
                text += '| <a id="' + curieAnchor + '"></a>**Term Name:** | **' + curie + '** |\n'
                text += '| Normative URI: | ' + table[row][1] + table[row][2] + ' |\n'
                text += '| Label: | ' + table[row][3] + ' |\n'
                text += '| | **Layer:** ' + table[row][4] + ' -- **Required:** ' + table[row][5] + ' -- **Repeatable:** ' + table[row][6] + ' |\n'
                text += '| Definition: | ' + table[row][7] + ' |\n'
                if table[row][8] != '':
                    text += '| Notes: | ' + table[row][8] + ' |\n'
                text += '| | |\n'
        text += '\n'
    return text
    
# ---------------------------------------------------------------------------
# read in header and footer, merge with terms table, and output
def outputMarkdown(text, headerFileName, footerFileName, outFileName):
    headerObject = open(headerFileName, 'rt')
    header = headerObject.read()
    headerObject.close()

    footerObject = open(footerFileName, 'rt')
    footer = footerObject.read()
    footerObject.close()

    outputObject = open(outFileName, 'wt')
    outputObject.write(header + text + footer)
    outputObject.close()

# ---------------------------------------------------------------------------
# main routine

# constants
githubBaseUri = 'https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/'
headerFileName = 'termlist-header.md'
footerFileName = 'termlist-footer.md'
outFileName = 'termlist.md'

displayOrder = ['http://rs.tdwg.org/dwc/terms/attributes/Management', 'http://rs.tdwg.org/dwc/terms/attributes/Attribution', 'http://purl.org/dc/terms/Agent', 'http://rs.tdwg.org/dwc/terms/attributes/ContentCoverage', 'http://purl.org/dc/terms/Location', 'http://purl.org/dc/terms/PeriodOfTime', 'http://rs.tdwg.org/dwc/terms/attributes/TaxonomicCoverage', 'http://rs.tdwg.org/dwc/terms/attributes/ResourceCreation', 'http://rs.tdwg.org/dwc/terms/attributes/RelatedResources', 'http://rs.tdwg.org/dwc/terms/attributes/ServiceAccessPoint']
displayLabel = ['Management Vocabulary', 'Attribution Vocabulary', 'Agents Vocabulary', 'Content Coverage Vocabulary', 'Geography Vocabulary', 'Temporal Coverage Vocabulary', 'Taxonomic Coverage Vocabulary', 'Resource Creation Vocabulary', 'Related Resources Vocabulary', 'Service Access Point Vocabulary']
displayComments = ['','','','','All geography terms from the Darwin Core version of 9 Dec 2009 are deemed included in the Core Layer. Specifically, this includes exactly those which are declared by Darwin Core to be in Darwin Core Class [dwc:Location](http://rs.tdwg.org/dwc/terms/Location). Note that [dwc:locality](http://rs.tdwg.org/dwc/terms/locality) may be used, but as applied to media this term may be ambiguous as to whether it applies to the location depicted or the location at which the media was created. When disambiguating information is available, it is better to use the terms Location Shown and Location Created. The latter is in the Resource Creation Vocabulary.\n\nLocation Created and Location Shown are separated in the current version of IPTC, and the metadata working group ([Metadata Working Group Guidelines for Handling Image Metadata, Version 2.0, November 2010](http://www.metadataworkinggroup.org/pdf/mwg_guidance.pdf)) also recommends this. We follow this below in order to support the expected future increase of automatic GPS-based coordinate recording. As a special case, the AC group recommends to change the semantics of Location Shown in the case of biodiversity specimens, where the original location may differ from the current location at which the specimen is held in a collection. In this case, Location Shown should exclusively refer to the location where a specimen was originally collected (gathering or sampling location). Use Location Created to express the location where the resource was created (a specimen was digitized).\n\n','','','','','These terms are representation-dependent metadata, referring to specific digital representations of a resource (e.g., a specific resolution, quality, or format). They are used within whatever a particular AC implementation assigns to the value of hasServiceAccessPoint, whose label is simply "Service Access Point." Note that it is possible for an implementation to use syntactic conventions that avoid direct use of hasServiceAccessPoint, as illustrated in the final example in the section [Multiplicity/Cardinality in the Audubon Core Structure document](structure.md#3-multiplicity-and-cardinality).\n\n']
displayId = ['Management_Vocabulary', 'Attribution_Vocabulary', 'Agents_Vocabulary', 'Content_Coverage_Vocabulary', 'Geography_Vocabulary', 'Temporal_Coverage_Vocabulary', 'Taxonomic_Coverage_Vocabulary', 'Resource_Creation_Vocabulary', 'Related_Resources_Vocabulary', 'Service_Access_Point_Vocabulary']

termLists = retrieveVocabularyInfo(githubBaseUri)

listMetadata = retrieveTermListMetadata(githubBaseUri)

table = createMasterMetadataTable(termLists, listMetadata)

localnameSortedTable = sorted(table, key = lambda term: term[2].lower() ) # perform sort on lowercase of the third column: localNameColumn
labelSortedTable = sorted(table, key = lambda term: term[3].lower() ) # perform sort on lowercase of the fourth column: labelColumn

indexByName = buildIndexByTermName(localnameSortedTable, displayOrder, displayLabel, displayId)
indexByLabel = buildIndexByTermLabel(labelSortedTable, displayOrder, displayLabel, displayId)
termTable = buildMarkdown(localnameSortedTable, displayOrder, displayLabel, displayComments, displayId)

text = indexByName + indexByLabel + termTable

outputMarkdown(text, headerFileName, footerFileName, outFileName)

