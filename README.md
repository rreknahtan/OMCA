# OMCA
Some simple tools developed for managing collectionspace at OMCA.


**makerelations** - Script to relate records via api. Supply the csid of the single record, a txt file with a list of csids to relate (must be same doctype), and the doctypes of both.

**fixblob** - Script to fix blobs with missing derivatives. Supply csv with: image filenmae, media handling csid, damaged blob csid, uri / url to source image for upload

**merge_terms** - A tool for mergeing duplicate authority terms. See [merge_terms.md](./merge_terms_tool/merge_terms.md) for documentation.
