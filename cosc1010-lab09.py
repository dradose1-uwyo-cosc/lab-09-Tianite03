# Talon Bluemel
# UWYO COSC 1010
# 10-14-24
# Lab 9
# Lab Section:12
# Sources, people worked with, help given to:
# Your
# Comments
# Here

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.


# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
# - getNumberOfOrders()
#   - This will simply return the number of orders.


# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.


# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""

class Pizza:
    def __init__(self, size, sauce='red'):
        if size < 10:
            size = 10
        self.size = size
        self.sauce = sauce
        self.toppings = ["cheese"]
    def define_size(self, size):
        if size > 10:
            self.size = size
        else:
            self.size = 10
    def get_size(self):
        return self.size
    def set_toppings(self, *toppings):
        self.toppings.extend(toppings)
    def get_amount_of_toppings(self):
        return len(self.toppings)
    def get_sauce(self):
        return self.sauce
class Pizzeria:
    price_per_topping = 0.30
    price_per_inch = 0.60

    def __init__(self):
        self.orders = 0
        self.pizzas = []

    def place_order(self):
        self.orders += 1
        size = int(input("Please enter the size of the pizza you want as a whole number. Smallest size is 10: "))
        sauce = input("What kind of sauce would you like? If left blank the sauce will be red: ")
        toppings = []
        while True:
            topping = input("Enter the toppings you would like one by one, leave blank when done: ")
            if not topping:
                break
            toppings.append(topping)
        
        pizza = Pizza(size, sauce)
        pizza.set_toppings(*toppings)
        self.pizzas.append(pizza)
    def get_price(self):
        if not self.pizzas:
            return "No pizzas ordered yet"
        last_ordered = self.pizzas[-1]
        size_price = last_ordered.get_size() * self.price_per_inch
        toppings_price = last_ordered.get_amount_of_toppings * self.price_per_topping
        total_price = size_price + toppings_price
        return total_price
    def receipt(self):
        if not self.pizzas:
            print("No pizzas ordered yet")
            return
        last_ordered = self.pizzas[-1]
        print(f"You ordered a {last_ordered.get_size()} pizza with {last_ordered.get_sauce()} sauce and the following toppings: ")
        for topping in last_ordered.toppings:
            print(f"{topping}")
        size_price = last_ordered.get_size() * self.price_per_inch
        toppings_price = last_ordered.get_amount_of_toppings() * self.price_per_topping
        total_price = size_price + toppings_price
        print(f"You ordered a {last_ordered.get_size()} pizza for ${size_price}")
        print(f"You had {last_ordered.get_amount_of_toppings()} topping(s) for ${toppings_price}")
        print(f"Your total price is ${total_price}")

    def get_number_of_orders(self):
        return self.orders
pizzeria = Pizzeria()
while True:
    order = input("Would you like to place an order? or exit to end: ")
    if order.lower() == 'exit':
        break
    elif order.lower() == 'yes':
        pizzeria.place_order()
        pizzeria.receipt()

print(f"Total orders placed: {pizzeria.get_number_of_orders()}")