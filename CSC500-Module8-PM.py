# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 11:02:50 2023

@author: pulik
"""

#%%

"""
Step 1: Build the ItemToPurchase class with attributes name, price, quantity, 
a default constructor, and a pethod to print the item's cost
"""

class ItemToPurchase:
    def __init__(self, 
                 name = "none", 
                 price = 0.0, 
                 quantity = 0.0, 
                 description = "none"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    def print_item_cost(self):
        self.cost = self.price * self.quantity
        print(f"{self.name} {self.quantity} @ ${self.price} = ${self.cost}")
        
#%%

"""
Step 2: Prompt the user for two items and create two objects of the 
ItemToPurchase class
"""

item1 = ItemToPurchase()
print("Item 1")
item1.name = input("Enter the item name:\n")
item1.price = float(input("Enter the item price:\n"))
item1.quantity = int(input("Enter the item quantity:\n"))

item2 = ItemToPurchase()
print("Item 2")
item2.name = input("Enter the item name:\n")
item2.price = float(input("Enter the item price:\n"))
item2.quantity = int(input("Enter the item quantity:\n"))

#%%

# Step 3: Add the costs of the two items together and output the total cost.

print("\nTOTAL COST")
item1.print_item_cost()
item2.print_item_cost()

total_cost = item1.cost + item2.cost 
print(f"Total: ${total_cost}")

#%%

"""
Step 4: Build the ShoppingCart class with attributes customer_name, current_date,
and cart_items, as well as with methods add_item(), remove_item(), modify_item(),
get_num_items_in_cart(), get_cost_of_cart(), print_total(), and print_descriptions()
"""

class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
        
    def add_item(self, added_item):
        self.cart_items.append(added_item)
        
    def remove_item(self, removed_item):
        for item in self.cart_items:
            if item.name == removed_item.name:
                self.cart_items.remove(item)
                return
        print('Item not found in cart. Nothing removed.')
        
    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.name == modified_item.name:
                if modified_item.description != 'none':
                    item.description = modified_item.description
                if modified_item.price != 0.0:
                    item.price = modified_item.price
                if modified_item.quantity != 0.0:
                    item.quantity = modified_item.quantity
                return
        print('Item not found in cart. Nothing modified.')
        
    def get_num_items_in_cart(self):
        total_quantity = sum(item.quantity for item in self.cart_items)
        return total_quantity
    
    def get_cost_of_cart(self):
        total_cost = sum(item.price * item.quantity for item in self.cart_items)
        return total_cost
    
    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())
        for item in self.cart_items:
            item.print_item_cost()
        print("Total: ${:.2f}".format(self.get_cost_of_cart()))
        
    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print('Item Descriptions')
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")
            
#%%

"""
Step 5: Implement the print_menu() function that takes a ShoppingCart parameter
and outputs a menu of options to manipulate.
"""

def print_menu(ShoppingCart):
    while True:
        print('\nMENU')
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        
        choice = input('Choose an option: ').lower()
        
        if choice == 'a':
            item = ItemToPurchase()
            print("\nADD ITEM TO CART")
            item.name = input("Enter the item name:\n")
            item.description = input("Enter the item description:\n")
            item.price = float(input("Enter the item price:\n"))
            item.quantity = int(input("Enter the item quantity:\n"))
            ShoppingCart.add_item(item)
        
        elif choice == 'r':
            removed_item = ItemToPurchase()
            print("\nREMOVE ITEM FROM CART")
            removed_item.name = input('Enter the name of the item to remove:\n')
            ShoppingCart.remove_item(removed_item)
            
        elif choice == 'c':
            modified_item = ItemToPurchase()
            print("\nCHANGE ITEM QUANTITY")
            modified_item.name = input("Enter the name of the item to modify:\n")
            modified_item.price = float(input("Enter the new price:\n"))
            modified_item.quantity = int(input("Enter the new quantity:\n"))
            modified_item.description = input("Enter the new description:\n")
            ShoppingCart.modify_item(modified_item)
            
        elif choice == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            ShoppingCart.print_descriptions()
            
        elif choice == 'o':
            print('\nOUTPUT SHOPPING CART')
            ShoppingCart.print_total()
            
        elif choice == 'q':
            break
        
        else:
            print('Invalid choice. Please try again.')
            
#%%

def main():
    customer_name = input("\nEnter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    shopping_cart = ShoppingCart(customer_name, current_date)
    print_menu(shopping_cart)


if __name__ == "__main__":
    main()
        
                
            
















