import smtplib
from email.message import EmailMessage


def sendEmail(time, msg_text=None):
    gmail_user = 'zhbitjean@gmail.com'
    gmail_password = "myGoogle_881"
    send_from = 'zhbitjean@gmail.com'
    to = ['zhbitjean@gmail.com', 'xhq422986742@gmail.com']
    subject = "Test email notification."
    msg = EmailMessage()
    if msg_text is None:
        msg_text = f"Testing email notification from Bing Li and the time is {time}. "
    msg.set_content(msg_text)
    msg['Subject'] = subject
    msg['From'] = send_from
    msg['To'] = to
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()
    s.login(gmail_user, gmail_password)
    s.ehlo()
    s.send_message(msg)
    s.close()
    print("Email sent")


if __name__ == "__main__":
    sendEmail("time")
