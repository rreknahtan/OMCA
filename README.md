# OMCA
Odds and ends for the OMCA CollectionSpace project.

**lange_batch_prod** - This is a script for creating new cataloging records in the A67.137 accesion in a sequentioal batch with certain fields populated. Written really badle just escaping the xml, will re-write with lxml in the future.

**makerelations** - Script to relate records via api. Supply the csid of the single record, a txt file with a list of csids to relate (must be same doctype) and the doctypes of the single record and records in the list.
