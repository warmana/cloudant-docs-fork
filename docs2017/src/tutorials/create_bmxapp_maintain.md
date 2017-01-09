---

copyright:
  years: 2017
lastupdated: "2017-01-09"

---

{:new_window: target="_blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}

# Creating a simple Bluemix application to access a Cloudant database: maintaining and troubleshooting

This tutorial shows you how to maintain an
{{site.data.keyword.Bluemix}} application,
hosted in your {{site.data.keyword.Bluemix_notm}} service instance.
{:shortdesc}

<div id="maintenance"></div>

## Performing basic application maintenance tasks

This section of the tutorial explains how to refresh,
start,
and stop,
your Python applications on {{site.data.keyword.Bluemix_notm}}.

### Finding the current status of your application

The status of applications within your
{{site.data.keyword.Bluemix_notm}} service instance is displayed on the dashboard.

In the following example,
The `Cloudant Python` application is not running,
and has a `Stopped` state:<br/>
![Screenshot showing dashboard for the application in a 'stopped' state](images/img0037.png)

### Starting your application

>   **Note**: If you attempt to start the tutorial application
    without first deleting the tutorial demonstration database,
    the application enters a cycle of attempting to start,
    failing because the database already exists,
    stopping,
    then attempting to start again.
    To solve the problem,
    [stop the application](#stopping-your-application),
    then delete the tutorial demonstration database.
    You should then be able to start the application successfully.

To start a stopped application,
first click on the application menu icon on the dashboard:<br/>
![Screenshot showing dashboard with application management icon](images/img0038.png)

Next,
click the `Start App` option in the menu:<br/>
![Screenshot showing 'Start App' option](images/img0039.png)

### Stopping your application

To stop a running application,
first click on the application menu icon on the dashboard:<br/>
![Screenshot showing dashboard with application management icon](images/img0040.png)

Next,
click the `Stop App` option in the menu:<br/>
![Screenshot showing 'Stop App' option](images/img0041.png)

<div id="troubleshooting"></div>

### Uploading a fresh version of your application

To upload a fresh version of your application,
simply follow the [upload process](create_bmxapp_upload.html).
The new version overwrites the older version of the application.

>   **Note**: If the older version of the application is already running when you start the upload,
    {{site.data.keyword.Bluemix_notm}} automatically stops the application first.

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

### Using the application log

The most useful resource for diagnosing and resolving problems with
{{site.data.keyword.Bluemix_notm}} application is the log file.

The log file for a {{site.data.keyword.Bluemix_notm}} application can be found on the `Logs` information page:<br/>
![Screenshot showing the link to access the 'Logs' information page](images/img0042.png)

Like most log files,
a {{site.data.keyword.Bluemix_notm}} application log contains details about what events occurred,
and when.

The log also identifies which component was involved in the recorded event.
The following table identifies key components:

Component label | Component
----------------|----------
`API`           | The Cloud Foundry system.
`APP`           | Your application.
`CELL`          | The container holding your application within {{site.data.keyword.Bluemix_notm}}.
`RTR`           | The networking components carry messages to or from your application.

For example,
the following screenshot includes a number of typical events:<br/>
![Screenshot showing indicative log information](images/img0043.png)

There are several points of interest:

-   At 1:56:56 PM, the application started successfully.
-   At 1:58:43 PM, the network received a simple HTTP request, to `GET /`.
-   Moments later, the application received the HTTP request, and replied to it.
-   At 2:13:46 PM, a request was received to stop the application.
-   At 2:13:48 PM, the application completed the process of halting.

The application described in this tutorial is deliberately minimal.
As a specific example,
no attempt is made to determine if the target database already exists,
and,
if it does exist,
to act accordingly.
The effect is that if you try to run the tutorial application more than once,
without removing the database beforehand,
the application will enter a cycle of failing,
and attempting to restart again.

You can see this effect in the following screenshot:<br/>
![Screenshot showing error information within the log](images/img0044.png)

At 2:31:23 PM,
the application detected a problem:<br/>
`"Database {0} already exists".format(dbname)`

The remainder of the messages are what you expect from any Python application encountering a problem.

In effect,
the log shows you what component encountered a problem,
and provides as much detail as possible.
You must then apply normal application troubleshooting procedures to resolve the problem.