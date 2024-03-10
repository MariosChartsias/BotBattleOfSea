import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    def __init__(self):
        self.smtp_server = 'smtpout.europe.secureserver.net' #'smtp-mail.outlook.com'
        self.smtp_port = 465 #587
        self.sender_email = 'info@playbotworld.com'
        self.sender_password = 'rT3$y9p2#x!'

    def send_email(self, recipient_email, verif_code):
        # Create a message object
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = recipient_email
        message['Subject'] = 'Please confirm your email address'

        # Add the email body
        body = verif_code
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.sender_email, self.sender_password)

            # Send the email
            server.send_message(message)

            # Send email
            server.sendmail(self.sender_email, recipient_email, message.as_string())
        
        print("Email sent successfully!")


if __name__ == '__main__':
    email_sender = EmailSender()
    email_sender.send_email('mytoplux@gmail.com','geia')


