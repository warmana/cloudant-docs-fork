## Cloud Consumption Model

The Cloudant database service is available in a number of performance and cost tiers.
The tiers costs range from free,
through to several thousand dollars per month,
depending on the storage capacity,
and the amount of data reads and writes.

The following table summarizes the tiers.

<aside class="warning" role="complementary" aria-label="indicativetierpricing">The costs and performance measures are indicative,
as at June 2016.
For current values,
please contact [Cloudant Support](mailto:support@cloudant.com).</aside>

Plans | Lite | Starter | Personal | Professional | Enterprise
---|---|---|---|---|---
Base Cost (monthly) | $0 | $50| $500 | $5000 | $25000
Disk Space Included | 1GB | 5GB | 100GB | 1TB | 6TB
Disk Overages (per GB) | $1 | $1 | $1 | $1 | $1
Lookups (per sec) | 50? | 100? | 200 | 3000 | 20000
Writes (per sec) | ? | ? | 150 | 2000 | 12000
Queries (per sec) | ? | ? | 50 | 250 | 1000

#### Disk Space Included

This is the maximum storage provided with the tier,
and is used for both data and index storage.

#### Disk Overages

All tiers are monitored for disk space used.
If the account exceeds the amount of storage allocated for the tier,
the account is billed at the indicated cost, per GB, per month.

#### Throughput

Throughput or data capacity usage is measured and identified as one of three kinds of events:

1.	A lookups, which is a read of a specific document, based on its `_id`.
2.	A write, which is a write of an individual document, or a write due to an index build.
3.	A query, which is a request made to one of the Cloudant query endpoints, including the following:
	-	Primary Index ([`_all_docs`](database.html#get-documents))
	-	MapReduce View ([`_view`](creating_views.html#using-views))
	-	Search Index ([`_search`](search.html#queries))
	-	Geospatial Index ([`_geo`](geo.html#querying-a-cloudant-geo-index))
	-	Cloudant Query ([`_find`](cloudant_query.html#finding-documents-using-an-index))
	-	Changes ([`_changes`](database.html#get-changes))

If your account exceeds the number of events for the tier,
access is throttled.
When the account is throttled because the number of events has been exceeded,
applications receive an HTTP [`429` Too Many Requests](http.html#429) response. 

The supported client libraries ([Java](libraries.html#java), [node.js](libraries.html#node.js), and [Python](libraries.html#python) languages all have provision for handling a `429` response.
If your application uses another library or language,
your should ensure you have made adequate provision for handling a `429` response correctly.

### Service Level Agreement

The Service Level Agreement (SLA) is 99.9% for all plans.

### Hardware specification

All tiers are implemented on multi-tenant clusters,
with full disk encryption.
All data is stored in triplicate,
across three separate physical nodes for High Availability and Data Recovery.

The tiers are currently available in the US South region,
with additional region available in the future,
based upon demand.

Single-tenant dedicated hardware can also be provided in any Softlayer data center.
for an additional $5000 per month (indicative cost, as at June 2016). 

### Support

All tiers include best effort support during business hours,
with a 24 hour Service Level Objective (SLO).

Additionally,
Gold Support offering a one hour response time SLA for Severity 1 (Sev 1) issues can be purchased for an supplementary $500 per month (indicative cost, as at June 2016).

Severity 1 issues are defined as being where business-critical functionality is inoperable, or a business-critical interface has failed.
The failure usually applies to a production environment,
and result in an inability to access services,
causing a critical impact on operations.
The failure condition requires an immediate solution.

All support correspondence is performed through the Support tab of the Cloudant Dashboard,
or through [Cloudant Support email](mailto:support@cloudant.com).

### Cloudant Accounts

To create a tiered account,
you must have an existing Cloudant account.
If necessary,
create a new Cloudant account by going to the [Cloudant Signup page](https://cloudant.com/sign-up/) and choosing any Shared cluster.

When you have a Cloudant account,
you then request that the account be moved to a tiered plan by opening a ticket with [Cloudant Support email](mailto:support@cloudant.com).

Tiered plans are enabled one per Cloudant account.
They apply only to accounts created on [cloudant.com](https://cloudant.com/) and not [Bluemix](https://console.ng.bluemix.net/registration/).

If you already have a Cloudant account on Bluemix,
you can create a new account on the [Cloudant Signup page](https://cloudant.com/sign-up/),
then replicate your data from the Bluemix account into the new account.

The tier associated with an account can be adjusted on a monthly basis.
There is normally a slight delay between the opening of plan change request,
and the fulfillment of the provisioned throughput capacity.

