## Metadata Discovery

Metadata indexes allow you to learn about schemas of JSON documents in a database. The metadata indexes describe what kind of documents are present in the database as a collection of document fields with data types and frequencies. 

### Creating a metadata index

To create an index, you supply a filter function. When the filter function is applied, it passes a document as an argument. If the result is true, the document can be included in the index. If the result is false, the document cannot be included in the index. 

#### Create filter functions

> Filter function to index all documents in a database

```
function(doc) {
 	return true;
}
```

> Filter function to index only documents where the value of the diet field is `'omnivore'`.

```
function(doc) {
 	return doc.diet == 'omnivore';
}
```

<div> </div> 

#### Save the filter functions in a design document

> Adding a design document with filter functions

```shell
curl -X PUT "https://$ACCOUNT.cloudant.com/$DATABASE/_design/metadata" -H 'Content-Type: application/json' -d '@filter.json'
# where filter.json contains the following document:
```

```http
PUT /$DATABASE/_design/metadata HTTP/1.1
Host: $ACCOUNT.cloudant.com
Content-Type: application/json

```

```json
{
  "_id":"_design/metadata",
  "schemas": {
    "allAnimals": {
      "filter":"function(doc) { return true; }"
    },
    "omnivores": {
      "filter":"function(doc) { return doc.diet == 'omnivore'; }"
    }
  }
}
```

Once you have written the filter functions, you store them in a design document. The design document contains a `schema` field where each field defines a schema with a `filter` field for the filter function.

### Querying an index

> Querying the allAnimals index

```shell
curl -X GET "https://examples.cloudant.com/animaldb/_design/metadata/_schema/allAnimals"
```

```http
GET /animaldb/_design/metadata/_schema/allAnimals HTTP/1.1
HOST examples.cloudant.com
```

> Querying the omnivores index

```shell
curl -X GET "https://examples.cloudant.com/animaldb/_design/metadata/_schema/omnivores"
```

```http
GET /animaldb/_design/metadata/_schema/omnivores HTTP/1.1
HOST examples.cloudant.com
```

When the filter function is in place, any document that meets the filter criteria is added to the index. A modified document changes the index immediately and a deleted document is removed from the index.

To query the index, you make a `GET` request to `/$DATABASE/$DESIGNDOC/_schema/$SCHEMANAME?schema=all` and insert the names of the database, the design document, and the schema to query. Optionally, you can add the `schema` query parameter to control the output format.

<div> </div>

#### The `schema` parameter

> Querying the allAnimals index with `schema=all`

```shell
curl -X GET "https://examples.cloudant.com/animaldb/_design/metadata/_schema/allAnimals?schema=all"
```

```http
GET /animaldb/_design/metadata/_schema/allAnimals?schema=all HTTP/1.1
HOST examples.cloudant.com
```

> Querying the allAnimals index with `schema=union`

```shell
curl -X GET "https://examples.cloudant.com/animaldb/_design/metadata/_schema/allAnimals?schema=union"
```

```http
GET /animaldb/_design/metadata/_schema/allAnimals?schema=union HTTP/1.1
HOST examples.cloudant.com
```

The `schema` parameter controls how detailed the output will be.

 - `all` (default): returns an array of objects, where each object represents a distinct schema.
 - `union`: returns a single object that combines multiple schemas into a union output by adding them together. For example `curl -X GET https://examples.cloudant.com/animaldb/_design/metadata/_schema/omnivores?schema=union`

### Schema variation

If there are documents that implement a different set of attributes and values, then schema variation exists in the database. Schema variation can exist globally or locally as described in the following list.

*	Globally: Different documents implement different schemas, for example, `{'product': ...}` and `{'customer': ...}`. You can use the query parameter `schema` to merge different schemas into one by using `?schema=union`, or list all schemas individually by using `?schema=all`.

*	Locally: Values for the same attribute use different data types, for example, `'age': 30` vs. `'age': 'unknown'`. In this case, the index lists all the data types used for the attribute values and their frequencies, including the number of values for each data type.

### Index output

If you query a `couch_md` index, the output includes a list of schemas. For the `union` endpoint, the list includes only one schema. For the `all` endpoint, the list includes one to several schemas

The following elements are contained in the schema index.

 * `object` an array of schemas returned by the index 

   * `__attributes` a set of named attributes contained in a schema
   * `__type` a known attribute value data type (String, Float, Integer, Boolean) or userdefined for a complex attribute or an unknown attribute data type 
   * `__freq` the number of times we count attribute values with this type
   * `__length` the maximum value length (applies only to String attributes)
   * `__repeated` equals true if the attribute is a JSON array, false otherwise

#### Output with `schema=union`

```json
    [
    {
        "object": [
            {
                "__type": "userdefined",
                "__freq": 4,
                "__attributes": {
                    "diet": [
                        {
                            "__type": "String",
                            "__freq": 4,
                            "__length": 8,
                            "__repeated": false
                        }
                    ],
                    "class": [
                        {
                            "__type": "String",
                            "__freq": 4,
                            "__length": 6,
                            "__repeated": false
                        }
                    ],
                    "wiki_page": [
                        {
                            "__type": "String",
                            "__freq": 4,
                            "__length": 46,
                            "__repeated": false
                        }
                    ],
                    "latin_name": [
                        {
                            "__type": "String",
                            "__freq": 3,
                            "__length": 19,
                            "__repeated": false
                        }
                    ],
                    "max_length": [
                        {
                            "__type": "Float",
                            "__freq": 4,
                            "__repeated": false
                        }
                    ],
                    "min_length": [
                        {
                            "__type": "Float",
                            "__freq": 3,
                            "__repeated": false
                        },
                        {
                            "__type": "Integer",
                            "__freq": 1,
                            "__repeated": false
                        }
                    ],
                    "max_weight": [
                        {
                            "__type": "Float",
                            "__freq": 2,
                            "__repeated": false
                        },
                        {
                            "__type": "Integer",
                            "__freq": 2,
                            "__repeated": false
                        }
                    ],
                    "min_weight": [
                        {
                            "__type": "Float",
                            "__freq": 2,
                            "__repeated": false
                        },
                        {
                            "__type": "Integer",
                            "__freq": 2,
                            "__repeated": false
                        }
                    ],
                    "_rev": [
                        {
                            "__type": "String",
                            "__freq": 4,
                            "__length": 34,
                            "__repeated": false
                        }
                    ],
                    "_id": [
                        {
                            "__type": "String",
                            "__freq": 4,
                            "__length": 8,
                            "__repeated": false
                        }
                    ]
                },
                "__repeated": false
            }
        ]
    }
	]
```

This response is produced by querying the index with `?schema=union`. 

<div> </div>

#### Output with `schema=all`

```json
    [
    {
        "object": [
            {
                "__type": "userdefined",
                "__freq": 1,
                "__attributes": {
                    "_id": [
                        {
                            "__type": "String",
                            "__freq": 1,
                            "__length": 8,
                            "__repeated": false
                        }
                    ],
                    "_rev": [
                        {
                            "__type": "String",
                            "__freq": 1,
                            "__length": 34,
                            "__repeated": false
                        }
                    ],
                    "wiki_page": [
                        {
                            "__type": "String",
                            "__freq": 1,
                            "__length": 46,
                            "__repeated": false
                        }
                    ],
                    "min_weight": [
                        {
                            "__type": "Float",
                            "__freq": 1,
                            "__repeated": false
                        },
                        {
                            "__type": "Integer",
                            "__freq": 1,
                            "__repeated": false
                        }
                    ],
                    "max_weight": [
                        {
                            "__type": "Float",
                            "__freq": 1,
                            "__repeated": false
                        },
                        {
                            "__type": "Integer",
                            "__freq": 1,
                            "__repeated": false
                        }
                    ],
                    "min_length": [
                        {
                            "__type": "Float",
                            "__freq": 1,
                            "__repeated": false
                        },
                        {
                            "__type": "Integer",
                            "__freq": 0,
                            "__repeated": false
                        }
                    ],
                    "max_length": [
                        {
                            "__type": "Float",
                            "__freq": 1,
                            "__repeated": false
                        }
                    ],
                    "class": [
                        {
                            "__type": "String",
                            "__freq": 1,
                            "__length": 6,
                            "__repeated": false
                        }
                    ],
                    "diet": [
                        {
                            "__type": "String",
                            "__freq": 1,
                            "__length": 8,
                            "__repeated": false
                        }
                    ]
                },
                "__repeated": false
            }
        ]
    },
    {
        "object": [
            {
                "__type": "userdefined",
                "__freq": 3,
                "__attributes": {
                    "_id": [
                        {
                            "__type": "String",
                            "__freq": 3,
                            "__length": 8,
                            "__repeated": false
                        }
                    ],
                    "_rev": [
                        {
                            "__type": "String",
                            "__freq": 3,
                            "__length": 34,
                            "__repeated": false
                        }
                    ],
                    "wiki_page": [
                        {
                            "__type": "String",
                            "__freq": 3,
                            "__length": 46,
                            "__repeated": false
                        }
                    ],
                    "min_weight": [
                        {
                            "__type": "Float",
                            "__freq": 2,
                            "__repeated": false
                        },
                        {
                            "__type": "Integer",
                            "__freq": 2,
                            "__repeated": false
                        }
                    ],
                    "max_weight": [
                        {
                            "__type": "Float",
                            "__freq": 2,
                            "__repeated": false
                        },
                        {
                            "__type": "Integer",
                            "__freq": 2,
                            "__repeated": false
                        }
                    ],
                    "min_length": [
                        {
                            "__type": "Float",
                            "__freq": 2,
                            "__repeated": false
                        },
                        {
                            "__type": "Integer",
                            "__freq": 1,
                            "__repeated": false
                        }
                    ],
                    "max_length": [
                        {
                            "__type": "Float",
                            "__freq": 3,
                            "__repeated": false
                        }
                    ],
                    "latin_name": [
                        {
                            "__type": "String",
                            "__freq": 3,
                            "__length": 19,
                            "__repeated": false
                        }
                    ],
                    "class": [
                        {
                            "__type": "String",
                            "__freq": 3,
                            "__length": 6,
                            "__repeated": false
                        }
                    ],
                    "diet": [
                        {
                            "__type": "String",
                            "__freq": 3,
                            "__length": 8,
                            "__repeated": false
                        }
                    ]
                },
                "__repeated": false
            }
        ]
    }
	]
```

This response is produced by querying the index with `?schema=all`. 

