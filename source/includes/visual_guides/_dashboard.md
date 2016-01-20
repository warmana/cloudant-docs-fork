## Overview

Welcome to IBM Cloudant. Cloudant is a database-as-a-service that manages, scales, and supports your fast-growing data needs 24x7, so you can stay focused on new development and growing your business.

---

### Getting Started

Before you can use the Cloudant Dashboard, you must sign up for an account. You can sign up for a 30-day, free account to check the dashboard out. 

1. Sign up for an account at [cloudant.com](http://cloudant.com/).
![sign up](images/visual_guide/1_getting_started/1.png)

2. See white papers, webinars, videos, blogs, and more under Resources.
![resources](images/visual_guide/1_getting_started/2.png)

---

### Databases

The Databases page is the landing page for the Dashboard. You can create documents and manage your Cloudant databases from this page.

→ [Learn more](https://docs.cloudant.com/database.html#undefined)

---

#### Add New Database
1. Click **Add New Database**.
2. Enter the name of the database.
3. Click **Create**.

![add new database](images/visual_guide/2_databases/1.png)

---

#### View Database Details
Click **Permissions** tab, and click the database whose information you want to view. Each database includes a tab with information about permissions, changes, documents, queries, and design documents. From those tabs, you can:

→ [Learn more](https://docs.cloudant.com/authorization.html#undefined)

* Share a database with change permissions.

![change database permissions](images/visual_guide/2_databases/2.png)

---

* View changes.
Click **Changes** tab.

![view changes](images/visual_guide/2_databases/3.png)

---
* Working with documents:
* **In multiple document**: Click the radio button on the All Documents page. You can select one or multiple documents to change the view or delete it.
	
![edit documents](images/visual_guide/2_databases/4.png)

---
* **In a single document**: Click the pencil button to edit, upload, or clone documents.
		
![menu bar](images/visual_guide/2_databases/5.png)

---
* **Run queries**: You can update a query or add an index to find documents.
	
→ [Learn more](https://docs.cloudant.com/cloudant_query.html#undefine)
	
![run queries](images/visual_guide/2_databases/6.png)

---

#### Use the Settings Menu
Click the gear icon to start the following tasks:

* Add New Doc: Enter the JSON to create the document. You can also upload an attachment or clone a document.

* Add New View: Enter your information and click **Save & Build Index**.

* Add New Query Indexes: Enter JSON query syntax to query your database and click **Create Index**.

* Add New Search Index: Enter information to create a search index and click **Create Index**.

![settings menu](images/visual_guide/2_databases/8.png)

---
	
### Replication

Replication is an interface to the replication system. You can initiate replication between local and remote databases You can find details about the _replicator database on the Databases page. 

→ [Learn more](https://docs.cloudant.com/replication.html#undefined)

---

#### Replicate a Database
1. In the left navigation, click **Replication**.
2. Select a **Source Database** and **Target Database**, and if needed, select the **Make this replication continuous** check box.
3. Click **Replicate**.

<span class=" fa fa-info">The source database can be a local or remote database. If you select a New Database as the Target Database, you can replicate into a new database. A target database can be local or remote.
![create replication](images/visual_guide/3_replication/2.png)

---

#### Cancel or Rerun a Replication
 
* If you want to rerun a replication, click ![rerun button](images/visual_guide/3_replication/4.png) to start another run, or if a replication is in progress, you can stop it by clicking ![cancel button](images/visual_guide/3_replication/5.png).

![all replications tab](images/visual_guide/3_replication/3.png)

---

#### Enable Continuous Replication

* If you want to propagate changes from your original source database to a replicated database, when you create a new replication, select the **Make this replication continuous** check box. Or after you create a replication, open the replication details by clicking the replication document link. 


![make this replication continuous check box](images/visual_guide/3_replication/6.png)	

### Warehousing

You can create a warehouse in IBM dashDB. A warehouse provides deep-dive analytics of your database activity.

* Click **Getting Started** to learn more about warehousing and it’s capabilities.
![getting started with warehousing](images/visual_guide/4_warehousing/1.png)

---

#### Creating a Warehouse
 
1. In the left navigation, click **Warehousing**, then **Create a Warehouse**.
	![warehouse menu](images/visual_guide/4_warehousing/2.png)

2. **Authenticate** with your IBM Bluemix username and password.
	![authenticate](images/visual_guide/4_warehousing/3.png)
	
3. **Pick a name** for your warehouse and **choose which database** you would like to add to the warehouse.
	![add a warehouse name](images/visual_guide/4_warehousing/4.png)
	
4. **Optional**: You can add the warehouse to an existing dashDB service instance or to a specific IBM Bluemix organization and space.
	![add a warehouse to a dashDB service](images/visual_guide/4_warehousing/5.png)
	
5. Click ![create warehouse button](images/visual_guide/4_warehousing/Button.png) and you will be taken to the warehouses page.
	![warehouse list](images/visual_guide/4_warehousing/6.png)

---

#### View Warehouse Analytics 
*Only available after previous steps*

* In the left navigation, click **Warehousing**, then the warehouse you want to view details about.

![warehouse list](images/visual_guide/4_warehousing/6.png)

---

### Active Tasks
Shows a list of the running background tasks on the server, including database compaction, index building, and replication.

→ [Learn more](https://docs.cloudant.com/active_tasks.html#undefined)

---

#### Sorting Active Tasks
* The Active Tasks dashboard shows multiple views of each active task. You can view all the active tasks together in a list, or you can select a tab that contains only replication tasks, database compaction tasks, indexer tasks, or view compaction tasks.
![active tasks tabs](images/visual_guide/5_active_tasks/1.png)

---

#### Change Polling Intervals
* When you view the active tasks, their status can change. Adjust the time between auto-updates by moving the **Polling Interval** slider.
![polling interval slider](images/visual_guide/5_active_tasks/2.png)

---

#### API URL
* The Active Tasks page is an interface to the Active Tasks API call. Click **API URL**, then **Copy** to view or copy the raw JSON.
![api url, view json button, and copy button](images/visual_guide/5_active_tasks/3.png)

---

### Account

On the Account page, you can see Cloudant announcements and usage statistics. Or you can update your profile, change your account password, add or update a credit card, and change the location of your data.

→ [Learn more](https://docs.cloudant.com/account.html)

---

#### Virtual Hosts
1. Click on **Account** > **Virtual Hosts** tabs.
1. Enter your **hostname**, or a **path** within your hostname, and click **Add** to map your domain to a Cloudant account.
2. **Update** your DNS record to point to `yourname`.cloudant.com using CNAME.
![virtual hosts window](images/visual_guide/6_account/4.png)

---

#### Cross-Origin Resource Sharing 
*CORS is only available after you complete the previous step.*

1. Click on **Account** > **CORS** tabs.
2. Select **Enable CORS**.
3. **Define** the domains where database accepts requests.
4. Click **Add**.

<span class=" fa fa-info">The source database can be a local or remote database. If you select a New Database as the Target Database, you can replicate into a new database. A target database can be local or remote.

![CORS window](images/visual_guide/6_account/5.png)

---	
### Support

Shows a list of the running background tasks on the server, including database compaction, index building, and replication.

---

#### Create a Support Case
1. Click **Support**, then ![new case button](images/visual_guide/7_support/button.png)
2. Enter a subject and the details of your question or problem.
3. **Optional**: Attach a file.
4. Click **Submit**.

![new case window](images/visual_guide/7_support/1.png)

---

### Helpful Links

---

* [Cloudant Homepage](https://www.cloudant.com)
* [Cloudant Documentation](https://docs.cloudant.com/)
* [Cloudant for Developers](https://cloudant.com/for-developers/)
* [Cloudant: The Definitive Guide](https://cloudant.com/resources/white-papers/)
* [Cloudant Learning Center](https://cloudant.com/learning-center/)
* [The Cloudant Blog](https://cloudant.com/blog/)	
