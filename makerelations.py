from lxml import etree as ET
import requests
import getpass


doctypes = {'1': 'ObjectExit', '2': 'Media', '3': 'Person', '4': 'Exhibition',
            '5': 'Conservation', '6': 'Group', '7': 'CollectionObject', '8':
            'Intake', '9': 'Intake', '10': 'Movement', '11': 'conceptitem',
            '12': 'taxonitem', '13': 'Loanin', '14': 'Valuationcontrol',
            '15': 'Acquisition', '16': 'Loanout', '17': 'Locationitem',
            '18': 'placeitem', '19': 'Restrictedmedia', '20': 'Conditioncheck'}
singlerecord = input("csid of the individual record to berelated to: ")
for elem in doctypes:
    print(elem, doctypes[elem])
singledoctype = doctypes[input("what type of document is this - choose a number: ")]
listofrecords = input("path to list of records to be related: ")
listdoctype = doctypes[input("what type of documents are these - choose a number: ")]
user = input("Enter your cspace user id: ")
pword = getpass.getpass("Enter your cspace password: ")
headers = {'Content-Type': 'application/xml'}
log = open('log.txt', 'w')


def upload(xmldata):
    r = requests.post('http://10.99.1.11:8180/cspace-services/relations',
                      data=xmldata, headers=headers, auth=(user, pword))
    print("\n" + str(r.status_code) + " ----> " + csid + " - " +
          singlerecord + "\n")
    log.write(str(r.status_code) + " ----> " + csid + " - " +
              singlerecord + "\n")


def writexml_1(subjectcsid):
    ns2_NAMESPACE = 'http://collectionspace.org/services/relation'
    ns2 = "{%s}" % ns2_NAMESPACE
    NSMAP = {'ns2': ns2_NAMESPACE}
    top = ET.Element('document', name="relations")
    second = ET.SubElement(top, ns2 + 'relations_common', nsmap=NSMAP)
    sbjdoctype = ET.SubElement(second, 'subjectDocumentType')
    objdoctype = ET.SubElement(second, 'objectDocumentType')
    sbjcsid = ET.SubElement(second, 'subjectCsid')
    objcsid = ET.SubElement(second, 'objectCsid')
    reltype = ET.SubElement(second, 'relationshipType')
    sbjdoctype.text = listdoctype
    objdoctype.text = singledoctype
    sbjcsid.text = subjectcsid
    objcsid.text = singlerecord
    reltype.text = 'affects'
    xml_1 = ET.tostring(top, pretty_print=True, xml_declaration=True,
                        encoding='UTF-8', standalone='yes')
    upload(xml_1)


def writexml_2(objectcsid):
    ns2_NAMESPACE = 'http://collectionspace.org/services/relation'
    ns2 = "{%s}" % ns2_NAMESPACE
    NSMAP = {'ns2': ns2_NAMESPACE}
    top = ET.Element('document', name="relations")
    second = ET.SubElement(top, ns2 + 'relations_common', nsmap=NSMAP)
    sbjdoctype = ET.SubElement(second, 'subjectDocumentType')
    objdoctype = ET.SubElement(second, 'objectDocumentType')
    sbjcsid = ET.SubElement(second, 'subjectCsid')
    objcsid = ET.SubElement(second, 'objectCsid')
    reltype = ET.SubElement(second, 'relationshipType')
    sbjdoctype.text = singledoctype
    objdoctype.text = listdoctype
    sbjcsid.text = singlerecord
    objcsid.text = objectcsid
    reltype.text = 'affects'
    xml_2 = ET.tostring(top, pretty_print=True, xml_declaration=True,
                        encoding='UTF-8', standalone='yes')
    upload(xml_2)


with open(listofrecords, 'r') as f:
    csids = [line.rstrip() for line in f]
    for csid in csids:
        writexml_1(csid)
        writexml_2(csid)
    f.close()
