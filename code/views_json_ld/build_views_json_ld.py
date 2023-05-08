# Script to build JSON-LD pages that provide multilingual labels and definitions controlled vocabularies
# Steve Baskauf 2021-01-08 CC0

import re
import requests   # best library to manage HTTP transactions
import csv        # library to read/write/parse CSV files
import json       # library to convert JSON to Python data structures
import pandas as pd

# -----------------
# Configuration section
# -----------------

# Read in mutable configuration variables
with open('config_views_json_ld.json', 'rt', encoding='utf-8') as file_object:
    config_text = file_object.read()
config = json.loads(config_text)

# This is the base URL for raw files from the branch of the repo that has been pushed to GitHub. 

github_base_url = 'https://raw.githubusercontent.com/tdwg/rs.tdwg.org/' + config['branch'] + '/'
database_name = config['database_name']

translations_url = github_base_url + database_name + '/' + database_name +'-translations.csv'

has_broader = config['has_broader'] # set to true in configuration file if any terms have skos:broader values
has_exactMatch = config['has_exactMatch'] # set to true of any terms have skos:exactMatch values

label_col_prefix = 'label_'
def_col_prefix = 'definition_'
localname_column_header = 'term_localName'

# ---------------
# Function definitions
# ---------------

# replace URL with link
#
def createLinks(text):
    def repl(match):
        if match.group(1)[-1] == '.':
            return '<a href="' + match.group(1)[:-1] + '">' + match.group(1)[:-1] + '</a>.'
        return '<a href="' + match.group(1) + '">' + match.group(1) + '</a>'

    pattern = '(https?://[^\s,;\)"]*)'
    result = re.sub(pattern, repl, text)
    return result

frame = pd.read_csv(github_base_url + database_name + '/constants.csv', na_filter=False)
namespace_iri = frame.domainRoot[0]

translations_frame = pd.read_csv(translations_url, na_filter=False)
columns = translations_frame.columns

# Extract the list of languages from the translations spreadsheet column headers
languages = []
for column_header in columns:
    if label_col_prefix in column_header:
        language_code = column_header.split(label_col_prefix)[1]
        if language_code != 'en':
            languages.append(column_header.split(label_col_prefix)[1])
print('translation languages:', languages)

# Create a dictionary of language dictionaries for the terms
translations_dictionary = {}
for index,row in translations_frame.iterrows():
    language_dictionary = {}
    for language in languages:
        term_dictionary = {'label': row[label_col_prefix + language], 'definition': row[def_col_prefix + language]}
        language_dictionary[language] = term_dictionary
    translations_dictionary[row[localname_column_header]] = language_dictionary
#print(json.dumps(translations_dictionary, indent = 2))

# Extract the term information from the CSV file and create a list of dictionaries

term_info = []
frame = pd.read_csv(github_base_url + database_name + '/' + database_name + '.csv', na_filter=False)
for index, row in frame.iterrows():
    term_dict = {}
    term_dict['localname'] = row['term_localName']
    term_dict['iri'] = namespace_iri + row['term_localName']
    term_dict['label'] = []
    term_dict['label'].append({'language': 'en', 'value': row['label']})
    for language in languages:
        term_dict['label'].append({'language': language, 'value': translations_dictionary[row['term_localName']][language]['label']})
    term_dict['definition'] = []
    term_dict['definition'].append({'language': 'en', 'value': row['definition']})
    for language in languages:
        term_dict['definition'].append({'language': language, 'value': translations_dictionary[row['term_localName']][language]['definition']})
    term_dict['cv_string'] = row['controlled_value_string']
    if row['skos_inScheme'] != '':
        term_dict['scheme'] = namespace_iri + row['skos_inScheme']
    else:
        term_dict['scheme'] = ''
    term_dict['type'] = row['type']
    if has_broader:
        if row['skos_broader'] != '':
            term_dict['broader'] = namespace_iri + row['skos_broader']
        else:
            term_dict['broader'] = ''
    if has_exactMatch:
        if row['skos_exactMatch'] != '':
            term_dict['match'] = namespace_iri + row['skos_exactMatch']
        else:
            term_dict['match'] = ''
    term_dict['value'] = row['controlled_value_string']
    term_dict['derived_from'] = row['definition_derived_from']
    term_info.append(term_dict)
#print(json.dumps(term_info, indent = 2))

# Create the JSON-LD context, then create the JSON LD for each term

context_dict = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "sawsdlrdf": "http://www.w3.org/ns/sawsdl#",
    "skos:inScheme": {"@type": "@id"}
  }

if has_broader:
    context_dict['skos:broader'] = {"@type": "@id"}

if has_exactMatch:
    context_dict['skos:exactMatch'] = {"@type": "@id"}

graph_list = []
for term in term_info:
    term_dict = {}
    term_dict['@id'] = term['iri']
    term_dict['@type'] = term['type']
    if term['value'] != '':
        term_dict['rdf:value'] = term['value']
    if term['scheme'] != '':
        term_dict['skos:inScheme'] = term['scheme']
    if has_broader:
        if term['broader'] != '':
            term_dict['skos:broader'] = term['broader']
    if has_exactMatch:
        if term['match'] != '':
            term_dict['skos:exactMatch'] = term['match']
    if term['derived_from'] != '':
        term_dict['sawsdlrdf:modelReference'] = term['derived_from']
    label_list = []
    for lang_label in term['label']:
        label_list.append({'@language': lang_label['language'], '@value': lang_label['value']})
    term_dict['skos:prefLabel'] = label_list
    
    def_list = []
    for lang_label in term['definition']:
        def_list.append({'@language': lang_label['language'], '@value': lang_label['value']})
    term_dict['skos:definition'] = def_list
    
    graph_list.append(term_dict)

output = {"@context": context_dict, "@graph": graph_list}
#jsonld_output = json.dumps(output, indent = 2) # output as escaped characters
jsonld_output = json.dumps(output, indent = 2, ensure_ascii=False) # output at UTF-8 strings
#print(jsonld_output)

# Write the JSON-LD to a file

# outputObject = open(out_filename, 'wt', encoding='utf-8') # use with escaped characters
for out_filename in [database_name + '.json', database_name + '.jsonld']:
    outputObject = open(out_filename, 'w', encoding='utf-8') # use with UTF-8 strings
    outputObject.write(jsonld_output)
    outputObject.close()
    
print('Done writing the multilingual JSON-LD file.')

# ---------------------------------------------
# Build the SKOS Collections
# ---------------------------------------------

# Set this value to "part" for the parts collections and to "orient" for orientations collections
if database_name == 'acorient':
    selection = 'orient'
elif database_name == 'acpart':
    selection = 'part'
else:
    print('Error: database name must be acorient or acpart')
    exit()

collections = pd.read_csv(selection + '_collections.csv', na_filter=False, dtype = str)
join = pd.read_csv('part_collection_join.csv', na_filter=False, dtype = str)
concepts = pd.read_csv(github_base_url + database_name + '/' + database_name + '.csv', na_filter=False)

#collections.head()
#join.head()
#concepts.head()

# Configuration
database_name = 'ac' + selection
languages = [] # Multilingual support needs to be added; see the older script which enabled it
collection_namespace_iri = 'http://rs.tdwg.org/' + database_name + '/collection/'
concept_namespace_iri = 'http://rs.tdwg.org/' + database_name + '/values/'

# Simultaneously generate a Markdown document
markdown_string = '# Controlled value strings from SKOS Collections for '
if selection == 'part':
    markdown_string += 'ac:subjectPartLiteral\n\n'
elif selection == 'orient':
    markdown_string += 'ac:subjectOrientationLiteral\n\n'
else:
    pass

# Extract data from the dataframe
term_info = []
for index, row in collections.iterrows():
    term_dict = {}
    term_dict['localname'] = row['term_localName']
    term_dict['iri'] = collection_namespace_iri + row['term_localName']
    
    term_dict['label'] = []
    term_dict['label'].append({'language': 'en', 'value': row['label']})
    for language in languages:
        term_dict['label'].append({'language': language, 'value': translations_dictionary[row['term_localName']][language]['label']})

    term_dict['definition'] = []
    term_dict['definition'].append({'language': 'en', 'value': row['definition']})
    for language in languages:
        term_dict['definition'].append({'language': language, 'value': translations_dictionary[row['term_localName']][language]['definition']})
        
    term_dict['type'] = row['type']
    term_info.append(term_dict)
    
# Start building the Python data structure analogous to the evental output JSON
context_dict = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "skos:member": {"@type": "@id"}
  }

if selection == 'orient': # only the orientation collections need to be linked back to part concepts
    context_dict['tdwgutility:ofConcept'] = {"@type": "@id"}

graph_list = []
for term in term_info:
    term_dict = {}
    term_dict['@id'] = term['iri']
    term_dict['@type'] = term['type']
    if selection == 'orient': # only orientation collections need to be linked to a part concept
        term_dict['tdwgutility:ofConcept'] = 'http://rs.tdwg.org/acpart/values/' + term['localname']
    
    label_list = []
    for lang_label in term['label']:
        label_list.append({'@language': lang_label['language'], '@value': lang_label['value']})

        # Add to Markdown doc
        if lang_label['language'] == 'en':
            markdown_string += '## ' + lang_label['value'] + '\n<ul>\n'
            #print(lang_label['value'])
        
    term_dict['skos:prefLabel'] = label_list
        
    def_list = []
    for lang_label in term['definition']:
        def_list.append({'@language': lang_label['language'], '@value': lang_label['value']})
    term_dict['skos:definition'] = def_list
    
    # Add the members of the collection
    members_list = []
    for index, row in join.iterrows():
        if row['collection_id'] == term['localname']:
            members_list.append(concept_namespace_iri + row['member_id'])
            
            # Add to Markdown doc: look up the CV string in the concepts dataframe
            cv_string = concepts.loc[concepts.term_localName == row['member_id'], 'controlled_value_string'].values[0]
            markdown_string += '<li>' + cv_string + '</li>\n'
            
    term_dict['skos:member'] = members_list
    
    # Add to Markdown doc
    markdown_string += '</ul>\n\n'
    
    graph_list.append(term_dict)

output = {"@context": context_dict, "@graph": graph_list}

jsonld_output = json.dumps(output, indent = 2, ensure_ascii=False) # output at UTF-8 strings
#print(jsonld_output)

# Write the SKOS Collections JSON-LD to a file

for out_filename in [database_name + '_collection.json', database_name + '_collection.jsonld']:
    outputObject = open(out_filename, 'w', encoding='utf-8') # use with UTF-8 strings
    outputObject.write(jsonld_output)
    outputObject.close()
    
with open('../../docs/' + selection + '_collections.md', 'wt', encoding='utf-8') as fileObject:
    fileObject.write(markdown_string)
    
print('Done writing SKOS Collections.')
