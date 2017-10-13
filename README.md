# SaleMail

## Table of Contents

  * [What is SaleMail?](#what-is-salemail)
  * How to Download
    * [Linux/Mac OS X Instructions](#linuxmac-os-x-download-instructions)
  * [How to Use SaleMail](#how-to-use-salemail)
    * [First Time Setup](#first-time-setup)
<br></br>

## What is SaleMail?

  SaleMail is a python tool that allows University of Texas students in the AroundCampus Group sales program to automate the process of sending follow-up emails to the company representatives they spoke to during the work day. The motivation for this project came from a discussion with my roommate, in which he told me that he and his associates must spend up to an hour or more each day after work sending individual follow-up emails to companies they pitched to that day. Often times, sales reps finish their day with a collection of business cards, scrap paper, and lists of contact info which they must organize before translating to individual emails. This process is not only tedious and time consuming, but also prone to errors in the case that they might accidentally forget to personalize all required fields in the email template for each unique customer.

  By using SaleMail, sales reps will be able to make changes to their email template when needed, store and organize client info into an excel workbook, and send all emails for the day with a single command rather than spending time copying/pasting through thier normal email portal. Additionally, SaleMail provides basic experience using a CLI (command line interface) and understanding the power of python scripting, which are both useful computer skills.
<br></br>

## Linux/Mac OS X Download Instructions

___Step 1.___ 

[Click here](https://www.python.org/ftp/python/3.6.1/python-3.6.1-macosx10.6.pkg) to download Python (version 3.6.1) and follow the default installation instructions.
<br></br>

___Step 2.___ 

When you have completed the Python installation, open your computer's terminal. The icon looks like this: 

![Terminal Icon](http://media.idownloadblog.com/wp-content/uploads/2015/01/Terminal-icon-Yosemite-220x220.png)
<br></br>

___Step 3.___ 

In the terminal, type the following command:
```
pip install -U pip setuptools
```
Press the Enter key to run the command, which will install/update the utility that will be used to install the SaleMail application.
<br></br>

___Step 4.___

Use the pip utility to install the [xlrd library](https://pypi.python.org/pypi/xlrd), which is what will allow the SaleMail application to read the excel file containing the information of your clients. To do this, type the following command into the terminal and then press the Enter key:
```
pip install xlrd
```

___Step 5.___

[Click here](https://github.com/tsevans/SaleMail/archive/master.zip) to download this project. It will be downloaded as a .zip file called "SaleMail-master".
<br></br>

___Step 6.___

Type the following series of commands into the terminal, following each command by a press of the Enter key:
```
mkdir Programs
```
  This command creates a folder called "Programs" on your computer.
```
cd Programs
```
  This command moves you into the newly created "Programs" folder in the terminal.
```
mkdir SaleMail
```
  This command creates a folder called "SaleMail" in the "Programs" folder.
```
cd SaleMail
```
  This command moves you into the newly created "SaleMail" folder in the terminal.
```
mv ~/Downloads/SaleMail-master ./
```
  This command moves all of the files downloaded in Step 5 into the "SaleMail" folder that was just created.
<br></br>

___Step 7.___

At this point, you should have all of the tools and files necessary to use SaleMail. If you would like to check that you have all the proper files, type the following command into the terminal and press the Enter key:
```
ls -l
```
You should see a listing of files like so:

<br></br>

## How to Use SaleMail
### First Time Setup
The first time you run SaleMail, you will go through a setup procedure that will initialize all of your personal information. This information will be used to send messages from your email and better personalize your messages. Make sure to pay attention while going through the setup procedure so that the correct information is entered, as it may be difficult to change later on.

___Step 1.___ 
