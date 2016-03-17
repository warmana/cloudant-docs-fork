# Metadata Discovery with Cloudant
Metadata Discovery with Cloudant, `couch_md`, provides a method to learn about a schema of JSON documents in your database. It describes the type of documents present in the database as a collection of document fields, including data types and frequencies. To achieve this end, `couch_md`, builds a special type of index that is updated automatically with documents in a database.

## Creating a `couch_md` index
To create a `couch_md` index, you must supply a filter function. The filter function determines which documents to add to the index and which documents to ignore. 

The following process describes how to create an index:


1.	Compose a JavaScript filter function using this format. 
	 
```function(doc) -> (true | false)```

For example:

	    function(doc){
	    	{return true};
	    }
	
	or
	
	    function(doc){
	    	if (doc.diet == 'omnivore') {return true} 
	    	else {return false};
		}

2.	Add filter functions as objects in a `schemas` array in a new `_design` document. Each filter function represents a separate index. For example:

```    {
		"_id":"_design/metadata",
	
			"schemas":{
				"allAnimals":{
					"filter":"function(doc){{return true};}"
				},
	
				"omnivores":{
	    			"filter":"function(doc){
						if (doc.diet == 'omnivore') {return true} 
						else {return false};}"
				}
			}
		}
		}
		```

3.	Add the `_design` document to your Cloudant database. For example:
	```
	`curl -X PUT https://<account>.cloudant.com/<database>/_design/metadata -H 'Content-Type: application/json' -d @filter.json`
	```

Where `filter.json` is a design document as shown above. 

When the filter function is in place, any document that meets the filter criteria is added to the index. A modified document changes the index immediately, while a deleted document is removed from the index.

## Querying a `couch_md` index
Use a single endpoint to query the index with one optional query parameter that controls the representation of the result.

`curl -X GET https://<account>.cloudant.com/<database>/<_design_doc>/_schema/<filter>`

For example:
 `curl -X GET https://examples.cloudant.com/animaldb/_design/metadata/_schema/allAnimals`

or 
`curl -X GET https://examples.cloudant.com/animaldb/_design/metadata/_schema/omnivores`


### Parameter `schema`
The parameter `schema` controls the details returned by the index.

Parameter | Description
---------- |--------------
`union` | Returns a single object that combines multiple schemas into a union output by adding them together. This element is the default. For example: `curl -X GET https://examples.cloudant.com/animaldb/_design/metadata/_schema/omnivores?schema=union`
`all` | Returns a set of objects where each object represents a distinct schema. For example: `curl -X GET https://examples.cloudant.com/animaldb/_design/metadata/_schema/omnivores?schema=all`

	 
## Query output

The following factors affect a query's output:
*	Schema variation
*	Output interpretation

### Schema variation

If there are documents that implement a different set of attributes and values, then schema variation exists in the database. Schema variation can exist globally or locally as described in the following list:

*	Globally: Different documents implement different schemas, for example, `{'product': ...}` and `{'customer': ...}`. You can use the query parameter `schema` to merge different schemas into one by using `?schema=union`, or list all schemas individually by using `?schema=all`.

*	Locally: Values for the same attribute use different data types, for example, `'age': 30` vs. `'age': 'unknown'`. In this case, the index lists all the data types used for the attribute values and their frequencies, including the number of values for each data type.


### Output interpretation

If you query a `couch_md` index, the output includes a list of schemas. For the `union` endpoint, the list includes only one schema. For the `all` endpoint, the list includes one to several schemas.

The following table describes the meaning of each element in the schema output:


Element | Description
-----|--------------
`schema` | A schema object.
`__type` | A data type of the attribute (field): String, Float, Integer, Boolean, User-defined for a complex attribute, Array for an array attribute, and an Unknown for attributes of undefined types, for example, null values.
`__docFreq` | The number of documents having this particular schema or an attribute.
`__attributes` | A set of named attributes contained in the schema. Also, for an attribute of the User-defined type, this describes attributes (fields) contained inside this complex attribute.
`__length` | For an attribute of the String type, this shows the maximum string length encountered among all values of this attribute.
`__elements` | For an attribute of the Array type, this describes elements in this array attribute across all documents.
`__arrayFreq` | For an attribute of the Array type, this shows the total number of elements in this array attribute, across all documents.


The following sample output is the result of the `?schema=union` query parameter. Notice a schema variation in the `max_length`, `max_weight`, `min_length` and `min_weight` attributes. The `max weight` attribute contains two data types: float and integer. The database includes two documents of the float type, and seven documents of the integer type. Since the database includes ten filtered documents (schema _docFreq - 10), the `max weight` attribute is missing one of the documents. 


```js
[
  {
    "schema": {
      "__type": "Userdefined",
      "__docFreq": 10,
      "__attributes": {
        "_id": [
          {
            "__type": "String",
            "__docFreq": 10,
            "__length": 10
          }
        ],
        "_rev": [
          {
            "__type": "String",
            "__docFreq": 10,
            "__length": 34
          }
        ],
        "class": [
          {
            "__type": "String",
            "__docFreq": 10,
            "__length": 6
          }
        ],
        "diet": [
          {
            "__type": "String",
            "__docFreq": 10,
            "__length": 9
          }
        ],
        "latin_name": [
          {
            "__type": "String",
            "__docFreq": 5,
            "__length": 19
          }
        ],
        "max_length": [
          {
            "__type": "Float",
            "__docFreq": 8
          },
          {
            "__type": "Integer",
            "__docFreq": 2
          }
        ],
        "max_weight": [
          {
            "__type": "Float",
            "__docFreq": 2
          },
          {
            "__type": "Integer",
            "__docFreq": 7
          }
        ],
        "min_length": [
          {
            "__type": "Float",
            "__docFreq": 7
          },
          {
            "__type": "Integer",
            "__docFreq": 3
          }
        ],
        "min_weight": [
          {
            "__type": "Float",
            "__docFreq": 2
          },
          {
            "__type": "Integer",
            "__docFreq": 7
          }
        ],
        "wiki_page": [
          {
            "__type": "String",
            "__docFreq": 10,
            "__length": 46
          }
        ]
      }
    }
  }
]
```
In comparison, the following sample output is the result of the `?schema=all` query parameter for the same design document. This output demonstrates that there are three distinct schemas in the database (with 1, 4, and 5 documents) defined by a unique set of attributes. 


```js
[
  {
    "schema": {
      "__docFreq": 1,
      "__attributes": [
        "_id",
        "_rev",
        "wiki_page",
        "min_length",
        "max_length",
        "class",
        "diet",
        "latin_name"
      ]
    }
  },
  {
    "schema": {
      "__docFreq": 4,
      "__attributes": [
        "_id",
        "_rev",
        "wiki_page",
        "min_length",
        "max_length",
        "min_weight",
        "max_weight",
        "class",
        "diet",
        "latin_name"
      ]
    }
  },
  {
    "schema": {
      "__docFreq": 5,
      "__attributes": [
        "_id",
        "_rev",
        "wiki_page",
        "min_length",
        "max_length",
        "min_weight",
        "max_weight",
        "class",
        "diet"
      ]
    }
  }
]
```

