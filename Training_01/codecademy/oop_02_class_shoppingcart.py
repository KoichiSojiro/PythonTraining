'''
Created on Jul 25, 2016

@author: trannh08
'''
class ShoppingCart(object):
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print(product + " added.")
        else:
            print(product + " is already in the cart.")

    def remove_item(self, product):
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product + " removed.")
        else:
            print(product + " is not in the cart.")

my_cart = ShoppingCart("Nhan the Pig")
my_cart.remove_item("car")
my_cart.add_item("car", "$50.00")
my_cart.remove_item("car")