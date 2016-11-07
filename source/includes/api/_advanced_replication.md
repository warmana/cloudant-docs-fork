## Advanced replication

This section contains details about more advanced replication concepts and tasks.

You might also find it helpful to review details of the
underlying [replication protocol](http://dataprotocols.org/couchdb-replication/),
as well as reviewing the [Advanced Methods](advanced.html) material.

### Replication Status

> Example replication document, `PUT` into `/_replicator`:

```json
{
  "_id": "my_rep",
  "source":  "https://username:password@myserver.com:5984/fromthis",
  "target":  "https://username:password@username.cloudant.com/tothat",
  "create_target":  true
}
```

> Example of automatic document update once replication starts:

```json
{
  "_id": "my_rep",
  "source":  "https://username:password@myserver.com:5984/fromthis",
  "target":  "https://username:password@username.cloudant.com/tothat",
  "create_target":  true,
  "_replication_id":  "c0ebe9256695ff083347cbf95f93e280",
  "_replication_state":  "triggered",
  "_replication_state_time":  "2011-06-07T16:54:35+01:00"
}
```

When replication is managed by storing a document in the `/_replicator` database,
the contents of the document are updated as the replication status changes.

In particular,
once replication starts,
three new fields are added automatically to the replication document.
The fields all have the prefix: `_replication_`

Field | Detail
------|-------
`_replication_id` | This is the internal ID assigned to the replication. It is the same ID that appears in the output from `/_active_tasks/`.
`_replication_state` | The current state of the replication. The possible states are:<dl><dt>`triggered`</dt><dd>The replication has started and is in progress.</dd><dt>`completed`</dt><dd>The replication completed successfully.</dd><dt>`error`</dt><dd>An error occurred during replication.</dd></dl>
`_replication_state_time` | An <a href="https://www.ietf.org/rfc/rfc3339.txt" target="_blank">RFC 3339</a> compliant timestamp that reports when the current replication state defined in `_replication_state` was set.

<div></div>

> Example replication document once replication has completed:

```json
{
  "_id": "my_rep",
  "source":  "https://username:password@myserver.com:5984/fromthis",
  "target":  "https://username:password@username.cloudant.com/tothat",
  "create_target":  true,
  "_replication_id":  "c0ebe9256695ff083347cbf95f93e280",
  "_replication_state":  "completed",
  "_replication_state_time":  "2011-06-07T16:56:21+01:00"
}
```

When the replication finishes,
it updates the `_replication_state` field with the value `completed`,
and the `_replication_state_time` field with the time that the completion status was recorded.

A continuous replication can never have a `completed` state.

### Authentication

> Example of specifying username and password values for accessing source and target databases during replication:

```json
{
  "source": "https://username:password@example.com/db", 
  "target": "https://username:password@username.cloudant.com/db"
}
```

In any production application,
security of the source and target databases is essential.
In order for replication to proceed,
authentication is necessary to access the databases.
In addition,
checkpoints for replication are [enabled by default](replication.html#checkpoints),
which means that replicating the source database requires write access.

To enable authentication during replication,
include a username and password in the database URL.
The replication process uses the supplied values for HTTP Basic Authentication.

### Filtered Replication

> Simple example of a filter function:

```
function(doc, req) {
  return !!(doc.type && doc.type == "foo");
}
```

Sometimes you do not want to transfer all documents from source to target.
To choose which documents to transfer,
include one or more filter functions in a design document on the source.
You can then tell the replicator to use these filter functions.

<aside role="complementary" aria-label="filtersimilartochanges">Filtering documents during replication is similar to the process of [filtering the `_changes` feed](design_documents.html#filter-functions).</aside>  

A filter function takes two arguments:

- The document to be replicated.
- The replication request.

A filter function returns a true or false value.
If the result is true, the document is replicated.

<div></div>

> Simple example of storing a filter function in a design document:

```json
{
  "_id": "_design/myddoc",
  "filters": {
    "myfilter": "function goes here"
  }
}
```

Filters are stored under the topmost `filters` key of the design document.

<div></div>

> Example JSON for invoking a filtered replication:

```json
{
  "source": "http://username:password@example.org/example-database",
  "target": "http://username:password@username.cloudant.com/example-database",
  "filter": "myddoc/myfilter"
}
```

Filters are invoked by using a JSON statement that identifies:

- The source database.
- The target database.
- The name of the filter stored under the `filters` key of the design document.

<div></div>

> Example JSON for invoking a filtered replication with supplied parameters:

```json
{
  "source": "http://username:password@example.org/example-database",
  "target": "http://username:password@username.cloudant.com/example-database",
  "filter": "myddoc/myfilter",
  "query_params": {
    "key": "value"
  }
}
```

Arguments can be supplied to the filter function by including 'key:value'
pairs in the `query_params` field of the invocation.

### Named Document Replication

> Example replication of specific documents:

```json
{
  "source": "http://username:password@example.org/example-database",
  "target": "http://username:password@127.0.0.1:5984/example-database",
  "doc_ids": ["foo", "bar", "baz"]
}
```

Sometimes you only want to replicate some documents.
For this simple case,
you do not need to write a filter function.
To replicate specific documents,
add the list of keys as an array in the `doc_ids` field.

### Replicating through a proxy

> Example showing replication through a proxy:

```json
{
  "source": "http://username:password@username.cloudant.com/example-database",
  "target": "http://username:password@example.org/example-database",
  "proxy": "http://my-proxy.com:8888"
}
```

If you want replication to pass through an HTTP proxy,
provide the proxy details in the `proxy` field of the replication data.

### The `user_ctx` property and delegations

> Example delegated replication document:

```json
{
  "_id": "my_rep",
  "source":  "https://username:password@myserver.com:5984/foo",
  "target":  "https://username:password@username.cloudant.com/bar",
  "continuous":  true,
  "user_ctx": {
    "name": "joe",
    "roles": ["erlanger", "researcher"]
  }
}
```

Replication documents can have a custom `user_ctx` property.
This property defines the user context under which a replication runs.
For the old way of triggering replications (`POST`ing to `/_replicate/`),
this property was not needed (it didn't exist in fact).
This is because at the moment of triggering the replication,
it has information about the authenticated user.

With the replicator database,
since it's a regular database,
the information about the authenticated user is only present
at the moment the replication document is written to the database.
The replicator database implementation is like a `_changes` feed consumer with `?include_docs=true`;
it reacts to what was written to the replicator database.
Indeed,
this feature could be approximated with an external script program.

This implementation detail implies that for non admin users,
a `user_ctx` property,
containing the user's name and a subset of their roles,
_must_ be defined in the replication document.
This is enforced by the document update validation function
present in the default design document of the replicator database.
The validation function also ensures that a non admin user
can set a user name property in the `user_ctx` property
that does not match their own name.
The same principle also applies for user roles.

For admins, the `user_ctx` property is optional.
If the property is missing,
the value defaults to a user context with name `null`,
and an empty list of roles.
This means design documents will not be written to local targets.
If writing design documents to local targets is desired,
then a user context with the role `_admin` must be set explicitly.

Also,
admins can use the `user_ctx` property to trigger a replication on behalf of another user.
The `user_ctx` value is the user context that is passed
to local target database document validation functions.

<aside class="warning" role="complementary" aria-label="ctxonlylocal">The `user_ctx` property only has an effect for local endpoints.</aside>

For admins,
the `user_ctx` property is optional.
For regular non-admin users,
the property is mandatory.
When the roles property of `user_ctx` is missing,
it defaults to the empty list `[ ]`.

### Performance related options

> Example of including performance options in a replication document:

```json
{
  "source": "https://username:password@example.com/example-database",
  "target": "https://username:password@example.org/example-database",
  "connection_timeout": 60000,
  "retries_per_request": 20,
  "http_connections": 30
}
```

These options can be set for a replication by including them in the replication document.

-   `worker_processes` - The number of processes the replicator uses (per replication) to transfer documents from the source to the target database. Higher values can imply better throughput (due to more parallelism of network and disk IO) at the expense of more memory and eventually CPU. Default value is 4.
-   `worker_batch_size` - Workers process batches with the size defined by this parameter (the size corresponds to number of `_changes` feed rows). Larger values for the batch size might result in better performance. Smaller values mean that checkpointing is done more frequently. Default value is 500.
-   `http_connections` - The maximum number of HTTP connections per replication. For push replications, the effective number of HTTP connections used is `min(worker_processes + 1, http_connections)`. For pull replications, the effective number of connections used corresponds to this parameter's value. Default value is 20.
-   `connection_timeout` - The maximum period of inactivity for a connection in milliseconds. If a connection is idle for this period of time, its current request will be retried. Default value is 30000 milliseconds (30 seconds).
-   `retries_per_request` - The maximum number of retries per request. Before a retry, the replicator will wait for a short period of time before repeating the request. This period of time doubles between each consecutive retry attempt. This period of time never goes beyond 5 minutes and its minimum value (before the first retry is attempted) is 0.25 seconds. The default value of this parameter is 10 attempts.
-   `socket_options` - A list of options to pass to the connection sockets. The available options can be found in the [documentation for the Erlang function `setopts` of the inet module](http://www.erlang.org/doc/man/inet.html#setopts-2). Default value is `[{keepalive, true}, {nodelay, false}]`.

### Attachments

Having large numbers of attachments on documents might cause an adverse effect on replication performance.

For more information about the effect of attachments on replication performance,
see [here](attachments.html#performance-considerations).

### The replication scheduler

Replication tasks within a distributed system are clearly extremely important,
to ensure that required information is communicated between the components
correctly and as quickly as possible.
Management of the replication activities requires a scheduler.
The scheduler helps organize what replication tasks take place, and when.

Information about the replication status is available
using the [`_active_tasks` endpoint](managing_tasks.html).

More detailed information about replication tasks is available
by issuing requests directly to one of two scheduler endpoints:

-	[`_scheduler/docs`](advanced_replication.html#the-_scheduler/docs-endpoint)
-	[`_scheduler/jobs`](advanced_replication.html#the-_scheduler/jobs-endpoint)

#### The `_scheduler/docs` endpoint

> Example request for a simple list of replication documents:

```http
GET /_scheduler/docs HTTP/1.1
HOST: $ACCOUNT.cloudant.com
```

```shell
curl https://$ACCOUNT.cloudant.com/_scheduler/docs
```

> Example response, listing replication documents:

```json
{
    "offset": 0,
    "docs": [
        {
            "doc_id": "840b6b3a464a2a1134bb18184e10331f",
            "database": "yehudit/_replicator",
            "id": "590e3fb6cc21b0ee2176d337a2b1296e",
            "node": "dbcore@db1.bigblue.cloudant.net",
            "source": "https://yehudit.cloudant.com/dw_storageref/",
            "target": "https://aeperf:*****@aeperf.cloudant.com/perf_storageref/",
            "state": "crashing",
            "info": "db_not_found: could not open https://aeperf:*****@aeperf.cloudant.com/perf_storageref/",
            "error_count": 10
        },
        {
          # ... Another doc, same structure as above
        },
          # ... Etc... Default limit is 100
    ],
    "total": 1647
}
```

The `_scheduler/docs` endpoint returns the set of replication documents that are driving the replication activity.

<div></div>

> Example request for the first replication document after the initial 100 replication documents:

```http
GET /_scheduler/docs?limit=1&skip=100 HTTP/1.1
HOST: $ACCOUNT.cloudant.com
```

```shell
curl https://$ACCOUNT.cloudant.com/_scheduler/docs?limit=1&skip=100
```

> Example response, listing replication documents:

```json
{
    "offset": 100,
    "docs": [
        {
            "doc_id": "layoutdb1003123_databackup_replicator",
            "database": "eng-ci-qa-backup/_replicator",
            "id": "10a57dc93948ba318b02dd09e21bc122+continuous",
            "node": "dbcore@db1.bigblue.cloudant.net",
            "source": "https://omentooditillesesideplar:*****@eng-ci-qa-backup.cloudant.com/layoutdb1003123/",
            "target": "https://distichatheelledientseak:*****@eng-ci-qa.cloudant.com/layoutdb1003123/",
            "state": "running",
            "info": null,
            "error_count": 0
        }
    ],
    "total": 1647
}
```

The endpoint accepts three optional parameters:

Parameter | Definition
----------|-----------
`limit`   | The maximum number of replication documents returned in response to the request. Defaults to 100.
`skip`    | The number of replication documents to 'skip' (or offset) before being included in the response. Used in conjunction with the `limit` option, the `skip` option enables you to 'page' through a large collection of replication documents. Defaults to 0.
`state`   | Include the replication document in the response list if its current state matches one of those provided by the `state` parameter. Possible values include: `completed`, `crashing`, `error`, `failed`, `pending`, and `running`. Default is to include the replication document regardless of its current state.

<div></div>

> Example request for the first two replication documents after the initial 10 replication documents, all of which are either in an `error` or `crashing` state:

```http
GET /_scheduler/docs?limit=2&skip=10&states=error,crashing HTTP/1.1
HOST: $ACCOUNT.cloudant.com
```

```shell
curl https://$ACCOUNT.cloudant.com/_scheduler/docs?limit=2&skip=10&states=error,crashing
```

> Example response, listing replication documents:

```json
{
    "offset": 10,
    "docs": [
        {
            "doc_id": "b293087944134fa68b54ebac6f4a2a6d",
            "database": "ricellis/_replicator",
            "id": null,
            "state": "error",
            "info": "Could not open source database `https://ricellis:*****@ricellis.cloudant.com:443/com_cloudant_tests_replicatortest-replication_filteredwithqueryparams-4f2620fc49e34152af990aff8bb2e0f4/`: {db_not_found,<<\"https://ricellis:*****@ricellis.cloudant.com:443/com_cloudant_tests_replicatortest-replication_filteredwithqueryparams-4f2620fc49e34152af990aff8bb2e0f4/\">>}",
            "error_count": 12,
            "node": "dbcore@db1.bigblue.cloudant.net"
        },
        {
            "doc_id": "3fdecb279195401196d79e80c7197cb2",
            "database": "ricellis/_replicator",
            "id": "a705679767500a66abfe8d58528af03d+create_target",
            "node": "dbcore@db1.bigblue.cloudant.net",
            "source": "https://ricellis:*****@ricellis.cloudant.com:443/com_cloudant_tests_replicatortest-replication-9737ea7d388144769d40a7fe05e1c8e7/",
            "target": "https://ricellis:*****@ricellis.cloudant.com:443/com_cloudant_tests_replicatortest-replication-a64264bd649e40b8a644a43bc97e1cea/",
            "state": "crashing",
            "info": "db_not_found: could not open https://ricellis:*****@ricellis.cloudant.com:443/com_cloudant_tests_replicatortest-replication-9737ea7d388144769d40a7fe05e1c8e7/",
            "error_count": 10
        }
    ],
    "total": 497
}
```

<div></div>

#### The `_scheduler/jobs` endpoint

The `_scheduler/jobs` endpoint returns the current scheduling state of
replication tasks that are in an active state,
in other words tasks that are not in a terminal condition of `completed` or `failed`.
More information about replication task state is available in the
[replication guide](replication_guide.html#replication-status).

Jobs that are technically runnable but are erroring or crashing in some way get an exponential backoff.
The scheduling history of any given job is recorded in a history array,
which has a default length of 20 entries.

The endpoint accepts two optional parameters:

Parameter | Definition
----------|-----------
`limit`   | The maximum number of replication tasks returned in response to the request. Defaults to 25.
`skip`    | The number of replication tasks to 'skip' (or offset) before being included in the response. Used in conjunction with the `limit` option, the `skip` option enables you to 'page' through a large collection of replication tasks. Defaults to 0.

<div></div>

> Example request for the second and third of the first three replication tasks:

```http
GET /_scheduler/jobs?limit=2&skip=1 HTTP/1.1
HOST: $ACCOUNT.cloudant.com
```

```shell
curl https://$ACCOUNT.cloudant.com/_scheduler/jobs?limit=2&skip=1
```

> Example response, listing replication tasks:

```json
{
    "total": 760,
    "offset": 1,
    "jobs": [
        {
            "id": "00443684e65dc00168e1ec083eab4b61+continuous",
            "pid": "<0.14686.10>",
            "source": "https://distichatheelledientseak:*****@eng-ci-qa.cloudant.com/widget_registry_1003123/",
            "target": "https://omentooditillesesideplar:*****@eng-ci-qa-backup.cloudant.com/widget_registry_1003123/",
            "database": "shards/40000000-7fffffff/eng-ci-qa/_replicator.1473966838",
            "user": null,
            "doc_id": "widget_registry_1003123_databackup_replicator",
            "history": [
                {
                    "timestamp": "2016-10-15T00-18-27.542892Z",
                    "type": "started"
                },
                {
                    "timestamp": "2016-10-15T00-18-27.539875Z",
                    "type": "added"
                }
            ],
            "node": "dbcore@db5.bigblue.cloudant.net"
        },
        {
            "id": "0045628678071ac26a844d1b3404b23e",
            "pid": null,
            "source": "https://aebuild.cloudant.com/test_ci_dw_storageref/",
            "target": "https://arbuild:*****@puhirema.cloudant.com/b_dw_storageref/",
            "database": "shards/80000000-bfffffff/aebuild/_replicator.1462459910",
            "user": "aebuild",
            "doc_id": "a39378cc27574bfa7c9faf8fdf03f4d7",
            "history": [
                {
                    "timestamp": "2016-10-17T07-42-33.74368Z",
                    "type": "crashed",
                    "reason": "unauthorized: unauthorized to access or create database https://arbuild:*****@puhirema.cloudant.com/b_dw_storageref/"
                },
                {
                    "timestamp": "2016-10-17T07-42-32.492205Z",
                    "type": "started"
                },
                {
                    "timestamp": "2016-10-17T03-26-30.873958Z",
                    "type": "crashed",
                    "reason": "unauthorized: unauthorized to access or create database https://arbuild:*****@puhirema.cloudant.com/b_dw_storageref/"
                },
                {
                    "timestamp": "2016-10-17T03-26-30.465005Z",
                    "type": "started"
                },
                {
                    "timestamp": "2016-10-16T23-10-28.809024Z",
                    "type": "crashed",
                    "reason": "unauthorized: unauthorized to access or create database https://arbuild:*****@puhirema.cloudant.com/b_dw_storageref/"
                },
                {
                    "timestamp": "2016-10-16T23-10-28.429145Z",
                    "type": "started"
                },
                {
                    "timestamp": "2016-10-16T18-54-26.789244Z",
                    "type": "crashed",
                    "reason": "unauthorized: unauthorized to access or create database https://arbuild:*****@puhirema.cloudant.com/b_dw_storageref/"
                },
                {
                    "timestamp": "2016-10-16T18-54-26.417864Z",
                    "type": "started"
                },
                {
                    "timestamp": "2016-10-16T14-38-24.734541Z",
                    "type": "crashed",
                    "reason": "unauthorized: unauthorized to access or create database https://arbuild:*****@puhirema.cloudant.com/b_dw_storageref/"
                },
                {
                    "timestamp": "2016-10-16T14-38-24.385768Z",
                    "type": "started"
                },
                {
                    "timestamp": "2016-10-16T10-22-22.807824Z",
                    "type": "crashed",
                    "reason": "unauthorized: unauthorized to access or create database https://arbuild:*****@puhirema.cloudant.com/b_dw_storageref/"
                },
                {
                    "timestamp": "2016-10-16T10-22-22.369072Z",
                    "type": "started"
                },
                {
                    "timestamp": "2016-10-16T06-06-21.702519Z",
                    "type": "crashed",
                    "reason": "unauthorized: unauthorized to access or create database https://arbuild:*****@puhirema.cloudant.com/b_dw_storageref/"
                },
                {
                    "timestamp": "2016-10-16T06-06-20.323982Z",
                    "type": "started"
                },
                {
                    "timestamp": "2016-10-16T01-50-18.707950Z",
                    "type": "crashed",
                    "reason": "unauthorized: unauthorized to access or create database https://arbuild:*****@puhirema.cloudant.com/b_dw_storageref/"
                },
                {
                    "timestamp": "2016-10-16T01-50-18.336168Z",
                    "type": "started"
                },
                {
                    "timestamp": "2016-10-15T21-34-16.489545Z",
                    "type": "crashed",
                    "reason": "unauthorized: unauthorized to access or create database https://arbuild:*****@puhirema.cloudant.com/b_dw_storageref/"
                },
                {
                    "timestamp": "2016-10-15T21-34-16.94108Z",
                    "type": "started"
                },
                {
                    "timestamp": "2016-10-15T17-18-14.456592Z",
                    "type": "crashed",
                    "reason": "unauthorized: unauthorized to access or create database https://arbuild:*****@puhirema.cloudant.com/b_dw_storageref/"
                },
                {
                    "timestamp": "2016-10-15T17-18-14.52615Z",
                    "type": "started"
                }
            ],
            "node": "dbcore@db2.bigblue.cloudant.net"
        }
    ]
}
```
