from datetime import date
from datetime import datetime
import calendar
from discount_policy import DiscountPolicy


class Sale:

    def __end_of_next_month(self, current_date):
        last_day_of_month = calendar.monthrange(current_date.year, current_date.month)[1]
        return datetime(current_date.year, current_date.month + 1, last_day_of_month)

    def send_discount_message(self, customer):
        policy = DiscountPolicy()
        is_birthday = customer.has_birthday_in(date.today().month)
        is_pensioner = customer.is_pensioner_by(self.__end_of_next_month(date.today()))
        birthday_discount = is_birthday*policy.birthday_discount
        pensioner_discount = is_pensioner*policy.pensioner_discount
        return max(birthday_discount, pensioner_discount)
