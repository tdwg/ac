# Script to build the Audubon Core term list page using Markdown.
# Steve Baskauf 2018-06-12
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
    listCurie = {}
    listUri = {}

    for row in range(1,len(table)):    #skip the header row
        for termList in termLists:
            if termList == table[row][listColumn]:
                listCurie[termList] = table[row][prefixColumn] # make a dictionary of CURIEs
                listUri[termList] = table[row][uriColumn] # make a dictionary of CURIEs
                if table[row][prefixColumn] == 'ac':
                    listFilename[termList] = 'audubon'
                else:
                    listFilename[termList] = table[row][prefixColumn] + '-for-ac' # make a dictionary of filenames
    return [listFilename, listCurie, listUri]

# ---------------------------------------------------------------------------
def createMasterMetadataTable(termLists, listMetadata):
    fileNameDict = listMetadata[0]
    curieDict = listMetadata[1]
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
            masterTable.append([ curieDict[termList], uriDict[termList], table[row][localNameColumn], table[row][labelColumn], table[row][layerColumn], table[row][requiredColumn], table[row][repeatableColumn], table[row][definitionColumn], table[row][notesColumn], table[row][organizedColumn] ])

    return masterTable

# ---------------------------------------------------------------------------
def buildMarkdown(table):
    displayOrder = ['http://rs.tdwg.org/dwc/terms/attributes/Management', 'http://rs.tdwg.org/dwc/terms/attributes/Attribution', 'http://purl.org/dc/terms/Agent', 'http://rs.tdwg.org/dwc/terms/attributes/ContentCoverage', 'http://purl.org/dc/terms/Location', 'http://purl.org/dc/terms/PeriodOfTime', 'http://rs.tdwg.org/dwc/terms/attributes/TaxonomicCoverage', 'http://rs.tdwg.org/dwc/terms/attributes/ResourceCreation', 'http://rs.tdwg.org/dwc/terms/attributes/RelatedResources', 'http://rs.tdwg.org/dwc/terms/attributes/ServiceAccessPoint']
    displayLabel = ['Management Vocabulary', 'Attribution Vocabulary', 'Agents Vocabulary', 'Content Coverage Vocabulary', 'Geography Vocabulary', 'Temporal Coverage Vocabulary', 'Taxonomic Coverage Vocabulary', 'Resource Creation Vocabulary', 'Related Resources Vocabulary', 'Service Access Point Vocabulary']
    displayId = ['Management_Vocabulary', 'Attribution_Vocabulary', 'Agents_Vocabulary', 'Content_Coverage_Vocabulary', 'Geography_Vocabulary', 'Temporal_Coverage_Vocabulary', 'Taxonomic_Coverage_Vocabulary', 'Resource_Creation_Vocabulary', 'Related_Resources_Vocabulary', 'Service_Access_Point_Vocabulary']

    # generate the Markdown for the terms table
    text = ''
    for category in range(0,len(displayOrder)):
        text += '### <a id="' + displayId[category] + '">7.' + str(category + 1) + ' ' + displayLabel[category] + '\n'
        text += '\n'
        text += '| property | value |\n'
        text += '|----------|-------|\n'
        for row in range(0,len(table)):    #no header row
            if displayOrder[category] == table[row][9]:
                text += '| **Term Name:** | **' + table[row][0] + ":" + table[row][2] + '** |\n'
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
def outputMarkdown(text, headerFileName, footerFileName, outFileName):
    # read in header and footer, merge with terms table, and output
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
# constants
githubBaseUri = 'https://raw.githubusercontent.com/tdwg/rs.tdwg.org/split_ac_terms/'
headerFileName = 'termlist-header.md'
footerFileName = 'termlist-footer.md'
outFileName = 'termlist.md'

termLists = retrieveVocabularyInfo(githubBaseUri)

listMetadata = retrieveTermListMetadata(githubBaseUri)

table = createMasterMetadataTable(termLists, listMetadata)

text = buildMarkdown(table)

outputMarkdown(text, headerFileName, footerFileName, outFileName)

