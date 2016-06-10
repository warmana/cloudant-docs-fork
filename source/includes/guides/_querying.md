## Querying data

In this guide you learn how to create a database by replicating some sample data, and make queries
using Cloudant Query or map-reduce indexes. You can follow along and run our curl commands from
the browser.

## How to use the interactive guide

All code snippets can be *run and edited* in the browser. Make sure to follow along step-by-step
and run the examples in the correct order. If you skip one of the code snippets, other ones might
not work. For example, if you don't run the first step, creating a session token, none of the other
code snippets will work because you need the session token to authenticate. We encourage you to
change the examples and see how the service will respond.

Note: The interactive guide is only intended as a "playground" to try out Cloudant.
*Don't use it with sensitive data!*

You can find instructions on [how to run the code snippets locally](#running-code-locally) towards
the end of this guide.

### Logging in

Before you can do anything with the service, you need to obtain a session token. Use basic
authentication to get the token and then use the session token to authenticate. Otherwise,
requests will take longer because the service will need to verify your credentials at each step.

The following code sets up a few variables to authenticate to Cloudant. If you don't have an account
yet, you can [sign up](https://console.ng.bluemix.net/catalog/services/ibm-graph/) and copy your
credentials into the script.

Once the variables are set, the script sends a request to the [`/_session` endpoint](api.html#authentication).
The response contains your session token in the `SET-COOKIE` header, which curl stores in `cookie.txt`.

We use [jq](https://stedolan.github.io/jq/) to parse and display the JSON response.

<pre class="thebe">
# Copy your credentials(username, password, and account name) here.
USER='your username or api key here'
PASS='your password goes here'
URL='https://your-account-name.cloudant.com'
# some defaults for curl
alias curl='curl --max-time 60 --connect-timeout 5 --silent --show-error --cookie cookie.txt'
# get the session cookie and store it in cookie.txt
curl "${URL}/_session" -X POST -d "name=$USER" -d "password=$PASS" -c cookie.txt | jq '.'
</pre>

#### Things you might want to try - logging in

 * Change your user name or password and see what errors you get.
 * Look at the response header with `curl -v`.

### Replicating sample data

After successfully logging in, we create a new database by replicating a sample dataset from
examples.cloudant.com. We pipe the response through `jq '.'` for nicer output formatting.

The sample database contains 9,000 movie documents like the following one:

```json
{
    "_id": "71562",
    "_rev": "1-72726eda3b8b2973ef259dd0c7410a83",
    "title": "The Godfather: Part II",
    "year": 1974,
    "rating": "R",
    "runtime": "200 min",
    "genre": [
        "Crime",
        "Drama"
    ],
    "director": "Francis Ford Coppola",
    "writer": [
        "Francis Ford Coppola (screenplay)",
        "Mario Puzo (screenplay)",
        "Mario Puzo (based on the novel \"The Godfather\")"
    ],
    "cast": [
        "Al Pacino",
        "Robert Duvall",
        "Diane Keaton",
        "Robert De Niro"
    ],
    "poster": "http://ia.media-imdb.com/images/M/..._V1_SX300.jpg",
    "imdb": {
        "rating": 9.1,
        "votes": 656,
        "id": "tt0071562"
    }
}
```

<pre class="thebe">
# write everything until ENDREPLICATION into replication.json
cat << ENDREPLICATION >replication.json
{
  "source": "https://examples.cloudant.com/query-movies",
  "target": {
    "url": "$URL/movies",
    "headers": {
      "Cookie": "AuthSession=$(tail -1 cookie.txt | cut -f 7)"
    }
  },
  "create_target": true
}
ENDREPLICATION

curl "$URL/_replicate" \
     -X POST \
     -H 'Content-Type: application/json' \
     -d @replication.json \
| jq '.'
</pre>

This response to the replication request will give you a lot of stats about the replication job,
such has how many documents were replicated and whether there were any write failures. You can safely
ignore those details for now as long as you see `"ok": true`, indicating that the replication was successful.

Let's check that the list of your databases contains the one we just created.
To do that, we send a `GET` request to [`/_all_dbs`](database.html#get-databases).

<pre class="thebe">
curl "$URL/_all_dbs" | jq '.'
</pre>

#### Things you might want to try - creating a database

 * Changing the database name.
 * Creating multiple databases.
 * Using `curl "$URL/movies" -X DELETE` to remove the movies database.

### Creating an index

Cloudant supports different ways of querying data: Cloudant Query, map-reduce indexes, and full-text
search indexes. Let's start with the easiest one, Cloudant Query.

First, we'll need to create an index. We make a `POST` request to the `/_index` endpoint of our
newly created movies database containing a description of the index we want to create in the request
body.

<pre class="thebe">
curl "$URL/movies/_index" \
     -X POST \
     -H 'Content-Type: application/json' \
     -d '{
           "type": "text",
           "index": {}
         }' \
| jq '.'
</pre>

We choose a text index so that we'll be able to do full-text queries. Since we haven't specified
any fields to index, Cloudant Query will index everything.

#### Things to try

 * Creating an index of type `json`
 * Indexing only some fields
 * Have a look at the API reference to learn more about [creating Cloudant Query indexes](cloudant_query.html#creating-an-index)

### Querying data

With Cloudant Query, you can do far more complex queries, but let's start with something simple -
getting all movies with an IMDB rating of exactly 8. This time we send a `POST` request to the
`/_find` endpoint. Similarly to the index creation, we send a JSON document describing the
query in the request body. We limit our query to 3 so that the output won't be too long.

<pre class="thebe">
curl "$URL/movies/_find" \
     -X 'POST' \
     -H 'Content-Type: application/json' \
     -d '{
           "selector": {
             "imdb": { "rating": 8}
           },
           "limit": 3
         }' \
| jq '.'
</pre>

The result will contain 3 documents from our database that match the given selector. Try to change
the selector and run the code again to experiment with different conditions. The
[API reference for Cloudant Query](cloudant_query.html#finding-documents-using-an-index)
provides more in depth information about different querying options.

#### Sorting

To sort your results, just specify a field name and its type (`string` or `number`) to sort by. In
this example, we sort alphabetically by movie title. Setting `fields` to `["title"]` let's us
retrieve only the `title` field of each document.

<pre class="thebe">
curl "$URL/movies/_find" \
     -X 'POST' \
     -H 'Content-Type: application/json' \
     -d  '{
            "selector": {
              "year": 2001
            },
            "sort": [ "title:string" ],
            "fields": [ "title" ],
            "limit": 3
          }' \
| jq '.'
</pre>

#### Searching the entire document

Until now we have only searched within specific fields, but sometimes you might want to search the
entire document. The `$text` operator does just that (and more), as the following example
illustrates:

<pre class="thebe">
curl "$URL/movies/_find" \
     -X 'POST' \
     -H 'Content-Type: application/json' \
     -d  '{
            "selector": {
              "$text": "Bond"
            },
            "fields": [ "title", "cast" ],
            "limit": 3
          }' \
| jq '.'
</pre>

#### Finding a value in an array

A common query against a movie database is to list all movies an actor has appeared in. We can use
the `$in` operator to find out whether a value is present in the array of actors that is the value
of the `cast` field.

<pre class="thebe">
curl "$URL/movies/_find" \
     -X 'POST' \
     -H 'Content-Type: application/json' \
     -d  '{
            "selector": {
              "cast": {
                "$in": [ "Zoe Saldana" ]
              }
            },
            "fields": [ "title", "cast", "director" ],
            "limit": 3
          }' \
| jq '.'
</pre>

The examples in this guide only scratch the surface of what you can do with Cloudant Query. To learn
more, check out the [API Reference](cloudant_query.html) and play around with the queries on this site.

### Running code locally

To run the code snippets in this guide on your own machine, you need `bash`, `curl`, and `jq`.

1. If you're using MacOS or Linux, `bash` will already be installed as the default shell. On Windows, you need to install [Cygwin](https://cygwin.com/install.html).
2. Download and install [curl](https://curl.haxx.se/download.html).
3. Download the [jq](https://stedolan.github.io/jq/download/) executable and put it on your path.
