import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint

class EmailSender:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = 'smtpout.secureserver.net'
        self.smtp_port = 465  # 465 is the default port for SMTP over SSL/TLS
    
    def send_email(self, receiver_email, subject, body):
        # Create a MIME multipart message
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = receiver_email
        message['Subject'] = subject

        # Attach the body to the email
        message.attach(MIMEText(body, 'plain'))

        # Create SMTP session
        server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)  # SMTP_SSL for SSL/TLS
        server.login(self.sender_email, self.sender_password)  # Login

        # Send the email
        server.sendmail(self.sender_email, receiver_email, message.as_string())

        # Quit the SMTP session
        server.quit()



if __name__ == '__main__':
    # Example usage:
    sender = EmailSender('info@playbotworld.com', 'rT3$y9p2#x') #email credentials
    sender.send_email('mytoplux@gmail.com', 'Please activate your account', f'Your temporary code is {randint(1000,9999)} ')