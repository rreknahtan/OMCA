# OMCA
Odds and ends for the OMCA CollectionSpace project.

**lange_batch_prod** - This is a script for creating new cataloging records in the A67.137 accesion in a sequentioal batch with certain fields populated. Written very poorly, just escaping the xml, will re-write with lxml in the future.

**makerelations** - Script to relate records via api. Supply the csid of the single record, a txt file with a list of csids to relate (must be same doctype), and the doctypes of both.

**newfixblob** - Script to fix blobs with missing derivatives. Supply csv with: image filenmae, media handling csid, damaged blob csid, uri / url to source image for upload
