---

copyright:
  years: 2015, 2016
lastupdated: "2016-12-09"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}

# ACID

ACID is an acronym for [atomic](#atomic),
[consistent](#consistent),
[isolated](#isolated),
[durable](#durable).
{:shortdesc}

ACID is a set of properties which guarantee that transactions with a database are processed and reported reliably.
Strictly,
Cloudant is AcID:
the "c" is lowercase because Cloudant is [eventually consistent](cap_theorem.html)
rather than strongly consistent.

<div id="acid_atomic"></div>

## Atomic

Atomic is just another way of saying that something cannot be further divided.
An atomic transaction means that if one part of the transaction fails,
the whole transaction fails.
The failure helps ensure that the database remains in a consistent state.

For example,
a request to modify a document only reports success after the change has been written to disk.

<div id="acid_consistent"></div>

## Consistent

Cloudant is eventually consistent,
such that any change normally propagates to the whole cluster within milliseconds,
but the system does not wait for that propagation be completed before reporting success. 

<div id="acid_isolated"></div>

## Isolated

Cloudant is lockless,
so that even simultaneous reads and writes do not delay or impact other reads and writes.
Isolation just means that concurrent processes result in the same state that would be the outcome
if things happened one at a time.

<div id="acid_durable"></div>

## Durable

Durability ensures that changes remain once committed,
even after power failures or other errors.
Document updates and insertions are written to disk before the request is considered complete.
