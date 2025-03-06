import smtplib
from email.mime.text import MIMEText
import configparser

class EmailClient:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config/credentials.ini")
        self.smtp_server = config["EMAIL"]["smtp_server"]
        self.port = int(config["EMAIL"]["port"])
        self.email = config["EMAIL"]["address"]
        self.password = config["EMAIL"]["password"]

    def send_email(self, recipient: str, subject: str, body: str):
        """Send email using SMTP"""
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = self.email
        msg["To"] = recipient

        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.starttls()
            server.login(self.email, self.password)
            server.send_message(msg)
