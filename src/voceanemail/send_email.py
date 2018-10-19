# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
# fp = open(textfile, 'rb')
# fp.close()
def sendEmail(time):
    msg = MIMEText(f"Testing email notification from Bing Li and the time is {time}")
    me = 'zhbitjean@gmail.com'
    you = 'zhbitjean@gmail.com'
    msg['Subject'] = 'Testing email notification'
    msg['From'] = me
    msg['To'] = you
    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com:587')
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(me, "myGoogle_881")
    s.sendmail(me, [you], msg.as_string())
    s.quit()
