from json import load
import csv

linkArray = []
outputLine = ""
wherePresent = ""

def outputDatabase(dbName, docLink, default):
    global outputLine
    global wherePresent
    if (dbName in wherePresent):
        shortName = dbName.replace(' ', '')
        if (docLink != ""):
            outputLine += "[![small" + shortName + "](images/small" + shortName + ".png)](" + docLink + "){:new_window} | "
        else:
            outputLine += "[![small" + shortName + "](images/small" + shortName + ".png)](" + default + "){:new_window} | "
    else:
        outputLine += " | "

with open('cloudant-couchdb-api-ref.json') as json_data_file:
    data = load(json_data_file)

print("Endpoint | Method | Cloudant | CouchDB 2.0 | CouchDB 1.6 | Summary | Notes")
print("---------|--------|----------|-------------|-------------|---------|------")

for row in data:
    # linkDictKey = row["endpoint"] + row["method"]
    linkArray = row["links"]
    linkArray.append("")
    linkArray.append("")
    linkArray.append("")
    outputLine = row["endpoint"] + " | "
    outputLine += row["method"] + " | "
    wherePresent = row['database']
    outputDatabase("Cloudant", linkArray[0], "http://docs.cloudant.com/")
    outputDatabase("CouchDB 2.0", linkArray[2], "http://docs.couchdb.org/en/2.0.0/")
    outputDatabase("CouchDB 1.6", linkArray[1], "http://docs.couchdb.org/en/1.6.1/")
    # testDatabase("Cloudant", linkDictKey, "Cloudant")
    # testDatabase("CouchDB 2.0", linkDictKey, "Couch20")
    # testDatabase("CouchDB 1.6", linkDictKey, "Couch16")
    outputLine += row['summary'] + " | "
    if (row['comment'] != ""):
        outputLine += row['comment']
    outputLine = outputLine.replace(u"\u2019", "\'").replace("_", "\\_").replace("\n", " ")
    outputLine = outputLine.replace("new\_window", "new_window")
    print outputLine
