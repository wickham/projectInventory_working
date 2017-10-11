'''
    This program is for open source use
    Designed by Allen Wickham
    Q3 2017
    Project info @
    www.allenwickham.me
    Contact:
    allenwickhamiii@gmail.com
'''

# This is a program used to import an excel spreadsheet; test cases; and send an automated email
# regarding the results
# Allen Wickham III

# Import smtplib for the actual sending function for email
import smtplib
import time
# Import the email modules we'll need
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart

var = "username"
rec = "password"

#----------------------------------------# 
# 			   Email Script				 #
#----------------------------------------#
def send(body):
	print("Sending Email...")
	fromaddr = "Project Inventory"
	toaddr = "username"
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Order List " + time.strftime("%d/%m/%Y")
	 
	#body = "This is a test"
	msg.attach(MIMEText(body, 'html'))
	 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(var, rec)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
	print("Email: SENT!\n")
