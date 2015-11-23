<link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
## Replication

Replication is an interface to the replication system. You can initiate replication between local and remote databases You can find details about the _replicator database on the Databases page. 

→ [Learn more](https://docs.cloudant.com/replication.html#undefined)

---

### REPLICATE A DATABASE
1. In the left navigation click **Replication**, then ![alt text](images/visual_guide/3_replication/1.png)
2. Select a **Source Database** and **Target Database**, and if needed, select the **Make this replication continuous** checkbox.
3. Click **Replicate**.

	**BOX??**
<span class=" fa fa-info">The source database can be a local or remote database. If you select a New Database as the Target Database, you can replicate into a new database. A target database can be local or remote.
	![alt text](images/visual_guide/3_replication/2.png)

---

### CANCEL OR RERUN AN REPLICATION
 
* If you want to rerun a replication, click ![alt text](images/visual_guide/3_replication/4.png) to start another run, or if a replication is in progress, you can stop it by clicking ![alt text](images/visual_guide/3_replication/5.png).

	![alt text](images/visual_guide/3_replication/3.png)

---

### ENABLE CONTINUOUS REPLICAITON

* If you want to propagate changes from your original source database to a replicated database, when you create a new replication, select the **Make this replication continuous** checkbox. Or after you create a replication, open the replication details by clicking the replication document link. 


	![alt text](images/visual_guide/3_replication/6.png)