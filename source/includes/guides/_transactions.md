## Storing purchase orders in Cloudant

> Example shopping app documents

```
{
  "_id": "023f7a21dbe8a4177a2816e4ad1ea27e",
  "type": "purchase",
  "order_id": "320afa89017426b994162ab004ce3383",
  "basket": [
     {
       "product_id": "A56",
       "title": "Adele - 25",
       "category": "Audio CD",
       "price": 8.33,
       "tax": 0.2,
       "quantity": 2
      },
      {
        "product_id": "B32",
        "title": "The Lady In The Van - Alan Bennett",
        "category": "Paperback book",
        "price": 3.49,
        "tax": 0,
        "quantity": 2
      }
   ],
  "account_id": "985522332",
  "delivery": {
    "option": "Next Day",
    "price": 2.99
  },
  "pretax" : 20.15,
  "tax" : 3.32,
  "total": 26.46
}
```

If you intend to create an e-commerce system and use Cloudant to store the purchase order records, then 
you can model a single purchase order this way:

<div></div>

This example provides enough data in a purchase record to render a summary of an order on a web page, or an email, without fetching additional records. Notice the order's details in the following list:
 
-	The basket contains reference ids (product_id) to a database of products stored elsewhere.
-	The basket duplicates some of the product data in this record; enough to record the state of the items purchased at the point of sale.
-	The document does not contain fields that mark the status of the order. Additional documents will be added later to record payments and delivery.
-	The database automatically generates a document _id when it inserts the document into the database.
-	A unique identifier (order_id) is supplied with each purchase record to reference the order later. 
 
When the customer places an order, typically when the customer enters the "checkout" phase on the website, a purchase order record is created. 

###Generating your own unique identifiers (UUIDs)
 
In a relational database, sequential "auto incrementing" numbers are often used but in distributed databases, where data is spread around of cluster of servers, longer UUIDs are used to ensure that documents are stored with their own unique id.
 
To create a unique identifier to use in your application, such as an "order_id", call the "GET _uuids" endpoint on the Cloudant API and the database will generate an identifier for you. The same endpoint can be used to generate multiple ids by adding a "count" parameter, for example, `/_uuids?count=10`.

###Recording payments

> Payment record

```
{
  "_id": "bf70c30ea5d8c3cd088fef98ad678e9e",
  "type": "payment",
  "account_id": "985522332",
  "order_id": "320afa89017426b994162ab004ce3383",
  "value": 6.46,
  "method": "credit card",
  "payment_reference": "AB9977G244FF2F667"
}
{
   "_id": "12c0ea6cd3d2c6e3b1d34442aea6a2d9",
   "type": "payment",
   "account_id": "985522332",
   "order_id": "320afa89017426b994162ab004ce3383",
   "value": 20.00,
   "method": "voucher",
   "payment_reference": "Q88775662377224"
}
```


If the customer successfully pays for their items, additional records are added to the database to record the order:
<div></div>

In this example, the customer paid by supplying a credit card and redeeming a pre-paid voucher. The total of the two payment added up to the amount of the order. Each payment was written to Cloudant as a separate document. You can see the status of an account by creating a view of everything you know about an account as a ledger containing the following information: 
 
-	Purchase totals as positive numbers
-	Payments against the account as negative numbers

> Map function

```
{
function (doc) 
	{
	if (doc.type === 'purchase') {
		emit(doc.order_id, doc.total);
		} else{
	if (doc.type === 'payment') {
		emit(doc.order_id, -doc.value);
	  }
	 }
	 }
 }
```

The example below shows the Map function: 

<div></div>

> Built-in "_sum" reducer

```
{
"total_rows":3,"offset":0,"rows":[
	{"id":"320afa89017426b994162ab004ce3383","key":"985522332","value":26.46},
	{"id":"320afa89017426b994162ab004ce3383","key":"985522332","value":-20},
	{"id":"320afa89017426b994162ab004ce3383","key":"985522332","value":-6.46}
	]
 }
```

Select the built-in "_sum" reducer which produces output either as a ledger of payment events (queried with ?reduce=false): 
<div></div>

> Totals grouped by order_id

```
{
"rows":[
 	{"key":"320afa89017426b994162ab004ce3383","value":0}
 ]
 }
``` 

Or totals grouped by order_id (?group_level=1):


