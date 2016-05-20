## Metadata Indexing
Metadata indexing provides information about schemas of JSON documents in a database. With Cloudant, you can create a couch_md index for metadata discovery. The couch_md index describes what kind of documents are present in the database as a collection of document fields with data types and frequencies. For this, couch_md builds a special type of index that gets updated automatically by updating documents in a database.

### <a name="id-section1">Creating a couch_md index</a>
To create a couch_md index, you must supply a filter function. The function determines which documents to add to the index and which documents to ignore. 

The index is created using the following process. 

<ol><li> Compose a JavaScript filter function in the following format, <code>function(doc) -> (true | false)</code>.

<p>For example:</p>
<p>
<code>
	    function(doc){
	    	{return true};
	    }
</code>
</p>	    
or
<p>
<code>	
	    function(doc){
	    	if (doc.diet == 'omnivore') {return true} 
	    	else {return false};
		}
</code></p>
</li>    

<li> Add filter functions as objects into a <code>schemas</code> array in a new <code>_design</code> document. Each filter function represents a separate index.
<p>For example:</p>
<p>
<code>{
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
}</code>
</p></li>

<li>Add the _design document to your Cloudant database (where <code>filter.json</code> is a design document like the one shown above).

<p>For example:</p>

<code>curl -X PUT https://<account>.cloudant.com/<database>/_design/metadata -H 'Content-Type: application/json' -d @filter.json</code>
<p></p>

</li></ol>

When you create the filter function, the documents that meet the filter criteria are added to the index. A modified document changes the index immediately, and a deleted document is removed from the index immediately.


### <a name="id-section2">Querying a couch_md index</a>
A single end point queries the index with one optional query parameter to control the representation of the result. Replace the account, database, design doc, and filter values with the names you use in your environment, as in the examples that follow. 

`curl -X GET https://<account>.cloudant.com/<database>/<_design_doc>/_schema/<filter>`

For example:

 `curl -X GET https://examples.cloudant.com/animaldb/_design/metadata/_schema/allAnimals`

or 

`curl -X GET https://examples.cloudant.com/animaldb/_design/metadata/_schema/omnivores`

#### Parameter `schema`
The `schema`	 parameter controls the amount of detail returned by the index using the `union` and `all` elements.

*	`union`: (default) Returns a single object that combines multiple schemas into a union output by adding them together. 

For example:

`curl -X GET https://examples.cloudant.com/animaldb/_design/metadata/_schema/omnivores?schema=union`

*	`all`: Returns a set of objects where each object represents a distinct schema. 

For example:

`curl -X GET https://examples.cloudant.com/animaldb/_design/metadata/_schema/omnivores?schema=all`


### <a name="id-section3">Query Output</a>

#### Schema variation
In general, schema variation exists in a database if there are documents that implement a different set of attributes or values. Schema variation can exist globally and locally. 
<ul><li>
**Globally** Different documents implement different schemas, for example, `{'product': ...}` and `{'customer': ...}`. The query parameter `schema` can be used to merge or list schemas.
	<ul><li>`?schema=union` Merge the different schemas into one.</li>
	<li>`?schema=all` List all schemas individually.</li></ul>
	<p></p>
</li>

<li>
**Locally** Different data types are used for values in the same attribute, for example, `'age': 30` versus `'age': 'unknown'`. In this case, the index lists all used data types for the attribute values together with their frequencies. Frequencies are defined by how many values each particular data type contains.
</li></ul>

#### Output interpretation
The output of querying the couch_md index includes a list of schemas. The `union` end point contains only one schema in the list. The `all` end point can include from one to several schemas in the list. 

The schema output includes the following elements. 

Element | Description
-----|------------
`schema`| A schema object.
`__type` | A data type of the attribute (field), including `String`, `Float`, `Integer`, `Boolean`, `Userdefined` for a complex attribute, `Array` for an array attribute, and an `Unknown` for attributes of undefined types such as null values.
`__docFreq` | The number of documents with this particular schema or attribute.
`__attributes` | A set of named attributes contained in the schema. Also, for an attribute of the `Userdefined` type, this describes attributes (fields) contained inside this complex attribute. 
`__length` | For an attribute of the `String` type, this shows the maximum string length encountered by all values of this attribute.
`__elements` | For an attribute of the `Array` type, this describes elements in this Array attribute across all documents.
`__arrayFreq` | For an attribute of the `Array` type, this shows the total number of elements in this array attribute, across all documents.


> An example of the `?schema=union` query parameter output

```
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

```



The following example shows the output produced by the `?schema=union` query parameter. Notice the schema variation in attributes `max_length`, `max_weight`, `min_length`, and `min_weight`. For the `max_weight` attribute, this means that the database contains 2 documents where the `max_weight` attribute is of type `Float`, and the database contains 7 documents where the `max_weight` attribute is of type `Integer`. Since the database contains 10 filtered documents (`schema _docFreq = 10`), the `max_weight` attribute is missing in 1 of the documents.

<div></div>

> An example of the `?schema=all` query parameter output

```

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

```

As a comparison, the following example shows output produced with the `?schema=all` query parameter for the same design document. The output shows three distinct schemas in a database (with 1, 4, and 5 documents) defined by a unique set of attributes. 

<div></div>

