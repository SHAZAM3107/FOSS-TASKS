#! python3  # this is called shebang line used to tell the cli to run the following python program

import smtplib   # importing smtp module
import config    # this is to access the credential in config.py
from email.mime.text import MIMEText     # this module is used to add subject or attachments to the mail
from email.mime.multipart import MIMEMultipart


from_addr=config.EMAIL_ADDRESS   # giving from adress from config.py

password=config.PASSWORD   # giving password

mailto = input("TO: ")  # giving to adress

subject=input("SUBJECT: ")  # adding subject to the mail

body=input("BODY: ")   # your content goes here..

msg = MIMEMultipart()
msg['From']=from_addr
msg['To'] = mailto
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))   # this is to attach subject and body of the mail

mailServer = smtplib.SMTP('smtp.gmail.com' , 587)   # connecting to gmail servers using port number

mailServer.starttls()   # starting transport layer security to encode the message

mailServer.login(from_addr ,password)    # connection to the gmail account of sender

mailServer.sendmail(from_addr, mailto , msg.as_string())  # sending the mail to reciever

print(" \n Sent!")   # if it is succesfull it prints sent
  
mailServer.quit()   # closing the connection after the email is sent
