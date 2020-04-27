from customer import Customer
from discount_policy import DiscountPolicy

from datetime import date, datetime
import pandas as pd


class Shop:

    def __init__(self, file_name):
        self._customers = self.__get_customers(file_name)
        self._email = "shop@shopemail.co.za"

    def __get_customers(self, file_name):
        customer_list = pd.read_csv(file_name)
        customers = []
        for index, customer in customer_list.iterrows():
            customers.append(Customer(customer["name"], datetime.strptime(customer["date_of_birth"], "%Y-%m-%d"),
                                      customer["email"], customer["phone"], customer["preference"]))
        return customers

    def issue_discounts(self):
        today = date.today()
        next_month = datetime(today.year, today.month + 1, today.day)
        for customer in self._customers:
            discount = self.__get_discount_for(customer, next_month)
            if discount > 0:
                subject = self.__get_subject(customer, next_month)
                message = self.__get_message(customer, discount)
                customer.contact(self._email, subject, message)

    def __get_discount_for(self, customer, date):
        policy = DiscountPolicy()
        return max(policy.pensioner_discount * customer.is_pensioner_by(date),
                   policy.birthday_discount * customer.has_birthday_in(date))

    def __get_subject(self, customer, date):
        if customer.is_pensioner_by(date):
            return "Pensioner discount available next month!"
        if customer.has_birthday_in(date):
            return "Enjoy your birthday discount next month!"
        return ""

    def __get_message(self, customer, discount):
        return f"Dear {customer.name}, for the duration of next month you will be eligible for a discount " \
               f"of {discount * 100}% at all our stores!"
