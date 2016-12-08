---

copyright:
  years: 2015, 2016
lastupdated: "2016-12-08"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}

# Third-party client libraries

>   **Note**: Third-party client libraries are not maintained or supported by Cloudant.

## Third-party Mobile libraries

Working with a Cloudant database:

-   [IBM Worklight Powered Native Objective-C iOS Apps](http://www.tricedesigns.com/2014/11/17/ibm-worklight-powered-native-objective-c-ios-apps/){:new_window} with a Cloudant Adapter.

## C# / .NET

[MyCouch](https://github.com/danielwertheim/mycouch){:new_window}
is an asynchronous CouchDB and Cloudant client for .Net.

To install the library,
open up the Package manager console,
and invoke:

```
install-package mycouch.cloudant
```
{:screen}

### Libraries and Frameworks

-   [MyCouch](https://github.com/danielwertheim/mycouch){:new_window}.
-   [LoveSeat](https://github.com/soitgoes/LoveSeat){:new_window}.
-   [Divan](https://github.com/foretagsplatsen/Divan){:new_window}.
-   [Relax](https://github.com/arobson/Relax){:new_window}.
-   [Hammock](http://code.google.com/p/relax-net/){:new_window}.
-   [EasyCouchDB](https://github.com/hhariri/EasyCouchDB){:new_window}.
-   `WDK.API.CouchDB` from [Kanapes IDE](http://kanapeside.com/){:new_window}.

### Examples and Tutorials

-   [CRUD](https://github.com/cloudant/haengematte/tree/master/c%23){:new_window}.

## PHP

[Sag](https://github.com/sbisbee/sag){:new_window} is PHP's CouchDB and Cloudant client.
[Sag.js](https://github.com/sbisbee/sag-js){:new_window} is Sag's JavaScript counterpart.

To install,
download `sag` from [https://github.com/sbisbee/sag](https://github.com/sbisbee/sag){:new_window},
then include the library in your application:

```
require_once('./src/Sag.php');
```
{:screen}

### Libraries and Frameworks

-   [sag](https://github.com/sbisbee/sag){:new_window}.
-   [Doctrine CouchDB Client](https://github.com/doctrine/couchdb-client){:new_window}.
-   [PHP-on-Couch](https://github.com/dready92/PHP-on-Couch){:new_window}.

### Examples and Tutorials

-   [CRUD](https://github.com/cloudant/haengematte/tree/master/php){:new_window}.

## JavaScript

[PouchDB](http://pouchdb.com/){:new_window} is a JavaScript database that can sync with Cloudant,
meaning you can make your apps offline-ready just by using PouchDB.
For more info,
see [our blog post](https://cloudant.com/blog/pouchdb){:new_window} on PouchDB.

To obtain PouchDB,
and for setup details,
refer to [PouchDB](http://pouchdb.com/){:new_window}.

>   **Note**: PouchDB is also available for Node.js: `npm install pouchdb`.

>   **Note**: PouchDB can also be installed with Bower: `bower install pouchdb`.

### Libraries and Frameworks

-   [Backbone.cloudant](https://github.com/cloudant-labs/backbone.cloudant){:new_window}.
    See the [blog post](https://cloudant.com/blog/backbone-and-cloudant/){:new_window} for more information.
-   [sag.js](https://github.com/sbisbee/sag-js){:new_window}.
-   [PouchDB](http://pouchdb.com/){:new_window} - JavaScript database for browser,
    with offline synchronization.

### Examples and Tutorials

-   [CRUD](https://github.com/cloudant/haengematte/tree/master/javascript-jquery){:new_window} using jQuery.
-   [CSVtoCloudant](https://github.com/michellephung/CSVtoCloudant){:new_window} -
    UI for importing `.csv` files into Cloudant.
    The app can also be accessed [here](https://michellephung.github.io/CSVtoCloudant/){:new_window}.
-   [csv2couchdb](https://github.com/Mango-information-systems/csv2couchdb){:new_window} -
    UI from Mango Systems to import `.csv` files to CouchDB/Cloudant.
-   [songblog](https://github.com/millayr/songblog){:new_window} - example app using JQuery.
-   [PouchDB Getting Started Guide](http://pouchdb.com/getting-started.html){:new_window} -
    example Todo application that syncs from browser to Cloudant or CouchDB.
-   [locationtracker](https://github.com/rajrsingh/locationtracker){:new_window} -
    example app to record and map location using PouchDB,
    CouchApp,
    and Cloudant.

## Ruby

[CouchRest](https://github.com/couchrest/couchrest){:new_window} is a CouchDB and Cloudant client
with extensions for working with Rails using [CouchRest Model](https://github.com/couchrest/couchrest_model){:new_window}.

To install CouchRest,
run the command:

```
gem install couchrest
```
{:screen}

### Libraries and Frameworks

There are many CouchDB clients listed on
[Ruby Toolbox](https://www.ruby-toolbox.com/categories/couchdb_clients){:new_window}.

### Examples and Tutorials

-   [CRUD](https://github.com/cloudant/haengematte/tree/master/ruby){:new_window}.

<div id="couchdb"></div>

## Meteor

[cloudant:couchdb](https://atmospherejs.com/cloudant/couchdb){:new_window} is the
Cloudant library for the `couchdb-meteor` package.
Since Apache CouchDB does not ship with Meteor or the couchdb package,
you must provide a URL for Meteor to connect
to a running CouchDB or Cloudant server instance before you install Meteor.
Add this package to your Meteor application:

```
meteor add cloudant:couchdb
```
{:screen}

The couchdb-meteor package provides:

-   Livequery implementation and real-time updates from the database by consuming the CouchDB `_changes` feed.
-   Distributed Data Protocol (DDP) RPC endpoints that update data from clients connected locally.
-   Serialization and deserialization of updates to the DDP format.

>   **Note**: The JSON query syntax used by Cloudant Query,
    and initially developed by Cloudant,
    was contributed back to Apache CouchDB for version 2.0.
    Pre-built binaries for Apache CouchDB version 2.0 are not yet available.
    You can use this module with Cloudant DBaaS or Cloudant Local until the pre-built binaries are available.

To configure the Apache CouchDB or Cloudant server connection information,
pass its URL as the `COUCHDB_URL` environment variable to the Meteor server process:

```
$ export COUCHDB_URL=https://username:password@username.cloudant.com
```
{:screen}

See the [API Reference](/docs/api/index.html) for more information about meteor-couchdb APIs. 


