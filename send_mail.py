import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port =2525
    smtp_server = 'sandbox.smtp.mailtrap.io'
    login = '597bc3634014f7'
    password = '36f546fce6b5af'
    message = f"<h3>New Feedback Submission</h3><ul><li> Customer: {customer}</li><li> Dealer: {dealer}</li><li> Rating: {rating}</li><li> Comments: {comments}</li></ul>"
    
    sender_email = "DailyAsst_cs <Da@customersupport.com>"
    receiver_email = "Bob_dylan <BobD@yahoo.com>"
    msg = MIMEText (message, 'html')
    msg['Subject'] = 'App feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    #send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login,password)
        server.sendmail(sender_email,receiver_email,msg.as_string())