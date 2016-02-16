# Meteor

<a href="https://atmospherejs.com/cloudant/couchdb">cloudant:couchdb</a> is the official Cloudant library for the couchdb-meteor package. Since Apache CouchDB does not ship with Meteor or the couchdb package, you must provide a URL for Meteor to connect to and a running CouchDB or Cloudant server instance before you install Meteor. Add this package to your Meteor application:

`meteor add cloudant:couchdb`

The couchdb-meteor package provides:

+ Livequery implementation and real-time updates from the database by consuming the CouchDB `_changes` feed
+ Distributed Data Protocol (DDP) RPC endpoints that update data from clients connected locally
+ Serialization and deserialization of updates to the DDP format


**Note**: The JSON query syntax used by Cloudant Query, and initially developed by Cloudant, was contributed back to Apache CouchDB for version 2.0. Prebuilt binaries for Apache CouchDB version 2.0 are not yet available. You can use this module with Cloudant DBaaS or Cloudant Local until the prebuilt binaries are available.


To configure the Apache CouchDB or Cloudant server connection information, pass its URL as the COUCHDB_URL environment variable to the Meteor server process.

`$export COUCHDB_URL=https://username:password@username.cloudant.com`

See [API Reference](api.html) for more information about meteor-couchdb APIs. ### Couchdb

<a href="https://atmospherejs.com/cloudant/couchdb">cloudant:couchdb</a> is the official Cloudant library for the couchdb-meteor package. Since Apache CouchDB does not ship with Meteor or the couchdb package, you must provide a URL for Meteor to connect to and a running CouchDB or Cloudant server instance before you install Meteor. Add this package to your Meteor application:

`meteor add cloudant:couchdb`

The couchdb-meteor package provides:

+ Livequery implementation and real-time updates from the database by consuming the CouchDB `_changes` feed
+ Distributed Data Protocol (DDP) RPC endpoints that update data from clients connected locally
+ Serialization and deserialization of updates to the DDP format


**Note**: The JSON query syntax used by Cloudant Query, and initially developed by Cloudant, was contributed back to Apache CouchDB for version 2.0. Prebuilt binaries for Apache CouchDB version 2.0 are not yet available. You can use this module with Cloudant DBaaS or Cloudant Local until the prebuilt binaries are available.


To configure the Apache CouchDB or Cloudant server connection information, pass its URL as the COUCHDB_URL environment variable to the Meteor server process.

`$export COUCHDB_URL=https://username:password@username.cloudant.com`

See [API Reference](api.html) for more information about meteor-couchdb APIs. 
