---

copyright:
  years: 2015, 2017
lastupdated: "2017-01-06"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}

# Supported client libraries

## Mobile

The Cloudant Sync library is used to store,
index and query local JSON data on a mobile device.
It is also used to synchronise data between many devices.
Synchronisation is controlled by your application.
The library also provides helper methods for finding and resolving conflicts,
both in the local device and the remote database.

Two versions are available:

-   [Cloudant Sync - Android / JavaSE](https://github.com/cloudant/sync-android){:new_window}.
-   [Cloudant Sync - iOS (CDTDatastore)](https://github.com/cloudant/CDTDatastore){:new_window}.

An [overview](https://cloudant.com/product/cloudant-features/sync/){:new_window} of Cloudant Sync is available,
as are details of [resources](https://cloudant.com/cloudant-sync-resources/){:new_window}.

## Java

[java-cloudant](https://github.com/cloudant/java-cloudant){:new_window} is the official Cloudant library for Java.

Information about installing the library by adding it as a dependency to your maven or gradle builds is available
[here](https://github.com/cloudant/java-cloudant#installation-and-usage){:new_window},
along with details and examples of how to use the library.

### Libraries and Frameworks

#### Supported

-   [java-cloudant](https://github.com/cloudant/java-cloudant){:new_window}.

#### Unsupported

-   [ektorp](http://ektorp.org/){:new_window}.
-   [jcouchdb](http://code.google.com/p/jcouchdb/){:new_window}.
-   [jrelax](https://github.com/isterin/jrelax){:new_window}.
-   [LightCouch](http://www.lightcouch.org/){:new_window}.
-   [Java Cloudant Web Starter](https://ace.ng.bluemix.net/#/store/cloudOEPaneId=store&appTemplateGuid=CloudantJavaBPTemplate&fromCatalog=true){:new_window} boilerplate for Bluemix.

### Examples and Tutorials

-   [CRUD](https://github.com/cloudant/haengematte/tree/master/java){:new_window} with HTTP and JSON libraries.
-   [CRUD](https://github.com/cloudant/haengematte/tree/master/java/CrudWithEktorp){:new_window} with ektorp library.
-   [Building apps using Java with Cloudant on IBM Bluemix](https://cloudant.com/blog/building-apps-using-java-with-cloudant-on-ibm-bluemix/){:new_window}.
-   [Build a game app with Liberty, Cloudant, and Single Sign On](http://www.ibm.com/developerworks/cloud/library/cl-multiservicegame-app/index.html?ca=drs-){:new_window} Bluemix example.
-   [Building a Java EE app on IBM Bluemix Using Watson and Cloudant](https://developer.ibm.com/bluemix/2014/10/17/building-java-ee-app-ibm-bluemix-using-watson-cloudant/){:new_window} Bluemix example along with [YouTube video](https://www.youtube.com/watch?feature=youtu.be&v=9AFMY6m0LIU&app=desktop){:new_window}.


## Node.js

[nodejs-cloudant](https://github.com/cloudant/nodejs-cloudant){:new_window}
is the official Cloudant library for Node.js.
You can install it with npm:

```shell
npm install cloudant
```
{:codeblock}

### Libraries and Frameworks

-   [nodejs-cloudant](https://github.com/cloudant/nodejs-cloudant){:new_window} ([npm](https://www.npmjs.org/package/cloudant){:new_window}).
-   [sag-js](https://github.com/sbisbee/sag-js){:new_window} which also works in the browser.
    See [saggingcouch](https://github.com/sbisbee/saggingcouch.com){:new_window} for more detail.
-   [nano](https://github.com/dscape/nano){:new_window} is a minimalist implementation.
-   [restler](https://github.com/danwrong/restler){:new_window} delivers the best performance but is really barebones.
-   [cradle](https://github.com/flatiron/cradle){:new_window} is a high-level client that is also available
    if you absolutely need ease of use at the cost of reduced performance.
-   [cane_passport](https://github.com/ddemichele/cane_passport){:new_window} - Cloudant Angular Node Express with Bootstrap.
-   [express-cloudant](https://github.com/cloudant-labs/express-cloudant){:new_window} - a template for Node.js Express framework also using PouchDB and Grunt.
-   [Node.js Cloudant DB Web Starter](https://ace.ng.bluemix.net/#/store/cloudOEPaneId=store&appTemplateGuid=nodejscloudantbp&fromCatalog=true){:new_window} - boilerplate for Bluemix.
-   [Mobile Cloud](https://ace.ng.bluemix.net/#/store/cloudOEPaneId=store&appTemplateGuid=mobileBackendStarter&fromCatalog=true){:new_window} - boiler plate for Bluemix (Node.js, Security, Push, and Mobile Data/Cloudant).

### Examples and Tutorials

-   [CRUD](https://github.com/cloudant/haengematte/tree/master/nodejs){:new_window}.
-   [Cloudant-Uploader](https://github.com/garbados/Cloudant-Uploader){:new_window} - utility to upload `.csv` files to Cloudant.
-   [couchimport](https://github.com/glynnbird/couchimport){:new_window} - utility to import `.csv` or `.tsv` files into CouchDB or Cloudant.
-   [Getting started with IBM Bluemix and Node.js](http://thoughtsoncloud.com/2014/07/getting-started-ibm-bluemix-node-js/){:new_window}.
-   [A Cloud medley with IBM Bluemix, Cloudant DB and Node.js](https://gigadom.wordpress.com/2014/08/15/a-cloud-medley-with-ibm-bluemix-cloudant-db-and-node-js/){:new_window}.
-   [Build a simple word game app using Cloudant on Bluemix](http://www.ibm.com/developerworks/cloud/library/cl-guesstheword-app/index.html?ca=drs-){:new_window} - uses Node.js.
-   [Building a Real-time SMS Voting App](https://www.twilio.com/blog/2012/09/building-a-real-time-sms-voting-app-part-1-node-js-couchdb.html){:new_window} - six-part series using Node.js, Twilio, and Cloudant.
-   [Building a Multi-Tier Windows Azure Web application](http://msopentech.com/blog/2013/12/19/tutorial-building-multi-tier-windows-azure-web-application-use-cloudants-couchdb-service-node-js-cors-grunt-2/){:new_window} - uses Cloudant, Node.js, CORS, and Grunt.
-   [Do it yourself: Build a remote surveillance application using Bluemix, Cloudant, and Raspberry Pi.](http://www.ibm.com/developerworks/library/ba-remoteservpi-app/index.html){:new_window}.

## Python

A supported library for working with Cloudant using Python is
available [here](https://github.com/cloudant/python-cloudant){:new_window}.

Download the current library release [here](https://pypi.python.org/pypi/cloudant/){:new_window}.
Learn more information about the Python language at [python.org](https://www.python.org/about/){:new_window}. 

## Swift

A supported library is available for working with Cloudant.
The library is called SwiftCloudant,
and is installed using `cocoapods`.

The Podfile entry is:

```shell
pod 'SwiftCloudant'
```
{:codeblock}

More information about SwiftCloudant,
including details of installation and how to use the library to store,
index,
and query remote JSON data on Cloudant,
is available [here](https://github.com/cloudant/swift-cloudant){:new_window}.

The library is an early release version.
As such,
it does not currently have complete Cloudant API coverage. 

>   **Note**: SwiftCloudant is not supported on iOS,
    and you cannot call it from Objective-C.