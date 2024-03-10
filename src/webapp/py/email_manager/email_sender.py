import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    def __init__(self):
        self.smtp_server = 'smtp-mail.outlook.com'
        self.smtp_port = 587
        self.sender_email = 'p.menounos@outlook.com'
        self.sender_password = 'Kith@r@1996!'

    def send_email(self, email2send, verif_code):
        # Create a message object
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = email2send
        message['Subject'] = 'RealEstator'

        # Add the email body
        body = verif_code
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.sender_email, self.sender_password)

            # Send the email
            server.send_message(message)


if __name__ == '__main__':
    email_sender = EmailSender()
    email_sender.send_email()
