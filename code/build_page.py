# Script to build the Audiovisual Core term list page using Markdown.
# Steve Baskauf 2018-06-20
# Updated 2020-01-28
# Updated 2020-08-23 to handle examples in borrowed Darwin Core terms
# Updated 2021-10-07 to add Regions of Interest section
# This script merges static Markdown header and footer documents with term information tables (in Markdown) generated from data in the rs.tdwg.org repo from the TDWG Github site

# Note: this script calls a function from http_library.py, which requires importing the requests, csv, and json modules
import http_library
import re
import pandas as pd

# ---------------------------------------------------------------------------
# retrieve vocabularies members metadata from Github
def retrieveVocabularyInfo(githubBaseUri):
    dataUrl = githubBaseUri + 'vocabularies/vocabularies-members.csv'
    table = http_library.retrieveData(dataUrl, 'csv', ',')
    #print(table[0])
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

        # retrieve versions metadata for term list
        versions_url = githubBaseUri + fileNameDict[termList] + '-versions/' + fileNameDict[termList] + '-versions.csv'
        versions_df = pd.read_csv(versions_url, na_filter=False)

        # determine which columns contain specified metadata fields
        for column in range(len(header)):
            if header[column] == 'term_localName':
                localNameColumn = column
            if header[column] == 'term_modified':
                modifiedColumn = column
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
            if header[column] == 'skos_scopeNote':
                scopeNoteColumn = column
            if header[column] == 'examples':
                examplesColumn = column
            if header[column] == 'dcterms_description':
                notesColumn = column
            if header[column] == 'tdwgutility_organizedInClass':
                organizedColumn = column

        for row in range(1,len(table)):    #skip the header row

            # Borrowed terms really don't have implemented versions. They may be lacking values for version_status.
            # In their case, their version IRI will be omitted.
            found = False
            for vindex, vrow in versions_df.iterrows():
                if vrow['term_localName']==table[row][localNameColumn] and vrow['version_status']=='recommended':
                    found = True
                    version_iri = vrow['version']
                    # NOTE: the current hack for non-TDWG terms without a version is to append # to the end of the term IRI
                    if version_iri[len(version_iri)-1] == '#':
                        version_iri = ''
            if not found:
                version_iri = ''

            masterTable.append([ namespaceDict[termList], uriDict[termList], table[row][localNameColumn], table[row][labelColumn], table[row][layerColumn], table[row][requiredColumn], table[row][repeatableColumn], table[row][definitionColumn], table[row][scopeNoteColumn], table[row][notesColumn], table[row][organizedColumn], version_iri, table[row][modifiedColumn], table[row][examplesColumn] ])

    return masterTable

# ---------------------------------------------------------------------------
# generate the index of terms grouped by category and sorted alphabetically by lowercase term local name
def buildIndexByTermName(table, displayOrder, displayLabel, displayId):

    text = '### 6.1 Index By Term Name\n\n'
    text += '(See also [6.2 Index By Label](#62-index-by-label))\n\n'
    for category in range(0,len(displayOrder)):
        text += '**' + displayLabel[category] + '**\n'
        text += '\n'
        filteredTable = [x for x in table if x[10] == displayOrder[category]]
        for row in range(0,len(filteredTable)):    #no header row
            curie = filteredTable[row][0] + ":" + filteredTable[row][2]
            curieAnchor = curie.replace(':','_')
            text += '[' + curie + '](#' + curieAnchor + ')'
            if row < len(filteredTable) - 1:
                text += ' |'
            text += '\n'
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
        filteredTable = [x for x in table if x[10] == displayOrder[category]]
        for row in range(0,len(filteredTable)):    #no header row
            if row == 0 or (row != 0 and filteredTable[row][3] != filteredTable[row-1][3]): # this is a hack to prevent duplicate labels
                curieAnchor = filteredTable[row][0] + "_" + filteredTable[row][2]
                text += '[' + filteredTable[row][3] + '](#' + curieAnchor + ')'
                if row < len(filteredTable) - 2 or (row == len(filteredTable) -2 and filteredTable[row][3] != filteredTable[row + 1][3]):
                    text += ' |'
                text += '\n'
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
        for row in range(0,len(table)):    #no header row
            if displayOrder[category] == table[row][10]:
                text += '<table>\n'
                curie = table[row][0] + ":" + table[row][2]
                curieAnchor = curie.replace(':','_')
                text += '\t<thead>\n'
                text += '\t\t<tr>\n'
                text += '\t\t\t<th colspan="2"><a id="' + curieAnchor + '"></a>Term Name: ' + curie + '</th>\n'
                text += '\t\t</tr>\n'
                text += '\t</thead>\n'
                text += '\t<tbody>\n'
                text += '\t\t<tr>\n'
                text += '\t\t\t<td>Normative URI</td>\n'
                uri = table[row][1] + table[row][2]
                text += '\t\t\t<td><a href="' + uri + '">' + uri + '</a></td>\n'
                text += '\t\t</tr>\n'

                if table[row][12] != '':
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td>Modified</td>\n'
                    text += '\t\t\t<td>' + table[row][12] + '</td>\n'
                    text += '\t\t</tr>\n'

                if table[row][11] != '':
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td>Term version URI</td>\n'
                    text += '\t\t\t<td><a href="' + table[row][11] + '">' + table[row][11] + '</a></td>\n'
                    text += '\t\t</tr>\n'

                text += '\t\t<tr>\n'
                text += '\t\t\t<td>Label</td>\n'
                text += '\t\t\t<td>' + table[row][3] + '</td>\n'
                text += '\t\t</tr>\n'
                text += '\t\t<tr>\n'
                text += '\t\t\t<td></td>\n'
                text += '\t\t\t<td><b>Required:</b> ' + table[row][5] + ' -- <b>Repeatable:</b> ' + table[row][6] + '</td>\n'
                text += '\t\t</tr>\n'
                text += '\t\t<tr>\n'
                text += '\t\t\t<td>Definition</td>\n'
                text += '\t\t\t<td>' + table[row][7] + '</td>\n'
                text += '\t\t</tr>\n'
                if table[row][8] != '':
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td>Usage</td>\n'
                    text += '\t\t\t<td>' + convert_link(convert_code(table[row][8])) + '</td>\n'
                    #text += '\t\t\t<td>' + table[row][8] + '</td>\n'
                    text += '\t\t</tr>\n'
                if table[row][9] != '':
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td>Notes</td>\n'
                    text += '\t\t\t<td>' + convert_link(convert_code(table[row][9])) + '</td>\n'
                    #text += '\t\t\t<td>' + table[row][9] + '</td>\n'
                    text += '\t\t</tr>\n'
                if table[row][13] != '':
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td>Examples</td>\n'
                    text += '\t\t\t<td>' + convert_link(convert_code(table[row][13])) + '</td>\n'
                    text += '\t\t</tr>\n'
                text += '\t</tbody>\n'
                text += '</table>\n'
                text += '\n'
        text += '\n'
    return text
# ---------------------------------------------------------------------------
# replace URL with link (no longer used)
#
def createLinks(text):
    def repl(match):
        if match.group(1)[-1] == '.':
            return '<a href="' + match.group(1)[:-1] + '">' + match.group(1)[:-1] + '</a>.'
        return '<a href="' + match.group(1) + '">' + match.group(1) + '</a>'

    pattern = '(https?://[^\s,;\)"<]*)' # had to add left angle bracket after </code> tags inserted
    result = re.sub(pattern, repl, text)
    return result

# 2021-08-05 Add code to convert backticks copied from the DwC QRG build script written by S. Van Hoey
def convert_code(text_with_backticks):
    """Takes all back-quoted sections in a text field and converts it to
    the html tagged version of code blocks <code>...</code>
    """
    return re.sub(r'`([^`]*)`', r'<code>\1</code>', text_with_backticks)

def convert_link(text_with_urls):
    """Takes all links in a text field and converts it to the html tagged
    version of the link
    """
    def _handle_matched(inputstring):
        """quick hack version of url handling on the current prime versions data"""
        url = inputstring.group()
        return "<a href=\"{}\">{}</a>".format(url, url)

    regx = "(http[s]?://[\w\d:#@%/;$()~_?\+-;=\\\.&]*)(?<![\)\.,])"
    return re.sub(regx, _handle_matched, text_with_urls)

# ---------------------------------------------------------------------------
# read in header and footer, merge with terms table, and output
def outputMarkdown(text, headerFileName, footerFileName, outFileName):
    headerObject = open(headerFileName, 'rt', encoding='utf-8')
    header = headerObject.read()
    headerObject.close()

    footerObject = open(footerFileName, 'rt', encoding='utf-8')
    footer = footerObject.read()
    footerObject.close()

    output = header + text + footer
    outputObject = open(outFileName, 'wt', encoding='utf-8')
    outputObject.write(output)
    outputObject.close()

# ---------------------------------------------------------------------------
# main routine

# constants
githubBaseUri = 'https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/'
headerFileName = 'termlist-header.md'
footerFileName = 'termlist-footer.md'
outFileName = '../docs/termlist/index.md'

displayOrder = ['http://rs.tdwg.org/dwc/terms/attributes/Management', 
'http://rs.tdwg.org/dwc/terms/attributes/Attribution', 
'http://purl.org/dc/terms/Agent', 
'http://rs.tdwg.org/dwc/terms/attributes/ContentCoverage', 
'http://purl.org/dc/terms/Location', 
'http://purl.org/dc/terms/PeriodOfTime', 
'http://rs.tdwg.org/dwc/terms/attributes/TaxonomicCoverage', 
'http://rs.tdwg.org/dwc/terms/attributes/ResourceCreation', 
'http://rs.tdwg.org/dwc/terms/attributes/RelatedResources', 
'http://rs.tdwg.org/ac/terms/ServiceAccessPoint',
'http://rs.tdwg.org/ac/terms/RegionOfInterest'
]

displayLabel = ['Management Vocabulary', 
'Attribution Vocabulary', 
'Agents Vocabulary', 
'Content Coverage Vocabulary', 
'Geography Vocabulary', 
'Temporal Coverage Vocabulary', 
'Taxonomic Coverage Vocabulary', 
'Resource Creation Vocabulary', 
'Related Resources Vocabulary', 
'Service Access Point Vocabulary',
'Region of Interest Vocabulary'
]

displayComments = ['',
'',
'',
'',
'Note that [dwc:locality](http://rs.tdwg.org/dwc/terms/locality) may be used, but as applied to media this term may be ambiguous as to whether it applies to the location depicted or the location at which the media was created. When disambiguating information is available, it is better to use the terms Location Shown and Location Created. The latter is in the Resource Creation Vocabulary.\n\nLocation Created and Location Shown are separated in the current version of IPTC, and the Metadata Working Group ([Metadata Working Group Guidelines for Handling Image Metadata, Version 2.0, November 2010](https://web.archive.org/web/20180919181934/http://www.metadataworkinggroup.org/pdf/mwg_guidance.pdf)) also recommends this. We follow this below in order to support the expected future increase of automatic GPS-based coordinate recording. As a special case, the AC group recommends to change the semantics of Location Shown in the case of biodiversity specimens, where the original location may differ from the current location at which the specimen is held in a collection. In this case, Location Shown should exclusively refer to the location where a specimen was originally collected (gathering or sampling location). Use Location Created to express the location where the resource was created (a specimen was digitized).\n\n',
'',
'',
'',
'',
'These terms are representation-dependent metadata, referring to specific digital representations of a resource (e.g., a specific resolution, quality, or format). They are used within whatever a particular AC implementation assigns to the value of `ac:hasServiceAccessPoint`, whose label is simply "Service Access Point." Note that it is possible for an implementation to use syntactic conventions that avoid direct use of `ac:hasServiceAccessPoint`, as illustrated in the final example in the section [Multiplicity/Cardinality in the Audiovisual Core Structure document](structure.md#3-multiplicity-and-cardinality).\n\n', 
'Regions of Interest (ROI) designate specific parts of media items. Features within these regions can be taxonomically identified or linked to occurrence records. ROI metadata may also be used to generate annotations of the media item or to facilitate display or highlighting of specific parts. \n\nCurrently spatial ROIs are limited to two dimensions and can only be defined by rectangles or arcs (including circles). The terms in this group are not repeatable within a single ROI instance, although a media item may be linked to more than one ROI by the `ac:hasROI` property.\n\n For examples showing how to use these terms, see the <a href="https://github.com/tdwg/ac/blob/master/roi-recipes.md">ROI Recipes</a> page.\n\n'
]

displayId = ['Management_Vocabulary', 
'Attribution_Vocabulary', 
'Agents_Vocabulary', 
'Content_Coverage_Vocabulary', 
'Geography_Vocabulary', 
'Temporal_Coverage_Vocabulary', 
'Taxonomic_Coverage_Vocabulary', 
'Resource_Creation_Vocabulary', 
'Related_Resources_Vocabulary', 
'Service_Access_Point_Vocabulary',
'Region_of_Interest_Vocabulary'
]

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
