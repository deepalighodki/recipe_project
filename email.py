#Below code is used to send email using MIME
text=msg_body
subject="Test emai"
email_from="Sender"
email_to=['receipient email'] it can be lists of email
message=MIMEMultipart()
message['From']=email_from
message['To']=','.join(email_to)
message['Subject']=subject
email_session=smtplib.SMTP(Host,Port,timeout=30)
email_session.starttls()
email_session.sendmail(email_from,email_to,message.as_string())
email.session.quit()
