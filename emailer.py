from __future__ import print_function
from sys import argv
import os
from os.path import join, dirname, abspath
import smtplib
import xlrd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

cred_name = join(dirname(abspath(__file__)), 'credentials.txt')

excel_name = join(dirname(abspath(__file__)), 'sample_data.xlsx')

#If credentials file is empty, enter first time setup procedure
#if os.path.getsize(cred_name) == 0:
if os.stat(cred_name).st_size == 0:
	print("Enter your gmail email address: ")
	email = input()
	print("Enter the password for your email account: ")
	password = input()
	write_file = open(cred_name, "a")
	write_file.write(email)
	write_file.write("\n")
	write_file.write(password)
	write_file.close()
	
#Open the credentials file to get the email and password for logging in
cred_file = open(cred_name)
userline = cred_file.readline()
passline = cred_file.readline()

#Open the excel file
book = xlrd.open_workbook(excel_name)

#ADDRESSES TO SEND TO, LOOP THIS WITH ENTRIES FROM EXCEL FILE
toaddr = "tsevans@vt.edu"

message = MIMEMultipart()
message['From'] = userline
message['To'] = toaddr
message['Subject'] = "Subject Line"

body = "Your message here"
message.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(userline, passline)
text = message.as_string()
server.sendmail(userline, toaddr, text)
server.quit()