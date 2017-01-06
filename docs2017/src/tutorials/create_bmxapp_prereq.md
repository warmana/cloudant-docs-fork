---

copyright:
  years: 2017
lastupdated: "2017-01-06"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}

# Creating a simple Bluemix application to access a Cloudant database: Prerequisites

This section of the tutorial describes the prerequisites
for creating an {{site.data.keyword.Bluemix}} application.
{:shortdesc}

## Prerequisites

Ensure that you have the following resources or information ready
before you start working through the tutorial.

### Python

For all but the simplest possible development work,
it is much easier if you have a current installation of the
[Python programming language](https://www.python.org/){:new_window}
that is installed on your system.

To check,
run the following command at a prompt:

```shell
python --version
```
{:pre}

Expect a result similar to the following output:

```text
Python 2.7.12
```
{:codeblock}

<div id="csi"></div>

### A Cloudant service instance on Bluemix

A tutorial for creating a {{site.data.keyword.cloudant_short_notm}} service instance is available [here](create_service.html).

This tutorial assumes that you have a service instance called
`Cloudant Service 2017`.

### A Cloudant database application

A tutorial for creating a stand-alone Python application to work with a {{site.data.keyword.cloudant_short_notm}}
service instance is available [here](create_database.html).
It introduces a number of concepts that are helpful for understanding how to create and populate a
{{site.data.keyword.cloudant_short_notm}} database.

This tutorial assumes that you are familiar with those concepts.
