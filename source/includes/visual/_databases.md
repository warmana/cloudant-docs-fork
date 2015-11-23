<link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
## Databases

The Databases page is the landing page for the Dashboard. You can create documents and manage your Cloudant databases from this page.

→ [Learn more](https://docs.cloudant.com/database.html#undefined)

---

### ADD NEW DATABASE
1. Click **Add New Database**.
2. Enter the name of the database.
3. Click **Create**.

![alt text](images/visual_guide/2_databases/1.png)

---

### VIEW DATABASE DETAILS
Click the database whose information you want to view. Each database includes a tab with information about permissions, changes, documents, queries, and design documents. From those tabs, you can:
 
* Share a database with change permissions.

	→ [Learn more](https://docs.cloudant.com/authorization.html#undefined)

	![alt text](images/visual_guide//2_databases/2.png)

	---
* View Changes.

	![alt text](images/visual_guide//2_databases/3.png)

	---
* Edit documents:
	* **In Document**: Click the radio button on the All Documents page. You can select one or multiple documents to change the view or delete.
	
		![alt text](images/visual_guide/2_databases/4.png)

		---
	* **For an individual doc**: Click <span class=" fa fa-pencil"> button to edit, upload, or clone documents.
		
		![alt text](images/visual_guide/2_databases/5.png)

		---
* **Run Queries**: you can update a query or add an index to find documents.
	
	→ [Learn more](https://docs.cloudant.com/cloudant_query.html#undefine)
	
	![alt text](images/visual_guide/2_databases/6.png)
	
	---
* **Run Queries**: Click <span class=" fa fa-gear"> **Create New View**. Name the design document.
	
	→ [Learn more](https://docs.cloudant.com/creating_views.html)

	![alt text](images/visual_guide/2_databases/7.png)
---

### USE THE SETTINGS MENU
Click <span class=" fa fa-gear"> to start the following tasks:

* **Add New Doc**: Enter the JSON to create the document. You can also upload an attachment or clone a document.

* **Add New View**: Enter your information and click **Save & Build Index**.

* **Add New Query Indexes**: Enter JSON query syntax to query your database and click **Create Index**.

* **Add New Search Index**: Enter information to create a search index and click **Create Index**.

	![alt text](images/visual_guide/2_databases/8.png)