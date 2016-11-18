---

copyright:
  years: 2015, 2016
lastupdated: "2016-11-14"

---
{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}

# Account

Your account is your entry point for the {{site.data.keyword.cloudant}} API.
You access your account using the address prefix
`https://$USERNAME.cloudant.com`.
Your Cloudant dashboard is always
`https://$USERNAME.cloudant.com/dashboard.html`.
{:shortdesc}

If you don't yet have an account, [sign up](https://cloudant.com/sign-up/){:new_window}.

## Ping

To see if your Cloudant account is accessible,
make a `GET` against `https://$USERNAME.cloudant.com`.
If you misspelled your account name,
you might get a [503 'service unavailable' error](/docs/api/http.html#503).

_Example of connecting to your Cloudant account, using HTTP:_

```
GET / HTTP/1.1
HOST: $USERNAME.cloudant.com
```
{:screen}

_Example of connecting to your Cloudant account, using the command line:_

```
curl -u $USERNAME https://$USERNAME.cloudant.com
```
{:screen}

_Example of connecting to your Cloudant account, using Javascript:_

```
var nano = require('nano');
var account = nano("https://$USERNAME:$PASSWORD@$USERNAME.cloudant.com");
account.request(function (err, body) {
	if (!err) {
		console.log(body);
	}
});
```
{:screen}

_Example of connecting to your Cloudant account, using Python:_

```
import cloudant
account = cloudant.Account(USERNAME)
ping = account.get()
print ping.status_code
# Expected return code: 200
```
{:screen}

## CORS

[Cross-origin resource sharing (CORS)](http://www.w3.org/TR/cors/){:new_window} is a
mechanism that allows Javascript from another domain to interact with data in
your Cloudant account.

More information about CORS and Cloudant is available [here](/docs/api/cors.html).
