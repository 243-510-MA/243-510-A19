import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText





#   description
#       sends an email
#
#   param
#       emailTo : email address reciving the email
#       bodyContent : text to send
#
#   returns
#       NONE
#
def sendEmail(emailTo, bodyContent) :

    msg = MIMEMultipart()
    msg['From'] = "Serre3800@gmail.com"
    msg['To'] = emailTo
    password = "maisonneuve2019"
    msg['Subject'] = "Voici code de la boite"
    body = str(bodyContent)
    msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
