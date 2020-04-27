from discount_policy import DiscountPolicy
from email_messenger import EmailMessenger
from text_messenger import TextMessenger


class Customer:

    def __init__(self, name, birth_date, email, phone, preference):
        self.name = name
        self.birth_date = birth_date
        self.email = email
        self.phone = phone
        self.messenger = EmailMessenger(self.name, self.email) if preference.lower() == "email" \
            else TextMessenger(self.name, self.phone)

    def has_birthday_in(self, date):
        return date.month == self.birth_date.month

    def is_pensioner_by(self, target_date):
        policy = DiscountPolicy()
        return self.__get_age(self.birth_date, target_date) >= policy.pensionable_age

    def __get_age(self, born, today):
        age = today.year - born.year
        if today.month < born.month or (today.month == born.month and today.day < born.day):
            age -= 1
        return age

    def contact(self, message_from, subject="", body=""):
        self.messenger.send_message(message_from, subject, body)
