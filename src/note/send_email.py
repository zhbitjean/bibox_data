import smtplib
from email.message import EmailMessage
import os


def sendEmail(time):
    gmail_user = 'zhbitjean@gmail.com'
    gmail_password = "myGoogle_881"
    send_from = '<zhbitjean@gmail.com>'
    to = ['<zhbitjean@gmail.com>', '<xhq422986742@gmail.com>']
    subject = "Test email notification."
    msg = EmailMessage()
    msg.set_content(f"Testing email notification from Bing Li and the time is {time}")
    # msg = f"""
    # From: {send_from}\n
    # To: {to}\n
    # Subject: {subject}\n
    #
    # Testing email notification from Bing Li and the time is {time}"""
    msg['Subject'] = subject
    msg['From'] = send_from
    msg['To'] = to
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()
    s.login(gmail_user, gmail_password)
    s.ehlo()
    # s.sendmail(send_from, to, msg)
    s.send_message(msg)
    s.close()
    print("Email sent")


if __name__ == "__main__":
    sendEmail("time")
