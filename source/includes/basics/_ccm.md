## Cloud Consumption Model

<aside class="warning" role="complementary" aria-label="availability">The Cloud Consumption Model (CCM) is a new tier-based pricing model,
available to new customers,
on specific Cloudant clusters.
At present:
<ul>
<li>Not all Cloudant customers have immediate access to the model.</li>
<li>Not all Cloudant clusters support the model.</li>
</ul></aside>

The Cloud Consumption Model (CCM) offers a number of performance and pricing tiers
for using [Cloudant on Bluemix](https://www.ng.bluemix.net/docs/#services/Cloudant/index.html#Cloudant).
The tiers are distinguished by the maximum number of Lookups,
Writes,
and Queries.
Each tier has a base 20GB storage allocation,
with additional storage available
at $1 per GB per month (indicative pricing as at August 2016) .
The tier prices range from free,
through to several thousand dollars per month,
depending on the configuration you choose.

<div id="servicetier"></div>

You can see details of the tiers within the plans available for your Account,
and select the tier you wish to use,
through the Account tab of your Cloudant account Dashboard.
![Account Dashboard](images/AccountsCCM01.png)

To move to a different plan,
login to Bluemix using your Account details,
then go to the Service Catalog page for Cloudant.

The following table summarizes the price and performance measures for each of the tiers.

<aside class="warning" role="complementary" aria-label="indicativetierpricing">Note that the details in the table are indicative as at August 2016.
For current values,
please contact [Cloudant Support](mailto:support@cloudant.com).</aside>

<table border="1">
<tr>
<th colspan="2">Plans</th>
<th>Lite</th>
<th>Starter</th>
<th>Personal</th>
<th>Professional</th>
<th>Enterprise</th>
</tr>
<tr>
<td colspan="2">Base Price (monthly)</td>
<td>$0</td>
<td>$65</td>
<td>$375</td>
<td>$3,000</td>
<td>$16,000</td>
</tr>
<tr>
<td colspan="2">Disk Space Included (GB)</td>
<td>1</td>
<td>5</td>
<td>20</td>
<td>20</td>
<td>20</td>
</tr>
<tr>
<td colspan="2">Disk Space Overflow (per GB)</td>
<td><!--Not possible in this tier-->$1</td>
<td>$1</td>
<td>$1</td>
<td>$1</td>
<td>$1</td>
</tr>
<tr>
<td rowspan="3" valign="top">Throughput</td>
<td>Lookups (per sec)</td>
<td>10</td>
<td>20</td>
<td>200</td>
<td>3,000</td>
<td>20,000</td>
</tr>
<td>Writes (per sec)</td>
<td>10</td>
<td>20</td>
<td>150</td>
<td>2,000</td>
<td>12,000</td>
</tr>
<tr>
<td>Queries (per sec)</td>
<td>5</td>
<td>10</td>
<td>50</td>
<td>250</td>
<td>1,000</td>
</tr>
<tr>
<td colspan="2">Service SLA</td>
<td colspan="5" align="center">99.9%</td>
</tr>
<tr>
<td colspan="2" rowspan="2">Support SLA</td>
<td rowspan="2">Community OR Best Effort</td>
<td colspan="4">Business hours, 24 hour response Service Level Objective (SLO)</td>
</tr>
<tr>
<td colspan="4">Optional: 1 hour response for Severity 1 issues: $500 pr month</td>
</tr>
<tr>
<td colspan="2">Dedicated Hardware (monthly)</td>
<td>Not available in this tier</td>
<td colspan="4" align="center">$5,000</td>
</tr>
</table>

#### Disk Space Included

This is the storage capacity included in the tier.
It is used for both data and index storage.

#### Disk Space Overflow

All tiers are monitored for disk space used.
If the account uses more than the amount of storage indicated for the tier,
that is,
'overflows',
the account is billed at the indicated price for each additional GB used beyond the initial tier allocation.
The overflow use is calculated on an hourly basis.

For example,
if you are on the Personal tier,
and your project disk usage increases to 107GB for half a day (12 hours) during a given month of 31 calendar days,
you have overflowed by 7GB more than the 100GB tier allocation,
for 12 / (31 x 24) = 12 / 744 = 1.6% of the month.
This means you would be billed an overflow charge of $1 x 7GB x 1.6% = $0.11 for that month.

Overflow is measured as the maximum number of GB above the initial tier allocation during a single hour within the billing cycle.
For example,
if you start a 28-day month using 90GB of storage in a Personal tier,
then increase to 115GB for 15 minutes during hour 2 of day 3,
then drop back to 95GB for the next 10 minutes of hour 2,
then increase to 108GB for the next 25 minutes of hour 2,
then finish the hour and indeed the rest of month by dropping down to 80GB,
the maximum number of GB above the initial tier allocation was 15GB during hour 2 of day 3.
Therefore,
you would be billed an additional $1 x 15GB x ( 1 / (28 x 24) ) = $1 x 15GB x 0.2% = $0.02 for that month.

#### Throughput

Throughput is measured and identified as one of three kinds of events:

1.	A lookups which is a read of a specific document, based on its `_id`.
2.	A write, which is a write of an individual document, or a write due to an index build.
3.	A query, which is a request made to one of the Cloudant query endpoints, including the following:
	-	Primary Index ([`_all_docs`](database.html#get-documents))
	-	MapReduce View ([`_view`](creating_views.html#using-views))
	-	Search Index ([`_search`](search.html#queries))
	-	Geospatial Index ([`_geo`](geo.html#querying-a-cloudant-geo-index))
	-	Cloudant Query ([`_find`](cloudant_query.html#finding-documents-using-an-index))
	-	Changes ([`_changes`](database.html#get-changes))

The measurement of throughput is a simple count of the number of events of a given type,
per second,
where the second is a sliding window.
If your account exceeds the number of events for the tier,
requests are rejected until the number of events within the sliding window no longer exceeds that permitted within the tier.
It might be easier to think of the sliding one second window as being any consecutive period of 1,000 milliseconds.

For example,
if you are on the Personal tier,
your account could make a maximum of 200 lookup requests during a consecutive period of 1,000 milliseconds (one second).
Subsequent lookup requests issued during the sliding 1,000 millisecond period are rejected until the number of loopup requests in that period drops below 200 again.

When the a request is rejected because the number of events has been exceeded,
applications receive an HTTP [`429` Too Many Requests](http.html#429) response.

The supported client libraries (for [Java](libraries.html#java), [node.js](libraries.html#node.js), and [Python](libraries.html#python) languages) all have provision for handling a `429` response.
If your application uses another library or language,
you should ensure you have made adequate provision for handling a `429` response correctly.

#### Locations

By default,
all plans are based on multi-tenant clusters.
As part of your plan selection,
you can choose from the following [Softlayer data centers](http://www.softlayer.com/data-centers):
-	Softlayer Dallas
- Softlayer London
- Softlayer Sydney
-	Softlayer Washington DC

Alternatively,
a dedicated single-tenant environment can be provided in any Softlayer data center,
for an additional $5000 per month, per data center (indicative as at August 2016).

#### Security, Encryption and Compliance

All plans are provided on servers with [at-rest](https://en.wikipedia.org/wiki/Data_at_rest) disk encryption.
Access is encrypted over a network connection using HTTPS.
For more detail,
see [DBaaS Security](https://cloudant.com/product/cloudant-features/dbaas-security/).

The plans also offer [Security Compliance Certification](https://cloudant.com/product/cloudant-features/cloudant-compliance/).
[HIPAA](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act) compliance requires a [single-tenant environment](ccm.html#locations),
so you should request this before provisioning.

#### High Availability, Disaster Recovery, and Backup

To provide High Availability (HA) and Disaster Recovery (DR) within a data center,
all data is stored in triplicate across three separate physical servers in a cluster.
You can provision accounts in multiple data centers,
then use continuous data replication to provide HA/DR across data centers.

Cloudant data is not automatically backed up.
You can request enablement of an [incremental backup feature](https://docs.cloudant.com/backup-guide.html),
or alternatively implement your own solution using one of several possible techniques
described [here](https://developer.ibm.com/clouddataservices/2016/03/22/simple-couchdb-and-cloudant-backup/).  

### Monitoring usage

Information about your usage is available in the Usage panel of the Activity tab within your Cloudant Dashboard.
![Monitoring usage on the dashboard](images/MonitoringCCM08.png).

Details are provided there,
illustrating your current [throughput](ccm.html#throughput),
and quantity of [stored data](ccm.html#disk-space-included).

If your monitoring indicates that a change to your service tier might be advisable,
for example if you are frequently approaching the maximum number of database lookups for your current tier,
then you can modify the tier through the [Service Tier panel](ccm.html#servicetier) on the Account tab of the Dashboard.

### Service Level Agreement

The Service Level Agreement (SLA) is 99.9% for Cloudant-hosted plans.
If your Cloudant account is hosted on [Bluemix](https://console.ng.bluemix.net/registration/),
your SLA is determined by your Bluemix account.

### Hardware specification

All tiers are implemented on multi-tenant clusters.
All data is stored in triplicate,
across three separate physical nodes for High Availability and Data Recovery.

The tiers are currently available in all [Bluemix](https://console.ng.bluemix.net/registration/) regions.
Availability in [`cloudant.com`](https://cloudant.com/) regions is subject to demand.

An isolated environment can be provided in a Softlayer data center,
for an additional $5000 per month (indicative price, as at August 2016).

### Support

All tiers (_except_ the Lite tier) include best effort support during business hours,
with a 24 hour Service Level Objective (SLO).

Additionally,
Gold Support offering a one hour response time SLA for Severity 1 issues can be purchased for a supplementary $500 per month (indicative price, as at August 2016).

Severity 1 issues are defined as being where business-critical functionality is inoperable,
or a business-critical interface has failed.
The failure usually applies to a production environment,
and results in an inability to access services,
causing a critical impact on operations.
The failure condition requires an immediate solution.

All support correspondence is performed through the Support tab of the Cloudant Dashboard,
or through [Cloudant Support email](mailto:support@cloudant.com).

### CCM Accounts

By default,
accounts created on [`cloudant.com`](https://cloudant.com/) do not use the CCM.
As the CCM is made available on Cloudant clusters,
you will be able to create an account directly that specifies use of the CCM and your chosen tier.

If you already have a Cloudant account on [Bluemix](https://console.ng.bluemix.net/registration/),
that is an account created before CCM was made available,
the account is not using the CCM tiered plans.
To create a Bluemix account with a CCM tiered plan,
create a new account on Bluemix,
then replicate your data from the old Bluemix account into the new Bluemix account.

Once your account is using CCM,
plan changes can be made at any time during the month.
However,
for any given hour,
you are charged at the rate of the highest priced plan used during that hour.
Also,
there is normally a slight delay between the opening of plan change request,
and the fulfillment of the provisioned throughput capacity.
