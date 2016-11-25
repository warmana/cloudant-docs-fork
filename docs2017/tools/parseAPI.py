from json import load
import csv

linkDict = {}
outputLine = ""
used = False
wherePresent = ""

def testDatabase(dbname, key, apiname):
    global outputLine
    global used
    global wherePresent
    shortName = dbname.replace(' ', '')
    if (linkDict.has_key(key + apiname)):
        if (dbname in wherePresent):
            used = True
            docLink = linkDict[key + apiname]
            if (docLink != ""):
                outputLine += "[![small" + shortName + "](images/small" + shortName + ".png)](" + docLink + "){:new_window} | "
            else:
                outputLine += "![small" + shortName + "](images/small" + shortName + ".png) | "
    else:
        outputLine += "![small" + shortName + "](images/small" + shortName + ".png) | "

with open('APIlinks.csv', 'rb') as apiLinks:
    thedata = csv.DictReader(apiLinks, delimiter=',')
    for row in thedata:
        # print(row['Endpoint']+"\t"+row['Method']+"\t"+row['Cloudant']+"\t"+row['Couch20']+"\t"+row['Couch16'])
        linkDict[row['Endpoint']+row['Method']+'Cloudant'] = row['Cloudant']
        linkDict[row['Endpoint']+row['Method']+'Couch20']  = row['Couch20']
        linkDict[row['Endpoint']+row['Method']+'Couch16']  = row['Couch16']

with open('./couchdb-cloudant-api/cloudant-couchdb-api-ref.json') as json_data_file:
    data = load(json_data_file)

print("Endpoint | Method | Cloudant | CouchDB 2.0 | CouchDB 1.6 | Summary | Notes")
print("---------|--------|----------|-------------|-------------|---------|------")

for row in data:
    linkDictKey = row["endpoint"] + row["method"]
    outputLine = row["endpoint"] + " | "
    outputLine += row["method"] + " | "
    wherePresent = row['database']
    used = False
    testDatabase("Cloudant", linkDictKey, "Cloudant")
    testDatabase("CouchDB 2.0", linkDictKey, "Couch20")
    testDatabase("CouchDB 1.6", linkDictKey, "Couch16")
    outputLine += row['summary'] + " | "
    if (row['comment'] != ""):
        outputLine += row['comment']
    outputLine = outputLine.replace(u"\u2019", "\'").replace("_", "\\_").replace("\n", " ")
    outputLine = outputLine.replace("new\_window", "new_window")
    print outputLine
