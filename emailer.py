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
if os.stat(cred_name).st_size == 0:
	setup_complete = False
	while not setup_complete:
		print("Type your first name and then press [Enter]: ")
		firstname = input()
		print("Type your last name and then press [Enter]: ")
		lastname = input()
		print("Type your gmail address and then press [Enter]: ")
		email = input()
		print("Type the password for your gmail account and then press [Enter]:")
		password = input()
		write_file = open(cred_name, "w")
		print("You have entered the following...\nFirst Name: " + firstname + "\nLast Name: " + 
			lastname + "\nEmail: " + email + "\nPassword: " + password + "\nIs this correct? Type Y for yes or N for no and then press [Enter]")
		input_valid = False
		while not input_valid:
			choice = input()
			if choice == "Y":
				setup_complete = True
				break
			elif choice == "N":
				break
			else:
				print("Choice not recognized! Make sure to use uppercase letters!")
		write_file.write(firstname)
		write_file.write("\n")
		write_file.write(lastname)
		write_file.write("\n")
		write_file.write(email)
		write_file.write("\n")
		write_file.write(password)
		write_file.close()
	
#Open the credentials file and obtain credentials
credentials_file = open(cred_name)
user_firstname = credentials_file.readline()
user_lastname = credentials_file.readline()
user_email = credentials_file.readline()
user_password = credentials_file.readline()
credentials_file.close()

#Open the excel file
#book = xlrd.open_workbook(excel_name)

#ADDRESSES TO SEND TO, LOOP THIS WITH ENTRIES FROM EXCEL FILE
toaddr = "tsevans@vt.edu"

message = MIMEMultipart()
message['From'] = user_email
message['To'] = toaddr
message['Subject'] = "Subject Line"

body = "Your message here"
message.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(user_email, user_password)
text = message.as_string()
server.sendmail(user_email, toaddr, text)
server.quit()
