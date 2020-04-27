from messenger_service import MessengerService


class TextMessenger(MessengerService):

    def __init__(self, name, contact):
        super(TextMessenger, self).__init__(name, contact)
        print("Text Service instantiated")

    def send_message(self, message_from, subject="", body=""):
        print(f"The following message was successfully send via text from {message_from} to "\
              f"{self._name} on {self._contact}:\n\n{body}\n\n")
