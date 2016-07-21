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

### Conflicts

While revisions offer considerable benefits in terms of performance and reliability,
particularly in a distributed database,
they can also permit situations where changes made to a document stored in one
location might not instantly be reflected in other parts of the replicated database.

In other words,
if independent updates are made to other revisions of documents,
the effect might be to introduce disagreement or 'conflicts' as to what is the correct,
definitive content for the document.

Conflicts are a well-understood characteristic of MVCC systems.
A separate [guide](conflicts.html) is available for helping you deal with conflicts.
