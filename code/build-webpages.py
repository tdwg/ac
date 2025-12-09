# Script to build Markdown pages that provide term metadata for complex vocabularies
# Steve Baskauf 2020-08-12 CC0
# updated 2021-02-11
# Updated by Matthew Blissett 2025-03.
# Modified by Steve Baskauf on 2025-11-05 from the Darwin Core webpage build script at https://github.com/tdwg/dwc/blob/b13e56eb337c51c54dee59ff17152d8bcba5bac1/build/build-webpages.py

# This script merges static Markdown header documents with term information tables (in Markdown) generated from data in the rs.tdwg.org repo from the TDWG Github site
# It replaces the previous build scripts at https://github.com/tdwg/ac/tree/56884de53008f195b07207cb5631cf6c754d5de1/code and 
# incorporates some code from https://github.com/tdwg/ac/blob/56884de53008f195b07207cb5631cf6c754d5de1/code/build_page.py ,
# https://github.com/tdwg/ac/blob/56884de53008f195b07207cb5631cf6c754d5de1/code/build_subtype_cv/build-page-simple.ipynb , and
# some of the other idiosyncratic controlled vocabulary build scripts in that commit.

import re
import json       # library to convert JSON to Python data structures
import os
import sys
import pandas as pd

import dwcterms

# -----------------
# Configuration section
# -----------------
languages = ['en', 'cs', 'de', 'es', 'fr', 'ja', 'ko', 'nl', 'pt', 'ru', 'zh-Hant']

# -----------------
# Command line arguments
# -----------------

arg_vals = sys.argv[1:]
opts = [opt for opt in arg_vals if opt.startswith('-')]
args = [arg for arg in arg_vals if not arg.startswith('-')]

# "master" for production, something else for development
if '--branch' in opts:
    github_branch = args[opts.index('--branch')]
else:
    github_branch = 'master'

if '--rspath' in opts:
    local_path_to_rs = args[opts.index('--rspath')]
else:
    local_path_to_rs = None


# -----------------
# Classes
# -----------------

class TermList:
    def __init__(self, terms, vocabType, organizedInCategories, displayOrder, displayLabel, displayComments, displayId):
        """
        Tables of terms.

        Keyword arguments:
        terms -- the loaded dwcterms term lists
        vocabType -- 1 is simple vocabulary, 2 is simple controlled vocabulary, 3 is a c.v. with broader hierarchy
        organizedInCategories -- Terms in large vocabularies like Darwin and AV Cores may be organized into categories using tdwgutility_organizedInClass.  If so, those categories can be used to group terms in the generated term list document.
        displayOrder -- If organized in categories, the display_order list must contain the IRIs that are values of tdwgutility_organizedInClass. Otherwise set to [''].
        displayLabel -- these are the section labels for the categories in the page
        displayComments -- these are the comments about the category to be appended following the section labels
        displayId -- these are the fragment identifiers for the associated sections for the categories
        config_dir -- the subdirectory of process/document_metadata_processing/ in the rs.tdwg.org repo that contains the authors and document configuration YAML files
        """

        self.terms = terms
        self.vocab_type = vocabType
        self.organized_in_categories = organizedInCategories
        self.display_order = displayOrder
        self.display_label = displayLabel
        self.display_comments = displayComments
        self.display_id = displayId
        pass

    def t(self, key):
        """
        Retrieve the translation for the given dictionary key.
        """
        if key in self.dictionary:
            return self.dictionary[key]
        else:
            return key

    def t_val(self, row, key, l):
        """
        Retrieve the value of the given term in the given locale.  Fall back to English.
        """
        if key+l in row and row[key+l] != '':
            return row[key+l]
        else:
            return row[key]

    @staticmethod
    def first(row, column_names):
        """
        Return the value of the first extant column in the row.
        """
        for name in column_names:
            if name in row:
                return row[name]

    @staticmethod
    def createLinks(text):
        """
        replace URL with link (function used with Audubon Core list of terms build script)
        Does not correctly handle URLs with close parens ) characters, so no longer used.
        """
        def repl(match):
            if match.group(1)[-1] == '.':
                return '<a href="' + match.group(1)[:-1] + '">' + match.group(1)[:-1] + '</a>.'
            return '<a href="' + match.group(1) + '">' + match.group(1) + '</a>'

        pattern = r'(https?://[^\s,;\)"<]*)'
        result = re.sub(pattern, repl, text)
        return result


    # 2021-08-06 Replace the createLinks() function with functions copied from the QRG build script written by S. Van Hoey
    @staticmethod
    def convert_code(text_with_backticks):
        """Takes all back-quoted sections in a text field and converts it to
        the html tagged version of code blocks <code>...</code>
        """
        return re.sub(r'`([^`]*)`', r'<code>\1</code>', text_with_backticks)

    @staticmethod
    def convert_link(text_with_urls):
        """Takes all links in a text field and converts it to the html tagged
        version of the link
        """
        def _handle_matched(inputstring):
            """quick hack version of url handling on the current prime versions data"""
            url = inputstring.group()
            return "<a href=\"{}\">{}</a>".format(url, url)

        regx = r"(http[s]?://[\w\d:#@%/;$()~_?\+-;=\\\.&]*)(?<![\)\.,])"
        return re.sub(regx, _handle_matched, text_with_urls)

    # Hack the code taken from the terms.tmpl template to insert the HTML necessary to make the semicolon-separated
    # lists of examples into an HTML list.
    # {% set examples = term.examples.split("; ") %}
    # {% if examples | length == 1 %}{{ examples | first }}{% else %}<ul class="list-group list-group-flush">{% for example in examples %}<li class="list-group-item">{{ example }}</li>{% endfor %}</ul>{% endif %}
    @staticmethod
    def convert_examples(text_with_list_of_examples: str) -> str:
        examples_list = text_with_list_of_examples.split('; ')
        if len(examples_list) == 1:
            return examples_list[0]
        else:
            output = '<ul class="list-group list-group-flush">\n'
            for example in examples_list:
                output += '  <li class="list-group-item">' + example + '</li>\n'
            output += '</ul>'
            return output

    def generate_index_by_name(self):
        """
        generate the index of terms grouped by category and sorted alphabetically by lowercase term local name
        """

        print('Generating term index by CURIE')

        text = ''

        if self.vocab_type==1: # controlled vocabularies only have one index (of labels)
            text += '### {index_section_string}.1 %s\n\n' % self.t('index_by_term_name')
            text += '(%s {index_section_string}.2 %s)\n\n' % (self.t('see_also'), self.t('index_by_label'))

    
            text += '**%s**\n' % self.t('classes')
            text += '\n'
            for row_index,row in self.terms.terms_sorted_by_localname.iterrows():
                if row['rdf_type'] == 'http://www.w3.org/2000/01/rdf-schema#Class':
                    curie = row['pref_ns_prefix'] + ":" + row['term_localName']
                    curie_anchor = curie.replace(':','_')
                    text += '[' + curie + '](#' + curie_anchor + ') |\n'
            text = text[:len(text)-3] # remove final trailing " |\n"
            text += '\n\n' # put back removed newline

            for category in range(0,len(self.display_order)):
                text += '**%s**\n' % self.display_label[category]
                text += '\n'
                if self.organized_in_categories:
                    filtered_table = self.terms.terms_sorted_by_localname[self.terms.terms_sorted_by_localname['tdwgutility_organizedInClass']==self.display_order[category]]
                    filtered_table.reset_index(drop=True, inplace=True)
                else:
                    filtered_table = self.terms.terms_sorted_by_localname

                for row_index,row in filtered_table.iterrows():
                    if row['rdf_type'] != 'http://www.w3.org/2000/01/rdf-schema#Class':
                        curie = row['pref_ns_prefix'] + ":" + row['term_localName']
                        curie_anchor = curie.replace(':','_')
                        text += '[' + curie + '](#' + curie_anchor + ') |\n'
                text = text[:len(text)-3] # remove final trailing " |\n"
                text += '\n\n' # put back removed newline

        index_by_name = text

        #print(index_by_name)
        print()
        return index_by_name


    def generate_index_by_label(self):
        """
        generate the index of terms by label
        """

        print('Generating term index by label')
        text = '\n\n'

        if self.vocab_type==1: # controlled vocabularies only have one index (of labels)
            text += '### {index_section_string}.2 %s\n\n' % self.t('index_by_label')
            text += '(%s {index_section_string}.1 %s)\n\n' % (self.t('see_also'), self.t('index_by_term_name'))

        # Create a table of classes if the vocabulary is not a controlled vocabulary
        seen_class = False
        for row_index,row in self.terms.terms_sorted_by_label.iterrows():
            if row['rdf_type'] == 'http://www.w3.org/2000/01/rdf-schema#Class' and self.vocab_type==1:
                if not seen_class:
                    text += '**%s**\n' % self.t('classes')
                    text += '\n'
                    seen_class = True
                curie_anchor = row['pref_ns_prefix'] + "_" + row['term_localName']
                text += '[' + row['label'] + '](#' + curie_anchor + ') |\n'
        text = text[:len(text)-3] # remove final trailing " |\n"
        text += '\n\n' # put back removed newline

        # Create rows for all terms, but remove class terms if they were pulled out in the previous section.
        for category in range(0,len(self.display_order)):
            # If there are categories, start each section with the category label
            if self.organized_in_categories:
                text += '**%s**\n\n' % self.display_label[category]
                filtered_table = self.terms.terms_sorted_by_label[self.terms.terms_sorted_by_label['tdwgutility_organizedInClass']==self.display_order[category]]
                filtered_table.reset_index(drop=True, inplace=True)
            else:
                filtered_table = self.terms.terms_sorted_by_label

            # Now list the term. Skip it if is a class, unless it's a controlled vocabulary
            for row_index,row in filtered_table.iterrows():
                if ('rdf_type' in row and row['rdf_type'] != 'http://www.w3.org/2000/01/rdf-schema#Class') or self.vocab_type!=1:
                    # Hack to prevent duplicate labels. Don't add to index if the label is the same as the previous one.
                    if row_index == 0 or (row_index != 0 and filtered_table.loc[row_index,'label'] != filtered_table.loc[row_index-1,'label']):
                        curie_anchor = row['pref_ns_prefix'] + "_" + row['term_localName']
                        text += '[' + row['label'] + '](#' + curie_anchor + ') |\n'
            text = text[:len(text)-3] # remove final trailing " |\n"
            text += '\n\n' # put back removed newline

        index_by_label = text
        print()
        #print(index_by_label)
        return index_by_label


    def generate_vocabulary_tables(self, locale):
        """
        generate a table for each term, with terms grouped by category
        """

        print('Generating terms table in', locale)
        if locale == 'en':
            l = ''
        else:
            l = '_' + locale

        # generate the Markdown for the terms table

        # Hack to control whether "Vocabulary" or "Vocabularies".
        # In Audiovisual Core, traditionally, the terms have been subdivided into categories called "vocabularies".
        # Technically all of these "vocabularies" are actually in one vocabulary: the main AC vocabulary. 
        # But to maintain this convention, we apply the following hack. In the controlled vocabularies, they are considered 
        # to be only one "Vocabulary". If there is every a second vocabulary that is not a controlled vocabulary, this hack 
        # won't work.
        if self.vocab_type==1: # the main vocabulary is a "simple vocabulary"
            text = '## {vocabulary_section_string} %s\n' % self.t('vocabularies')
        else: # controlled vocabularies are either type 2 or 3
            text = '## {vocabulary_section_string} %s\n' % self.t('vocabulary')
        #if True:
        #    filtered_table = self.terms.terms_sorted_by_localname

        for category in range(0,len(self.display_order)):
            if self.organized_in_categories:
                text += '### {vocabulary_section_string}.' + str(category + 1) + ' ' + self.display_label[category] + '\n'
                text += '\n'
                text += self.display_comments[category] # insert the comments for the category, if any.
                filtered_table = self.terms.terms_sorted_by_localname[self.terms.terms_sorted_by_localname['tdwgutility_organizedInClass']==self.display_order[category]]
                filtered_table.reset_index(drop=True, inplace=True)
            else:
                filtered_table = self.terms.terms_sorted_by_localname

            for row_index,row in filtered_table.iterrows():
                text += '<table>\n'
                text += '\t<thead>\n'
                text += '\t\t<tr>\n'
                curie = row['pref_ns_prefix'] + ":" + row['term_localName']
                curieAnchor = curie.replace(':','_')
                text += '\t\t\t<th colspan="2"><a id="%s"></a>%s %s</th>\n' % (curieAnchor, self.t('term_name'), curie)
                text += '\t\t</tr>\n'
                text += '\t</thead>\n'
                text += '\t<tbody>\n'
                text += '\t\t<tr>\n'
                text += '\t\t\t<td>%s</td>\n' % self.t('term_iri')
                uri = row['pref_ns_uri'] + row['term_localName']
                text += '\t\t\t<td><a href="%s">%s</a></td>\n' % (uri, uri)
                text += '\t\t</tr>\n'
                text += '\t\t<tr>\n'
                text += '\t\t\t<td>%s</td>\n' % self.t('modified')
                text += '\t\t\t<td>%s</td>\n' % row['term_modified']
                text += '\t\t</tr>\n'

                if row['version_iri'] != '':
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td>%s</td>\n' % self.t('term_version_iri')
                    text += '\t\t\t<td><a href="%s">%s</a></td>\n' % (row['version_iri'], row['version_iri'])
                    text += '\t\t</tr>\n'

                text += '\t\t<tr>\n'
                text += '\t\t\t<td>%s</td>\n' % self.t('label')
                text += '\t\t\t<td>%s</td>\n' % self.t_val(row, 'label', l)
                text += '\t\t</tr>\n'

                # Terms are only required or repeatable if they are NOT part of a controlled vocabulary (i.e. vocabulary type 1)
                if self.vocab_type == 1:
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td></td>\n'
                    text += '\t\t\t<td><b>%s:</b> %s – <b>%s:</b> %s</td>\n' % (self.t('required'), self.t_val(row, 'tdwgutility_required', l), self.t('repeatable'), self.t_val(row, 'tdwgutility_repeatable', l))
                    text += '\t\t</tr>\n'

                if row['term_deprecated'] != '':
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td></td>\n'
                    text += '\t\t\t<td><strong>%s</strong></td>\n' % self.t('term_deprecated')
                    text += '\t\t</tr>\n'

                    for i,dep_row in filtered_table.loc[(filtered_table['replaces_term'] == uri) | (filtered_table['replaces1_term'] == uri)].iterrows():
                        text += '\t\t<tr>\n'
                        text += '\t\t\t<td>%s</td>\n' % self.t('term_replaced_by')
                        text += '\t\t\t<td><a href="#%s_%s">%s%s</a></td>\n' % (dep_row['pref_ns_prefix'], dep_row['term_localName'], dep_row['pref_ns_uri'], dep_row['term_localName'])
                        text += '\t\t</tr>\n'

                text += '\t\t<tr>\n'
                text += '\t\t\t<td>%s</td>\n' % self.t('definition')
                if 'rdfs_comment' in row:
                    text += '\t\t\t<td>%s</td>\n' % self.t_val(row, 'rdfs_comment', l)
                else:
                    text += '\t\t\t<td>' + self.t_val(row, 'definition', l) + '</td>\n'
                text += '\t\t</tr>\n'

                # Used when there's a machine link (IRI) to a semantic model.
                # Note: inconsistent use of column headers between subjectPart/subjectOrientation and subtype tables
                if 'sawsdlrdf_modelReference' in row and row['sawsdlrdf_modelReference'] != '':
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td>%s</td>\n' % self.t('definition_derived_from')
                    text += '\t\t\t<td>' + self.convert_link(self.convert_code(row['sawsdlrdf_modelReference'])) + '</td>\n'
                    text += '\t\t</tr>\n'
                elif 'definition_derived_from' in row and row['definition_derived_from'] != '':
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td>%s</td>\n' % self.t('definition_derived_from')
                    text += '\t\t\t<td>' + self.convert_link(self.convert_code(row['definition_derived_from'])) + '</td>\n'
                    text += '\t\t</tr>\n'

                if 'skos_scopeNote' in row and row['skos_scopeNote'] != '':
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td>%s</td>\n' % self.t('usage')
                    text += '\t\t\t<td>%s</td>\n' % self.convert_link(self.convert_code(self.t_val(row, 'skos_scopeNote', l)))
                    text += '\t\t</tr>\n'
                elif 'usage' in row and row['usage'] != '':
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td>%s</td>\n' % self.t('usage')
                    text += '\t\t\t<td>%s</td>\n' % self.convert_link(self.convert_code(self.t_val(row, 'usage', l)))
                    text += '\t\t</tr>\n'

                if 'dcterms_description' in row and row['dcterms_description'] != '':
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td>%s</td>\n' % self.t('notes')
                    text += '\t\t\t<td>%s</td>\n' % self.convert_link(self.convert_code(self.t_val(row, 'dcterms_description', l)))
                    text += '\t\t</tr>\n'
                elif 'notes' in row and row['notes'] != '':
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td>%s</td>\n' % self.t('notes')
                    text += '\t\t\t<td>%s</td>\n' % self.convert_link(self.convert_code(self.t_val(row, 'notes', l)))
                    text += '\t\t</tr>\n'

                if 'examples' in row and row['examples'] != '':
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td>%s</td>\n' % self.t('examples')
                    text += '\t\t\t<td>%s</td>\n' % self.convert_examples(self.convert_link(self.convert_code(self.t_val(row, 'examples', l))))
                    text += '\t\t</tr>\n'

                if 'tdwgutility_abcdEquivalence' in row and row['tdwgutility_abcdEquivalence'] != '':
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td>%s</td>\n' % self.t('abcd_equivalence')
                    text += '\t\t\t<td>%s</td>\n' % self.convert_link(self.convert_code(row['tdwgutility_abcdEquivalence']))
                    text += '\t\t</tr>\n'

                if (self.vocab_type == 2 or self.vocab_type == 3) and row['controlled_value_string'] != '': # controlled vocabulary
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td>%s</td>\n' % self.t('controlled_value')
                    text += '\t\t\t<td>%s</td>\n' % row['controlled_value_string']
                    text += '\t\t</tr>\n'

                if self.vocab_type == 3 and row['skos_broader'] != '': # controlled vocabulary with skos:broader relationships
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td>%s</td>\n' % self.t('has_broader_concept')
                    text += '\t\t\t<td><a href="#%s_%s">%s:%s</a></td>\n' % (row['pref_ns_prefix'], row['skos_broader'], row['pref_ns_prefix'], row['skos_broader'])
                    text += '\t\t</tr>\n'

                if 'skos_exactMatch' in row and row['skos_exactMatch'] != '':
                    text += '\t\t<tr>\n'
                    text += '\t\t\t<td>%s</td>\n' % self.t('has_exact_match')
                    text += '\t\t\t<td><a href="#%s_%s">%s:%s</a></td>\n' % (row['pref_ns_prefix'], row['skos_exactMatch'], row['pref_ns_prefix'], row['skos_exactMatch'])
                    text += '\t\t</tr>\n'

                text += '\t\t<tr>\n'
                text += '\t\t\t<td>%s</td>\n' % self.t('type')
                if row['rdf_type'] == 'http://www.w3.org/1999/02/22-rdf-syntax-ns#Property':
                    text += '\t\t\t<td>%s</td>\n' % self.t('property')
                elif row['rdf_type'] == 'http://www.w3.org/2000/01/rdf-schema#Class':
                    text += '\t\t\t<td>%s</td>\n' % self.t('class')
                elif row['rdf_type'] == 'http://www.w3.org/2004/02/skos/core#Concept':
                    text += '\t\t\t<td>%s</td>\n' % self.t('concept')
                else:
                    text += '\t\t\t<td>%s</td>\n' % row['rdf_type'] # this should rarely happen
                text += '\t\t</tr>\n'

                # Look up decisions related to this term
                for j, decision in self.terms.decisions_df.loc[self.terms.decisions_df['linked_affected_resource'] == uri].iterrows():
                    if decision['decision_localName'] != '':
                        text += '\t\t<tr>\n'
                        text += '\t\t\t<td>%s</td>\n' % self.t('executive_committee_decision')
                        text += '\t\t\t<td><a href="http://rs.tdwg.org/decisions/%s">http://rs.tdwg.org/decisions/%s</a></td>\n' % (decision['decision_localName'], decision['decision_localName'])
                        text += '\t\t</tr>\n'

                text += '\t</tbody>\n'
                text += '</table>\n'
                text += '\n'
            text += '\n'
        term_table = text
        print('done generating')
        print()

        #print(term_table)
        return term_table


    def generate_term_list_markdown(self, locale, outFileName, dictionaryFileName, headerFileName, index_section_number):
        """
        Merge term table with header Markdown, then save file
        """

        # read in header, merge with terms table, and output
        with open(dictionaryFileName, encoding='utf-8') as jsonFile:
            self.dictionary = json.load(jsonFile)

        print('Merging term table with header and saving file')
        text = ''
        if self.organized_in_categories:
            text += self.generate_index_by_name()
        text += self.generate_index_by_label()
        text += self.generate_vocabulary_tables(locale)

        # read in header, merge with terms table, and output
        headerObject = open(headerFileName, 'rt', encoding='utf-8')
        header = headerObject.read()
        headerObject.close()

        # Build the Markdown for the contributors list
        contributors = ''
        for contributor in self.terms.contributors_yaml:
            contributors += '[' + contributor['contributor_literal'] + '](' + contributor['contributor_iri'] + ')'
            if contributor['affiliation'] != '':
                contributors += ' ([' + contributor['affiliation'] + '](' + contributor['affiliation_uri'] + ')'
                if contributor['contributor_role'] == 'review manager':
                    contributors += ', review manager'
                contributors += ')'
            contributors += ', '
        contributors = contributors[:-2] # Remove the last comma and space

        # Substitute values of ratification_date and contributors into the header template
        header = header.replace('{document_title}', self.terms.document_configuration_yaml['documentTitle'])
        header = header.replace('{ratification_date}', self.terms.document_configuration_yaml['doc_modified'])
        header = header.replace('{created_date}', self.terms.document_configuration_yaml['doc_created'])
        header = header.replace('{contributors}', contributors)
        header = header.replace('{standard_iri}', self.terms.document_configuration_yaml['dcterms_isPartOf'])
        header = header.replace('{current_iri}', self.terms.document_configuration_yaml['current_iri'])
        header = header.replace('{abstract}', self.terms.document_configuration_yaml['abstract'])
        header = header.replace('{creator}', self.terms.document_configuration_yaml['creator'])
        header = header.replace('{publisher}', self.terms.document_configuration_yaml['publisher'])
        year = self.terms.document_configuration_yaml['doc_modified'].split('-')[0]
        header = header.replace('{year}', year)

        # Determine whether there was a previous version of the document.
        if self.terms.document_configuration_yaml['doc_created'] != self.terms.document_configuration_yaml['doc_modified']:
            # Load versions list from document versions data in the rs.tdwg.org repo and find most recent version.
            versions_data_url = self.terms.githubBaseUri + 'docs/docs-versions.csv'
            versions_list_df = pd.read_csv(versions_data_url, na_filter=False)
            # Slice all rows for versions of this document.
            matching_versions = versions_list_df[versions_list_df['current_iri']==self.terms.document_configuration_yaml['current_iri']]
            # Sort the matching versions by version IRI in descending order so that the most recent version is first.
            matching_versions = matching_versions.sort_values(by=['version_iri'], ascending=[False])
            # The previous version is the second row in the dataframe (row 1).
            # The version IRI is in the second column (column 1).
            most_recent_version_iri = matching_versions.iat[1, 1]
            #print(most_recent_version_iri)

            # Insert the previous version information into the header
            previous_version_metadata_string = "Previous version\n: <" + most_recent_version_iri + ">\n\n"
            # Insert the previous version information into the designated slot.
            header = header.replace('{previous_version_slot}\n\n', previous_version_metadata_string)
        else:
            # If there was no previous version, remove the slot from the header.
            header = header.replace('{previous_version_slot}\n\n', '')

        output = header + text

        # Substitute the indices and vocabulary section numbers
        index_section_string = str(index_section_number)
        output = output.replace('{index_section_string}', index_section_string)
        vocabulary_section_string = str(index_section_number + 1)
        output = output.replace('{vocabulary_section_string}', vocabulary_section_string)

        outputObject = open(outFileName, 'wt', encoding='utf-8')
        outputObject.write(output)
        outputObject.close()

        print('done')


    def get_term_definition(self, locale, term_iri):
        """Extract the required information from the terms table to show on
        the webpage of a single term by using the term_iri as the identifier
        """

        if locale == 'en':
            l = ''
        else:
            l = '_' + locale

        term_data = {}

        term = self.terms.terms_sorted_by_localname.loc[self.terms.terms_sorted_by_localname['term_iri'] == term_iri].iloc[0]

        term_data["label"] = term['term_localName'] # See https://github.com/tdwg/dwc/issues/253#issuecomment-670098202
        term_data["iri"] = term['pref_ns_uri'] + term['term_localName']
        term_data["class"] = term['tdwgutility_organizedInClass']
        term_data["definition"] = self.convert_link(self.t_val(term, 'rdfs_comment', l))
        term_data["comments"] = self.convert_link(self.convert_code(self.t_val(term, 'dcterms_description', l)))
        term_data["examples"] = self.convert_link(self.convert_code(self.t_val(term, 'examples', l)))
        term_data["rdf_type"] = term['rdf_type']
        term_data["namespace"] = term['pref_ns_prefix']
        return term_data


    def process_terms(self, locale):
        """Parse the config terms (sequence matters!)

        Collect all required data from both the normative versions file and
        the config file and return the template ready data.  Choose the
        relevant locale.

        Returns
        -------
        Data object that can be digested by the html-template file. Contains
        the term data formatted to create the indidivual outputs, each list
        element is a dictionary representing a class group. Hence, the data
        object is structured as follows:

            [
                {'name' : class_group_name_1, 'label': xxxx,...,
                    'terms':
                        [
                            {'name' : term_1, 'label': xxxx,...},
                            {'name' : term_2, 'label': xxxx,...},
                            ...
                        ]}
                {'name' : class_group_name_2,...
                ...},
                ...
            ]
        """
        template_data = []
        in_class = "Record-level"
        # sequence matters in config and it starts with Record-level which we populate here ad-hoc
        class_group = {}
        class_group["isRecordLevel"] = True
        class_group["label"] = self.t('record-level')
        class_group["iri"] = None
        class_group["class"] = None
        class_group["definition"] = None
        class_group["comments"] = None
        class_group["rdf_type"] = None
        class_group["terms"] = []
        class_group["namespace"] = None

        qrg_df = pd.read_csv('qrg-template/qrg-list.csv', na_filter=False)

        addedUseWithIRI = False
        for term_index,term in qrg_df.iterrows(): # sequence of the terms used as order
            term_data = self.get_term_definition(locale, term['recommended_term_iri'])
            if term_data["rdf_type"] == "http://www.w3.org/2000/01/rdf-schema#Class":
                # new class encountered
                # store previous section in template_data
                template_data.append(class_group)
                #start new class group
                class_group = term_data
                class_group["terms"] = []
                in_class = term_data["label"] # check on the class working in
            elif term_data['iri']=='http://rs.tdwg.org/dwc/iri/behavior':
                # This is the first row of dwciri terms
                # store previous section in template_data
                template_data.append(class_group)
                #start a class group for UseWithIRI
                class_group = {"label":"UseWithIRI"}
                class_group["terms"] = []
                in_class = "UseWithIRI" # check on the class working in
                addedUseWithIRI = True
                class_group['terms'].append(term_data)
            else:
                class_group['terms'].append(term_data)
        # save the last class to template_data
        template_data.append(class_group)
        return template_data

# -----------------
# Functions
# -----------------

def generate_all_markdown(termList, path, locales, index_section_number):
    """
    Generate a Darwin Core term list for DWC terms or one of its vocabularies.

    Keyword arguments:
    termList -- Term data to use
    path -- Path fragment used for output and finding templates
    locales -- Locales to generate
    """

    for locale in locales:
        print("Generating %s/index.md in" % path, locale)
        dictionaryFileName = 'termlist-dictionary.%s.json' % locale
        headerFileName = path + '-template/termlist-header.%s.md' % locale

        if locale == 'en':
            outFileName = '../docs/%s/index.md' % path
        else:
            outFilePath = '../docs/%s/%s' % (locale, path)
            os.makedirs(outFilePath, exist_ok=True)
            outFileName = outFilePath + '/index.md'

        termList.generate_term_list_markdown(locale, outFileName, dictionaryFileName, headerFileName, index_section_number)
        print("")

def retrieve_databases_for_vocabulary(vocabulary_iri):
    """Use the vocabulary IRI to determine which term lists are members of that vocabulary,
    by searching the table of vocabulary members in the rs.tdwg.org GitHub repository. 
    Then retrieve the rs.tdwg.org database names (i.e. directories) for each of those term lists,
    using the term-lists table in the rs.tdwg.org GitHub repository.

    NOTE: Currently operates only on remote GitHub data (local filesystem not yet supported).

    Returns
    -------
    List of database names
    """
    githubBaseUri = 'https://raw.githubusercontent.com/tdwg/rs.tdwg.org/' + github_branch + '/'

    # Load the table of term lists into a DataFrame with the list IRI as the row label index
    term_lists_df = pd.read_csv(githubBaseUri + 'term-lists/term-lists.csv', na_filter=False)
    term_lists_df = term_lists_df.set_index('list')

    # Load the table of vocabulary members into a DataFrame with the vocabulary IRI as the row label index
    vocabulary_members_df = pd.read_csv(githubBaseUri + 'vocabularies/vocabularies-members.csv', na_filter=False)
    vocabulary_members_df = vocabulary_members_df.set_index('vocabulary')

    # Slice rows in the vocabulary members DataFrame that match the vocabulary IRI, and extract the term list IRI column.
    # Result is a Series.
    matching_members = vocabulary_members_df.loc[vocabulary_iri, 'termList']
    # Use the series values as the selector for slicing the term lists dataframe to extract the rows whose indices are the term list IRIs.
    result = term_lists_df.loc[matching_members, 'database']
    # Return the database column as a list
    # If multiple values coerce from a Series. Otherwise it is a single string value.
    try:
        result_list = result.tolist()
    except:
        result_list = [result]
    return result_list

# -----------------
# Main routine
# -----------------

# List of Terms for the main vocabulary
document_iri = 'http://rs.tdwg.org/ac/doc/termlist/'
databases = retrieve_databases_for_vocabulary('http://rs.tdwg.org/ac/')

ac = dwcterms.DwcTerms(
    termLists = databases,
    docMetadataFilePath = document_iri[19:-1].replace('/','_') + '/',
    rsPath = local_path_to_rs,
    githubBranch = github_branch)
ac_list = TermList(
    terms = ac,
    vocabType = 1,
    organizedInCategories = True,
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
                    ],
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
                    ],
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
],
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
)

# Because different docs have a different section number for the indices, indicate it here.
# The Vocabulary section is assumed to be the next section after the indices.
index_section_number = 6
# List of Terms HTML. document_iri[19:-1].split('/')[2] gets the page slug
generate_all_markdown(ac_list, document_iri[19:-1].split('/')[2], languages, index_section_number)


# Variant Vocabulary
document_iri = 'http://rs.tdwg.org/ac/doc/variant/'
databases = retrieve_databases_for_vocabulary('http://rs.tdwg.org/acvariant/')
variant = dwcterms.DwcTerms(
    termLists = databases,
    docMetadataFilePath = document_iri[19:-1].replace('/','_') + '/',
    rsPath = local_path_to_rs,
    githubBranch = github_branch)
variant_list = TermList(
    terms = variant,
    vocabType = 2,
    organizedInCategories = False,
    displayOrder = [''],
    displayLabel = ['Vocabulary'],
    displayComments = [''],
    displayId = ['Vocabulary']
)

# Because different docs have a different section number for the indices, indicate it here.
# The Vocabulary section is assumed to be the next section after the indices.
index_section_number = 3
# List of Terms HTML. document_iri[19:-1].split('/')[2] gets the page slug
generate_all_markdown(variant_list, document_iri[19:-1].split('/')[2], languages, index_section_number)


# Subtype Vocabulary
document_iri = 'http://rs.tdwg.org/ac/doc/subtype/'
databases = retrieve_databases_for_vocabulary('http://rs.tdwg.org/acsubtype/')
subtype = dwcterms.DwcTerms(
    termLists = databases,
    docMetadataFilePath = document_iri[19:-1].replace('/','_') + '/',
    rsPath = local_path_to_rs,
    githubBranch = github_branch)
subtype_list = TermList(
    terms = subtype,
    vocabType = 2,
    organizedInCategories = False,
    displayOrder = [''],
    displayLabel = ['Vocabulary'],
    displayComments = [''],
    displayId = ['Vocabulary']
)

# Because different docs have a different section number for the indices, indicate it here.
# The Vocabulary section is assumed to be the next section after the indices.
index_section_number = 3
# List of Terms HTML. document_iri[19:-1].split('/')[2] gets the page slug
generate_all_markdown(subtype_list, document_iri[19:-1].split('/')[2], languages, index_section_number)


# Format Vocabulary
document_iri = 'http://rs.tdwg.org/ac/doc/format/'
databases = retrieve_databases_for_vocabulary('http://rs.tdwg.org/format/')
format = dwcterms.DwcTerms(
    termLists = databases,
    docMetadataFilePath = document_iri[19:-1].replace('/','_') + '/',
    rsPath = local_path_to_rs,
    githubBranch = github_branch)
format_list = TermList(
    terms = format,
    vocabType = 3,
    organizedInCategories = True,
    displayOrder = ['', 'm', 'e'],
    displayLabel = ['Concept schemes', 'Media types and physical media concept scheme', 'File extensions concept scheme'],
    displayComments = ['','',''],
    displayId = ['general_types', 'media_types', 'file_extensions']
)

# Because different docs have a different section number for the indices, indicate it here.
# The Vocabulary section is assumed to be the next section after the indices.
index_section_number = 3
# List of Terms HTML. document_iri[19:-1].split('/')[2] gets the page slug
generate_all_markdown(format_list, document_iri[19:-1].split('/')[2], languages, index_section_number)


# Subject Part Vocabulary
document_iri = 'http://rs.tdwg.org/ac/doc/part/'
databases = retrieve_databases_for_vocabulary('http://rs.tdwg.org/acpart/')
subjectPart = dwcterms.DwcTerms(
    termLists = databases,
    docMetadataFilePath = document_iri[19:-1].replace('/','_') + '/',
    rsPath = local_path_to_rs,
    githubBranch = github_branch)
subjectPart_list = TermList(
    terms = subjectPart,
    vocabType = 3,
    organizedInCategories = False,
    displayOrder = [''],
    displayLabel = ['Vocabulary'],
    displayComments = [''],
    displayId = ['Vocabulary']
)

# Because different docs have a different section number for the indices, indicate it here.
# The Vocabulary section is assumed to be the next section after the indices.
index_section_number = 3
# List of Terms HTML. document_iri[19:-1].split('/')[2] gets the page slug
generate_all_markdown(subjectPart_list, document_iri[19:-1].split('/')[2], languages, index_section_number)


# Subject Orientation Vocabulary
document_iri = 'http://rs.tdwg.org/ac/doc/orient/'
databases = retrieve_databases_for_vocabulary('http://rs.tdwg.org/acorient/')
subjectOrientation = dwcterms.DwcTerms(
    termLists = databases,
    docMetadataFilePath = document_iri[19:-1].replace('/','_') + '/',
    rsPath = local_path_to_rs,
    githubBranch = github_branch)
subjectOrientation_list = TermList(
    terms = subjectOrientation,
    vocabType = 3,
    organizedInCategories = False,
    displayOrder = [''],
    displayLabel = ['Vocabulary'],
    displayComments = [''],
    displayId = ['Vocabulary']
)

# Because different docs have a different section number for the indices, indicate it here.
# The Vocabulary section is assumed to be the next section after the indices.
index_section_number = 3
# List of Terms HTML. document_iri[19:-1].split('/')[2] gets the page slug
generate_all_markdown(subjectOrientation_list, document_iri[19:-1].split('/')[2], languages, index_section_number)
