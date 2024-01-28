import smtplib
sender_mail ='sender@gmail.com'
receiver_mail=['receiver@gmail.com']
message = """From: From Person %s
TO:ToPerson %s
Subject: Sending SMTP e-mail
This is a test e-mail message.
"""%(sender_mail,receiver_mail)
try:
    password = input('Enter the password ');
    smtplib.SMTP('gmail.com',587)
    smtpobj.login((sender_mail,password))
    smtpObj.sendmail(sender_mail,receiver_mail,message)
    print("successfully sent email")
except Exception:
    print("Error :unable to send email")
