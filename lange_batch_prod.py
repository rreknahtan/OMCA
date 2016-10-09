import requests
import getpass

firstseq = input("Starting object sequence number: ")
lastseq = input("Ending object sequence number: ")
user = raw_input("Enter your cspace user id: ")
pword = getpass.getpass("Enter your cspace password: ")
numbers = list(range(firstseq, (lastseq + 1)))
filename = "%s_%s.xml" % (firstseq, lastseq)
importfile = open(filename, 'w', 0)
headers = {'Content-Type': 'application/xml'}

importfile.write("""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<imports>
""")

for i in numbers:
	
	id = ("A67.137." + str(i))
	sortable = ("A0000000067.0000000137.00000" + str(i)) 
	
	importfile.write("<import service=\"CollectionObjects\" type=\"CollectionObject\" createdBy=\"" + user +  "\">\n" 
	"""<schema xmlns:collectionobject_common=\"http://collectionspace.org/services/collectionobject\" name=\"collectionobjects_common\">
                        <collection>urn:cspace:museumca.org:vocabularies:name(collection):item:name(Dorothea_Lange)\'Dorothea Lange\'</collection>
                        <objectProductionPersonGroupList>
                            <objectProductionPersonGroup>
                                <objectProductionPerson>urn:cspace:museumca.org:personauthorities:name(person):item:name(lexpers100478)\'Dorothea Lange\'</objectProductionPerson>
                            </objectProductionPersonGroup>
                        </objectProductionPersonGroupList>
                        <objectNameList>
                            <objectNameGroup>
                                 <objectName>urn:cspace:museumca.org:conceptauthorities:name(concept):item:name(cn97581)\'photograph\'</objectName>
                            </objectNameGroup>
                        </objectNameList>
                        <materialGroupList>
                            <materialGroup>
                                    <material>urn:cspace:museumca.org:conceptauthorities:name(concept):item:name(cn113512)\'gelatin silver print\'</material>
                            </materialGroup>
                        </materialGroupList>
                        <objectNumber>""" + str(id) + """</objectNumber>                    	
                        <recordStatus>urn:cspace:museumca.org:vocabularies:name(recordStatus):item:name(pending_curatorial_review)\'Pending curatorial review\'</recordStatus>        
        </schema>
        <schema xmlns:collectionobjects_omca=\"http://collectionspace.org/services/collectionobject/local/omca\" name=\"collectionobjects_omca\">
                        <art>true</art>
                        <ipAudit>urn:cspace:museumca.org:vocabularies:name(ipaudit):item:name(copyright_omca)\'Copyright OMCA\'</ipAudit>
                        <sortableObjectNumber>""" + str(sortable) + """</sortableObjectNumber>
                        <argusDescription>gelatin silver print</argusDescription>
        </schema>
    </import> \n""")
	
#importfile.flush	
importfile.close
	

r = requests.post('http://10.99.1.13:8180/cspace-services/imports', data = open(filename, 'rb'), headers = headers, auth = (user, pword))

print "\n\n" + str(r.status_code) + "\n\n"
print r.text

log = open ('log_' + filename, 'w')
log.write(r.text)

	
  