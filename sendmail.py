#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
import getpass
import sys

gmail_user = "manoj.p.gudi@gmail.com"
gmail_pwd = '' # Will  be fetched from user runtime

def getMultilineInput(): #For mail body.
   body = [] 
   entry = raw_input("\nEnter body, '##done' on its own line to quit: \n") 
   while entry != "##done": 
       body.append(entry) 
       entry = raw_input("") 
   body = '\n'.join(body)
   return body

def mail(to, subject, text, attach):
   msg = MIMEMultipart()
   gmail_pwd = getpass.getpass(stream=sys.stderr)
   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject
   msg.attach(MIMEText(text))
   if attach!="":
       msg.attach(MIMEText(text))
   
       part = MIMEBase('application', 'octet-stream')
       part.set_payload(open(attach, 'rb').read())
       Encoders.encode_base64(part)
       part.add_header('Content-Disposition',
               'attachment; filename="%s"' % os.path.basename(attach))
       msg.attach(part)
   try:
       mailServer = smtplib.SMTP("smtp.gmail.com", 587)
       mailServer.ehlo()
       mailServer.starttls()
       mailServer.ehlo()
       mailServer.login(gmail_user, gmail_pwd)
       mailServer.sendmail(gmail_user, to, msg.as_string())
       # Should be mailServer.quit(), but that crashes...
       mailServer.close()
       print 'Mail sent!'
   except :
       print 'Failure!'
print '\nFrom:',gmail_user
to = raw_input('To: ')
subject = raw_input('Subject: ')
body = getMultilineInput()

mail(to,
   subject,
   body,
   "")
