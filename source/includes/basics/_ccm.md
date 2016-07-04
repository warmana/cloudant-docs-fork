## Cloud Consumption Model

<aside class="warning" role="complementary" aria-label="availability">The Cloud Consumption Model (CCM) is a new tier-based pricing model,
available to new customers,
on specific Cloudant clusters.
At present:
<ul>
<li>Not all Cloudant customers have immediate access to the model.</li>
<li>Not all Cloudant clusters support the model.</li>
</ul></aside>

The CCM offers a number of performance and cost tiers.
The tiers costs range from free,
through to several thousand dollars per month,
depending on the storage capacity,
and the amount of data reads and writes.

The following table summarizes the tiers.

<aside class="warning" role="complementary" aria-label="indicativetierpricing">The costs and performance measures are indicative,
as at July 2016.
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
<td colspan="2">Base Cost (monthly)</td>
<td>$0</td>
<td>$50</td>
<td>$500</td>
<td>$5,000</td>
<td>$25,000</td>
</tr>
<tr>
<td colspan="2">Disk Space Included (GB)</td>
<td>1</td>
<td>5</td>
<td>100</td>
<td>1000</td>
<td>6000</td>
</tr>
<tr>
<td colspan="2">Disk Overages (per GB)</td>
<td>Not possible in this tier</td>
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
<td>3000</td>
<td>20000</td>
</tr>
<td>Writes (per sec)</td>
<td>10</td>
<td>20</td>
<td>150</td>
<td>2000</td>
<td>12000</td>
</tr>
<tr>
<td>Queries (per sec)</td>
<td>5</td>
<td>10</td>
<td>50</td>
<td>250</td>
<td>1000</td>
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

This is the initial storage capacity provided in the tier,
and is used for both data and index storage.

#### Disk Overages

All tiers are monitored for disk space used.
If the account exceeds the amount of storage inidcated for the tier,
the account is billed at the indicated cost, per additional GB used beyond the initial tier allocation, per month.

For example,
if you are on the Personal tier,
and your project disk usage increases to 107GB during a given month,
you have used 7GB more than the 100GB tier allocation,
and so would be billed an overage charge of $1 x 7GB = $7 for that month.

Overage is measured as the maximum number of GB above the initial tier allocation during a single monthly billing cycle.
For example,
if you start the month using 90GB of storage in a Personal tier,
then increase to 115GB for a week,
then drop back to 95GB for a week,
then increase to 108GB for a week,
then finish the month by dropping down to 80GB,
the maximum number of GB above the initial tier allocation was 15GB during the first week.
Therefore,
you would be billed an additional $1 x 15GB = $15 for that month.

#### Throughput

Throughput or data capacity usage is measured and identified as one of three kinds of events:

1.	A lookups which is a read of a specific document, based on its `_id`.
2.	A write, which is a write of an individual document. Currently, a write due to an index build is not included in the event count.
3.	A query, which is a request made to one of the Cloudant query endpoints, including the following:
	-	Primary Index ([`_all_docs`](database.html#get-documents))
	-	MapReduce View ([`_view`](creating_views.html#using-views))
	-	Search Index ([`_search`](search.html#queries))
	-	Geospatial Index ([`_geo`](geo.html#querying-a-cloudant-geo-index))
	-	Cloudant Query ([`_find`](cloudant_query.html#finding-documents-using-an-index))
	-	Changes ([`_changes`](database.html#get-changes))

The measurement of throughput is a simple count of the number of events of a given type,
per second.
If your account exceeds the number of events for the tier,
access is throttled.
For example,
if you are on the Personal tier,
your account could make a maximum of 200 lookup requests a second.
Subsequent lookup requests issued during that one second period would be throttled.

When the account is throttled because the number of events has been exceeded,
applications receive an HTTP [`429` Too Many Requests](http.html#429) response.

The supported client libraries (for [Java](libraries.html#java), [node.js](libraries.html#node.js), and [Python](libraries.html#python) languages) all have provision for handling a `429` response.
If your application uses another library or language,
you should ensure you have made adequate provision for handling a `429` response correctly.

### Service Level Agreement

The Service Level Agreement (SLA) is 99.9% for Cloudant-hosted plans.
If your Cloudant account is hosted on Bluemix,
your SLA is determined by your Bluemix account.

### Hardware specification

All tiers are implemented on multi-tenant clusters,
with full disk encryption.
All data is stored in triplicate,
across three separate physical nodes for High Availability and Data Recovery.

The tiers are currently available in the US South region,
with additional regions available in the future.
Availability is subject to demand.

An isolated (single-tenant) dedicated hardware environment can be provided in a Softlayer data center,
for an additional $5000 per month (indicative cost, as at July 2016).

### Support

All tiers (_except_ the Lite tier) include best effort support during business hours,
with a 24 hour Service Level Objective (SLO).

Additionally,
Gold Support offering a one hour response time SLA for Severity 1 issues can be purchased for a supplementary $500 per month (indicative cost, as at July 2016).

Severity 1 issues are defined as being where business-critical functionality is inoperable,
or a business-critical interface has failed.
The failure usually applies to a production environment,
and results in an inability to access services,
causing a critical impact on operations.
The failure condition requires an immediate solution.

All support correspondence is performed through the Support tab of the Cloudant Dashboard,
or through [Cloudant Support email](mailto:support@cloudant.com).

### CCM Accounts

As the CCM is made available on Cloudant clusters,
you will be able to create an account directly that specifies use of the CCM and your chosen tier.

Alternatively,
you can migrate an existing Cloudant account to the CCM.
If you do not yet have a Cloudant account,
create one by going to the [Cloudant Signup page](https://cloudant.com/sign-up/) and choosing any Shared cluster.

When you have a Cloudant account,
request that the account be moved to a CCM tiered plan by opening a ticket with [Cloudant Support email](mailto:support@cloudant.com).

Tiered plans are enabled one per Cloudant account.
They apply only to accounts created on [cloudant.com](https://cloudant.com/) and not [Bluemix](https://console.ng.bluemix.net/registration/).

If you already have a Cloudant account on Bluemix,
it will not be using the CCM tiered plans.
To create a Bluemix account with a CCM tiered plan,
create a new account on [Bluemix](https://console.ng.bluemix.net/registration/),
then replicate your data from the old Bluemix account into the new Bluemix account.

Once your account is using CCM,
the chosen tier can be adjusted on a monthly basis.
There is normally a slight delay between the opening of plan change request,
and the fulfillment of the provisioned throughput capacity.
