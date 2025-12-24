# Proposed 3D Terms - prep for rs.tdwg.org process

This is where the 3D Task group is staging 3D terms CSVs & related config docs to add proposed terms to rs.tdwg.org.

From [rs.tdwg.org/process/ac-revisions/ac-3d-terms-2025-12-24](https://github.com/magpiedin/rs.tdwg.org/tree/add-ac-3d/process/ac-revisions/ac-3d-terms-2025-12-24):

### For new AC 3D terms
- `config.yaml` = the config properties to add proposed AC 3D terms to existing main AC vocab using `process.py`.  It references these 3 CSVs:
- `ac_3d_terms.csv` = new AC 3D terms in the `ac` namespace
- `bf_3d_terms.csv` = new AC 3D terms borrowed from the BIBFRAME vocab, in the `bf` namespace.
- `exif_3d_terms.csv` = new AC 3D terms borrowed from EXIF vocab, in the `exif` namespace.

### For new 3D Resource Type controlled vocab
- `config_ac3dtype.yaml` = the config properties to add a new proposed AC 3D Resource Type hierarchical controlled vocab to the rs.tdwg.org repo. It references this CSV:
- `ac3dResourceType_cv.csv` = the proposed 3D Resource Type vocab values, for use with the new ac:3DResourceType term.
