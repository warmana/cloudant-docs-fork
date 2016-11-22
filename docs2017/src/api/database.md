---

copyright:
  years: 2015, 2016
lastupdated: "2016-11-16"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}

# Databases

Cloudant databases contain JSON objects.
These JSON objects are called [documents](/docs/api/document.html#documents).
All documents must be contained in a database.
{:shortdesc}

A guide is [available](/docs/guides/transactions.html),
providing an example of how documents for an e-commerce application might be used within a Cloudant database.

A more complex database application,
involving additional storage,
processing,
and analytics tasks,
is referred to as a [warehouse](/docs/guides/warehousing.html).  
Warehouses are also supported by Cloudant.

## Create

To create a database,
send a `PUT` request to `https://$USERNAME.cloudant.com/$DATABASE`.

The database name must start with a lowercase letter,
and contain only the following characters:

-	Lowercase characters (a-z)
-	Digits (0-9)
-	Any of the characters _, $, (, ), +, -, and /
 
_Example of creating a database, using HTTP:_

```
PUT /$DATABASE HTTP/1.1
HOST: $ACCOUNT.cloudant.com
```
{:screen}

_Example of creating a database, using the command line:_

```
curl https://$USERNAME:$PASSWORD@$ACCOUNT.cloudant.com/$DATABASE -X PUT
```
{:screen}

_Example of creating a database, using Javascript:_

```
var nano = require('nano');
var account = nano("https://"+$USERNAME+":"+$PASSWORD+"@"+$USERNAME+".cloudant.com");

account.db.create($DATABASE, function (err, body, headers) {
	if (!err) {
		console.log('database created!');
	}
});
```
{:screen}

<div id="response"></div>

If creation succeeds, you get a [201 or 202 response](/docs/api/http.html#201).
In case of an error,
the HTTP status code tells you what went wrong.

Code | Description
-----|------------
201  | Database created successfully
202  | The database has been successfully created on some nodes, but the number of nodes is less than the write quorum.
403  | Invalid database name.
412  | Database aleady exists.

_Example response following successful creation of a database:_

```
HTTP/1.1 201 Created

{
	ok": true
}
```
{:screen}

### Database topology

It is possible to modify the configuration of a database sharding topology of a
database on dedicated database clusters.
This can be done at the time a database is created.
However,
poor choices for configuration parameters can adversely affect database performance.

For more information about modifying database configuration
in a dedicated database environment,
please contact Cloudant support.

> **Note**: It is not possible to modify the configuration used for databases
on multi-tenant clusters.

<div id="read"></div>

## Getting database details 

Sending a `GET` request to `https://$USERNAME.cloudant.com/$DATABASE`
returns details about the database,
such as how many documents it contains.

_Example of getting database details, using HTTP:_

```
GET /$DATABASE HTTP/1.1
```
{:screen}

_Example of getting database details, using the command line:_

```
curl https://$USERNAME.cloudant.com/$DATABASE \
	-u $USERNAME
```
{:screen}

_Example of getting database details, using Javascript:_

```
var nano = require('nano');
var account = nano("https://"+$USERNAME+":"+$PASSWORD+"@"+$USERNAME+".cloudant.com");

account.db.get($DATABASE, function (err, body, headers) {
	if (!err) {
		console.log(body);
	}
});
```

The elements of the returned structure are shown in the following table:

Field                 | Description
----------------------|------------
`compact_running`     | Set to true if the database compaction routine is operating on this database.
`db_name`             | The name of the database.
`disk_format_version` | The version of the physical format used for the data when it is stored on disk.
`disk_size`           | Size in bytes of the data as stored on the disk. Views indexes are not included in the calculation.
`doc_count`           | A count of the documents in the specified database.
`doc_del_count`       | Number of deleted documents.
`instance_start_time` | Always 0.
`other`               | JSON object containing a `data_size` field.
`purge_seq`           | The number of purge operations on the database.
`sizes`               | JSON object containing file, external, and active sizes.
`update_seq`          | An opaque string describing the state of the database. It should not be relied on for counting the number of updates.

_Example response containing (abbreviated) database details:_

```json
{
	"update_seq": "982...uUQ",
	"db_name": "db",
	"sizes": {
		"file": 46114703224,
		"external": 193164408719,
		"active": 34961621142
	},
	"purge_seq": 0,
	"other": {
		"data_size": 193164408719
	},
	"doc_del_count": 5564,
	"doc_count": 9818541,
	"disk_size": 46114703224,
	"disk_format_version": 6,
	"compact_running": true,
	"instance_start_time": "0"
}
```
{:screen}

<div id="get-databases"></div>

## Get a list of all databases in the account

To list all the databases in an account,
send a `GET` request to `https://$USERNAME.cloudant.com/_all_dbs`.

_Example request to list all databases, using HTTP:_

```
GET /_all_dbs HTTP/1.1
```
{:screen}

_Example request to list all databases, using the command line:_

```
curl https://$USERNAME.cloudant.com/_all_dbs \
     -u $USERNAME
```
{:screen}

_Example request to list all databases, using Javascript:_

```
var nano = require('nano');
var account = nano("https://"+$USERNAME+":"+$PASSWORD+"@"+$USERNAME+".cloudant.com");

account.db.list(function (err, body, headers) {
  if (!err) {
    console.log(body);
  }
});
```
{:screen}

The response is a JSON array with all the database names.

_Example response:_

```json
[
	"_users",
	"contacts",
	"docs",
	"invoices",
	"locations"
]
```
{:screen}

## Get Documents

To list all the documents in a database,
send a `GET` request to `https://$USERNAME.cloudant.com/$DATABASE/_all_docs`.

The `_all_docs` endpoint accepts the following query arguments:

Argument        | Description                                                                                     | Optional | Type            | Default
----------------|-------------------------------------------------------------------------------------------------|----------|-----------------|--------
`conflicts`     | Can only be set if `include_docs` is `true`. Adds information about conflicts to each document. | yes      | boolean         | false
`descending`    | Return the documents in descending key order.                                                   | yes      | boolean         | false
`endkey`        | Stop returning records when the specified key is reached.                                       | yes      | string          |
`include_docs`  | Include the full content of the documents in the return.                                        | yes      | boolean         | false
`inclusive_end` | Include rows whose key equals the `endkey` value.                                               | yes      | boolean         | true
`key`           | Return only documents with IDs that match the specified key.                                    | yes      | string          |
`keys`          | Return only documents with IDs that match one of the specified keys.                            | yes      | list of strings |
`limit`         | Limit the number of returned documents to the specified number.                                 | yes      | numeric         |
`skip`          | Skip this number of records before starting to return the results.                              | yes      | numeric         | 0
`startkey`      | Return records starting with the specified key.                                                 | yes      | string          |

>	**Note**: Using `include_docs=true` might have [performance implications](/docs/api/using_views.html#include_docs_caveat).

>	**Note**: When using the `keys` argument,
it might be easier to use `POST` rather than `GET` if you require a large number of strings to list the desired keys.

_Example request to list all documents in a database, using HTTP:_

```
GET /_all_docs HTTP/1.1
```
{:screen}

_Example request to list all documents in a database, using the command line:_

```
curl https://%USERNAME:$PASSWORD@$USERNAME.cloudant.com/$DATABASE/_all_docs
```
{:screen}

_Example request to list all documents in a database, using Javascript:_

```
var nano = require('nano');
var account = nano("https://"+$USERNAME+":"+$PASSWORD+"@"+$USERNAME+".cloudant.com");
var db = account.use($DATABASE);

db.list(function (err, body, headers) {
  if (!err) {
    console.log(body);
  }
});
```
{:screen}

_Example request to list all documents in a database that match at least one of the specified keys, using HTTP:_

```
GET /_all_docs?keys=["somekey","someotherkey"] HTTP/1.1
```
{:screen}

_Example request to list all documents in a database that match at least one of the specified keys,
using the command line:_

```
curl https://%USERNAME:$PASSWORD@$USERNAME.cloudant.com/$DATABASE/_all_docs?keys=["somekey","someotherkey"]
```
{:screen}

The response is a JSON object containing all documents in the database matching the parameters.
The following table describes the meaning of the individual fields:

Field        | Description                                                                         | Type
-------------|-------------------------------------------------------------------------------------|-----
`offset`     | Offset where the document list started.                                             | numeric
`rows`       | Array of document objects.                                                          | array
`total_rows` | Number of documents in the database or view that match the parameters of the query. | numeric
`update_seq` | Current update sequence for the database.                                           | string

_Example response after requesting all documents in a database:_

```json
{
	"total_rows": 3,
	"offset": 0,
	"rows": [
		{
			"id": "5a049246-179f-42ad-87ac-8f080426c17c",
			"key": "5a049246-179f-42ad-87ac-8f080426c17c",
			"value": {
				"rev": "2-9d5401898196997853b5ac4163857a29"
			}
		},
		{
			"id": "96f898f0-f6ff-4a9b-aac4-503992f31b01",
			"key": "96f898f0-f6ff-4a9b-aac4-503992f31b01",
			"value": {
				"rev": "2-ff7b85665c4c297838963c80ecf481a3"
			}
		},
		{
			"id": "d1f61e66-7708-4da6-aa05-7cbc33b44b7e",
			"key": "d1f61e66-7708-4da6-aa05-7cbc33b44b7e",
			"value": {
				"rev": "2-cbdef49ef3ddc127eff86350844a6108"
			}
		}
	]
}
```
{:screen}

## Get Changes

Sending a `GET` request to `https://$USERNAME.cloudant.com/$DATABASE/_changes`
returns a list of changes made to documents in the database,
including insertions,
updates,
and deletions.

When a `_changes` request is received,
one replica for each shard of the database is asked to provide a list of changes.
These responses are combined and returned to the original requesting client.

`_changes` accepts several optional query arguments:

Argument       | Description | Supported Values | Default 
---------------|-------------|------------------|---------
`conflicts`    | Can only be set if `include_docs` is `true`. Adds information about conflicts to each document. | boolean | false 
`descending`   | Return the changes in sequential order. | boolean | false | 
`doc_ids`      | To be used only when `filter` is set to `_doc_ids`. Filters the feed so that only changes to the specified documents are sent. **Note**: The `doc_ids` parameter only works with versions of Cloudant that are compatible with CouchDB 2.0. See [API: GET / documentation](/docs/api/advanced.html#get-/) for more information. | A JSON array of document IDs | |
`feed`         | Type of feed required. For details see the [`feed` information](#the-feed-argument). | `"continuous"`, `"longpoll"`, `"normal"` | `"normal"`
`filter`       | Name of [filter function](/docs/api/design_documents.html#filter-functions) to use to get updates. The filter is defined in a [design document](/docs/api/design_documents.html). | string | no filter
`heartbeat`    | Time in milliseconds after which an empty line is sent during `feed=longpoll` or `feed=continuous` if there have been no changes. | any positive number | no heartbeat | 
`include_docs` | Include the document as part of the result. | boolean | false |
`limit`        | Maximum number of rows to return. | any non-negative number | none |  
`since`        | Start the results from changes _after_ the specified sequence identifier. For details see the [`since` information](#the-since-argument). | sequence identifier or `now` | 0 | 
`style`        | Specifies how many revisions are returned in the changes array. The `main_only` style returns only the current "winning" revision. The `all_docs` style returns all leaf revisions, including conflicts and deleted former conflicts. | `main_only`, `all_docs` | `main_only` | 
`timeout`      | Number of milliseconds to wait for data before terminating the response. If the `heartbeat` setting is also supplied, it takes precedence over the `timeout` setting. | any positive number | |

>	**Note**: Using `include_docs=true` might have
	[performance implications](/docs/api/using_views.html#include_docs_caveat).

_Example request to get list of changes made to documents in a database, using HTTP:_

```
GET /$DATABASE/_changes HTTP/1.1
```
{:screen}

_Example request to get list of changes made to documents in a database, using the command line:_

```
curl https://$USERNAME.cloudant.com/$DATABASE/_changes \
     -u $USERNAME
```
{:screen}

_Example request to get list of changes made to documents in a database, using Javascript:_

```
var nano = require('nano');
var account = nano("https://"+$USERNAME+":"+$PASSWORD+"@"+$USERNAME+".cloudant.com");

account.db.changes($DATABASE, function (err, body, headers) {
	if (!err) {
		console.log(body);
	}
});
```
{:screen}

### Changes in a distributed database

The distributed nature of Cloudant databases,
and in particular the shard and fault-tolerant characteristics,
means that the response provided by the `_changes` request might be different
to the behavior you expect.

In particular,
if you ask for a list of changes `_since` a given sequence identifier,
you get the requested information in response,
_but_ you might also get changes that were made before the change indicated by the sequence identifier.
The reason for this,
along with implications for applications,
is explained in the
[replication guide](/docs/guides/replication_guide.html#how-does-replication-affect-the-list-of-changes?).

>	**Note**: It is essential that any application using the `_changes` request should be able to process correctly a list of changes that might:
	-	Have a different order for the changes listed in the response,
		when compared with an earlier request for the same information.
	-	Include changes that are considered to be prior to the change specified by the sequence identifier.

### The `feed` argument

The `feed` argument changes how Cloudant sends the response.
By default,
`_changes` reports all changes,
then the connection closes.
This is the same as using the `feed=normal` argument.

If you set `feed=longpoll`,
requests to the server remain open until changes are reported.
This can help monitor changes specifically instead of continuously.

<div id="continuous-feed"></div>

If you set `feed=continuous`,
new changes are reported without closing the connection.
This means that the database connection stays open until explicitly closed,
and that all changes are returned to the client as soon as possible after they occur.

Each line in the continuous response is either empty or a JSON object representing a single change.
This ensures that the format of the report entries reflects the continuous nature of the changes,
while maintaining validity of the JSON output.

_Example (abbreviated) responses from a continuous changes feed:_

```json
{
	"seq": "1-g1A...qyw",
	"id": "2documentation22d01513-c30f-417b-8c27-56b3c0de12ac",
	"changes": [
		{
			"rev": "1-967a00dff5e02add41819138abb3284d"
		}
	]
}
{
	"seq": "2-g1A...ssQ",
	"id": "1documentation22d01513-c30f-417b-8c27-56b3c0de12ac",
	"changes": [
		{
			"rev": "1-967a00dff5e02add41819138abb3284d"
		}
	]
}
{
	"seq": "3-g1A...qyy",
	"id": "1documentation22d01513-c30f-417b-8c27-56b3c0de12ac",
	"changes": [
		{
			"rev": "2-eec205a9d413992850a6e32678485900"
		}
	],
	"deleted": true
}
{
	"seq": "4-g1A...qyz",
	"id": "2documentation22d01513-c30f-417b-8c27-56b3c0de12ac",
	"changes": [
		{
			"rev": "2-eec205a9d413992850a6e32678485900"
		}
	],
	"deleted": true
}
```
{:screen}

### The `filter` argument

The `filter` argument designates a pre-defined
[filter function](/docs/api/design_documents.html#filter-functions) to apply to the changes feed.
Additionally, there is a built-in filter available:

-	`_design`: The `_design` filter accepts only changes to design documents.

### The `since` argument

The `since` argument enables you to get a list of changes that occurred _after_ a specified sequence identifier.
If the `since` identifier is 0 (the default),
or omitted,
the request returns all changes.
If the `since` identifier is `now`,
the request asks for changes made after the current time.

The distributed nature of Cloudant can affect the results you get in a response.
For example,
if you request a list of changes twice,
using the same `since` sequence identifier both times,
the order of changes in the resulting list might not be the same.

You might also see some results that appear to be from _before_ the `since` parameter.
The reason is that you might be getting results from a different replica of a shard (a shard replica).

Shard replicas automatically and continuously replicate to each other
and therefore eventually have the same data.
However,
at any given point in time,
a shard replica might differ from another shard replica
because the replication between them has not completed yet.

When you request a list of changes,
normally the same replicas are used to respond.
But if the node holding the shard replica is unavailable,
the system substitutes a corresponding shard replica held on another node.
To guarantee that you see all the applicable changes,
the most recent checkpoint between the replicas is used -
effectively 'rolling back' to the most recent point in time when the shard replicas were confirmed to be in agreement with each other.
This 'rolling back' means you might see changes listed that took place 'before' your `since` sequence identifier.

It is very important that your application is able to deal with a given change being reported more than once if you issue a `_changes` request several times.

More information about the behavior of the `_changes` response is
provided in the
[replication guide](/docs/guides/replication_guide.html#how-does-replication-affect-the-list-of-changes?).

<div id="changes_responses"></div>

### Responses from the `_changes` request

The response from a `_changes` request is a JSON object containing a list of the changes made to documents within the database.
The following table describes the meaning of the individual fields:

Field      | Description | Type
-----------|-------------|------
`changes`  | An array listing the changes made to the specific document. | Array
`deleted`  | Boolean indicating if the corresponding document was deleted. If present, it always has the value `true`. | Boolean
`id`       | Document identifier. | String
`last_seq` | Identifier of the last of the sequence identifiers. Currently this is the same as the sequence identifier of the last item in the `results`. | String
`results`  | Array of changes made to the database. | Array
`seq`      | Update sequence identifier. | String

_Example (abbreviated) response to a `_changes` request:_

```json
{
	"results": [
		{
			"seq": "1-g1A...sIg",
			"id": "foo",
			"changes": [
				{
					"rev": "1-967...84d"
				}
			]
		}
	],
	"last_seq": "1-g1A...sIg",
	"pending": 0
}
```
{:screen}

### Important notes about `_changes`

When using `_changes`,
you should be aware that:

-	The results returned by `_changes` are partially ordered.
	In other words,
	the order is not guaranteed to be preserved for multiple calls.
	You might decide to get a current list using `_changes` which includes the [`last_seq` value](#changes_responses),
	then use this as the starting point for subsequent `_changes` lists by providing the `since` query argument.
-	Although shard copies of the same range contain the same data,
	their `_changes` history is often unique.
	This is a result of how writes have been applied to the shard. For example,
	they might have been applied in a different order.
	To be sure all changes are reported for your specified sequence,
	it might be necessary to go further back into the shard's history to find a suitable starting point from which to start reporting the changes.
	This might give the appearance of duplicate updates,
	or updates that are apparently prior to the specified `since` value.
-	`_changes` reported by a given shard are always presented in order.
	But the ordering between all the contributing shards might appear to be different.
	For more information,
	see [this example](https://gist.github.com/smithsz/30fb97662c549061e581){:new_window}.
-	Sequence values are unique for a shard,
	but might vary between shards.
	This means that if you have sequence values from different shards,
	you cannot assume that the same sequence value refers to the same document within the different shards.

<div id="post"></div>

### Using `POST` to get changes

Instead of `GET`,
an alternative is to use `POST` to query the changes feed.
The only difference to the `GET` method is that parameters are specified in a JSON object in the request body.

_Example of `POST`ing to the `_changes` endpoint, using HTTP:_

```
POST /$DB/_changes HTTP/1.1
Host: $USERNAME.cloudant.com
Content-Type: application/json
```
{:screen}

_Example of `POST`ing to the `_changes` endpoint, using the command line:_

```
curl -X POST "https://$USERNAME.cloudant.com/$DB/_changes" -d @request.json
```
{:screen}

_Example of a JSON object `POST`ed to the `_changes` endpoint:_

```json
{
	"limit": 10
}
```
{:screen}

## Deleting a database

To delete a databases and its contents,
send a `DELETE` request to `https://$USERNAME.cloudant.com/$DATABASE`.

>	**Note**: There is no additional check to ensure that you really intended to delete the database ("Are you sure?").

_Example request to delete a Cloudant database, using HTTP:_

```
DELETE /$DATABASE HTTP/1.1
Host: $USERNAME.cloudant.com
```
{:screen}

_Example request to delete a Cloudant database, using the command line:_

```
curl https://$USERNAME.cloudant.com/$DATABASE \
	-X DELETE \
	-u $USERNAME
```
{:screen}

_Example request to delete a Cloudant database, using Javascript:_

```
var nano = require('nano');
var account = nano("https://"+$USERNAME+":"+$PASSWORD+"@"+$USERNAME+".cloudant.com");

account.db.destroy($DATABASE, function (err, body, headers) {
	if (!err) {
		console.log(body);
	}
});
```
{:screen}

The response confirms successful deletion of the database or describes any errors that occurred,
for example if you try to delete a database that does not exist.

_Example response:_

```json
{
	"ok": true
}
```
{:screen}

## Backing up your data

It is essential that you protect your data by taking good quality backups.
An overview of backing up your data is [available](/docs/api/backup.html),
with more detailed information in the [backup guide](/docs/guides/backup-guide.html).

## Using a different domain

Virtual hosts (vhosts) are a way to make Cloudant serve data from a different domain
than the one normally associated with your Cloudant account.

More information is available [here](/docs/api/vhosts.html).

## Creating database applications

In addition to data stored in documents within the database,
you could also have client-side application code - typically Javascript - in documents within the database.
Two-tier combinations of data and client code,
stored within a database,
are called [CouchApps](/docs/guides/couchapps.html).

More information about CouchApps,
and to help you decide whether they are a good match for your application,
is [available](/docs/guides/couchapps.html).
