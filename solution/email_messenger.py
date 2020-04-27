from messenger_service import MessengerService
from os import environ
import smtplib


class EmailMessenger(MessengerService):

    def __init__(self, name, contact):
        super(EmailMessenger, self).__init__(name, contact)
        print("Email Service instantiated")

    def send_message(self, message_from, subject="", body=""):
        message = f"""Subject: {subject}\n
            
                {body}
                """
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(environ.get("email"), environ.get("pwd"))
        server.sendmail(message_from, self._contact, message)
        print(f"The following message was successfully emailed from {message_from} to "
              f"{self._name} on {self._contact}:\n\n{message}\n\n")
