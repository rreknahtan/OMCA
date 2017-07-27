import requests
import getpass
import os
from lxml import etree as ET

doctypes = ['ObjectExit', 'Media', 'Person', 'Exhibition', 'Conservation', 'Group', 'CollectionObject', 'Intake', 'Movement', 'conceptitem', 'taxonitem', 'Loanin', 'Valuationcontrol', 'Acquisition', 'Loanout', 'Locationitem', 'placeitem', 'Restrictedmedia', 'Conditioncheck']

singlerecord = raw_input("csid of the individual record to berelated to: ")
for elem in doctypes: 
	print elem
singledoctype = raw_input("what type of document is this: ")
listoffiles = raw_input("path to list of files to be related: ")
listdoctype = raw_input("what type of documents are these: ")

def writexml_1(subjectcsid):
	ns2_NAMESPACE = 'http://collectionspace.org/services/relation'
	ns2 = "{%s}" % ns2_NAMESPACE

	NSMAP = {'ns2':ns2_NAMESPACE}

	top = ET.Element('document', name="relations")
	second = ET.SubElement(top, ns2 + 'relations_common', nsmap=NSMAP)
	sbjdoctype = ET.SubElement (second, 'subjectDocumentType')
	objdoctype = ET.SubElement (second, 'objectDocumentType')
	sbjcsid = ET.SubElement (second, 'subjectCsid')
	objcsid = ET.SubElement (second, 'objectCsid')
	reltype = ET.SubElement (second, 'relationshipType')

	sbjdoctype.text = listdoctype
	objdoctype.text = singledoctype
	sbjcsid.text = subjectcsid
	objcsid.text = singlerecord
	reltype.text = 'affects'

	#print ET.tostring(top, pretty_print=True, xml_declaration=True, encoding='UTF-8', standalone='yes')
	tree = ET.ElementTree(top)
	tree.write(('output/' + subjectcsid + '_subj.xml'), pretty_print=True, xml_declaration=True, encoding='UTF-8', standalone='yes')
	
def writexml_2(objectcsid):
	ns2_NAMESPACE = 'http://collectionspace.org/services/relation'
	ns2 = "{%s}" % ns2_NAMESPACE

	NSMAP = {'ns2':ns2_NAMESPACE}

	top = ET.Element('document', name="relations")
	second = ET.SubElement(top, ns2 + 'relations_common', nsmap=NSMAP)
	sbjdoctype = ET.SubElement (second, 'subjectDocumentType')
	objdoctype = ET.SubElement (second, 'objectDocumentType')
	sbjcsid = ET.SubElement (second, 'subjectCsid')
	objcsid = ET.SubElement (second, 'objectCsid')
	reltype = ET.SubElement (second, 'relationshipType')

	sbjdoctype.text = singledoctype
	objdoctype.text = listdoctype
	sbjcsid.text = singlerecord
	objcsid.text = objectcsid
	reltype.text = 'affects'

	#print ET.tostring(top, pretty_print=True, xml_declaration=True, encoding='UTF-8', standalone='yes')
	tree = ET.ElementTree(top)
	tree.write(('output/' + objectcsid + '_obj.xml'), pretty_print=True, xml_declaration=True, encoding='UTF-8', standalone='yes')
	
with open(listoffiles, 'r') as f:
	csids = [line.rstrip() for line in f]
	for csid in csids: 
		writexml_1(csid)
		writexml_2(csid)
	f.close()

user = raw_input("Enter your cspace user id: ")
pword = getpass.getpass("Enter your cspace password: ")
headers = {'Content-Type': 'application/xml'}
log = open ('log.txt', 'w')

for filename in os.listdir('output/'):
	if not filename.startswith('.'):
		r = requests.post('http://10.99.1.13:8180/cspace-services/relations', data = open('output/' + filename, 'rb'), headers = headers, auth = (user, pword))
		print "\n\n" + str(r.status_code) + " ----> " + filename + "\n\n" 
		log.write(str(r.status_code) + " ----> " + filename + "\n")

log.close
	
	
	
	
