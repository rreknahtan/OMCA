import requests
import sys
import re


user = 'nkerr@museumca.org'
pword = 'basqbasq'
headers = {'Content-Type': 'application/xml'}
baseurl = 'http://10.99.1.11:8180/cspace-services'
urlparams = '/refObjs?pgSz=1000'
newcsid = sys.argv[2]
oldcsid = sys.argv[4]
to_update = []
vocabs = ['concept', 'org', 'location', 'place', 'person']


def getrefname(csid, vocab):
    info = requests.get(baseurl + '/' + vocab + '/*/items/' + csid,
                        headers=headers, auth=(user, pword))
    refname = re.search('<refName>(.*?)</refName>', info.text)
    return(refname.group(1))


def getobjs(oldcsid):
    usedby = requests.get(baseurl + '/' + oldvocab + '/*/items/' + oldcsid +
                          urlparams, headers=headers, auth=(user, pword))
    for match in re.findall('<uri>(.*?)</uri>', usedby.text):
        to_update.append(match)
        to_update.sort()
    print(to_update)


def updateobjs(uri, oldrefname, newrefname):
    record = requests.get(baseurl + uri, headers=headers, auth=(user, pword))
    document = re.search('<document name=(.*?)>', record.text)
    updated = re.search('</ns2:collectionspace_core>(.*?)<ns2:account_',
                        record.text.replace(oldrefname, newrefname), re.DOTALL)
    for_upload = ('<?xml version="1.0" encoding="UTF-8"?>' + document.group(0)
                  + updated.group(1) + '</document>')
    update = requests.put(baseurl + uri, headers=headers, data=for_upload,
                          auth=(user, pword))
    print(uri + ' ' + str(update.status_code))


def mergeterms():
    oldrefname = getrefname(oldcsid, oldvocab)
    newrefname = getrefname(newcsid, newvocab)
    getobjs(oldcsid)
    for uri in to_update:
        updateobjs(uri, oldrefname, newrefname)


if sys.argv[1] not in vocabs or sys.argv[3] not in vocabs:
        print('Invalid authority use one of the following:')
        for v in vocabs:
            print(v)
else:
    newvocab = sys.argv[1] + 'authorities'
    oldvocab = sys.argv[3] + 'authorities'
    mergeterms()
