import csv
import sys
import requests

textfile = sys.argv[1]
user = sys.argv[2]
pword = sys.argv[3]
heads = {'Content-Type': 'application/xml'}

half1 = ['<?xml version="1.0" encoding="utf-8"?>\n', '<document name="media">\n', '\t<ns2:media_common xmlns:ns2="http://collectionspace.org/services/media" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n', '\t<blobCsid>']
half2 = ['</blobCsid>\n', '\t</ns2:media_common>\n', '</document>\t']

bloblog = open('bloblog.txt','w')

def uploadblob(path, mediacsid, oldblob):
	
	nb = requests.post('http://10.99.1.13:8180/cspace-services/blobs?blobUri=' + path, headers = heads, auth = (user, pword))
	 
	url = nb.headers['Location']
	nbcsid = url.split('/', 5)[-1]
	
	print str(nb.status_code) + " " + nbcsid
	
	mhdata = half1[0] + half1[1]+ half1[2] + half1[3] + nbcsid + half2[0] + half2[1] + half2[2]
	
	umh= requests.put('http://10.99.1.13:8180/cspace-services/media/' + mediacsid, data = mhdata, headers = heads, auth = (user, pword))
	
	bloblog.write(str(nb.status_code) + "|" + path + "|" + nbcsid + "\n") 
	bloblog.write(str(umh.status_code) + "|" + mediacsid + "\n\n")
	
	print str(umh.status_code) + " " + mediacsid

with open(textfile, 'rb') as f:
	reader = csv.reader(f)
	onhdd2 = list(reader)
	for set in onhdd2: 
		filename = set[0]
		mediacsid = set[1]
		oldb = set[2]
		filepath = ('file://' + set[3])
	
		uploadblob(filepath, mediacsid, oldb)

bloblog.close		

