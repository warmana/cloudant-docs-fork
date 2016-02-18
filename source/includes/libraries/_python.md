# Python

[python-cloudant](https://github.com/cloudant/python-cloudant) is a supported library for working with Cloudant using Python.

The library is a preview (alpha version). It does not currently have complete API coverage or documentation.

You're still with us? Okay, here is how to get started:

<pre class="thebe">
import cloudant

account = cloudant.Account('examples')
db = account.database('animaldb')
response = db.get('zebra')
print(response.json())
</pre>
