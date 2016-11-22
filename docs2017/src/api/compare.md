---

copyright:
  years: 2015, 2016
lastupdated: "2016-11-22"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}

# Comparison of Cloudant and CouchDB API endpoints

This section provides a simple list of the Cloudant and CouchDB API endpoints,
showing you which endpoints are present in each service.
{:shortdesc}

Some CouchDB endpoints do not have Cloudant equivalents,
because it would not be meaningful.

Endpoint |Method |Cloudant |CouchDB |Summary |Notes
---------|-------|---------|--------|--------|-----
/ | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Meta information about the cluster. | 
/\_active\_tasks | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | List running tasks. | 
/\_all\_dbs | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | List all the databases in the instance. | 
/\_api/v2/api\_keys | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | | Generate an API key. | 
/\_api/v2/db/{db}/\_security | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | | Who has permissions to read, write, and manage the database. | 
/\_api/v2/db/{db}/\_security | PUT | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | | Modify who has permissions to read, write, and manage a database. Assign an API key. | 
/\_api/v2/monitoring/{endpoint} | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | | Monitor a specific cluster aspect. | 
/\_api/v2/user/config/cors | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | | Current CORS configuration. | 
/\_api/v2/user/config/cors | PUT | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | | Changes the CORS configuration. | 
/\_api/v2/user/virtual\_hosts | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | | List all virtual hosts. | 
/\_api/v2/user/virtual\_hosts | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | | Create a virtual host. | 
/\_api/v2/user/virtual\_hosts | DELETE | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | | Delete a virtual host. | 
/\_config | GET | | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Get the server configuration. | 
/\_config/{section} | GET | | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Get the configuration for the specified section. | 
/\_config/{section}/{key} | GET | | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Get the configuration value of a specific key within a configuration section. | 
/\_config/{section}/{key} | PUT | | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Update a configuration value. The new value should be supplied in the request body in the corresponding JSON format. | 
/\_config/{section}/{key} | DELETE | | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Delete a configuration value. | 
/\_db\_updates | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | List all database events in the instance. | In Cloudant the endpoint is only available to dedicated customers. Its documentation references additional query params (limit, since, descending) and an additional feed type value (normal) For CouchDB, its documentation references an additional feed type value (eventsource)
/\_log | GET | | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Get the log. Equivalent to accessing the local log file of the corresponding instance. | 
/\_membership | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | List the names of nodes in the cluster. Active clusters are indicated in the cluster\_nodes field, while all\_nodes has all nodes. | 
/\_replicate | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Request, configure, or stop, a replication operation. | Cloudant documentation references additional request body fields (selector, since\_seq).
/\_replicator | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Trigger a replication. | Cloudant documentation references additional request body fields (selector, since\_seq).
/\_replicator | PUT | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Trigger a replication. | Cloudant documentation references additional request body fields (selector, since\_seq).
/\_replicator | DELETE | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Cancel an ongoing replication | Cloudant documentation references additional request body fields (selector, since\_seq).
/\_restart | POST | | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Restart the instance. You must be authenticated as a user with administration privileges. | 
/\_search\_analyze | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | | Test the results of analyzer tokenization by posting sample data. | 
/\_session | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Returns information about the authenticated user. | CouchDB documentation references an additional query param (basic).
/\_session | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Initiate a new session for the specified user credentials. Cookie based user login. | CouchDB documentation references an additional query param (next).
/\_session | DELETE | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Closes user’s session. Logout cookie based user. | 
/\_stats | GET | | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Return the statistics for the running server. | 
/\_utils | GET | | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Access the built-in Fauxton administration interface. | 
/\_uuids | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Request one or more Universally Unique Identifiers (UUIDs). | 
/favicon.ico | GET | | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Get the binary content for the favicon.ico site icon. | 
/{db} | HEAD | | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Return the HTTP Headers containing a minimal amount of information about the specified database. | 
/{db} | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Get information about the specified database. | 
/{db} | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Create a new document in the specified database, using the supplied JSON document structure. | 
/{db} | PUT | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Create a new database. | Database names must start with a lowercase letter and contain only the following characters: Lowercase characters (a-z), Digits (0-9), Any of the characters \_, $, (, ), +, -, and /
/{db} | DELETE | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Delete the specified database, and all the documents and attachments contained within it. | 
/{db}/\_all\_docs | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | List all the documents in a database. | CouchDB documentation references additional query params (end\_key, endkey\_docid, end\_key\_doc\_id, stale, start\_key, startkey\_docid, start\_key\_doc\_id, update\_seq).
/{db}/\_all\_docs | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | List all the documents in a database. | CouchDB documentation references additional query params (end\_key, endkey\_docid, end\_key\_doc\_id, stale, start\_key, startkey\_docid, start\_key\_doc\_id, update\_seq).
/{db}/\_bulk\_docs | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Create and update multiple documents at the same time within a single request. | CouchDB documentation references an additional request object field (new\_edits).
/{db}/\_bulk\_get | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Get multiple documents in a single request. | 
/{db}/\_changes | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | List of changes made to documents in the database, including insertions, updates, and deletions. | CouchDB includes query params (attachments, att\_encoding\_info, last-event-id, view).
/{db}/\_changes | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | List of changes made to documents in the database, including insertions, updates, and deletions. | 
/{db}/\_compact | POST | | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Request compaction of the specified database. | 
/{db}/\_compact/{ddoc} | POST | | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Compact the view indexes associated with the specified design document. | 
/{db}/\_design/{ddoc} | HEAD | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Return the HTTP Headers containing a minimal amount of information about the specified design document. | 
/{db}/\_design/{ddoc} | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Get the contents of the design document specified with the name of the design document and from the specified database from the URL. | 
/{db}/\_design/{ddoc} | PUT | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Create a new named design document or create a new revision of the existing design document. | Cloudant documentation references an additional request body field (indexes) CouchDB documentation references additional request body fields (language, options).
/{db}/\_design/{ddoc} | DELETE | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Delete the specified document from the database. | 
/{db}/\_design/{ddoc} | COPY | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Copy an existing design document to a new or existing one. | 
/{db}/\_design/{ddoc}/\_geo\_info/{index} | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | | Obtain information about a geospatial index. | 
/{db}/\_design/{ddoc}/\_geo/{index} | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | | Query a geo index. | 
/{db}/\_design/{ddoc}/\_info | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Obtain information about the specified design document, including the index, index size, and current status of the design document. | 
/{db}/\_design/{ddoc}/\_list/{func}/{other-ddoc}/{view} | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Apply the list function for the view function from the other design document. | 
/{db}/\_design/{ddoc}/\_list/{func}/{other-ddoc}/{view} | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Apply the list function for the view function from the other design document. | 
/{db}/\_design/{ddoc}/\_list/{func}/{view} | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Apply the list function for the view function from the same design document. | The result of a list function is not stored. This means that the function is executed every time a request is made.
/{db}/\_design/{ddoc}/\_list/{func}/{view} | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Apply the list function for the view function from the same design document. | 
/{db}/\_design/{ddoc}/\_rewrite/{path} | ANY | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Rewrite the specified path by rules defined in the specified design document. | 
/{db}/\_design/{ddoc}/\_search\_info/{index} | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | | Obtain information about a search specified within a given design document. | 
/{db}/\_design/{ddoc}/\_search/{index} | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | | Query an index. | 
/{db}/\_design/{ddoc}/\_search/{index} | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | | Query an index. | 
/{db}/\_design/{ddoc}/\_show/{func} | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Apply the show function for null document. | 
/{db}/\_design/{ddoc}/\_show/{func} | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Apply the show function for null document. | 
/{db}/\_design/{ddoc}/\_show/{func}/{docid} | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Apply the show function for the specified document. | The result of a show function is not stored. This means that the function is executed every time a request is made.
/{db}/\_design/{ddoc}/\_show/{func}/{docid} | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Apply the show function for the specified document. | 
/{db}/\_design/{ddoc}/\_update/{func} | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Execute the update function on server side for null document. | 
/{db}/\_design/{ddoc}/\_update/{func}/{docid} | PUT | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Execute the update function on server side for the specified document. | 
/{db}/\_design/{ddoc}/\_view/{view} | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Execute the view function from the specified design document. | CouchDB documentation references additional query params (conflicts, end\_key, end\_key\_doc\_id, attachments, att\_encoding\_info, sorted, start\_key, start\_key\_doc\_id, update\_seq).
/{db}/\_design/{ddoc}/\_view/{view} | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Execute the view function from the specified design document. | CouchDB documentation references additional query params (conflicts, end\_key, end\_key\_doc\_id, attachments, att\_encoding\_info, sorted, start\_key, start\_key\_doc\_id, update\_seq).
/{db}/\_design/{ddoc}/{attname} | HEAD | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Return the HTTP headers containing a minimal amount of information about the specified attachment. | 
/{db}/\_design/{ddoc}/{attname} | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Return the file attachment associated with the design document. | 
/{db}/\_design/{ddoc}/{attname} | PUT | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Upload the supplied content as an attachment to the specified design document. | 
/{db}/\_design/{ddoc}/{attname} | DELETE | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Delete the attachment of the specified design document. | 
/{db}/\_ensure\_full\_commit | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Commit any recent changes to the specified database to disk. | 
/{db}/\_explain | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Identify which index is being used by a particular query. | 
/{db}/\_find | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Find documents using a declarative JSON querying syntax. | Cloudant documentation references additional request body fields (r, bookmark)
/{db}/\_index | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | List indexes. | 
/{db}/\_index | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Create a new index. | 
/{db}/\_index/\_design/{ddoc}/{type}/{name} | DELETE | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Delete an index. | 
/{db}/\_local/{docid} | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Get the specified local document. | 
/{db}/\_local/{docid} | PUT | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Store the specified local document. | Local documents are not replicated to other databases.
/{db}/\_local/{docid} | DELETE | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Delete the specified local document. | 
/{db}/\_local/{docid} | COPY | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Copy the specified local document. | 
/{db}/\_missing\_revs | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | | Return the document revisions from the given list that do not exist in the database. | 
/{db}/\_missing\_revs | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Return the document revisions from the given list that do not exist in the database. | 
/{db}/\_purge | POST | | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Remove the references to deleted documents from the database. | 
/{db}/\_revs\_diff | POST | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Given a set of document/revision IDs, return the subset of those that do not correspond to revisions stored in the database. | 
/{db}/\_revs\_limit | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Get the number of document revisions tracked. | 
/{db}/\_revs\_limit | PUT | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Set the maximum number of document revisions tracked. | 
/{db}/\_security | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Return the current security object from the specified database. | 
/{db}/\_security | PUT | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Set the security object for the given database. | 
/{db}/\_shards | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | | Return information about the shards in the cluster | 
/{db}/\_view\_cleanup | POST | | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Remove view index files that are no longer required by as a result of changed views within design documents. | 
/{db}/{docid} | HEAD | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Return the HTTP Headers containing a minimal amount of information about the specified document. | 
/{db}/{docid} | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Return the document specified by the docid from the specified db. | 
/{db}/{docid} | PUT | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Create a new named document or create a new revision of the existing document. | 
/{db}/{docid} | DELETE | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Mark the specified document as deleted. | 
/{db}/{docid} | COPY | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Copy an existing document to a new or existing document. | 
/{db}/{docid}/{attname} | HEAD | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Return the HTTP headers containing a minimal amount of information about the specified attachment. | 
/{db}/{docid}/{attname} | GET | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Return the file attachment associated with the document. | 
/{db}/{docid}/{attname} | PUT | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Upload the supplied content as an attachment to the specified document. | 
/{db}/{docid}/{attname} | DELETE | ![smallCloudantLogo](/docs/images/smallCloudantLogo.png) | ![smallCouchLogo](/docs/images/smallCouchLogo.png) | Delete the attachment associated with the specified doc. | 
