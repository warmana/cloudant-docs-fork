#### Frequently Asked Questions about Cloudant on Bluemix Local


*Does Cloudant have an architecture diagram for deployments in Bluemix Local?*
<p>Yes, it can be found here: https://ibm.box.com/s/7kycwiiyyoz4a651l6lkuafkylu0eo6p</p>

**How is Cloudant for Bluemix Local deployed?**
<p>You must download the OVA and ISO files and upload them to the datastore. You must
provide Cloudant information on the network, datastore, and locations of the OVA and ISO files. Cloudant runs a script and wraps ovftool. This process creates the VMs with the proper settings and ISOs mounted. A startup
script, packaged in the OVA, configures the networking and sets up reverse-ssh tunneling. Chef configuration management runs the remaining provisioning tasks.</p>

**Can Cloudant be deployed within a normal customer maintenance window?**
<p>Deploying Cloudant in your data center is still a lengthy process. Currently, Cloudant needs about 1-2 weeks of time to deploy and verify. Support is working to improve the deployment and automation process. </p>

**Does Cloudant follow the same Bluemix CR/DR process? Can I decide when changes are deployed?**
**Can I review the changes before they are deployed?**
<p>Cloudant does not follow the CR/DR process. Cloudant is delivered as a service and manages thousands of
machines between public DBaaS and Bluemix Local. Support uses Chef to handle configuration management across
our infrastructure, including clusters in Bluemix Local. As a result, non-disruptive changes are delivered
regularly multiple times a week and sometimes multiple times per day. Therefore, changes and updates are not
bound to predetermined maintenance windows. Cloudant does not require customer sign-off on
changes and updates to their clusters in Bluemix Local.</p>

**What about changes that are disruptive?**
<p>While the vast majority of updates are non-disruptive, Cloudant might deploy changes that cause a temporary outage. These outages are rare. In the event of an outage, Cloudant support will coordinate with you to find a maintenance window that is the least disruptive to deploy these types of releases.</p>

*What operating systems are available for Cloudant?*
<p>Cloudant uses Debian 8 exclusively.</p>

**Where are the Cloudant VMs being deployed?**
<p>The VMs deploy within the private VLANs inside of your Bluemix Local deployment.</p>

**How does Cloudant obtain IP addresses for the VMs?**
<p>Cloudant is on the private network inside of Bluemix Local and only requires private IPs, which are provided by the Bluemix team.</p>

**What name will display in the catalog for Cloudant service?**
<p>The Cloudant service name will display as "Local".</p>

*How many Cloudant clusters does I need?*
<p>Cloudant in Bluemix Local requires two clusters minimum. One cluster internally
powers the Bluemix platform, while the other cluster powers external customer accounts and data.</p>

**Who is responsible for the Cloudant service broker?**
<p>Support will make the appropriate changes to the service broker. If you have an existing dedicated cluster, support must configure the broker to point to the new local cluster. Support will follow the normal Bluemix
CR/DR process.</p>

*Does Cloudant require external internet access?*
<p>Yes, external internet access is required. However, there is no need to make any networking changes. The Cloudant initial architecture design routes external internet traffic to pypi, rubygems, github, and dynect through the tether. Future versions will pull all dependencies into the local deployment, eliminating this requirement.
</p>

**How does the Cloudant operations team access my Bluemix Local environment?**
<p>The Cloudant team uses the existing tether/relay provided by Bluemix. No new networking
requirements are required for Cloudant support to access the your environment.</p>

**What is Logmet? Why does Cloudant need it?**
<p>Logmet is our logging infrastructure. Logmet requires its own hardware resources. Cloudant sends logs to
Logmet so that your information can be stored locally. Logmet is a separate deployment. You do not need one
Logmet deployment per Cloudant cluster. All Cloudant clusters, within one Bluemix Local environment, can
share the same Logmet instance.</p>

**Where do you send metrics and monitoring information?**
<p>Metrics and monitoring information is sent to Cloudant through the tether. Without it, you could not properly maintain your local cluster.<p>

*Is thick provision eager zeroed required?*
<p>In order to ensure the highest possible performance for your database deployment, Cloudant requires that each virtual machine meet the following specifications.  

*	Set up VMs using a thick provision eager zeroed disk.
*	Configure the infra-auxiliary VM and the three data partitions for the backup database VMs using thin provisioning.

This configuration equals 7 TB thick and 21 TB thin virtual disks. Initially, you must prepare to use 8 TB virtual disk space out of the box.</p>

*How much disk space will I need on day 1?*
<p>Initially, you must prepare to use 8 TB virtual disk space out of the box.</p>

**How is VMware clustering set up for Cloudant, Logmet, and Bluemix?**
<p>Cloudant must be on a VMware cluster separate from Bluemix to prevent noisy neighbor
problems. Logmet must be in the same cluster with Bluemix.</p>

*Which versions of VMware are supported?*
<p>Versions 5.5 and 6.0.</p>

**How are VMs distributed across hosts?**
<p>Cloudant determines which VMs deploy and on which hosts. The goal is to keep database nodes and
load balancers separate, so if one host goes down, the cluster continues to operate. Research is in progress to  determine how to enable DRS with specific rules in order to keep VMs separated.</p>

*Are there any network requirements specific to Cloudant?*
<p>Yes. You must set the MTU to 9000 on the virtual switches.</p>

**Does Cloudant feed logs to the QRadar deployment that is included with Bluemix Local?**
<p>Yes. Cloudant sends `auth` and `auditd` logs to QRadar and stores them for 1 year.</p>

**How does backup work?**
<p>Cloudant offers a backup service that schedules and runs incremental backups of your data. It is strongly
recommended that you purchase a separate cluster, specifically dedicated to storing backup data. The Cloudant backup cluster must be inside the same Bluemix Local environment. More information on backing up your data can be found here, https://docs.cloudant.com/backup-guide.html.</p>

<p>Both the customer and ops cluster can backup to the same location. If you do not want to use the Cloudant
backup product, you are responsible for backing up your data.</p>

**Where can I find Bluemix Local documentation?**
<p>Blue Mix documentation is located here, https://console.ng.bluemix.net/docs/local/index.html#local.</p>
