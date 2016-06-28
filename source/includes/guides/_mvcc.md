## Document Versioning and MVCC

Multi-version concurrency control (MVCC) is how Cloudant databases ensure that all of the nodes in a database's cluster contain only the [newest version](document.html) of a document.
Since Cloudant databases are [eventually consistent](cap_theorem.html),
this is necessary to prevent inconsistencies arising between nodes as a result of synchronizing between outdated documents.

Multi-Version Concurrency Control (MVCC) enables concurrent read and write access to a Cloudant database.
MVCC is a form of [optimistic concurrency](http://en.wikipedia.org/wiki/Optimistic_concurrency_control).
It makes both read and write operations on Cloudant databases faster because there is no need for database locking on either read or write operations.
MVCC also enables synchronization between Cloudant database nodes.

### Revisions

Every document in a Cloudant database has a `_rev` field indicating its revision number.

A revision number is added to your documents by the server when you insert or modify them.
The number is included in the server response when you make changes or read a document.
The `_rev` value is constructed using a combination of a simple counter and a hash of the document.

The two main uses of the revision number are to help:

1.	Determine what documents must be replicated between servers.
2.	Confirm that a client is trying to modify the latest version of a document.

You must specify the previous `_rev` when [updating a document](document.html#update) or else your request will fail and return a [409 error](http.html#409).

<aside class="warning" role="complementary" aria-label="revnotVCS">`_rev` should not be used to build a version control system.
The reason is that it is an internal value used by the server.
In addition,
older revisions of a document are transient,
and therefore removed regularly.</aside>

You can query a particular revision using its `_rev`,
however,
older revisions are regularly deleted by a process called [compaction](http://en.wikipedia.org/wiki/Data_compaction).
A consequence of compaction is that you cannot rely on a successful response when querying a particular document revision using its `_rev` to obtain a history of revisions to your document.
If you need a version history of your documents,
a solution is to [create a new document](document.html#documentCreate) for each revision.

### Distributed Databases and Conflicts

Distributed databases work do not require a constant connection to a 'main' database.
This means that changes made to a document might not instantly update or replicate to other parts of the replicated database.
If other,
independent,
updates are made to those older versions of documents,
the effect might be to introduce disagreement or 'conflicts' as to the correct,
definitive content for the document.

<div></div>

#### Finding conflicts

To find conflicts,
add the query parameter `conflicts=true` when retrieving a document.
When returned,
the resulting document contains a `_conflicts` array,
which includes a list of all the conflicting revisions.

<div></div>

> Example map function to find document conflicts:

```
function (doc) {
  if (doc._conflicts) {
    emit(null, [doc._rev].concat(doc._conflicts));
  }
}
```

To find conflicts for multiple documents in a database,
write a [view](creating_views.html).
An example map function is provided,
that emits all revisions for every document with a conflict.

When you have such a view,
you can regularly query this view and resolve conflicts as needed.
Alternatively,
you might query the view after each replication to identify and resolve conflicts immediately.

### How to resolve conflicts

Once you've found a conflict, you can resolve it by following 4 steps:

1.	[Get](mvcc.html#get-conflicting-revisions) the conflicting revisions.
2.	[Merge](mvcc.html#merge-the-changes) them in your application or ask the user what he wants to do.
3.	[Upload](mvcc.html#upload-the-new-revision) the new revision.
4.	[Delete](mvcc.html#delete-old-revisions) old revisions.

<div></div>

> Example first version of the document.

```json
{
  "_id": "74b2be56045bed0c8c9d24b939000dbe",
  "_rev": "1-7438df87b632b312c53a08361a7c3299",
  "name": "Samsung Galaxy S4",
  "description": "",
  "price": 650
}
```

Let's consider an example of how this can be done.
Suppose you have a database of products for an online shop.
The first version of a document might look like the example provided.

<div></div>

> Second version (first revision) of the document, adding a description.

```json
{
  "_id": "74b2be56045bed0c8c9d24b939000dbe",
  "_rev": "2-61ae00e029d4f5edd2981841243ded13",
  "name": "Samsung Galaxy S4",
  "description": "Latest smartphone from Samsung",
  "price": 650
}
```

The document doesn't have a description yet,
so someone might add one.

<div></div>

> _Alternative_ second version, introducing a price reduction data change that conflicts with the addition of a description.

```json
{
  "_id": "74b2be56045bed0c8c9d24b939000dbe",
  "_rev": "2-f796915a291b37254f6df8f6f3389121",
  "name": "Samsung Galaxy S4",
  "description": "",
  "price": 600
}
```

At the same time, someone else - working with a replicated database - reduces the price.

<div></div>

When the two databases are replicated,
it is not clear which of the two alternative versions of the document is correct,
leading to a conflict.

#### Get conflicting revisions

To find the conflicting revisions for a document,
retrieve the document,
including the `conflicts=true` parameter,
similar to the following example:

`http://$USERNAME.cloudant.com/products/$_ID?conflicts=true`

<div></div>

> Example response to document retrieval, showing conflicting revisions

```json
{
  "_id":"74b2be56045bed0c8c9d24b939000dbe",
  "_rev":"2-f796915a291b37254f6df8f6f3389121",
  "name":"Samsung Galaxy S4",
  "description":"",
  "price":600,
  "_conflicts":["2-61ae00e029d4f5edd2981841243ded13"]
}
```

If the document has any conflicts,
you would get a response similar to the example provided,
which is based on the changed description or changed price problem.

The version with the changed price has been chosen _arbitrarily_ as the latest version of the document.
You should not assume that the most recently updated version of the document is considered to be the latest version for conflict resolution purposes.

In this example,
a conflict is considered to exist between the retrieved document which has the `_rev` value `2-f796915a291b37254f6df8f6f3389121`,
and another document which has the `_rev` value `2-61ae00e029d4f5edd2981841243ded13`.
The conflicting document details are noted in the `_conflicts` array.

Often,
you might find that the array has only one element,
but it is possible for there to be many conflicting revisions,
each of which is listed in the array.

#### Merge the changes

Your application must identify all the potential changes,
and reconcile them,
effectively merging the correct and valid updates to produce a single,
non-conflicting version of the document.

To compare the revisions and identify what has been changed,
your application must retrieve all of the versions from the database.
This is done by issuing requests similar to the following:

*	`http://$USERNAME.cloudant.com/products/$_ID?conflicts=true`
*	`http://$USERNAME.cloudant.com/products/$_ID?rev=2-61ae00e029d4f5edd2981841243ded13`
*	`http://$USERNAME.cloudant.com/products/$_ID?rev=1-7438df87b632b312c53a08361a7c3299`

The first document retrieval also requests the `_conflicts` array.
This gives us a current version of the document,
_and_ a list of all the other conflicting documents that must also be retrieved,
for example `...rev=2-61ae00e029d4f5edd2981841243ded13` and `...rev=1-7438df87b632b312c53a08361a7c3299`.
Each of these other conflicting versions is also retrieved.

Once you have all of the conflicting revisions of a document available,
you can proceed to resolve the conflicts.

In our example,
the differences between the versions of the document were for different fields within the document,
making it easier to merge them.

More complicated conflicts are likely to require correspondingly more analysis.
To help,
you might choose from a variety of different conflict resolution strategies,
such as:

*	Time based: using a simple test of the first or most recent edit.
*	User assessment: the conflicts are reported to users, who then decide on the best resolution.
*	Sophisticated merging algorithms: these are often used in [version control systems](https://en.wikipedia.org/wiki/Merge_%28version_control%29). An example is the [3-way merge](https://en.wikipedia.org/wiki/Merge_%28version_control%29#Three-way_merge).

For a practical example of how to implement these changes, see [this project with sample code](https://github.com/glynnbird/deconflict).

<div></div>

#### Upload the new revision

> Final revision, after resolving and merging changes from the previous conflicting revisions.

```json
{
  "_id": "74b2be56045bed0c8c9d24b939000dbe",
  "_rev": "3-daaecd7213301a1ad5493186d6916755",
  "name": "Samsung Galaxy S4",
  "description": "Latest smartphone from Samsung",
  "price": 600
}
```

After assessing and resolving the conflicts,
you create a document containing the current and definitive data.
This fresh document is uploaded into the database.

<div></div>

#### Delete old revisions

> Example requests to delete the old revisions.

```http
DELETE http://$USERNAME.cloudant.com/products/$_ID?rev=2-61ae00e029d4f5edd2981841243ded13

DELETE http://$USERNAME.cloudant.com/products/$_ID?rev=2-f796915a291b37254f6df8f6f3389121
```

The final step is where you delete the old revisions.
You do this by sending a `DELETE` request,
specifying the revisions to delete.

When the older versions of a document are deleted,
the conflicts associated with that document are marked as resolved.
You can verify that no conflicts remain by requesting the document again,
with the `conflicts` parameter set to true,
[as before](mvcc.html#finding-conflicts).
