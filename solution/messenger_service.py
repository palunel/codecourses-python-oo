from abc import ABC, abstractmethod


class MessengerService(ABC):

    def __init__(self, name, contact):
        self._name = name
        self._contact = contact
        print("Message Service instantiated")

    @abstractmethod
    def send_message(self):
        pass
