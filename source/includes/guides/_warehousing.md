## Data Warehousing

A database is essential for storing data.
But being able to apply that data for business purposes is what makes a database valuable:
being able to retrieve relevant data,
quickly and easily,
and putting the data to work within your applications.

But many of the storage,
processing,
and analytics tasks you perform with the data are used again and again in your applications.
Or they might be good examples of industry best practices.

So,
it makes sense to extend standard database capabilities with additional features,
supporting tasks such as reporting,
or analytics.

For nearly 30 years,
'Data Warehouses' have been the industry standard for data storage,
reporting,
and analytics,
based on relational database technology.
In general,
a [data warehouse is](https://en.wikipedia.org/wiki/Data_warehouse):
"... a central repository of integrated data from one or more sources. It stores current and historical data. It can be used for performing analysis and creating reports for knowledge workers throughout the enterprise."

The technologies that enable data storage,
reporting,
and analytics have emerged in recent years as a response to the need to process '[Big Data](https://en.wikipedia.org/wiki/Big_data)'.
"Big data is a term for data sets that are so large or complex that traditional data processing applications are inadequate."

At the same time,
the properties and characteristics of Data Warehouses and related products mean that using relational database technology to enable the Data Warehouses is a popular choice,
even for big data tasks.

There are many use cases that nicely illustrate the benefits of integrating Cloudant capabilities with a relational data warehouse,
such as the following examples.

### Joining data

Joining data from multiple data stores for cross-domain analysis is a task that can be performed easily and efficiently using a relational data warehouse.

Data from different sources is prepared and transformed to a common format during the load of a data warehouse.
Records are stored in tables,
and operations are available to join those tables to enable combined analysis.

Doing the join in a relational data warehouse is especially useful if some of the data is already available in relational representation,
for example master data or reference data.

### Flexibility

Cloudant databases are flexible at representing data.
For example,
they do not enforce a schema during read or write.

By contrast,
a well-defined and rigorously enforced model is required for reporting and analytics tasks.

With your documents available in a relational warehouse you can base your model on a fixed set of table definitions. Only documents that fit the table schema can get loaded while violations are rejected. You can train your models with consistent data using a fixed relational schema.

### Data integrity assertion

Data Warehouses can use constraints to assert data integrity.
For example:
- No two records can have the same primary key.
- Foreign keys guarantee that records are complete.
- Functions are available to validate records against business rules.

Uniqueness,
correctness,
and completeness are essential requirements for any enterprise service.
Loading your Cloudant documents into a data warehouse helps you meet these requirements.

### Cloudant and Data Warehousing

Data Warehouses are a mature and important technology.
Cloudant provides a tight integration with relational data warehouses,
giving you the benefit of this technology.

IBM Cloudant has a basic warehousing capability built in,
in the form of [MapReduce views](using_views.html) that enable you to perform a range of basic analytical tasks.

For more advanced warehousing tasks,
you can leverage the full capabilities provided by the IBM cloud-based warehousing service [IBM dashDB](http://www-01.ibm.com/software/data/dashdb/).

When you use IBM Cloudant,
you have integrated and easy access to advanced warehousing capabilities,
such as:

-	Seeing your JSON data in a relational database format.
-	Performing SQL-based queries on your data.
-	Building analytics from your data.

These advanced warehousing capabilities are enabled through services such as IBM dashDB,
which is a natural complement to Cloudant.

Alternatively,
if you only need a relational data store for your documents,
without the warehousing capabilities,
you can load your Cloudant documents into the [IBM DB2 on Cloud](warehousing.html#ibm-db2-on-cloud) service.

### IBM dashDB

IBM dashDB is a cloud-based data warehouse service,
purpose-built for analytic work.
While especially suited for Cloudant JSON data,
dashDB can accept data from a variety of sources by
examining the structure of data when it is loaded.

For more information,
see the [IBM dashDB Cloud Data Warehouse documentation](https://www.ibm.com/support/knowledgecenter/SS6NHC/com.ibm.swg.im.dashdb.kc.doc/welcome.html).

### IBM DB2 on Cloud

[IBM DB2 on Cloud](https://console.ng.bluemix.net/catalog/services/ibm-db2-on-cloud) provides you with a database on IBM's SoftLayer® global cloud infrastructure.
It offers you the rich features of an on-premise DB2 deployment,
but without the cost,
complexity,
and risk of managing your own infrastructure.

For more information, see the [IBM DB2 on Cloud documentation](https://console.ng.bluemix.net/docs/services/DB2OnCloud/index.html#DB2OnCloud)

### Creating a warehouse

There are two ways you can create a warehouse.

-	Provide IBM Bluemix credentials in your Cloudant dashboard, then use the Cloudant Warehousing feature to create a dashDB warehouse instance for you within Bluemix. Do this using the "Create a dashDB Warehouse" task within your Cloudant dashboard.<br/>![Screenshot of the "Create a dashDB warehouse" task within the Cloudant dashboard](images/createDashDBWH.png)
-	Alternatively, create a dashDB warehouse instance within Bluemix, then go to your Cloudant account dashboard and connect to that instance.<br/>![Screenshot of the "Connect to an existing dashDB warehouse" task within the Cloudant dashboard](images/connectDashDBWH.png)

If you prefer,
you can create a DB2 warehouse instance instead of dashDB. Do this by using the "Create a DB2 Warehouse" task within your Cloudant dashboard to connect to an existing DB2 instance.<br/>![Screenshot of the Create a DB2 warehouse" task within the Cloudant dashboard](images/createDB2WH.png)

<aside class="notify">The remainder of this topic refers to dashDB as the warehouse instance.
However,
the topic applies equally if you are using an instance of DB2.
A tutorial is also available describing how to "[Load JSON Data from Cloudant into dashDB](https://developer.ibm.com/clouddataservices/docs/dashdb/get/load-json-from-cloudant-database-in-to-dashdb/)",
and includes examples of using DB2 as the warehouse database.</aside>

When you first create a warehouse from within Cloudant,
dashDB creates the best possible schema for the data within the database,
helping ensure that each of the fields within your JSON documents has a corresponding entry within the new schema.
Optionally,
when creating the warehouse,
you can choose to [customize the schema](#customizing-the-warehouse-schema) manually.

Once the schema is created,
the warehouse is able to hold your data in a relational format.
Cloudant then [replicates](http://docs.cloudant.com/replication.html) to perform
an 'initial load' of the database documents into the warehouse,
giving you a working collection of your data in the dashDB relational database.

### Working with your warehouse

With Cloudant warehousing,
you can run 'traditional' SQL queries,
and view the results,
all from within the dashDB console.<br/>
![Screenshot of the "dashDB dashboard" within Bluemix](images/useDashDBdashboard.png)

External applications can interact with the data in the same way as with any other relational database.

The advantage of dashDB is that you can perform other warehousing tasks,
such as loading more data from other sources,
and analyzing the data using built-in analytic tools.
DashDB supports the [`'R'` programming language](https://en.wikipedia.org/wiki/R_%28programming_language%29) and software environment for statistical computing and graphics.
This means you have access to algorithms that let you perform database analytic tasks such as linear regression,
'k-means' clustering,
and geospatial analysis.

The `RStudio` tool allows you to create `'R'` scripts which are then uploaded into dashDB,
then run using your data.

For more information about working with dashDB,
see the [IBM dashDB Cloud Data Warehouse documentation](https://www.ibm.com/support/knowledgecenter/SS6NHC/com.ibm.swg.im.dashdb.kc.doc/welcome.html).

### Keeping the data and structure fresh

Data is loaded from Cloudant into dashDB using a [replication](http://docs.cloudant.com/replication.html) process.
This means that if your Cloudant data is updated or modified in some way,
replication of the documents into dashDB must take place again to ensure your analytic tasks continue to work using the most up-to-date information.

As with normal Cloudant replication,
data is transferred one-way only: for a warehouse the transfer is from Cloudant to dashDB.
After the initial load of data,
the warehouse subscribes to changes in the Cloudant database.
Any changes are replicated from the Cloudant source to the dashDB target.
Therefore,
warehousing is a form of continuous replication from Cloudant to dashDB.

Over time,
your Cloudant database might also have structural changes.
This might include the addition or removal of fields from the JSON documents.
When this happens,
the schema used by the warehouse might become invalid,
resulting in errors reported when fresh data is replicated from Cloudant to dashDB.

To solve this problem,
Cloudant warehousing has a 'rescan' facility.
This rescans the structure of the Cloudant database,
and determines the new schema required in dashDB.
The old tables within dashDB that were created during the previous scan are then dropped,
new tables created using the new schema,
and finally the current Cloudant data is loaded as a fresh 'initial load'.

To use the rescan facility,
first ensure that your warehouse is not running.
Do this by:

1.	Selecting the 'Warehouse' tab within the Cloudant dashboard.
2.	Find your warehouse:<br/>![Screenshot of the "warehouse" tab within the Cloudant dashboard](images/selectWarehouse.png)
3.	Click on the warehouse link, which opens the warehouse detail view:<br/>![Screenshot of the detailed warehouse view within the Cloudant dashboard](images/viewWarehouseDetail.png)
4.	Check the current status of the warehouse. A rotating green circle indicates that the warehouse is running. To stop the warehouse, click the square `Stop Database` icon in the Actions column:<br/>![Screenshot of the "stop warehouse database" icon within the Cloudant dashboard](images/stopWarehouseDatabase.png)
5.	When the warehouse database is not running, the `Rescan` icon in the Action column is enabled:<br/>![Screenshot of the rescan icon within the Cloudant dashboard](images/rescanIcon.png)

#### Rescanning the source database

![Screenshot of the window enabling you to rescan the warehouse source database.](images/rescanSource.png)

When you click the `Rescan` icon,
you have two choices:

-	A straightforward scan of your database. This is the default action, and is very similar to the initial scan of your database performed when the warehouse was first created.
-	Customize the warehouse schema.

If you choose the default action of a simple rescan,
your source database is inspected and a fresh warehouse database schema is generated.
As soon as the rescan completes,
the warehouse is started.

If you want to customize the warehouse schema,
enable the `Customize Schema` checkbox,
before clicking the `Rescan` button.

![Screen shot of 'Rescan Source' panel, showing the 'Customize Schema' option enabled.](images/rescanSource2.png)

The `Customize Schema` checkbox enables two options.

1.  The discovery algorithm used.
2. The sample size.

#### The discovery algorithm

The default option for rescanning is the `Union` algorithm.
This uses all the attributes in all the sampled Cloudant database documents to create a single set of tables in the warehouse database.
The result is that all the Cloudant database documents can be stored in the warehouse database,
but some rows in the database might not have content in some of the fields.

The alternative option for rescanning is the `Cluster` algorithm.
This identifies documents within the Cloudant database that have the same set of attributes,
then creates corresponding warehouse database table schemas.

#### The sample size

This option determines how many documents within the Cloudant database are inspected as part of the schema determination.

The default value is 10,000 documents.

Setting the value too low introduces the risk that some Cloudant documents have attributes that are not detected,
and are therefore omitted from the warehouse database structure.

Setting the value too high means that the scanning process to determine the warehosue database structure will take longer to complete.

#### After the rescan

Once the Cloudant database rescan has finished,
the warehouse is not autoamtically started.
Instead,
it is left in halted state,
so that the warehouse database can be customized.

### Customizing the warehouse schema

It is possible to modify the database schema that is determined automatically during the initial warehouse creation process,
or after a rescan.
To do this,
ensure that you check the `Customize Schema` option during the creation process:<br/>
![Screen shot of warehouse creation panel, showing the 'Customize Schema' option enabled.](images/customizeSchema01.png)

The warehouse is created in dashDB as normal,
however it is not started immediately.
Instead,
you have the opportunity to customize the schema before proceeding.

To do this,
click the link for your warehouse:<br/>
![Screen shot of `Open in dashDB` button.](images/openInDashDB.png)

The resulting display gives you a button to customize the schema used for your source database.
Hovering over the Status indicator confirms that the schema is ready for customization:<br/>
![Screen shot of `Customize <source database name>` button.](images/customizeSchema02.png)

Clicking on the 'Customize' button results in a panel where you can modify the fields in the database schema:<br/>
![Screen shot of Customize Schema panel.](images/customizeSchema03.png)

To reset the schema to the default,
click the `Rescan` button:<br/>
![Screen shot of `Rescan` button.](images/customizeSchema04.png)

When you are happy with the database schema for the warehouse,
simply click the `Run` button:<br/>
![Screen shot of `Run` button.](images/customizeSchema05.png)

The schema is saved,
and the warehouse is started.

#### Customizing an existing warehouse schema

If the database schema for your warehouse already exists,
you have the [option to customize it](warehousing.html#keeping-the-data-and-structure-fresh).

### Troubleshooting

From time-to-time,
you might encounter problems when using the warehousing facility.
Information on some of these problems is provided later in this topic.

Additionally,
discussion of some common errors or problems,
as well as details of how to troubleshoot them,
is available in [Stack Overflow](http://stackoverflow.com/questions/tagged/cloudant+dashdb).

If you need further help,
and can't find solutions in Stack Overflow,
please contact [Cloudant support](mailto:support@cloudant.com).

### Exceptions visible in the dashboard
