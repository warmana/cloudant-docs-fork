## Monitoring a Cloudant cluster

A key part of ensuring best performance,
or troubleshooting any problems,
is monitoring the affected system.
You want to be able to answer the question:
"In what way has the system behavior changed as a result of any configuration or application modifications?"
To answer the question,
you need data.
The data comes from monitoring the system.

Monitoring the system while it replicates can be performed using the `_active_tasks` endpoint,
which is described in more detail [here](managing_tasks.html).

For more detailed system information,
you make use of the cluster monitoring API,
"knockwurst".

### Monitoring metrics overview

When monitoring the cluster,
you can obtain data about how it is performing.
Details such as the number of HTTP requests processed per second,
or how many documents are processed per second,
can all be obtained through the monitoring API.

The API can be invoked only by an administrative user,
and is applied to a specific monitoring endpoint.
For example,
if you wanted to monitor the number of documents processed by a map function each second,
you would direct the request to the `map_doc` endpoint.
A full list of the available endpoints is [available](monitoring.html#monitoring_endpoints).

### Monitoring endpoints

The following table lists the available monitoring endpoints provided by the API.

=============== Source code from github ===============

        The request must be both authenticated as and provide the
        ``X-Cloudant-User`` header of an admin account on the cluster.
        By default, data returned is for the last 5 minutes. In order to specify
        a different timeseries query, provide either a ``start`` or ``end``
        timestamp along with a desired ``duration``.
        Providing a value for ``duration`` without specifying one of ``start`` or ``end``
        will default to a timeseries query for data from the last ``duration`` amount of
        time until now.
        :arg target: name of a single metric (i.e. ``disk_use``)
        :query cluster: name of the cluster for which metrics are to be returned
                        user must be an admin for this cluster
        :query format: one of ``raw``, ``json`` (defaults to ``json``)
        :query start: UTC timestamp in ISO-8601 or integer seconds since epoch format
                      specifies starting point of a timeseries query
                      mutually exclusive with ``end`` param
        :query end: UTC timestamp in ISO-8601 or integer seconds since epoch format
                    specifies end point of a timeseries query
                    mutually exclusive with ``start`` param
        :query duration: one of ``5min``, ``30min``, ``1h``, ``12h``, ``24h``, ``1d``,
                         ``3d``, ``7d``, ``1w``, ``1m``, ``3m``, ``6m``, ``12m``, ``1y``
                         specifies the duration of the desired timeseries query,
                         must be paired with either ``start`` or ``end``
        :statuscode 200: no error
        :statuscode 400: unsupported format requested either ``raw`` or
                         ``json``
        :statuscode 404: unknown group or target requested

=============== Wil's gist ===============

# Knockwurst
 
## Syntax
 
* curl -u [ADMIN_USER] https://[ADMIN USER].cloudant.com/_api/v2/monitoring/[END_POINT]?cluster=[CLUSTER]
 
## Output
 
### With ?format=raw
 
Using disk_use as an example:
 
* curl -u myusername https://myusername.cloudant.com/_api/v2/monitoring/disk_use?cluster=myclustername&format=raw
 
sumSeries(net.cloudant.mycustomer001.db*.df.srv.used),1391019780,1391020080,60|344708448256.0,345318227968.0,346120126464.0,346716471296.0,175483256832.0
sumSeries(net.cloudant.mycustomer001.db*.df.srv.free),1391019780,1391020080,60|6.49070326579e+12,6.4896982057e+12,6.48884414054e+12,6.48801589658e+12,4.32277107507e+12
 
The text string is the name of the metric stored in our graphite server (the current backend to the API).
 
The next three numbers are start, end (both expressed as UTC epoch seconds) and step size (seconds). The numbers after the | (for this example) are bytes stored (the output of a df).
 
### With format=json (default)
 
* curl -u myusername https://myusername.cloudant.com/_api/v2/monitoring/disk_use?cluster=myclustername&format=json
 
Each value is [datapoint, timestamp].
 
[{"target": "sumSeries(net.cloudant.mycustomer001.db*.df.srv.used)", "datapoints": [[523562172416.0, 1391019360], [524413976576.0, 1391019420], [519036682240.0, 1391019480], [518762102784.0, 1391019540], [523719393280.0, 1391019600]]}, {"target": "sumSeries(net.cloudant.mycustomer001.db*.df.srv.free)", "datapoints": [[6488926978048.0, 1391019360], [6487768301568.0, 1391019420], [6493145661440.0, 1391019480], [6493420257280.0, 1391019540], [4330660167680.0, 1391019600]]}]
 
## End points
 
Use this request to list all of the currently supported end points:
 
* curl -u myusername https://myusername.cloudant.com/_api/v2/monitoring
 
### End point descriptions
 
"map_doc" - number of documents processed by a map function/sec
"kv_emits" - number of key:value emits/sec
"rps" - reads per second
"wps" - writes per second
"rate/status_code" - rate of requests by status code
"rate/verb" - rate of requests by HTTP verb
"disk_use" - disk use
"response_time" - average response time to a request in ms
 
### Request examples
 
#### map_doc
 
* curl -u myusername https://myusername.cloudant.com/_api/v2/monitoring/map_doc?cluster=myclustername&format=json
 
#### kv_emits
 
* curl -u myusername https://myusername.cloudant.com/_api/v2/monitoring/kv_emits?cluster=myclustername&format=json
 
#### rps
 
* curl -u myusername https://myusername.cloudant.com/_api/v2/monitoring/rps?cluster=myclustername&format=json
 
#### wps
 
* curl -u myusername https://myusername.cloudant.com/_api/v2/monitoring/wps?cluster=myclustername&format=json
 
#### rate/status_code
 
* curl -u myusername https://myusername.cloudant.com/_api/v2/monitoring/rate/status_code?cluster=myclustername&format=json
 
#### rate/verb
 
* curl -u myusername https://myusername.cloudant.com/_api/v2/monitoring/rate/verb?cluster=myclustername&format=json
 
#### disk_use
 
* curl -u myusername https://myusername.cloudant.com/_api/v2/monitoring/disk_use?cluster=myclustername&format=json
 
#### response_time
 
* curl -u myusername https://myusername.cloudant.com/_api/v2/monitoring/response_time?cluster=myclustername&format=json 