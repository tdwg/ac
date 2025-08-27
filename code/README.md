# Notes on generating new Audiovisual Core list of terms documents

## Workflow for generating the main Audiovisual Core List of Terms page

**Note:** This describes the process for using scripts as they exist 2025-08-27. Eventually the scripts should be modified to follow the procedures used with the scripts that generate the Darwin Core Lists of Terms documents, which are more streamlined, include all of the controlled vocabularies, and facilitate non-English translations. 

1. Carry out the steps for updating the underlying metadata in the rs.tdwg.org GitHub repository, outlined [here](https://github.com/tdwg/rs.tdwg.org/blob/master/process/process-vocabulary.md#3-detailed-workflow-steps) in Section 3.

2. It is best to create a branch of the `ac` repo before generating the new page. The avoids messing up the existing page in the event that something goes wrong and also makes it possible to create drafts that can be viewed prior to ratification, or for proofreading. When ratified changes have been proofread, the branch can be merged into the `master` branch to make the updated page go live on the AC website.

3. The current Markdown file for the current List of Terms document must be renamed to be a dated version, with updated  interversion links. This is done using the [update_previous_doc.py](https://github.com/tdwg/ac/blob/master/code/update_previous_doc.py) Python script in the `code` directory of the ac GitHub repo. The script must be run with the following command line arguments:

```
python update_previous_doc.py --dir ac_doc_termlist --slug termlist 
```

If the data in rs.tdwg.org are provisional and present in a branch other than `master`, the `--branch` argument can be used to specify the branch of rs.tdwg.org to be used as the data source, e.g. 

```
python update_previous_doc.py --dir ac_doc_termlist --slug termlist --branch ac-revisions
```

4. After running the script, check the diffs to make sure that the new dated version of the file has been added and that the `index.md` version was deleted. It is best to not yet make a commit, so that the changes in the `index.md` files can be seen in the diff after the next script is run.

5. To generate the new list of terms, run the Python script [build_page.py](https://github.com/tdwg/ac/blob/master/code/build_page.py). The command line arguments are the same as with the `update_previous_doc.py` script above:

```
python build_page.py --dir ac_doc_termlist --slug termlist
```

As above, you can supply a branch of rs.tdwg.org other than `master` using the `--branch` argument.

6. After the script has been run, check the diffs for the `index.md` file to make sure that the changes make sense. If they do, commit and push the changes to GitHub. If the changes have been ratified, make a pull request to merge the provisional branch of the ac repo into the `master` branch.

## Workflow for generating Views controlled vocabularies

Past source data files are in subdirectories of `process/ac-revisions/` using the naming pattern `ac-views-cv-yyyy-mm-dd`. The files placed in this directory only include the rows for terms that have bein **changed** from what they were before (modified or new). Rows for existing terms that are unmodified are **not** be included. When making a change to the vocabularies, create a new dated directory that includes source data files for the vocabullaries to be changed. Those files should include rows for new terms following the column header patterns of existing files. Changed terms should include the entire row for the term that is to be changed. 

Unless otherwise noted, the location of other files mentioned here are in the `views_json_ld` directory that is a subdirectory of this one.

1. If creating terms for a new organism group, add the group to `part_collections.csv`.
2. Add any new subjectPart values for the group to a new `subjectPart_cv.csv` file in the `process/ac-revisions/ac-views-cv-yyyy-mm-dd/` folder of the rs.tdwg.org repo. Don't add any that already exist as analogs from other organism groups.
3. Create the links between the organism group to all of the parts (new or existing) in the top section of `part_collection_join.csv`.
4. If there are any new subjectOrientation values (unlikely at this point), add them to `subjectOrientation_cv.csv` file in the `process/ac-revisions/ac-views-cv-yyyy-mm-dd/` folder of the rs.tdwg.org repo. 
5. For each new part added in 2 above, create links from the part to each orientation appropriate for that part in the lower section of `part_collection_join.csv`. NOTE: if a part in a certain organism group has different possible orientations from the same part in other organism groups, then that part can't be considered to be the same and a new part specific to that group should be created!
6. The `subjectPart_cv.csv` and `subjectOrientation_cv.csv` files with the basic part and orientation data need to be uploaded to the `rs.tdwg.org` repo on the TDWG GitHub site. For provisional changes, this should be done using a branch. If it's a ratified change, that branch can eventually be merged to the main (master) branch after testing. To make it easier to see what the new information is that's being added, we've been storing the changed files in subdirectories of `process/ac-revisions/` using the naming pattern `ac-views-cv-yyyy-mm-dd`. NOTE: as described above, the files placed in this directory should only have the rows for terms that are being **changed** from what they were before (modified or new). Rows for existing terms that are unmodified should **not** be included. 
7. When the script is run to update the data in the `rs.tdwg.org` repo, it needs information from a `config.json` file to tell it where the source files are and some other information. There is a separate one for each vocab to be updated, so I've been keeping versions `config_orient.json` and `config_part.json` in the `process/ac-revisions/ac-views-cv-yyyy-mm-dd` folder as a record, and then copying them to the `process` directory and changing their name to `config.json` as I ran the script to regenerate each vocabulary.
8. Prior to running the processing script, copy the appropriate config file from 7 into the `process` directory and change its name to `config.json`. 
9. Run the Python script `process.py` in the `process` directory of the `rs.tdwg.org` repo. Check the git diffs to make sure everything looks good, then push the changes. Change the `config.json` to the other vocabulary and repeat (if necessary). If everything is good, push the changes. NOTE: If new ratified terms or changes have occurred, the Decision history will have to be updated prior to the next step, otherwise the decision won't be included in the metadata for the term. See [step 9 of this workflow](https://github.com/tdwg/rs.tdwg.org/blob/master/process/process-vocabulary.md#143-general-workflow).
10. Run the Python Jupyter script `build-page.py` in the `build_subjectOrientation_cv` subdirectory. It outputs the List of terms file as `index.md` in the `docs/orient/` directory and uses the header information from the `termlist-header.md` file in the same directory.
11. Run the Python Jupyter notebook `build-page.py` in the `build_subjectPart_cv` subdirectory as above. Push the changes to GitHub and Jekyll will rebuild the AC website with the changed documents.
12. Edit the `config_views_json_ld.json` file in the `views_json_ld` subdirectory to pull data from the appropriate directory of the `rs.tdwg.org` repo (e.g. `acorient`). Run the Python script `build-views-json-ld.py` to generate the new JSON-LD for the terms, collections, as well as the collection Markdown documents. Repeat for the other vocab.
13. The Markdown documents containing the human-readable lists will automatically go into their correct places in the `docs` directory of the AC repo. The JSON-LD documents with the `.json` and `.jsonld` file extensions need to be moved to the `cvJson` directory of the `gh-pages` branch of the `rs.tdwg.org` repo. This allows them to be served with the correct Content-Type header (as with all of the other controlled vocabulary files in that repo).

---
Revised 2023-05-08
