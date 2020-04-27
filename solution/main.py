from shop import Shop


if __name__ == "__main__":
    # customer = Customer("Paul", datetime.datetime(1951, 4, 13), "paul.nel@pm.me", "555-555-5555", "email")
    # sale = Sale()
    # sale_amount = 1000
    # discount = sale.send_discount_message(customer)
    # print(f"{customer.name} received R{discount*sale_amount} discount on their purchase of R{sale_amount} ")

    shop = Shop("customers.csv")
    shop.issue_discounts()
