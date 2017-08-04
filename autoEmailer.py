
# This is a program used to import an excel spreadsheet; test cases; and send an automated email
# regarding the results
# Allen Wickham III

# Import smtplib for the actual sending function for email
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart



#----------------------------------------# 
# 			       Email Script				       #
#----------------------------------------#

fromaddr = "allen.wickhamiii@gmail.com"
toaddr = "allen.wickhamiii@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE MAIL"
 
body = "This is a test"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Kap-5711")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
