
---

copyright:
  years: 2015, 2016
lastupdated: "2016-11-21"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}

<div id="ReplicationAPI"/>

# Replication

Cloudant replication is the process that synchronizes ('syncs') the state of two databases.
{:shortdesc}

Any change which has occurred in the source database is reproduced in the target database.
You can create replications between any number of databases, whether continuous or not.

Depending on your application requirements,
you use replication to share and aggregate state and content.

Replication takes place in one direction only.
To keep two databases synchronized with each other,
you must replicate in both directions.
This means that you must replicate from `database1` to `database2`,
and separately from `database2` to `database1`.

## Important notes

Replications can severely impact the performance of a Cloudant cluster.
Performance testing is recommended to understand the impact on your environment
under an increasing number of concurrent replications.

Continuous replication can result in a large number of internal calls.
This might affect costs for multi-tenant users of Cloudant systems.
Continuous replication is disabled by default.

The target database must exist.
It is not automatically created if it does not exist.
Add `"create_target":true` to the JSON document describing the replication
if the target database does not exist prior to replication.

Replicator databases must be maintained and looked after,
just like any other valuable data store.
For more information,
see [replication database maintenance](#replication-database-maintenance).

## Creating replications

Replications are created in one of two ways:

1.	A replication can be created using a [replication document](#replication-document-format)
	in the `_replicator` database.
	Creating and modifying replications in this way allows you to control replication
	in the same as working with other documents.
	Replication jobs created this way are resumed automatically after a node restart.
2.	A replication can be started by `POST`ing a JSON document describing the desired replication
	directly to the `/_replicate` endpoint.
	Replication jobs created this way are not resumed if the node they run on is restarted. 

## Replication document format

>	**Note**: You must use the *full* URL
	when specifying the source and target databases in a replication document.

The format of the document used to describe a replication is as follows:

<div id="checkpoints"/>

Field Name | Required | Description
-----------|----------|-------------
`source` | yes | Identifies the database to copy revisions from. Can be a database URL, or an object whose url property contains the full URL of the database.
`target` | yes | Identifies the database to copy revisions to. Same format and interpretation as source. Does not have to be the same value as the `source` field.
`continuous` | no | Continuously syncs state from the `source` to the `target`, only stopping when deleted.
`create_target` | no | A value of `true` tells the replicator to create the `target` database if it does not exist.
`doc_ids` | no | Array of document IDs; if given, only these documents are replicated.
`filter` | no | Name of a [filter function](/docs/api/design_documents.html#filter-functions), defined in a design document. The filter function determines which documents get replicated. Note that using the `selector` option provides performance benefits compared with using the `filter` option. You should use the `selector` option where possible.
`proxy` | no | Proxy server URL.
`selector` | no | Provide a simple filter to select the documents that are included in the replication. Using the `selector` option provides performance benefits compared with using the `filter` option. More information about `selector` is available [here](#selector-field).
`since_seq` | no | Sequence from which the replication should start. More information about `since_seq` is available [here](#since-seq-field).
`use_checkpoints` | no | Indicate whether to create checkpoints. Checkpoints greatly reduce the time and resources needed for repeated replications. Setting this to `false` removes the requirement for write access to the `source` database. Defaults to `true`.
`user_ctx` | no | An object containing the username and optionally an array of roles, for example: `"user_ctx": {"name": "jane", "roles": ["admin"]} `. This is needed for the replication to show up in the output of `/_active_tasks`.

<div id="selector-field"/>

### The `selector` field

If you do not want to replicate the entire contents of a database,
you can specify a simple filter in the `selector` field.
The filter takes the form of a [Cloudant Query](/docs/api/cloudant_query.html) selector object.

Using a selector object provides performance benefits when compared with using a
[filter function](/docs/api/design_documents.html#filter-functions).
You should use the `selector` option where possible.


The selector object identifies a field (such as `_id` in the following example),
and an expression (such as `"$gte": "d2"`) that must be true for that field
in order for the selector to allow the document to be replicated.
In the following example,
only documents that have a `_id` field with a value greater than or equal to `"d2"` are replicated.

_Example `selector` object in a replication document:_

```json
{
	"source": "https://$USERNAME1:$PASSWORD1@$USERNAME1.cloudant.com/$DATABASE1",
	"target": "https://$USERNAME2:$PASSWORD2@$USERNAME2.cloudant.com/$DATABASE2",
	"selector": {
		"_id": {
			"$gte": "d2"
		}
	},
	"continuous": true
}
```
{:screen}


If there is a problem with the replication request,
an HTTP [`400`](/docs/api/http.html#400) error is returned,
including more details about the problem in the `"reason"` field of the response.
The reason might be one of:

-	The Cloudant Query selector object is missing.
-	The selector object is not valid JSON.
-	The selector object does not describe a valid Cloudant Query.

More information about using a `selector` object is available in the
[Apache CouchDB documentation](http://docs.couchdb.org/en/2.0.0/api/database/changes.html#selector){:new_window}.

_Example error response if the selector is not valid:_

```json
{
	"error": "bad request",
	"reason": "<details of the problem>"
}
```
{:screen}

<div id="since-seq-field"/>

### The `since_seq` field

If you do not want to replicate the entire contents of a database,
you can specify a 'replication sequence value' in the `since_seq` field.

The replication sequence value indicates how far you have progressed 'through' a database,
for example as part of a replication.
Setting the contents of the `since_seq` field to this value ensures that the replication starts from that point,
rather than from the very beginning.

This field is especially useful for creating incremental copies of databases. To do this:

1.	Find the ID of the [checkpoint](#checkpoints) document for the last replication. It is stored in the  `_replication_id` field of the replication document in the [`_replicator` database](#replicator-database).
2.	Open the checkpoint document at `/<database>/_local/<_replication_id>`, where `<_replication_id>` is the ID you found in the previous step, and `<database>` is the name of the source or the target database. The document usually exists on both databases but might only exist on one.
3.	Search for the `recorded_seq` field of the first element in the history array.
4.	Set the `since_seq` field in the replication document to the value of the `recorded_seq` field.
5.	Start replicating to a new database.

<div id="replicator-database"/>

## The `_replicator` database

The `_replicator` database is a special database where you can `PUT` or `POST` documents to trigger replications,
or `DELETE` to cancel ongoing replications.
These documents have exactly the same content as the JSON documents you can `POST` to the
[`/_replicate`](#the-_replicate-endpoint) endpoint.
The fields supplied in the replication document are `source`,
`target`,
`continuous`,
`create_target`,
`doc_ids`,
`filter`,
`proxy`,
`query_params`,
and`use_checkpoints`.
These fields are described in the [Replication document format](#replication-document-format).

Replication documents can have a user defined `_id`.

The names of the source and target databases do not have to be the same.

>	**Note**: All design documents and `_local` documents added to the `/_replicator` database are ignored.

### Creating a replication

To start a replication,
add a [replication document](#replication-document-format) to the `_replicator` database.

_Example instructions for creating a replication document, using HTTP:_

```http
PUT /_replicator/replication-doc HTTP/1.1
Content-Type: application/json
```

_Example instructions for creating a replication document, using the command line:_

```
curl -X PUT https://$USERNAME:$PASSWORD@USERNAME.cloudant.com/_replicator/replication-doc -H 'Content-Type: application/json' -d @replication-document.json
#assuming replication-document.json is a json file with valid replication information.
```
{:screen}

_Example replication document:_

```json
{
	"source": "https://$USERNAME1:$PASSWORD1@$USERNAME1.cloudant.com/$DATABASE1",
	"target": "https://$USERNAME2:$PASSWORD2@$USERNAME2.cloudant.com/$DATABASE2",
	"create_target": true,
	"continuous": true
}
```
{:screen}

### (Optional) Creating a replication to two Bluemix environments

You can replicate a Cloudant database to multiple Bluemix environments.
When you set up the replication job for each environment,
the source database and target database names you provide must use the following format:

```
https://$USERNAME:$PASSWORD@$REMOTE_USERNAME.cloudant.com/$DATABASE_NAME
```
{:screen}

You create the database within Bluemix using the name: `$DATABASE_NAME`,
and add it to the URL format.
Do not copy the `URL` field from the `VCAP_SERVICES` environment variable.

### Monitoring a replication

To monitor replicators currently in process,
make a `GET` request to `https://$USERNAME.cloudant.com/_active_tasks`.
This returns any active tasks,
including replications.
To filter for replications,
look for documents with `"type": "replication"`.

If you monitor the `_active_tasks` and find that the state of a replication is not changing,
you might have a 'stalled' replication.
If you are sure that the replication has stalled,
contact Cloudant support for assistance.

For more details about the information provided by `_active_tasks`,
see [Active tasks](/docs/api/active_tasks.html).

_Example instructions for monitoring a replication, using HTTP:_

```
GET /_active_tasks HTTP/1.1
```
{:screen}

_Example instructions for monitoring a replication, using the command line:_

```
curl https://$USERNAME:$PASSWORD@$USERNAME.cloudant.com/_active_tasks
```
{:screen}

_Example instructions for monitoring a replication, using Javascript:_

```
var nano = require('nano');
var account = nano("https://"+$USERNAME+":"+$PASSWORD+"@"+$USERNAME+".cloudant.com");

account.request(
	{ path: '_active_tasks' },
	function (err, body, headers) {
		if (!err) {
			console.log( body.filter( function (task) {
						return (task.type === 'replication');
					} ) ); 
		}
	}
);
```
{:screen}

_Example response (abbreviated) following active task request, including continuous replication:_

```json
[
	{
		"user": null,
		"updated_on": 1363274088,
		"type": "replication",
		"target": "https://username:password@tsm.cloudant.com/user-3dg...imy/",
		"docs_read": 0,
		"doc_write_failures": 0,
		"doc_id": "tsm-admin__to__user-3dg...imy",
		"continuous": true,
		"checkpointed_source_seq": "403-g1AAA...SStc",
		"changes_pending": 134,
		"pid": "<0.1781.4101>",
		"node": "dbcore@db11.julep.cloudant.net",
		"docs_written": 0,
		"missing_revisions_found": 0,
		"replication_id": "d0cdbfee50a80fd43e83a9f62ea650ad+continuous",
		"revisions_checked": 0,
		"source": "https://repl:*****@tsm.cloudant.com/tsm-admin/",
		"source_seq": "537-g1A...LVQ",
		"started_on": 1363274083
	}
]
```
{:screen}

_Example response following active task, including single replication:_

```json
[
	{
		"pid": "<0.1303.0>",
		"replication_id": "e42a443f5d08375c8c7a1c3af60518fb+create_target",
		"checkpointed_source_seq": 17333,
		"continuous": false,
		"doc_write_failures": 0,
		"docs_read": 17833,
		"docs_written": 17833,
		"missing_revisions_found": 17833,
		"progress": 3,
		"revisions_checked": 17833,
		"source": "http://username.cloudant.com/db/",
		"source_seq": 551202,
		"started_on": 1316229471,
		"target": "test_db",
		"type": "replication",
		"updated_on": 1316230082
	}
]
```
{:screen}

<div id="delete"/>

### Cancelling a replication

To cancel a replication,
simply [delete its replication document](#document-delete) from the `_replicator` database.

If the replication is in an [`error` state](/docs/api/advanced_replication.html#replication-status),
the replicator makes repeated attempts to achieve a successful replication.
A consequence is that the replication document is updated with each attempt.
This also changes the document revision value.
Therefore,
you should get the revision value immediately before deleting the document,
otherwise you might get an [HTTP 409 "document update conflict"](/docs/api/http.html#409) response.

_Example instructions for deleting a replication document, using HTTP:_

```
DELETE /_replicator/replication-doc?rev=1-... HTTP/1.1
```
{:screen}

_Example instructions for deleting a replication document, the command line:_

```
curl -X DELETE https://$USERNAME:$PASSWORD@$USERNAME.cloudant.com/_replicator/replication-doc?rev=1-...
```
{:screen}

## The `/_replicate` endpoint

You can use this endpoint to request,
configure,
or stop,
a replication operation.

You do this by sending a `POST` request directly to the `/_replicate` endpoint.
The `POST` contains a JSON document that describes the desired replication.

-	**Method**: `POST`
-	**Path**: `/_replicate`
-	**Request**: Replication specification
-	**Response**: TBD
-	**Roles permitted**: `_admin`

The specification of the replication request is controlled through the JSON content of the request.
The JSON should be an object with fields defining the source,
target and other options.

The fields of the JSON request are as follows:

Field           | Purpose                                                           | Optional
----------------|-------------------------------------------------------------------|---------
`cancel`        | Cancels the replication.                                          | Yes
`continuous`    | Configure the replication to be continuous.                       | Yes
`create_target` | Creates the target database.                                      | Yes
`doc_ids`       | Array of document IDs to be synchronized.                         | Yes
`proxy`         | Address of a proxy server through which replication should occur. | Yes
`source`        | Source database URL, including user name and password.            | No
`target`        | Target database URL, including user name and password.            | No

>	**Note**: It is preferable to use the [Replicator Database](#the-_replicator-database) to manage replication.
	Details of why are provided [here](#avoiding-the-_replicate-endpoint).

_Example instructions for starting a replication through the `_replicate` endpoint, using HTTP:_

```
POST /_replicate HTTP/1.1
Content-Type: application/json
```
{:screen}

_Example instructions for starting a replication through the `_replicate` endpoint, using the command line:_

```
curl -H 'Content-Type: application/json' -X POST "https://$USERNAME:$PASSWORD@$USERNAME.cloudant.com/_replicate" -d @replication-doc.json
#with the file replication-doc.json containing the required replication information.
```
{:screen}

_Example JSON document describing the required replication:_

```json
{
	"source": "http://$USERNAME:$PASSWORD@username.cloudant.com/example-database",
	"target": "http://$USERNAME2:$PASSWORD2@example.org/example-target-database"
}
```
{:screen}

### Return Codes

Code  | Description
------|------------
`200` | Replication request successfully completed.
`202` | Continuous replication request has been accepted.
`404` | Either the source or target database was not found.
`500` | JSON specification was invalid.

### Avoiding the `/_replicate` endpoint

You should use the [`_replicator` database](#replicator-database) in preference to the `/_replicate` endpoint.

A significant reason for this is that in the event of problem during replication,
such as a stall,
timeout,
or application crash,
a replication defined within the `_replicator` database is automatically restarted by the system.

If you defined a replication by sending a request to the `/_replicate` endpoint,
it cannot be restarted by the system if a problem occurs because the replication request does not persist.

In addition,
replications defined in the `_replicator` database are easier to [monitor](/docs/api/advanced_replication.html#replication-status).

## Replication Operation

The aim of replication is that at the end of the process,
all active documents in the source database are also in the destination or 'target' database,
_and_ that all documents deleted from the source databases are also
deleted from the destination database (if they existed there).

Replication has two forms: push or pull replication:

-	*Push replication* is where the source is a local database,
	and the destination is a remote database.
-	*Pull replication* is where the source is a remote database instance,
	and the destination is the local database.

Pull replication is helpful if your source database has a permanent IP address,
and your destination database is local and has a dynamically assigned IP address,
for example, obtained through DHCP.
Pull replication is especially appropriate if you are replicating to a mobile or other device from a central server.

In all cases,
the requested databases in the source and target specification must exist.
If they do not,
an error is returned within the JSON object.

_Example request to replicate between a database on the source server `example.com`,
and a target database on Cloudant:_

```
POST /_replicate
Content-Type: application/json
Accept: application/json

{
	"source" : "http://user:pass@example.com/db",
	"target" : "http://user:pass@user.cloudant.com/db",
}
```
{:screen}

_Example error response if one of the requested databases for a replication does not exist:_

```json
{
	"error" : "db_not_found"
	"reason" : "could not open http://username.cloudant.com/ol1ka/",
}
```
{:screen}

