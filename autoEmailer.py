
# This is a program used to import an excel spreadsheet; test cases; and send an automated email
# regarding the results
# Allen Wickham III

# Import smtplib for the actual sending function for email
import smtplib
import time
# Import the email modules we'll need
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart



#----------------------------------------# 
# 			       Email Script			 #
#----------------------------------------#
def send(body):
	fromaddr = "Project Inventory"
	toaddr = "allen.wickhamiii@gmail.com"
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Order List " + time.strftime("%d/%m/%Y")
	 
	#body = "This is a test"
	msg.attach(MIMEText(body, 'html'))
	 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("allen.wickhamiii@gmail.com", "Kap-5711")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
