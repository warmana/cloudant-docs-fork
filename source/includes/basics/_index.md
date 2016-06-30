# ![alt tag](images/cloudantbasics_icon.png) Cloudant Basics

If it's your first time here, scan this section before you scroll further. The sections on [Client Libraries](libraries.html#-client-libraries), [API Reference](api.html#-api-reference), and [Guides](guides.html#-guides) assume you know some basic things about Cloudant.

## Database as a Service

As a hosted and managed database-as-a-service (DBaaS),
Cloudant provides an [HTTP API](basics.html#http-api) to your [JSON](basics.html#json) data,
and 24-hour operational support and maintenance.
Cloudant is based on [Apache CouchDB](http://couchdb.apache.org/),
and is delivered as a multi-tenant, dedicated, and installed service.

## IBM Bluemix

Cloudant is also available as an [IBM Bluemix service](https://www.ng.bluemix.net/docs/?cm_mmc=dw-_-bluemix-_-ibmsite-_-cloudantdocs).
Bluemix is an open-standards, cloud platform for building, running, and managing applications.
Find out more,
and get started with Bluemix,
at the [home page](https://console.ng.bluemix.net/?cm_mmc=dw-_-bluemix-_-ibmsite-_-cloudantdocs).

## HTTP API
All requests to Cloudant go over the web, which means any system that can speak to the web, can speak to Cloudant. All language-specific libraries for Cloudant are really just wrappers that provide some convenience and linguistic niceties to help you work with a simple API. Many users even choose to use raw HTTP libraries for working with Cloudant.

Specific details about how Cloudant uses HTTP is provided in the [HTTP topic of the API Reference](http.html).

Cloudant supports the following HTTP request methods:

-   `GET`

    Request the specified item. As with normal HTTP requests, the format of the URL defines what is returned. With Cloudant this can include static items, database documents, and configuration and statistical information. In most cases the information is returned in the form of a JSON document.

-   `HEAD`

    The `HEAD` method is used to get the HTTP header of a `GET` request without the body of the response.

-   `POST`

    Upload data. Within Cloudant's API, `POST` is used to set values, including uploading documents, setting document values, and starting certain administration commands.

-   `PUT`

    Used to put a specified resource. In Cloudant's API, `PUT` is used to create new objects, including databases, documents, views and design documents.

-   `DELETE`

    Deletes the specified resource, including documents, views, and design documents.

-   `COPY`

    A special method that can be used to copy documents and objects.

If the client (such as some web browsers) does not support using these HTTP methods, `POST` can be used instead with the `X-HTTP-Method-Override` request header set to the actual HTTP method.

### Method not allowed error

> Example error message

```json
{
    "error":"method_not_allowed",
    "reason":"Only GET,HEAD allowed"
}
```

If you use an unsupported HTTP request type with a URL that does not support the specified type, a [405](http.html#405) error is returned, listing the supported HTTP methods, as shown in the example.

## JSON
Cloudant stores documents using JSON (JavaScript Object Notion) encoding, so anything encoded into JSON can be stored as a document. Files like images, videos, and audio are called BLObs (binary large objects) and can be stored as attachments within documents.

More information about JSON can be found in the [JSON Guide](json.html).

## Distributed

Cloudant's API enables you to interact with a collaboration of numerous machines, called a cluster. The machines in a cluster must be in the same datacenter, but can be within different 'pods' in that datacenter. Using different pods helps improve the High Availability characteristics of Cloudant.

An advantage of clustering is that when you need more computing capacity, you just add more machines. This is often more cost-effective and fault-tolerant than scaling up or enhancing an existing single machine.

For more information about Cloudant and distributed system concepts, see the [CAP Theorem](cap_theorem.html) guide.

## Replication

[Replication](replication.html) is a procedure followed by Cloudant, [CouchDB](http://couchdb.apache.org/), [PouchDB](http://pouchdb.com/), and others. It synchronizes the state of two databases so that their contents are identical.

You can continuously replicate. This means that a target database updates every time the source database changes. Testing for source changes involves ongoing internal calls.
Continuous replication can be used for backups of data, aggregation across multiple databases, or for sharing data.

<aside class="warning" role="complementary" aria-label="internalcalls">Continuous replication can result in a large number of internal calls. This might affect costs for multi-tenant users of Cloudant systems. Continuous replication is disabled by default.</aside>

<<<<<<< 8777a5f1d0c5fa1ff6a1028d920da04ff6aef4a4
## Cloudant Local

<a href="https://www.ibm.com/support/knowledgecenter/SSTPQH_1.0.0/com.ibm.cloudant.local.doc/SSTPQH_1.0.0_welcome.html" target="_blank">IBM Cloudant Data Layer Local Edition (Cloudant Local)</a> is a locally installed version of the Cloudant Database-as-a-Service (DBaaS) offering.
=======
## Versions of Cloudant

IBM offers additional versions of Cloudant.

*	Cloudant Data Layer Local Edition is a locally installed version of the Cloudant Database-as-a-Service (DBaaS) offering. 
*	Cloudant on Bluemix Local is delivered as-a-service and in constant collaboration with your IT team.  

You can read more information in the following sections. 

### Cloudant Local
<a href="http://www-01.ibm.com/support/knowledgecenter/SSTPQH/SSTPQH_welcome.html" target="_blank">IBM Cloudant Data Layer Local Edition (Cloudant Local)</a> is a locally installed version of the Cloudant Database-as-a-Service (DBaaS) offering.

Cloudant Local provides you with the same basic capabilities as the full Cloudant single-tenant offering,
but hosted within your own data center installation.

A more detailed overview of Cloudant Local is <a href="http://www-01.ibm.com/support/knowledgecenter/SSTPQH_1.0.0/com.ibm.cloudant.local.install.doc/topics/clinstall_cloudant_local_overview.html?lang=en-us" target="_blank">available</a>.

The <a href="http://www-01.ibm.com/support/knowledgecenter/SSTPQH_1.0.0/com.ibm.cloudant.local.doc/SSTPQH_1.0.0_welcome.html?lang=en" target="_blank">IBM Knowledge Center</a> provides information on many aspects of Cloudant Local,
including:

- <a href="http://www.ibm.com/support/knowledgecenter/SSTPQH_1.0.0/com.ibm.cloudant.local.install.doc/topics/clinstall_extract_install_cloudant_local.html?lang=en" target="_blank">Installation and Configuration</a>
- <a href="http://www-01.ibm.com/support/knowledgecenter/SSTPQH_1.0.0/com.ibm.cloudant.local.install.doc/topics/clinstall_maintenance_tasks_overview.html?lang=en" target="_blank">Maintenance Tasks</a>
- <a href="http://www-01.ibm.com/support/knowledgecenter/SSTPQH_1.0.0/com.ibm.cloudant.local.install.doc/topics/clinstall_tuning_parameters_replication_cases.html?lang=en" target="_blank">Tuning replication parameters</a>

### Cloudant on Bluemix Local
Cloudant on Bluemix Local is a NoSQL database-as-a-service (DBaaS) built from the ground up to scale globally, run non-stop, and handle a wide variety of data types like JSON, full-text, and geospatial. Cloudant is an operational data store optimized to handle concurrent reads & writes, and provide high availability and data durability.

####Prerequisites
To ensure that Cloudant on Bluemix Local functions properly, ensure that you follow these requirements with your installation.  

*	Use a Debian version 8 operating system for deployed virtual machines.   
*	Use one of the supported VMware platforms, either version 5.5 or 6.0.  

####Requirements 
You must meet the following requirements to run Cloudant on Bluemix Local.

<table>
<tr>
<th>Type</th>
<th>Requirement</th>
</tr>
<tr><td>Cluster requirements   </td>
<td>Cloudant on Bluemix Local requires two clusters minimum. One cluster internally
powers the Bluemix platform, while the other cluster powers external customer accounts and data.   </td>
</tr>
<tr><td>Network setting for virtual switches   </td>
<td>Set the maximum transmission unit (MTU) value to 9000 for virtual switches.   </td>
</tr>
<tr><td>External internet access requirement</td>
<td>External internet access is required. However, there is no need to change your network settings. The Cloudant initial architecture design routes external internet traffic to pypi, rubygems, github, and dynect through the tether. Future versions will pull all dependencies into the local deployment, eliminating this requirement.    </td>
</tr>
<tr><td>Virtual machine</td>
<td>In order to ensure the highest possible performance for your database deployment, Cloudant requires that each virtual machine meet the following specifications.  

<ul><li>Set up VMs using a thick provision eager zeroed disk.</li>
<li>Configure the infra-auxiliary VM and the three data partitions for the backup database VMs using thin provisioning.</li></ul>

This configuration equals 7 TB thick and 21 TB thin virtual disks. Initially, you must be prepared to use 8 TB virtual disk space out of the box.</td>
</tr>
</table>

#### Hardware Requirements for Cloudant on Bluemix Local
Before you install Cloudant® on Bluemix Local, confirm that your system meets these requirements. The requirements include hardware and cluster  requirements, Cloudant VM distribution and physical host recommendations, and Logmet hardware requirements for installing the product.

<table>
<tr>
<th>Type</th>
<th>Count</th>
<th>Optional?</th>
<th>VM name format</th>
<th>min vCPU</th>
<th>recommended vCPU</th>
<th>min RAM (GB)</th>
<th>recommended RAM (GB)</th>
<th>Disk-OS (GB)</th>
<th>Disk Config-OS</th>
<th>min Disk-Data (GB)</th>
<th>recommended min Disk-Data (GB)</th>
<th>Disk Config-Data</th>
<th>Network (Gbps)</th>
</tr>

<tr>
<td>Infra</td>
<td>1</td>
<td>No</td>
<td>infra1.bml-<\customer\></td>
<td>8</td>
<td>8</td>
<td>16</td>
<td>16</td>
<td>10</td>
<td>VMDK-thick eager zeroed</td>
<td>3000</td>
<td>3000</td>
<td>VMDK-thin/independent persistent</td>
<td>1</td>
</tr>

<tr>
<td>SAPI</td>
<td>2</td>
<td>No</td>
<td>sapi<\#\>.bml-<\customer\></td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>10</td>
<td>VMDK-thick eager zeroed</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>1</td>
</tr>

<tr>
<td>Load Balancer (Bluemix Ops Cluster)</td>
<td>2</td>
<td>No</td>
<td>lb<\#\>.bml-ops-<\customer\>001</td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>10</td>
<td>VMDK-thick eager zeroed</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>1</td>
</tr>

<tr>
<td>Load Balancer (Customer Cluster)</td>
<td>2</td>
<td>No</td>
<td>lb<\#\>.bml-<\customer\>001</td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>10</td>
<td>VMDK-thick eager zeroed</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>1</td>
</tr>

<tr>
<td>DB Node (Bluemix Ops Cluster)</td>
<td>3</td>
<td>No</td>
<td>db<\#\>.bml-ops-<\customer\>001</td>
<td>8</td>
<td>8</td>
<td>16</td>
<td>16</td>
<td>10</td>
<td>VMDK-thick eager zeroed</td>
<td>800</td>
<td>800</td>
<td>VMDK-thick eager zeroed/independent persistent</td>
<td>1</td>
</tr>

<tr>
<td>DB Node (Customer Cluster) </td>
<td>3</td>
<td>No</td>
<td>db<\#\>.bml-<\customer\>001</td>
<td>8</td>
<td>48</td>
<td>16</td>
<td>64</td>
<td>10</td>
<td>VMDK-thick eager zeroed</td>
<td>800</td>
<td>1000</td>
<td>VMDK-thick eager zeroed/independent persistent</td>
<td>1</td>
</tr>

<tr>
<td>Load Balancer (Backup Cluster)</td>
<td>2</td>
<td>Yes</td>
<td>lb<\#\>.bml-<\customer\>-bk001</td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>8</td>
<td>10</td>
<td>VMDK-thick eager zeroed</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>1</td>
</tr>

<tr>
<td>DB Node (Backup Cluster)</td>
<td>3</td>
<td>Yes</td>
<td>db<\#\>.bml-<\customer\>-bk001</td>
<td>8</td>
<td>24</td>
<td>16</td>
<td>64</td>
<td>10</td>
<td>VMDK-thick eager zeroed</td>
<td>800</td>
<td>18000</td>
<td>VMDK-thin/independent persistent</td>
<td>1</td>
</tr>
</table>

###### Logmet hardware requirements							
<table>
<tr>
<th>Type</th>
<th>Count</th>
<th>Optional?</th>
<th>min vCPU</th>
<th>recommended vCPU</th>
<th>min RAM (GB)</th>
<th>recommended RAM (GB)</th>
<th>min Disk (GB)</th>
<th>recommended Disk (GB)</th>
</tr>
<tr>
<td>Logmet Core</td>
<td>3</td>
<td>No</td>
<td>4</td>
<td>4</td>
<td>20</td>
<td>20</td>
<td>900</td>
<td>900</td>
</tr>
<tr><td>Logmet HAProxy
</td>
<td>2</td>
<td>No</td>
<td>1</td>
<td>1</td>
<td>4</td>
<td>4</td>
<td>40</td>
<td>40</td></tr>
<tr>
<td>Logmet Manager
</td>
<td>1</td>
<td>No</td>
<td>1</td>
<td>1</td>
<td>4</td>
<td>4</td>
<td>40</td>
<td>40</td></tr>
<tr><td>Logmet Expansion
</td>
<td>3</td>
<td>Yes</td>
<td>3</td>
<td>3</td>
<td>12</td>
<td>12</td>
<td>600</td>
<td>600</td>
</tr>
<td>CFS Ops
</td>
<td>1</td>
<td>No</td>
<td>2</td>
<td>2</td>
<td>8</td>
<td>8</td>
<td>350</td>
<td>350</td>
</tr>
</table>

##### Cloudant virtual machine distribution and physical host recommendations			
These recommendations assume that you are using the required hardware for Cloudant on Bluemix Local and a backup cluster.		

<table>
<tr>
<th>Host</th>
<th>vCPU</th>
<th>RAM used</th>
<th>VMs deployed</th>
</tr>

<tr><td>1</td>
<td>48</td>
<td>64</td>
<td>db1.bml-<customer>001</td>
</tr>
<tr><td>2</td>
<td>48</td>
<td>64</td>
<td>db2.bml-<customer>001</td>
</tr>
<tr><td>3</td>
<td>48</td>
<td>64</td>
<td>db3.bml-<customer>001</td>
</tr>
<tr><td>4</td>
<td>48</td>
<td>96</td>
<td>lb1.bml-<customer>001
lb1.bml-ops-<customer>001
db1.bml-ops-<customer>001
db1.bml-<customer>-bk0011</td>
</tr>
<tr><td>5</td>
<td>48</td>
<td>96</td>
<td>lb2.bml-<customer>001
lb2.bml-ops-<customer>001
db2.bml-ops-<customer>001
db2.bml-<customer>-bk0011</td>
</tr>
<tr><td>6</td>
<td>44</td>
<td>92</td>
<td>lb1.bml-<customer>-bk001
db3.bml-ops-<customer>001
db3.bml-<customer>-bk001
sapi1.bml-<customer></td>
</tr>
<tr><td>7</td>
<td>20</td>
<td>38</td>
<td>lb2.bml-<customer>-bk001
sapi2.bml-customer
infra1.bml-customer</td>
</tr>
</table>

#### Frequently Asked Questions about Cloudant on Bluemix Local

**How is Cloudant for Bluemix Local deployed?**
<p>You must download the OVA and ISO files and upload them to the datastore. You then
provide your network, datastore, and locations of the OVA and ISO files to Cloudant. Cloudant runs a script and wraps the ovftool, which creates VMs that are ISO mounted and use the proper settings. A startup script, packaged in the OVA, configures the networking and sets up reverse SSH tunneling. The remaining provisioning tasks are run by Chef configuration management.</p>

**Where are the Cloudant virtual machines deployed?**
<p>The VMs deploy within the private VLANs inside your Bluemix Local deployment.</p>

**Can Cloudant be deployed within a normal customer maintenance window?**
<p>Deploying Cloudant in your data center is a lengthy process. Currently, Cloudant needs approximately 1-2 weeks to deploy and verify your installation. Support is working to improve the deployment and automation process. </p>

**Does Cloudant follow the same Bluemix CR/DR process? Can I decide when changes are deployed?**
**Can I review the changes before they are deployed?**
<p>Cloudant does not follow the CR/DR process. Cloudant is delivered as a service and manages thousands of
machines between public DBaaS and Bluemix Local. Support uses Chef to handle configuration management across
our infrastructure, including clusters in Bluemix Local. As a result, non-disruptive changes are delivered
regularly multiple times a week and sometimes multiple times per day. Therefore, changes and updates are not
bound to predetermined maintenance windows. Cloudant does not require customer sign-off on
changes and updates to their clusters in Bluemix Local.</p>

**What about changes that are potentially disruptive?**
<p>While the vast majority of updates are not disruptive, Cloudant may deploy changes that cause a temporary outage. These outages are rare. If an outage occurs, Cloudant will coordinate with you to find a maintenance window that minimizes any disruption to your business.</p>

**What name displays in the catalog for Cloudant service?**
<p>The Cloudant service name displays as "Local".</p>

**How does Cloudant obtain IP addresses for the virtual machines?**
<p>Cloudant is on the private network inside Bluemix Local and only requires private IPs, which are provided by the Bluemix team.</p>

**Does Cloudant have an architecture diagram for deployments in Bluemix Local?**
<p>Yes, it can be found here, ![alt tag](images/bml_architecture_diagram.png).</p>

**Who is responsible for the Cloudant service broker?**
<p>Cloudant makes the appropriate changes to the service broker. If you have an existing dedicated cluster, Cloudant configures the broker to point to the new local cluster and follows the normal Bluemix
CR/DR process.</p>

**How will Cloudant operations access my Bluemix Local environment?**
<p>The Cloudant team uses the existing tether/relay provided by Bluemix. No new networking
requirements are required for Cloudant to access your environment.</p>

**What is Logmet? Why does Cloudant need it?**
<p>Logmet is our logging infrastructure. Logmet requires its own hardware resources. Cloudant sends logs to
Logmet so that your information can be stored locally. Logmet is a separate deployment. You do not need one
Logmet deployment per Cloudant cluster. All Cloudant clusters, within one Bluemix Local environment, share the same Logmet instance.</p>

**Where do you send metrics and monitoring information?**
<p>Cloudant receives metrics and monitoring information through the tether. Without it, you cannot properly maintain your local cluster.<p>

**How is VMware clustering set up for Cloudant, Logmet, and Bluemix?**
<p>Cloudant must be on a VMware cluster separate from Bluemix to prevent noisy neighbor
problems. Logmet must be in the same cluster with Bluemix.</p>

**How are virtual machines distributed across hosts?**
<p>Cloudant determines which VMs deploy and on which hosts. The goal is to keep database nodes and
load balancers separate, so if one host goes down, the cluster continues to operate. Research is in progress to  determine how to enable DRS with specific rules in order to keep VMs separate.</p>

**Does Cloudant feed logs to the QRadar deployment that is included with Bluemix Local?**
<p>Yes. Cloudant sends `auth` and `auditd` logs to QRadar and stores them for 1 year.</p>

**How does backup work?**
<p>Cloudant offers a backup service that schedules and runs incremental backups of your data. It is strongly
recommended that you purchase a separate cluster, specifically dedicated to storing backup data. The Cloudant backup cluster must be inside the same Bluemix Local environment. More information on backing up your data can be found here, https://docs.cloudant.com/backup-guide.html.</p>

<p>Both the customer and ops cluster can backup to the same location. If you do not want to use the Cloudant
backup product, you are responsible for backing up your data.</p>

**Where can I find Bluemix Local documentation?**
<p>Blue Mix documentation is located here, https://console.ng.bluemix.net/docs/local/index.html#local.</p>