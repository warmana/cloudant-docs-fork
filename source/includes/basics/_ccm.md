## Cloud Consumption Model

<aside role="complementary" aria-label="availability">The Cloud Consumption Model (CCM) is a new plan-based pricing model,
available on Bluemix Public regions.</aside>

The CCM offers a number of performance and pricing plans
for using [Cloudant on Bluemix](https://www.ng.bluemix.net/docs/#services/Cloudant/index.html#Cloudant).
The Standard plan includes 20GB of data storage.
Above 20GB,
you are charged $0.0014 per GB per hour.
On the Standard plan,
you can also change the amount of provisioned throughput capacity for lookups, writes and queries.
The plan prices range from free,
through to several thousand dollars per month,
depending on the configuration you choose.

<aside class="warning" role="complementary" aria-label="pricing">All currency values in this document are in US dollars ($).</aside>

<div id="servicetier"></div>

You can see details of the throughput capacity within the plans available for your account,
and select the level of provisioning that you want to use,
through the Account tab of your Cloudant account Dashboard.
![Account Dashboard](images/AccountsCCM01.png)

To move to a different plan,
use your account details to log in to Bluemix,
then go to the Service catalog page for Cloudant.

<div id="servicetier"></div>

You can see details of the tiers within the plans available for your Account,
and select the tier you wish to use,
through the Account tab of your Cloudant account Dashboard.
![Account Dashboard](images/AccountsCCM01.png)

To move to a different plan,
login to Bluemix using your Account details,
then go to the Service Catalog page for Cloudant.

The following table summarizes the price and performance measures for each of the tiers.

<aside class="warning" role="complementary" aria-label="indicativetierpricing">The details in the table are indicative as at August 2016.
For current values,
contact [Cloudant Support](mailto:support@cloudant.com).</aside>

<table border="1" summary="A table summarizing the available pricing and performance details for each of the available plans of service.">
<tr valign="top">
<th colspan="2" id="planCharacteristic">Plans</th>
<th id="litePlan">Lite</th>
<th colspan="4" id="standardPlan">Standard</th>
</tr>
<tr>
<td colspan="2" headers="planCharacteristic" id="basePrice">Base Price (per hour)</td>
<td headers="litePlan basePrice">$0</td>
<td headers="standardPlan basePrice">$0.089</td>
<td headers="standardPlan basePrice">$0.5317</td>
<td headers="standardPlan basePrice">$4.1096</td>
<td headers="standardPlan basePrice">$21.9178</td>
</tr>
<tr>
<td colspan="2" headers="planCharacteristic" id="diskSpace">Disk Space Included (GB)</td>
<td headers="litePlan diskSpace">1</td>
<td headers="standardPlan diskSpace">20</td>
<td headers="standardPlan diskSpace">20</td>
<td headers="standardPlan diskSpace">20</td>
<td headers="standardPlan diskSpace">20</td>
</tr>
<tr>
<td colspan="2" headers="planCharacteristic" id="diskOverage">Disk Overage (per GB/hour)</td>
<td headers="litePlan diskOverage">Not available</td>
<td headers="standardPlan diskOverage">$0.0014</td>
<td headers="standardPlan diskOverage">$0.0014</td>
<td headers="standardPlan diskOverage">$0.0014</td>
<td headers="standardPlan diskOverage">$0.0014</td>
</tr>
<tr>
<td rowspan="3" valign="top" headers="planCharacteristic" id="throughputLabel">Throughput</td>
<td headers="planCharacteristic throughputLabel" id="lookups">Lookups (per sec)</td>
<td headers="litePlan throughputLabel lookups">10</td>
<td headers="standardPlan throughputLabel lookups">20</td>
<td headers="standardPlan throughputLabel lookups">200</td>
<td headers="standardPlan throughputLabel lookups">3,000</td>
<td headers="standardPlan throughputLabel lookups">20,000</td>
</tr>
<tr>
<td headers="planCharacteristic throughputLabel" id="writes">Writes (per sec)</td>
<td headers="litePlan throughputLabel writes">10</td>
<td headers="standardPlan throughputLabel writes">20</td>
<td headers="standardPlan throughputLabel writes">150</td>
<td headers="standardPlan throughputLabel writes">2,000</td>
<td headers="standardPlan throughputLabel writes">12,000</td>
</tr>
<tr>
<td headers="planCharacteristic throughputLabel" id="queries">Queries (per sec)</td>
<td headers="litePlan throughputLabel queries">5</td>
<td headers="standardPlan throughputLabel queries">10</td>
<td headers="standardPlan throughputLabel queries">50</td>
<td headers="standardPlan throughputLabel queries">250</td>
<td headers="standardPlan throughputLabel queries">1,000</td>
</tr>
</table>

#### Disk Space Included

This value is the storage capacity included in the plan.
It is used for both data and index storage.

#### Disk Overage

All standard plans are monitored for disk space used.
If the account uses more than the amount of storage that is provided in your plan configuration,
it is considered to 'overflow'.
An overflow causes the account to be billed at the indicated price for each extra GB used beyond the plan allocation.
The extra amount of money that you must pay for using more disk space than is provided in the plan is called an 'overage'.
Overage is calculated on an hourly basis.
It is not possible to overflow the disk space available in the Lite plan.

For example,
assume that your Standard plan project increases disk usage to 107 GB for half a day (12 hours).
This change means your project caused an overflow of 87 GB more than the 20 GB plan allocation,
for 12 hours.
Therefore,
you would be billed an overage charge of $0.0014 x 87 GB x 12 hours = $1.46 for that extra space.

Overage is calculated by using the maximum number of GB above the plan allocation during a particular hour within the billing cycle.

##### A worked overage example

Assume that you start a month of 30 days with a Standard plan project that uses 9 GB of storage.
Next,
your storage increases to 21.5 GB for 15 minutes during the hour beginning at 02:00 of day 3.
The project drops back to 9.5 GB for the next 10 minutes of hour 02:00,
then increases to 108 GB for the next 25 minutes of hour 02:00.
Finally,
your project finishes the hour and indeed the rest of month by dropping down to 28 GB.

This pattern means the maximum number of GB above the plan allocation was 88 GB during hour 2 of day 3.
For hour 03:00 of day 3,
and for the rest of the month,
your project was 8 GB above the plan allocation.

Therefore,
for hour 02:00 of day 3,
you would be billed an overage of $0.0014 x 88 GB x 1 hour = $0.1232.

For hour 03:00 of day 3 to the end of the month,
you would be billed an overage of ($0.0014 * 8 GB * 21 hours * 1 day) + ($0.0014 * 8 GB * 24 hours * 27 days) = $0.2352 + $7.2576 = $7.4928.

The total overage bill for the month would be $0.1232 + $7.4928 = $7.62.

#### Throughput

Throughput provision is identified and measured as one of three kinds of events:

1.	A lookup, which is a read of a specific document, based on its `_id`.
2.	A write, which is a write of an individual document, or a write due to an index build.
3.	A query, which is a request made to one of the Cloudant query endpoints, including the following types:
	-	Primary Index ([`_all_docs`](database.html#get-documents))
	-	MapReduce View ([`_view`](creating_views.html#using-views))
	-	Search Index ([`_search`](search.html#queries))
	-	Geospatial Index ([`_geo`](geo.html#querying-a-cloudant-geo-index))
	-	Cloudant Query ([`_find`](cloudant_query.html#finding-documents-using-an-index))
	-	Changes ([`_changes`](database.html#get-changes))

The measurement of throughput is a simple count of the number of events of each type,
per second,
where the second is a _sliding_ window.
If your account exceeds the number of throughput events that are provisioned for the plan,
requests are rejected until the number of events within the sliding window no longer exceeds the number provisioned.
It might help to think of the sliding one-second window as being any consecutive period of 1,000 milliseconds.

For example,
if you are on the Standard plan and have provisioned 200 lookups per second,
your account might make a maximum of 200 lookup requests during a consecutive period of 1,000 milliseconds (1 second).
Subsequent lookup requests made during the sliding 1,000 millisecond period are rejected until the number of lookup requests in that period drops below 200 again.

When a request is rejected because the number of events is exceeded,
applications receive an HTTP response: [`429` Too Many Requests](http.html#429).

The supported client libraries (for [Java](libraries.html#java), [node.js](libraries.html#node.js), and [Python](libraries.html#python) languages) all have the ability to handle a `429` response.
If your application uses another library or language,
ensure that it is able to handle a `429` response correctly.

#### Locations

By default,
all plans are based on multi-tenant clusters.
As part of your plan selection,
you can choose from the following Bluemix Public regions:

-	US South
- United Kingdom
- Sydney

#### Security, Encryption, and Compliance

All plans are provided on servers with [at-rest](https://en.wikipedia.org/wiki/Data_at_rest) disk encryption.
Access is encrypted over a network connection by using HTTPS.
For more detail,
see [DBaaS Security](https://cloudant.com/product/cloudant-features/dbaas-security/).

The plans also offer [Security Compliance Certification](https://cloudant.com/product/cloudant-features/cloudant-compliance/).
[HIPAA](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act) compliance requires a [single-tenant environment](ccm.html#locations),
so request this environment before provisioning.

#### High Availability, Disaster Recovery, and Backup

To provide High Availability (HA) and Disaster Recovery (DR) within a data center,
all data is stored in triplicate across three separate physical servers in a cluster.
You can provision accounts in multiple data centers,
then use continuous data replication to provide HA/DR across data centers.

Cloudant data is not automatically backed up.
You can request enablement of an [incremental backup feature](https://docs.cloudant.com/backup-guide.html),
or alternatively implement your own solution by using one of several possible techniques that are described [here](https://developer.ibm.com/clouddataservices/2016/03/22/simple-couchdb-and-cloudant-backup/).  

### Monitoring usage

Information about your usage is available in the Usage pane of the Activity tab within your Cloudant Dashboard.
![Monitoring usage on the dashboard](images/MonitoringCCM08.png).

Details are provided there,
illustrating your current [throughput](ccm.html#throughput),
and quantity of [stored data](ccm.html#disk-space-included).

If your monitoring indicates that a change to the provisioning in your plan might be advisable,
for example if you are frequently approaching the maximum number of database lookups,
then you can modify the provisioning through the [Service pane](ccm.html#servicetier) on the Account tab of the Dashboard.

### Hardware specification

All plans are implemented on multi-tenant clusters.
All data is stored in triplicate,
across three separate physical nodes for High Availability and Data Recovery.

### Support

Support for Standard plan (_not_ the Lite plan) is optional and provided by purchasing "Bluemix Standard Support".
The monthly cost (as at August 2016) is the greater of 10% of the account charge,
or $200.

A pricing calculator for Bluemix Standard Support is available
[here](https://console.ng.bluemix.net/?direct=classic/#/pricing/cloudOEPaneId=pricing&paneId=pricingSheet).
Information about the details of the Support Service Level Agreement (SLA) is available
[here](http://www-03.ibm.com/software/sla/sladb.nsf/pdf/6606-08/$file/i126-6606-08_05-2016_en_US.pdf).

### CCM Accounts

By default,
accounts created on [`cloudant.com`](https://cloudant.com/) do not use the CCM.
As the CCM is made available on Cloudant clusters,
you are able to create an account directly that specifies use of the CCM and your chosen plan.

If you already have a Cloudant account on [Bluemix](https://console.ng.bluemix.net/registration/)
that was created before CCM was made available),
the account is not using the CCM plans.
To create a Bluemix account with a CCM plan,
create a new account on Bluemix,
then replicate your data from the old Bluemix account into the new Bluemix account.

When your account is using CCM,
plan changes can be made at any time during the month.
However,
you are charged at the rate of the highest priced plan configuration that is used during the hour when the plan changes.
Also,
a slight delay normally occurs between the opening of plan change request,
and the fulfillment of the provisioned throughput capacity.
