---

copyright:
  years: 2015, 2017
lastupdated: "2017-01-04"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}

# Creating a simple Bluemix application to access a Cloudant database: maintaining and troubleshooting

This tutorial shows you how to maintain an
{{site.data.keyword.Bluemix}} application that uses the
[Python programming language](https://www.python.org/){:new_window} to
access an {{site.data.keyword.cloudantfull}} database,
hosted in your {{site.data.keyword.Bluemix_notm}} service instance.
{:shortdesc}

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

A good source of advice on best practice for creating {{site.data.keyword.Bluemix_notm}} or
Cloud Foundry applications is
[here](https://docs.cloudfoundry.org/devguide/deploy-apps/prepare-to-deploy.html){:new_window}.

In particular,
the advice on
[avoiding writes to the local file system](https://docs.cloudfoundry.org/devguide/deploy-apps/prepare-to-deploy.html#filesystem){:new_window}
is prudent.

>   **Note**: For reasons of simplicity,
    this tutorial does write content to the local file system,
    however,
    the quantity of material is very small,
    it is not expected to persist,
    and it is not 'mission critical'.

