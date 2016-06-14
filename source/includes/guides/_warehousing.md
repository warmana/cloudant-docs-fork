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

When we provide enterprise abilities as part of a database service,
we create what is often called a 'Data Warehouse'.

In general,
a [data warehouse is](https://en.wikipedia.org/wiki/Data_warehouse):
"... a central repository of integrated data from one or more sources. It stores current and historical data. It can be used for performing analysis and creating reports for knowledge workers throughout the enterprise."

{Need discussion on the business benefit of Cloudant/DashDB/DB2 integration here. Use cases, etc. Input from Holger and Mike?}

### Cloudant and Data Warehousing

IBM Cloudant has a basic warehousing capability,
in the form of [MapReduce views](using_views.html) that enable you to perform a range of basic analytical tasks.

For more advanced warehousing tasks,
it helps to have the additional capabilities provided by warehousing services such as [IBM dashDB](http://www-01.ibm.com/software/data/dashdb/).

When you use IBM Cloudant,
you have integrated and easy access to advanced warehousing capabilities,
such as:

-	Seeing your JSON data in a relational database format.
-	Performing SQL-based queries on your data.
-	Building analytics from your data.

These advanced warehousing capabilities are enabled through services such as IBM dashDB,
which is a natural complement to Cloudant.

### IBM dashDB

IBM dashDB is a cloud-based data warehouse service,
purpose-built for analytic work.
While especially suited for Cloudant JSON data,
dashDB can accept data from a variety of sources by
examining the structure of data when it is loaded.

For more information,
see the [IBM dashDB Cloud Data Warehouse documentation](https://www.ibm.com/support/knowledgecenter/SS6NHC/com.ibm.swg.im.dashdb.kc.doc/welcome.html).

#### Creating a warehouse

There are two ways you can create a warehouse.

-	Provide IBM Bluemix credentials in your Cloudant dashboard, then use the Cloudant Warehousing feature to create a dashDB warehouse instance for you within Bluemix. Do this using the "Create a dashDB Warehouse" task within your Cloudant dashboard.<br/>![Screenshot of the "Create a dashDB warehouse" task within the Cloudant dashboard](images/createDashDBWH.png)
-	Alternatively, create a dashDB warehouse instance within Bluemix, then go to your Cloudant account dashboard and connect to that instance.<br/>![Screenshot of the "Connect to an existing dashDB warehouse" task within the Cloudant dashboard](images/connectDashDBWH.png)

If you prefer,
you can create a DB2 warehouse instance instead of dashDB. Do this by using the "Create a DB2 Warehouse" task within your Cloudant dashboard to connect to an existing DB2 instance.<br/>![Screenshot of the Create a DB2 warehouse" task within the Cloudant dashboard](images/createDB2WH.png)

<aside class="notify">The remainder of this topic refers to dashDB as the warehouse instance.
However,
the topic applies equally if you are using an instance of DB2.</aside> 

When you first create a warehouse from within Cloudant,
dashDB creates the best possible schema for the data within the database,
helping ensure that each of the fields within your JSON documents has a corresponding entry within the new schema.
Optionally,
when creating the warehouse,
you can choose to [customize the schema](#customizing_the_warehouse_schema) manually.

Once the schema is created,
the warehouse is able to hold your data in a relational format.
Cloudant then [replicates](http://docs.cloudant.com/replication.html) to perform
an 'initial load' of the database documents into the warehouse,
giving you a working collection of your data in the dashDB relational database.

#### Working with your warehouse

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

#### Keeping the data and structure fresh

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
The old tables within dashDB are then dropped,
new tables created using the new schema,
and finally the current Cloudant data is loaded as a fresh replication.

To use the rescan facility,
first ensure that your warehouse is not running.
Do this by:

1.	Selecting the 'Warehouse' tab within the Cloudant dashboard.
2.	Find your warehouse:<br/>![Screenshot of the "warehouse" tab within the Cloudant dashboard](images/selectWarehouse.png)
3.	Click on the warehouse link, which opens the warehouse detail view:<br/>![Screenshot of the detailed warehouse view within the Cloudant dashboard](images/viewWarehouseDetail.png)
4.	Check the current status of the warehouse. A rotating green circle indicates that the warehouse is running. To stop the warehouse, click the square `Stop Database` icon in the Actions column:<br/>![Screenshot of the "stop warehouse database" icon within the Cloudant dashboard](images/stopWarehouseDatabase.png)
5.	When the warehouse database is not running, the `Rescan` icon in the Action column is enabled:<br/>![Screenshot of the rescan icon within the Cloudant dashboard](images/rescanIcon.png)

##### Rescanning the source database

![Screenshot of the window enabling you to rescan the warehouse source database.](images/rescanSource.png)

When you click the `Rescan` icon,
you have two choices:

-	A straightforward scan of your database. This is the default action, and is very similar to the initial scan of your database performed when the warehouse was first created.
-	Customize the warehouse schema. 

To manually customize the warehouse schema, enabled the `Customize Schema` checkbox then click the `Rescan` button.

##### Customizing the warehouse schema

