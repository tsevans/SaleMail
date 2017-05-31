from sys import argv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Grab arguments from command line
script, credentials_filename, excel_filename = argv
credentials_file = open(credentials_filename)
userline = credentials_file.readline()
passline = credentials_file.readline()

#ADDRESSES TO SEND TO, LOOP THIS WITH ENTRIES FROM EXCEL FILE
toaddr = "tsevans@vt.edu"

message = MIMEMultipart()
message['From'] = userline
message['To'] = toaddr
message['Subject'] = "Subject Line"

body = "Ypur message here"
message.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(userline, passline)
text = message.as_string()
server.sendmail(userline, toaddr, text)
server.quit()
