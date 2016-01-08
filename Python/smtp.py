# Send email with text format
import smtplib

sender = 'from@fromdomain.com'
receivers = ['test_thysa1@mailinator.com']
#message = "This is a test e-mail message"
message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

s = smtplib.SMTP("67.20.167.99",25)
s.set_debuglevel(1)
s.sendmail(sender, receivers, message)
print "Successfully sent email"

# Send email with HTML format
import smtplib

sender = 'from@fromdomain.com'
receivers = ['test_thysa1@mailinator.com']
message = """From: From Person <from@fromdomain.com>
To: To Person <test_thysa1@mailinator.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

s = smtplib.SMTP("67.20.167.99",25)
s.set_debuglevel(1)
s.sendmail(sender, receivers, message)
print "Successfully sent email"

# Send email with attachment
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders

SUBJECT = "Email Data"
sender = 'from@fromdomain.com'
receivers = ['namitachaudhari119@gmail.com']

msg = MIMEMultipart()
msg['Subject'] = "Email Data"
msg['From'] = "from@fromdomain.com"
msg['To'] = "test_thysa1@mailinator.com"

part = MIMEBase('application', "octet-stream")
part.set_payload(open("/tmp/test.txt", "rb").read())
Encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="/tmp/test.txt"')

msg.attach(part)

s = smtplib.SMTP("67.20.167.99",25)
s.sendmail(sender, receivers, msg.as_string())
print "Successfully sent email"

