'''
Created on Jul 25, 2016

@author: trannh08
'''
class Customer(object):
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print("This is your shopping cart!")

class ReturningCustomer(Customer):
    def display_order_history(self):
        print("This is your order history!")

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()
