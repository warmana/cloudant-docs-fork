---

copyright:
  years: 2015, 2016
lastupdated: "2016-12-20"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}

# Comparison of Cloudant and CouchDB API endpoints

This section provides a simple list of the Cloudant (![Cloudant Logo](../images/smallCloudant.png)),
CouchDB 2.0 (![CouchDB 2.0 Logo](../images/smallCouchDB2.png)),
and CouchDB 1.6 (![CouchDB 1.6 Logo](../images/smallCouchDB1.png)) API endpoints and the methods for accessing them,
showing you which endpoints are present in each service.
{:shortdesc}

Some CouchDB endpoints do not have Cloudant equivalents,
because it would not be meaningful.
Similarly,
some Cloudant endpoints do not have CouchDB equivalents.

For more information about a given endpoint on a service,
click the corresponding icon.

<table border='1'>

<tr>
<td rowspan='2'><code>/</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/advanced.html#get-/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/server/common.html#get--' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/server/common.html#get--' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Meta information about the cluster.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_active\_tasks</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/active_tasks.html#active-tasks' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/server/common.html#get--_active_tasks' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/server/common.html#get--_active_tasks' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>List running tasks.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_all\_dbs</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/database.html#get-databases' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/server/common.html#get--_all_dbs' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/server/common.html#get--_all_dbs' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>List all the databases in the instance.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_api/v2/api\_keys</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/authorization.html#creating-api-keys' target='_blank'><img src='../images/smallCloudant.png'/></a>
</td>
</tr>
<tr>
<td>Generate an API key.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_api/v2/db/{db}/\_security</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/authorization.html#viewing-permissions' target='_blank'><img src='../images/smallCloudant.png'/></a>
</td>
</tr>
<tr>
<td>Who has permissions to read, write, and manage the database.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_api/v2/db/{db}/\_security</code><p><code>PUT</code></p></td><td>
<a href='https://docs.cloudant.com/authorization.html#modifying-permissions' target='_blank'><img src='../images/smallCloudant.png'/></a>
</td>
</tr>
<tr>
<td>Modify who has permissions to read, write, and manage a database. Assign an API key.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_api/v2/monitoring/{endpoint}</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/monitoring.html#monitoring-metrics-overview' target='_blank'><img src='../images/smallCloudant.png'/></a>
</td>
</tr>
<tr>
<td>Monitor a specific cluster aspect.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_api/v2/user/config/cors</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/cors.html#reading-the-cors-configuration' target='_blank'><img src='../images/smallCloudant.png'/></a>
</td>
</tr>
<tr>
<td>Current CORS configuration.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_api/v2/user/config/cors</code><p><code>PUT</code></p></td><td>
<a href='https://docs.cloudant.com/cors.html#setting-the-cors-configuration' target='_blank'><img src='../images/smallCloudant.png'/></a>
</td>
</tr>
<tr>
<td>Changes the CORS configuration.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_api/v2/user/virtual\_hosts</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/vhosts.html#listing-virtual-hosts' target='_blank'><img src='../images/smallCloudant.png'/></a>
</td>
</tr>
<tr>
<td>List all virtual hosts.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_api/v2/user/virtual\_hosts</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/vhosts.html#creating-a-virtual-host' target='_blank'><img src='../images/smallCloudant.png'/></a>
</td>
</tr>
<tr>
<td>Create a virtual host.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_api/v2/user/virtual\_hosts</code><p><code>DELETE</code></p></td><td>
<a href='https://docs.cloudant.com/vhosts.html#deleting-a-virtual-host' target='_blank'><img src='../images/smallCloudant.png'/></a>
</td>
</tr>
<tr>
<td>Delete a virtual host.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_config</code><p><code>GET</code></p></td><td>
<a href='http://docs.couchdb.org/en/1.6.0/api/server/configuration.html#config' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Get the server configuration.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_config/{section}</code><p><code>GET</code></p></td><td>
<a href='http://docs.couchdb.org/en/1.6.0/api/server/configuration.html#config-section' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Get the configuration for the specified section.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_config/{section}/{key}</code><p><code>GET</code></p></td><td>
<a href='http://docs.couchdb.org/en/1.6.0/api/server/configuration.html#get--_config-section-key' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Get the configuration value of a specific key within a configuration section.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_config/{section}/{key}</code><p><code>PUT</code></p></td><td>
<a href='http://docs.couchdb.org/en/1.6.0/api/server/configuration.html#put--_config-section-key' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Update a configuration value. The new value should be supplied in the request body in the corresponding JSON format.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_config/{section}/{key}</code><p><code>DELETE</code></p></td><td>
<a href='http://docs.couchdb.org/en/1.6.0/api/server/configuration.html#delete--_config-section-key' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Delete a configuration value.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_db\_updates</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/advanced.html#get-/_db_updates' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/server/common.html#get--_db_updates' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/server/common.html#get--_db_updates' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>List all database events in the instance.<br/>In Cloudant the endpoint is only available to dedicated customers. Its documentation references additional query params (limit, since, descending) and an additional feed type value (normal) For CouchDB, its documentation references an additional feed type value (eventsource)</td>
</tr>
<tr>
<td rowspan='2'><code>/\_log</code><p><code>GET</code></p></td><td>
<a href='http://docs.couchdb.org/en/1.6.0/api/server/common.html#get--_log' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Get the log. Equivalent to accessing the local log file of the corresponding instance.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_membership</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/advanced.html#get-/_membership' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/server/common.html#membership' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
</td>
</tr>
<tr>
<td>List the names of nodes in the cluster. Active clusters are indicated in the cluster\_nodes field, while all\_nodes has all nodes.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_replicate</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/replication.html#the-/_replicate-endpoint' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/server/common.html#post--_replicate' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/server/common.html#post--_replicate' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Request, configure, or stop, a replication operation.<br/>Cloudant documentation references additional request body fields (selector, since\_seq).</td>
</tr>
<tr>
<td rowspan='2'><code>/\_replicator</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/replication.html#the-/_replicator-database' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/replication/replicator.html' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/replication/replicator.html' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Trigger a replication.<br/>Cloudant documentation references additional request body fields (selector, since\_seq).</td>
</tr>
<tr>
<td rowspan='2'><code>/\_replicator</code><p><code>PUT</code></p></td><td>
<a href='https://docs.cloudant.com/replication.html#the-/_replicator-database' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/replication/replicator.html' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/replication/replicator.html' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Trigger a replication.<br/>Cloudant documentation references additional request body fields (selector, since\_seq).</td>
</tr>
<tr>
<td rowspan='2'><code>/\_replicator</code><p><code>DELETE</code></p></td><td>
<a href='https://docs.cloudant.com/replication.html#the-/_replicator-database' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/replication/replicator.html' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/replication/replicator.html' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Cancel an ongoing replication<br/>Cloudant documentation references additional request body fields (selector, since\_seq).</td>
</tr>
<tr>
<td rowspan='2'><code>/\_restart</code><p><code>POST</code></p></td><td>
<a href='http://docs.couchdb.org/en/1.6.0/api/server/common.html#post--_restart' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Restart the instance. You must be authenticated as a user with administration privileges.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_search\_analyze</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/search.html#testing-analyzer-tokenization' target='_blank'><img src='../images/smallCloudant.png'/></a>
</td>
</tr>
<tr>
<td>Test the results of analyzer tokenization by posting sample data.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_session</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/authentication.html#cookie-authentication' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/server/authn.html#get--_session' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/server/authn.html#get--_session' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Returns information about the authenticated user.<br/>CouchDB documentation references an additional query param (basic).</td>
</tr>
<tr>
<td rowspan='2'><code>/\_session</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/authentication.html#cookie-authentication' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/server/authn.html#post--_session' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/server/authn.html#post--_session' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Initiate a new session for the specified user credentials. Cookie based user login.<br/>CouchDB documentation references an additional query param (next).</td>
</tr>
<tr>
<td rowspan='2'><code>/\_session</code><p><code>DELETE</code></p></td><td>
<a href='https://docs.cloudant.com/authentication.html#cookie-authentication' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/server/authn.html#delete--_session' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/server/authn.html#delete--_session' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Closes user's session. Logout cookie based user.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_stats</code><p><code>GET</code></p></td><td>
<a href='http://docs.couchdb.org/en/1.6.0/api/server/common.html#get--_stats' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Return the statistics for the running server.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_utils</code><p><code>GET</code></p></td><td>
<a href='http://docs.couchdb.org/en/2.0.0/api/server/common.html#get--_utils' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/server/common.html#get--_utils' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Access the built-in Fauxton administration interface.</td>
</tr>
<tr>
<td rowspan='2'><code>/\_uuids</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/advanced.html#get-/_uuids' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/server/common.html#uuids' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/server/common.html#uuids' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Request one or more Universally Unique Identifiers (UUIDs).</td>
</tr>
<tr>
<td rowspan='2'><code>/favicon.ico</code><p><code>GET</code></p></td><td>
<a href='http://docs.couchdb.org/en/2.0.0/api/server/common.html#get--favicon.ico' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/server/common.html#get--favicon.ico' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Get the binary content for the favicon.ico site icon.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}</code><p><code>HEAD</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/common.html#head--db' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/common.html#head--db' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Return the HTTP Headers containing a minimal amount of information about the specified database.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/database.html#read' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/common.html#get--db' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/common.html#get--db' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Get information about the specified database.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/common.html#post--db' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/common.html#post--db' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Create a new document in the specified database, using the supplied JSON document structure.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}</code><p><code>PUT</code></p></td><td>
<a href='https://docs.cloudant.com/database.html#create' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/common.html#put--db' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/common.html#put--db' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Create a new database.<br/>Database names must start with a lowercase letter and contain only the following characters: Lowercase characters (a-z), Digits (0-9), Any of the characters \_, $, (, ), +, -, and /</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}</code><p><code>DELETE</code></p></td><td>
<a href='https://docs.cloudant.com/database.html#deleting-a-database' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/common.html#delete--db' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/common.html#delete--db' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Delete the specified database, and all the documents and attachments contained within it.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_all\_docs</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/database.html#get-documents' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/bulk-api.html#get--db-_all_docs' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/bulk-api.html#get--db-_all_docs' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>List all the documents in a database.<br/>CouchDB documentation references additional query params (end\_key, endkey\_docid, end\_key\_doc\_id, stale, start\_key, startkey\_docid, start\_key\_doc\_id, update\_seq).</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_all\_docs</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/database.html#get-documents' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/bulk-api.html#post--db-_all_docs' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/bulk-api.html#post--db-_all_docs' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>List all the documents in a database.<br/>CouchDB documentation references additional query params (end\_key, endkey\_docid, end\_key\_doc\_id, stale, start\_key, startkey\_docid, start\_key\_doc\_id, update\_seq).</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_bulk\_docs</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/document.html#bulk-operations' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/bulk-api.html#post--db-_bulk_docs' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/bulk-api.html#post--db-_bulk_docs' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Create and update multiple documents at the same time within a single request.<br/>CouchDB documentation references an additional request object field (new\_edits).</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_bulk\_get</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
</td>
</tr>
<tr>
<td>Get multiple documents in a single request.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_changes</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/database.html#get-changes' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/changes.html#get--db-_changes' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/changes.html#get--db-_changes' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>List of changes made to documents in the database, including insertions, updates, and deletions.<br/>CouchDB includes query params (attachments, att\_encoding\_info, last-event-id, view). Also filtering using a selector is new in CouchDB 2.0.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_changes</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/database.html#using-post-to-get-changes' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/changes.html#post--db-_changes' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/changes.html#post--db-_changes' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>List of changes made to documents in the database, including insertions, updates, and deletions.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_compact</code><p><code>POST</code></p></td><td>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/compact.html#post--db-_compact' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Request compaction of the specified database.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_compact/{ddoc}</code><p><code>POST</code></p></td><td>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/compact.html#post--db-_compact-ddoc' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Compact the view indexes associated with the specified design document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}</code><p><code>HEAD</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/common.html#head--db-_design-ddoc' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/common.html#head--db-_design-ddoc' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Return the HTTP Headers containing a minimal amount of information about the specified design document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/common.html#get--db-_design-ddoc' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/common.html#get--db-_design-ddoc' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Get the contents of the design document specified with the name of the design document and from the specified database from the URL.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}</code><p><code>PUT</code></p></td><td>
<a href='https://docs.cloudant.com/design_documents.html#creating-or-updating-a-design-document' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/common.html#put--db-_design-ddoc' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/common.html#put--db-_design-ddoc' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Create a new named design document or create a new revision of the existing design document.<br/>Cloudant documentation references an additional request body field (indexes) CouchDB documentation references additional request body fields (language, options).</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}</code><p><code>DELETE</code></p></td><td>
<a href='https://docs.cloudant.com/design_documents.html#deleting-a-design-document' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/common.html#delete--db-_design-ddoc' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/common.html#delete--db-_design-ddoc' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Delete the specified document from the database.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}</code><p><code>COPY</code></p></td><td>
<a href='https://docs.cloudant.com/design_documents.html#copying-a-design-document' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/common.html#copy--db-_design-ddoc' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/common.html#copy--db-_design-ddoc' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Copy an existing design document to a new or existing one.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/\_geo\_info/{index}</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/geo.html#obtaining-information-about-a-cloudant-geo-index' target='_blank'><img src='../images/smallCloudant.png'/></a>
</td>
</tr>
<tr>
<td>Obtain information about a geospatial index.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/\_geo/{index}</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/geo.html#querying-a-cloudant-geo-index' target='_blank'><img src='../images/smallCloudant.png'/></a>
</td>
</tr>
<tr>
<td>Query a geo index.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/\_info</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/design_documents.html#retrieving-information-about-a-design-document' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/common.html#get--db-_design-ddoc-_info' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/common.html#get--db-_design-ddoc-_info' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Obtain information about the specified design document, including the index, index size, and current status of the design document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/\_list/{func}/{other-ddoc}/{view}</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/render.html#get--db-_design-ddoc-_list-func-other-ddoc-view' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/render.html#get--db-_design-ddoc-_list-func-other-ddoc-view' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Apply the list function for the view function from the other design document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/\_list/{func}/{other-ddoc}/{view}</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/render.html#post--db-_design-ddoc-_list-func-other-ddoc-view' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/render.html#post--db-_design-ddoc-_list-func-other-ddoc-view' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Apply the list function for the view function from the other design document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/\_list/{func}/{view}</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/design_documents.html#list-functions' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/render.html#get--db-_design-ddoc-_list-func-view' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/render.html#get--db-_design-ddoc-_list-func-view' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Apply the list function for the view function from the same design document.<br/>The result of a list function is not stored. This means that the function is executed every time a request is made.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/\_list/{func}/{view}</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/render.html#post--db-_design-ddoc-_list-func-view' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/render.html#post--db-_design-ddoc-_list-func-view' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Apply the list function for the view function from the same design document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/\_rewrite/{path}</code><p><code>ANY</code></p></td><td>
<a href='https://docs.cloudant.com/design_documents.html#rewrite-rules' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/rewrites.html#any--db-_design-ddoc-_rewrite-path' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/rewrites.html#any--db-_design-ddoc-_rewrite-path' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Rewrite the specified path by rules defined in the specified design document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/\_search\_info/{index}</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/search.html#search-index-metadata' target='_blank'><img src='../images/smallCloudant.png'/></a>
</td>
</tr>
<tr>
<td>Obtain information about a search specified within a given design document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/\_search/{index}</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/search.html#queries' target='_blank'><img src='../images/smallCloudant.png'/></a>
</td>
</tr>
<tr>
<td>Query an index.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/\_search/{index}</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/search.html#posting-search-queries' target='_blank'><img src='../images/smallCloudant.png'/></a>
</td>
</tr>
<tr>
<td>Query an index.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/\_show/{func}</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/render.html#get--db-_design-ddoc-_show-func' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/render.html#get--db-_design-ddoc-_show-func' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Apply the show function for null document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/\_show/{func}</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/render.html#post--db-_design-ddoc-_show-func' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/render.html#post--db-_design-ddoc-_show-func' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Apply the show function for null document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/\_show/{func}/{docid}</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/design_documents.html#show-functions' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/render.html#get--db-_design-ddoc-_show-func-docid' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/render.html#get--db-_design-ddoc-_show-func-docid' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Apply the show function for the specified document.<br/>The result of a show function is not stored. This means that the function is executed every time a request is made.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/\_show/{func}/{docid}</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/render.html#post--db-_design-ddoc-_show-func-docid' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/render.html#post--db-_design-ddoc-_show-func-docid' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Apply the show function for the specified document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/\_update/{func}</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/design_documents.html#update-handlers' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/render.html#post--db-_design-ddoc-_update-func' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/render.html#post--db-_design-ddoc-_update-func' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Execute the update function on server side for null document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/\_update/{func}/{docid}</code><p><code>PUT</code></p></td><td>
<a href='https://docs.cloudant.com/design_documents.html#update-handlers' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/render.html#put--db-_design-ddoc-_update-func-docid' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/render.html#put--db-_design-ddoc-_update-func-docid' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Execute the update function on server side for the specified document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/\_view/{view}</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/creating_views.html#using-views' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/views.html#get--db-_design-ddoc-_view-view' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/views.html#get--db-_design-ddoc-_view-view' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Execute the view function from the specified design document.<br/>CouchDB documentation references additional query params (conflicts, end\_key, end\_key\_doc\_id, attachments, att\_encoding\_info, sorted, start\_key, start\_key\_doc\_id, update\_seq). CouchDB 2.0 added sorted parameter not available in CouchDB 1.6.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/\_view/{view}</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/creating_views.html#querying-a-view-using-a-list-of-keys' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/views.html#post--db-_design-ddoc-_view-view' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/views.html#post--db-_design-ddoc-_view-view' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Execute the view function from the specified design document.<br/>CouchDB documentation references additional query params (conflicts, end\_key, end\_key\_doc\_id, attachments, att\_encoding\_info, sorted, start\_key, start\_key\_doc\_id, update\_seq).</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/{attname}</code><p><code>HEAD</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/common.html#head--db-_design-ddoc-attname' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/common.html#head--db-_design-ddoc-attname' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Return the HTTP headers containing a minimal amount of information about the specified attachment.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/{attname}</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/attachments.html#read' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/common.html#get--db-_design-ddoc-attname' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/common.html#get--db-_design-ddoc-attname' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Return the file attachment associated with the design document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/{attname}</code><p><code>PUT</code></p></td><td>
<a href='https://docs.cloudant.com/attachments.html#create-/-update' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/common.html#put--db-_design-ddoc-attname' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/common.html#put--db-_design-ddoc-attname' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Upload the supplied content as an attachment to the specified design document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_design/{ddoc}/{attname}</code><p><code>DELETE</code></p></td><td>
<a href='https://docs.cloudant.com/attachments.html#delete' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/ddoc/common.html#delete--db-_design-ddoc-attname' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/ddoc/common.html#delete--db-_design-ddoc-attname' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Delete the attachment of the specified design document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_ensure\_full\_commit</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/compact.html#post--db-_ensure_full_commit' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/compact.html#post--db-_ensure_full_commit' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Commit any recent changes to the specified database to disk.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_explain</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/cloudant_query.html#explain-plans' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/find.html#post--db-_explain' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
</td>
</tr>
<tr>
<td>Identify which index is being used by a particular query.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_find</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/cloudant_query.html#finding-documents-using-an-index' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/find.html#post--db-_find' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
</td>
</tr>
<tr>
<td>Find documents using a declarative JSON querying syntax.<br/>Cloudant documentation references additional request body fields (r, bookmark)</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_index</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/cloudant_query.html#list-all-cloudant-query-indexes' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/find.html#get--db-_index' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
</td>
</tr>
<tr>
<td>List indexes.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_index</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/cloudant_query.html#creating-an-index' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/find.html#post--db-_index' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
</td>
</tr>
<tr>
<td>Create a new index.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_index/\_design/{ddoc}/{type}/{name}</code><p><code>DELETE</code></p></td><td>
<a href='https://docs.cloudant.com/cloudant_query.html#deleting-an-index' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/find.html#delete--db-_index-designdoc-json-name' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
</td>
</tr>
<tr>
<td>Delete an index.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_local/{docid}</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/local.html#get--db-_local-docid' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/local.html#get--db-_local-docid' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Get the specified local document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_local/{docid}</code><p><code>PUT</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/local.html#put--db-_local-docid' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/local.html#put--db-_local-docid' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Store the specified local document.<br/>Local documents are not replicated to other databases.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_local/{docid}</code><p><code>DELETE</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/local.html#delete--db-_local-docid' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/local.html#delete--db-_local-docid' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Delete the specified local document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_local/{docid}</code><p><code>COPY</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/local.html#copy--db-_local-docid' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/local.html#copy--db-_local-docid' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Copy the specified local document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_missing\_revs</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/advanced.html#get-/$db/missingrevs' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/misc.html#post--db-_missing_revs' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/misc.html#post--db-_missing_revs' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Return the document revisions from the given list that do not exist in the database.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_purge</code><p><code>POST</code></p></td><td>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/misc.html#post--db-_purge' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Remove the references to deleted documents from the database.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_revs\_diff</code><p><code>POST</code></p></td><td>
<a href='https://docs.cloudant.com/advanced.html#post-/$db/_revs_diff' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/misc.html#post--db-_revs_diff' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/misc.html#post--db-_revs_diff' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Given a set of document/revision IDs, return the subset of those that do not correspond to revisions stored in the database.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_revs\_limit</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/advanced.html#get-/$db/_revs_limit' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/misc.html#get--db-_revs_limit' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/misc.html#get--db-_revs_limit' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Get the number of document revisions tracked.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_revs\_limit</code><p><code>PUT</code></p></td><td>
<a href='https://docs.cloudant.com/advanced.html#put-/$db/_revs_limit' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/misc.html#put--db-_revs_limit' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/misc.html#put--db-_revs_limit' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Set the maximum number of document revisions tracked.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_security</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/authorization.html#viewing-permissions' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/security.html#get--db-_security' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/security.html#get--db-_security' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Return the current security object from the specified database.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_security</code><p><code>PUT</code></p></td><td>
<a href='https://docs.cloudant.com/authorization.html#modifying-permissions' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/database/security.html#put--db-_security' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/security.html#put--db-_security' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Set the security object for the given database.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_shards</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/advanced.html#get-/$db/_shards' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
</td>
</tr>
<tr>
<td>Return information about the shards in the cluster</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/\_view\_cleanup</code><p><code>POST</code></p></td><td>
<a href='http://docs.couchdb.org/en/1.6.0/api/database/compact.html#post--db-_view_cleanup' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Remove view index files that are no longer required by as a result of changed views within design documents.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/{docid}</code><p><code>HEAD</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/document/common.html#head--db-docid' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/document/common.html#head--db-docid' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Return the HTTP Headers containing a minimal amount of information about the specified document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/{docid}</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/document.html#read' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/document/common.html#get--db-docid' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/document/common.html#get--db-docid' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Return the document specified by the docid from the specified db.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/{docid}</code><p><code>PUT</code></p></td><td>
<a href='https://docs.cloudant.com/document.html#update' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/document/common.html#put--db-docid' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/document/common.html#put--db-docid' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Create a new named document or create a new revision of the existing document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/{docid}</code><p><code>DELETE</code></p></td><td>
<a href='https://docs.cloudant.com/document.html#delete' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/document/common.html#delete--db-docid' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/document/common.html#delete--db-docid' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Mark the specified document as deleted.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/{docid}</code><p><code>COPY</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/document/common.html#copy--db-docid' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/document/common.html#copy--db-docid' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Copy an existing document to a new or existing document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/{docid}/{attname}</code><p><code>HEAD</code></p></td><td>
<a href='https://docs.cloudant.com/' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/document/attachments.html#head--db-docid-attname' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/document/attachments.html#head--db-docid-attname' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Return the HTTP headers containing a minimal amount of information about the specified attachment.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/{docid}/{attname}</code><p><code>GET</code></p></td><td>
<a href='https://docs.cloudant.com/attachments.html#read' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/document/attachments.html#get--db-docid-attname' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/document/attachments.html#get--db-docid-attname' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Return the file attachment associated with the document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/{docid}/{attname}</code><p><code>PUT</code></p></td><td>
<a href='https://docs.cloudant.com/attachments.html#create-/-update' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/document/attachments.html#put--db-docid-attname' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/document/attachments.html#put--db-docid-attname' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Upload the supplied content as an attachment to the specified document.</td>
</tr>
<tr>
<td rowspan='2'><code>/{db}/{docid}/{attname}</code><p><code>DELETE</code></p></td><td>
<a href='https://docs.cloudant.com/attachments.html#delete' target='_blank'><img src='../images/smallCloudant.png'/></a>
<a href='http://docs.couchdb.org/en/2.0.0/api/document/attachments.html#delete--db-docid-attname' target='_blank'><img src='../images/smallCouchDB2.png'/></a>
<a href='http://docs.couchdb.org/en/1.6.0/api/document/attachments.html#delete--db-docid-attname' target='_blank'><img src='../images/smallCouchDB1.png'/></a>
</td>
</tr>
<tr>
<td>Delete the attachment associated with the specified doc.</td>
</tr>
</table>

