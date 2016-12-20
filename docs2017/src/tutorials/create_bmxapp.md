---

copyright:
  years: 2015, 2016
lastupdated: "2016-12-19"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}

# Creating a simple Bluemix application to access a Cloudant database on Bluemix

This tutorial shows you how to create a {{site.data.keyword.Bluemix_notm}} application that uses the
[Python programming language](https://www.python.org/){:new_window} to
access an {{site.data.keyword.cloudantfull}} database in your {{site.data.keyword.Bluemix_notm}} service instance.
{:shortdesc}

## Pre-requisites

Ensure that you have the following resources or information ready,
before you start working through the tutorial.

### Python

For all but the simplest possible development work,
it is much easier if you have a current installation of the
[Python programming language](https://www.python.org/){:new_window}
installed on your system.

To check this,
run the following command at a prompt:

```shell
python --version
```
{:pre}

You should get a result similar to:

```text
Python 2.7.12
```
{:codeblock}

### A Cloudant service instance on Bluemix

The process for creating a suitable service instance is described in [here](create_service.html).

In this tutorial,
we assume that you have a service instance called
`Cloudant Service 2017`.

HERE

## Context

A big advantage of {{site.data.keyword.Bluemix_notm}} is that you can create and deploy applications within
{{site.data.keyword.Bluemix_notm}} itself.
This means that you do not have to find and maintain a server to run your applications.

If you are already using a {{site.data.keyword.cloudant_short_notm}} database instance
within {{site.data.keyword.Bluemix_notm}},
it makes sense to have your applications there,
too.

[Another tutorial](create_database.html) showed you how to create a Python application
that uses a {{site.data.keyword.cloudant_short_notm}}
database instance within {{site.data.keyword.Bluemix_notm}}.
In this tutorial,
we show you how to set-up and create a simple Python application,
hosted within {{site.data.keyword.Bluemix_notm}}.
The application connects to your {{site.data.keyword.cloudant_short_notm}} database instance,
and creates a single,
simple document.

Python code specific to each task is provided as part of this tutorial.
A complete Python program,
sufficient to demonstrate the concepts working,
is provided at the end of the tutorial,
[here](#complete-listing).

No attempt has been made to create _efficient_ Python code for this tutorial;
the intention is to show simple and easy-to-understand working code
that you can learn from and apply for your own applications.

Also,
no attempt has been made to address all possible checks or error conditions.
Some example checks are shown here,
to illustrate the techniques,
but you should apply normal best practices for checking and handling all
warning or error conditions encountered by your own applications.

## Task overview

To create a working Python application on {{site.data.keyword.Bluemix_notm}},
that can access a {{site.data.keyword.cloudant_short_notm}} database instance,
you need to perform the following tasks:

1.  [Create a Python application enviroment on {{site.data.keyword.Bluemix_notm}}.](#creating)
2.  [Ensure that the Python application environment has a 'connection' to a {{site.data.keyword.cloudant_short_notm}} database instance.](#connecting)
3.  [(One-off task) Download and install the Cloud Foundry and Bluemix command line toolkits.](#toolkits)
4.  [Download the 'starter' application.](#starter)
5.  [Customize the starter application to create your own application for accessing the {{site.data.keyword.cloudant_short_notm}} database instance.](#creating)
6.  [Upload your application and test that it works.](#uploading)
7.  [Perform basic application maintenance tasks.](#maintenance)
8.  [Diagnose and resolve problems (troubleshooting).](#troubleshooting)

<div id="creating"></div>

## Creating {{site.data.keyword.Bluemix_notm}} application environment

<div id="connecting"></div>

## Connecting {{site.data.keyword.Bluemix_notm}} applications and services

This section of the tutorial explains how you connect
{{site.data.keyword.Bluemix_notm}} applications and services.

<div id="toolkits"></div>

## The Cloud Foundry and Bluemix command line toolkits

This section of the tutorial describes the toolkits you require to work with
your {{site.data.keyword.Bluemix_notm}} environment,
applications,
and services.

<div id="starter"></div>

## The 'starter' application

This section of the tutorial describes a {{site.data.keyword.Bluemix_notm}}
'starter' application,
and explains how you customize it to access
a {{site.data.keyword.cloudant_short_notm}} database instance.

<div id="creating"></div>

## Creating your application

This section of the tutorial explains how to create a Python
application that can access
the {{site.data.keyword.cloudant_short_notm}} database instance.

<div id="uploading"></div>

## Uploading your application and testing that it works

<div id="maintenance"></div>

## Performing basic application maintenance tasks

This section of the tutorial explains how to upload,
start,
and stop,
your Python applications on {{site.data.keyword.Bluemix_notm}}.

<div id="troubleshooting"></div>

## Diagnosing and resolving problems

This section of the tutorial provides some basic troubleshooting tips to help
you identify,
diagnose,
and resolve some problems you might encounter when developing and deploying
your first {{site.data.keyword.Bluemix_notm}} applications.


## Complete listing

The following code is a complete Python program to access a
{{site.data.keyword.cloudant_short_notm}} service instance on {{site.data.keyword.Bluemix_notm}},
and perform a typical series of tasks: