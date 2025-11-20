# 5.  RetailItem Class
# Write a class named RetailItem that holds data about an item in a retail store. The class 
# should store the following data in attributes: item description, units in inventory, and price.
# Once  you  have  written  the  class,  write  a  program  that  creates  three  RetailItem  objects  
# and stores the following data in them:
# Description Units in Inventory Price
# Item #1 Jacket 12 59.95
# Item #2 Designer Jeans 40 34.95
# Item #3 Shirt 20 24.95

class RetailItem:
    def __init__(self, description, units, price):
        self.description = description
        self.units = units
        self.price = price

# Create three RetailItem objects
item1 = RetailItem("Jacket", 12, 59.95)
item2 = RetailItem("Designer Jeans", 40, 34.95)
item3 = RetailItem("Shirt", 20, 24.95)

# Display the items
print(f"Item #1: {item1.description}, Units: {item1.units}, Price: ${item1.price}")
print(f"Item #2: {item2.description}, Units: {item2.units}, Price: ${item2.price}")
print(f"Item #3: {item3.description}, Units: {item3.units}, Price: ${item3.price}")