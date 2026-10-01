class Account:

    def account_info(self):
        print("This is a bank account")


class Saving(Account):

    def save_money(self):
        print("Saving account saves money")


class Current(Account):

    def withdraw(self):
        print("Current account withdraws money")


class Customer(Saving, Current):

    def customer_info(self):
        print("Customer can use saving and current account both")


# Object
c = Customer()

c.account_info()
c.save_money()
c.withdraw()
c.customer_info()