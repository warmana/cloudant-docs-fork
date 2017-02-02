## Managing tasks

Creating new indexes over lots of data or replicating a large database can take quite a while. So how can you see whether your tasks are making progress, or if they have completed? The `_active_tasks` endpoint provides information about all ongoing tasks. However, if you start a lot of tasks, some of them might be scheduled to run later and do not show up under `_active_tasks` until they have been started.

This guide tells you how to use the `_active_tasks` endpoint to monitor long-running tasks.
The `curl` command is used to access the endpoint.
The `jq` command-line JSON processor is used to process the JSON response.

Since this is a task-focused tutorial, it covers only what is essential to accomplish this task. Please refer to the [API reference](api.html#-api-reference) for a complete guide to the available options.

### curl and jq basics

> Obtaining and formatting a list of active tasks:

```
curl 'https://username:password@username.cloudant.com/_active_tasks' | jq '.'
```

To get all active tasks and format the output nicely, call your account using `curl`,
and pipe the output to `jq`.

`jq` lets you filter a list of documents by their field values.
This makes it easier to get all replication documents, or the details of just one particular view indexing task. The [API reference](api.html#-api-reference) has more information about the options.

### Monitoring view builds and search indexes

> Finding all view indexing tasks, by filtering for the `indexer` type:

```
curl -s 'https://username:password@username.cloudant.com/_active_tasks' | jq '.[] | select(.type=="indexer")'
```

> Finding all search indexing tasks, by filtering for the `search_indexer` type:

```
curl -s 'https://username:password@username.cloudant.com/_active_tasks' | jq '.[] | select(.type=="search_indexer")'
```

> Sample result after searching for view indexing tasks:

```json
{
  "total_changes": 6435,
  "started_on": 1371118332,
  "user": "username",
  "updated_on": 1371118334,
  "type": "indexer",
  "node": "dbcore@db6.meritage.cloudant.net",
  "pid": "<0.16366.6103>",
  "changes_done": 364,
  "database": "shards/40000000-7fffffff/username/database",
  "design_document": "_design/ngrams"
 }
```

View indexes are rebuilt when a design document is updated. An update to any one of the views causes all the views in the document to be rebuilt.

Search indexes are rebuilt only when their corresponding index function is changed. For each search index that is being built and for each design document with views that are changed, a new task is created for each replica of each shard in a cluster. For example, if there are 24 shards, with three replicas each, and you update two search indexes, then 24 x 3 x 2 = 144 tasks are run.

To find all the view indexing tasks, pipe the `curl` output to `jq`, and let it filter the documents in the array by their type field. 
A corresponding command works for search indexing tasks.

In each case, the results of searching for a list of indexing tasks is a list of JSON objects: one for each of the active tasks found.

### Estimating the time to complete a task

> Extracting the `changes_done` field using `jq`:

```
curl ... | jq '.[] | select(.type=="search_indexer") | .changes_done'
```

To estimate the time needed until the indexing task is complete, monitor the number of `changes_done` and compare this value to `total_changes`. For instance, if `changes_done` increases by 250 per second and `total_changes` is 1,000,000, the task is expected to take 4,000 seconds, or about 66 minutes, to complete.

<aside class="warning" role="complementary" aria-label="estimates">Estimates of the time to complete an indexing task cannot be 100% accurate. The actual time to complete the task depends on several factors, including:

- The time it takes to process each document. For instance, a view might check the type of a document first, and only emit new index entries for one type.
- The size of the documents.
- The current workload on the cluster.

You should assume that these factors might combine to produce considerable inaccuracy in your estimate.</aside>

### Monitoring replication

> Finding all replication tasks, by filtering for the `replication` type:

```
curl -s 'https://username:password@username.cloudant.com/_active_tasks' | jq '.[] | select(.type=="replication")'
```

> Finding a specific replication task, by filtering for a known document identity:

```
curl ... | jq '.[] | select(.doc_id=="ID")'
```

> Finding a specific replication task, by filtering for a known `replication_id`:

```
curl ... | jq '.[] | select(.replication_id=="ID")'
```

> Sample result after searching for a replication task:

``` json
{
  "started_on": 1371094220,
  "source_seq": "62960-sakdjflksdfjsdlkafjalskdfjlsakfjlasdkjksald",
  "source": "",
  "revisions_checked": 12,
  "continuous": true,
  "doc_id": null,
  "doc_write_failures": 0,
  "docs_read": 12,
  "target": "",
  "type": "replication",
  "updated_on": 1371118477,
  "user": "username",
  "checkpointed_source_seq": "61764-dskfjalsfjsalkfjssadjfhasdfkjhsdkfhsdkf",
  "changes_pending": 1196,
  "pid": "<0.9955.4120>",
  "node": "dbcore@db7.meritage.cloudant.net",
  "docs_written": 12,
  "missing_revisions_found": 12,
  "replication_id": "asfksdlfkjsadkfjsdalkfjas+continuous+create_target"
}
```

To find all replication tasks, pipe the `curl` output to `jq`, and filter the documents in the array by their type field.

To make it easier to select the information about a replication process from the list of active tasks,
start the replication process by creating a document in the `_replicator` database, and set its `_id` field to a known value.

### Troubleshooting

#### Is a task stuck?

For a one-off, non-continuous replication, where the source database is not updated significantly during the replication, the `changes_pending` value tells you how many documents remain to be processed.
This means that the `changes_pending` value is good indicator of when the replication is likely to be finished.

For a continuous replication, you are more interested in how the number of documents processed changes over time, and whether the `changes_pending` value increases.
If `changes_pending` increases, but `revisions_checked` stays constant for a while, the replication is probably stalled.
If `changes_pending` increases, and `revisions_checked` also increases, this might indicate that the replication cannot keep up with the volume of data added to, or updated in, the database.

#### What to do about a stuck task?

To resolve a stalled replication, you might have to cancel the replication process and start it again.

If that does not help, the replication might be stalled because the user accessing the source or target databases does not have write permissions.

<aside class="notice" role="complementary" aria-label="checkpoints">Replication makes use of checkpoints. This means that content already replicated and unchanged does not have to be replicated again if the replication is restarted.</aside>

If you created the replication process by creating a document in the `_replicator` database, you can also check the status of the replication there.
