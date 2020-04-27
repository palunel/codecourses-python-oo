from datetime import datetime
import pandas as pd
import smtplib
from os import environ


def send_discount_message():
    # We want to send an email to all customers in our database informing them of the discounts the are eligible
    # for in hte upcoming month

    # Business rules:
    # 1. On your birthday you get 10% discount
    # 2. If you are a pensioner (older than 62) you get 15% discount
    # 3. You get maximum of birthday and pensioner discount

    # First read list of all customers
    customers = pd.read_csv("customers.csv")

    # For each customer see if they it is their birthday next month or if they are pensioner next month
    today = datetime.today()
    discounts = pd.DataFrame(columns=["birth_day", "pensioner"])
    for i in range(len(customers)):
        birth_date = datetime.strptime(customers["customer_date_of_birth"][i], "%Y-%m-%d")
        customers.loc[i, "birth_day"] = (today.month + 1) == birth_date.month
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age = today.year - birth_date.year - 1
        else:
            age = today.year - birth_date.year
        customers.loc[i, "pensioner"] = age >= 62

    # Now we can calculate the discount for each customer
    for i in range(len(customers)):
        discount = 0
        if customers.loc[i, "birth_day"]:
            customers.loc[i, "discount"] = 0.1
        elif customers.loc[i, "pensioner"]:
            customers.loc[i, "discount"] = 0.15
        elif customers.loc[i, "birth_day"] and customers.loc[i, "pensioner"]:
            customers.loc[i, "discount"] = max(0.15, 0.1)
        else:
            customers.loc[i, "discount"] = 0
    print(customers)

    # Now we send them all messages
    sender = "info@the_store_company.com"
    message = ""
    receivers = ""

    for i in range(len(customers)):
        if customers.loc[i, "discount"] > 0:
            subject = ""
            body = ""
            if customers.loc[i, "pensioner"]:
                subject = "Pensioner discount available next month!"
                body = f"Dear {customers.loc[i, 'customer_name']}, since you are a pensioner next month, " \
                       f"you will be eligible" \
                       f" for a discount of {customers.loc[i, 'discount'] * 100}%"
            if customers.loc[i, "birth_day"]:
                subject = "Enjoy your birthday discount next month!"
                body = f"Dear {customers.loc[i, 'customer_name']}, since it is your birthday next month, " \
                       f"you will be eligible" \
                       f" for a discount of {customers.loc[i, 'discount'] * 100}%"

            if customers.loc[i, "contact_preference"] == "email":
                # implement email protocols
                message = f"""Subject: {subject}

                {body}.
                """

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(environ.get("email"), environ.get("pwd"))
                server.sendmail(sender, "paul.nel@pm.me", message,)

                print(f"The following message was successfully emailed from {sender} to "
                      f"{customers.loc[i, 'customer_email']}:\n\n{message}\n\n")

            if customers.loc[i, "contact_preference"] == "text":
                # implement email protocols
                message = f'{body}'
                print(f"The following message was successfully send via text from {sender} to "
                      f"{customers.loc[i, 'customer_phone']}:\n\n{message}\n\n")


if __name__ == "__main__":
    send_discount_message()
