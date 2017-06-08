# SaleMail
#### Application that allows University of Texas students in the AroundCampus Group program to quickly send follow-up sales emails

Table of Contents
=================

  * How to Download
    * [Mac OS X Instructions](#mac-os-x-download-instructions)
  * [How to Use SaleMail](#how-to-use-salemail)

## Mac OS X Download Instructions

___Step 1.___ 

[Click here](https://www.python.org/ftp/python/3.6.1/python-3.6.1-macosx10.6.pkg) to download the latest version of Python (version 3.6.1) and follow the default installation instructions.
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

Use the pip utility to install the xlrd library, which is what will allow the SaleMail application to read the excel file containing the information of your clients. To do this, type the following command into the terminal and then press the Enter key:
```
pip install xlrd
```
<br></br>

___Step 5.___

[Click here](https://github.com/tsevans/SaleMail/archive/master.zip) to download this project. It will be downloaded as a .zip file called "SaleMail-master".
<br></br>

___Step 6.___

Type the following series of commands into the terminal, following each command by a press of the Enter key:
```
mkdir Programs
```
```
cd Programs
```
```
mkdir SaleMail
```
```
cd SaleMail
```
```
mv ~/Downloads/SaleMail-master ./
```
<br></br>

___Step 7.___

At this point, you should have all of the tools and files necessary to use SaleMail. If you would like to check that you have all the proper files, type the following command into the terminal and press the Enter key:
```
ls -l
```
You should see a listing of files like so:

<br></br>

## How to Use SaleMail

___Step 1.___ 
