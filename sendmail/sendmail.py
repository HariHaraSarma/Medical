import smtplib
from email.mime.text import MIMEText
SMTP_SERVER = "smtp.mail.yahoo.com"
SMTP_PORT = 587
SMTP_USERNAME = "dineshreddy60"
SMTP_PASSWORD = "denee225522"
EMAIL_FROM = "dineshreddy60@yahoo.com"
EMAIL_TO = "damavinod7@gmail.com"
EMAIL_SUBJECT = "your transport details"
co_msg = """
Dear customer,

     We have sent your ordered items by navatha transport



     ****HAVE A NICEDAY****

"""
def send_email():
    msg = MIMEText(co_msg)
    msg['Subject'] = EMAIL_SUBJECT +   "thanks for your order"
    msg['From'] = EMAIL_FROM 
    msg['To'] = EMAIL_TO
    debuglevel = True
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.set_debuglevel(debuglevel)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()

if __name__=='__main__':
    send_email()
