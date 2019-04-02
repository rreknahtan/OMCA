# OMCA ‘Merge Terms’ Tool for Cleanup of Duplicate Authority Terms

The merge terms tool is a python script that utilizes CollectionSpace’s service layer api to merge duplicate authority records into a single authority record and then delete the unwanted duplicate. 

The tool works by querying the api for all of the records in which the term to be deleted is used, then it updates all of those records replacing the term to be deleted with the term to be kept. Finally, if all instances of the term to be deleted are successfully removed the authority record for the term is deleted. If for any reason an instances of the term to be removed remains the tool will list the record(s) where the term remains and will not delete the authority record for the term.

### Usage:

Before using add your cspace credentials in the user and pword variables, or change the code to accept them as arguments, etc. You may also need to edit the base_url variable to reflect the address for your instance if not running from the server.

The script is run via the command line and requires 3 arguments in the following order: the authority type, csid of the term being merged into (kept), and the csid of the unwanted duplicate to be deleted. 

Valid authority types are:

* concept
* org  
* location  
* place 
* person 

Here is an example of how the command should look:

``python merge_terms org ccc778d8-b8cf-4865-8d1b-ddd66d1c6753 d1f52fed-a4e5-421b-a4ba-4c09653ed39f``

After executing the command it will provide some feedback about how many records it will attempt to update, how many records were successfully updated, and if the duplicate term was deleted or not. Here is an example:

``Found 3 records to be updated.
All records were successfully updated.
d1f52fed-a4e5-421b-a4ba-4c09653ed39f successfully deleted.``

If for some reason there are records that cannot be updated they will be listed in the output and the duplicate term will not be deleted.

### Limitations:

* Currently the tool can only handle 1000 references at a time. This means if the term to be deleted is used more than 1000 times (very unlikely for OMCA anyhow) the tool would need to be run with the same input until all records were merged.
* Cross-authority merges - currently the tool only merges terms within the same authority, v.2 should add support for cross authority merges.
* Does not currently work with taxon authority, another feature to be included in v.2


### Requirements:

* Python3 with the [requests](http://docs.python-requests.org/en/master/) library installed
* Valid cspace credentials for an account with delete permissions
