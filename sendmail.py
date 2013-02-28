#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
import getpass
import sys
import argparse


parser = argparse.ArgumentParser(description="A script which is to be attached to an automated script for automated bug/report mailing")
parser.add_argument("-c", help="takes username and password from a file")
parser.add_argument("-b", help="takes a string variable")
parser.add_argument("-t", help="takes send to email id")
parser.add_argument("-s", help="takes subject line")

args = parser.parse_args()

# From
gmail_user = ""
gmail_pwd = ""

def content_from_file(filename):
	try:
		file_obj = open(filename, 'r')
		content = file_obj.read()
	except:
		print("file not found!..")
		content = ""	
	finally:
		return content

def mail(to, subject, text, attach):
	msg = MIMEMultipart()
	#gmail_pwd = getpass.getpass(stream=sys.stderr)
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



# For gmail_user and password from file credentials
if args.c != None:
	credentials = content_from_file(args.c).splitlines()
	gmail_user = credentials[0]
	gmail_pwd = credentials[1]
	print gmail_user
else:
	print "requires email details"
	exit()
	
# Body file
if args.b != None:
	body = content_from_file(args.b)
	print body
else:
	print "requires text file path (email_body)"
	exit()
	
# For getting To email id
if args.t != None:
	to = args.t
else:
	print("requires valid TO address")
	exit()
	
# For getting subject line
if args.s != None:
	subject = args.s
else:
	print("requires valid subject line")
	exit()
	

# MAIL To function
mail(to,  subject,  body, "")

# To do:
# Multiple send addresses
# Attachments
