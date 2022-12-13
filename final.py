# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 10:17:54 2022

@author: qomon
"""
#in this assignment, i created a code which helps you know estimated amount of money you might spend when you go out. i added several restaurants with its menu and prices. the code also asks coupon or membership card and check it if it is valid.
#you will see the final estimated amount of money on there.

# Define the menus and prices for each restaurant
leo_pizza = {
    "cheese pizza": 6000,
    "grilled pizza": 7000,
    "potato pizza": 9000,
    "special pizza":12000,
    "cola": 2000,
    "fanta": 2000,
    "water": 1000,
}

burger = {
    "chicken burger": 8000,
    "beef burger": 9000,
    "fish burger": 10000,
    "sandwich":8000,
    "fries":4000,
    "cola": 1500,
    "fanta": 1400,
    "water": 0,
}

kfc = {
    "burger": 6000,
    "chicken kfc": 8000,
    "triple treat": 10000,
    "strips": 12000,
    "wings":500,
    "double":6500,
    "cola": 1600,
    "fanta": 1200,
    "water": 0,
}

kebab = {
    "uz kebab": 10000,
    "chicken kebab": 7000,
    "rice kebab": 6500,
    "special kebab": 9500,
    "samosa":4000,
    "shashlik":6000,
    "cola": 1900,
    "fanta": 1900,
    "water": 0,
}

# Ask the user to choose a restaurant
restaurant = input("Please choose a restaurant: Leo_pizza, Burger, KFC, Kebab: ")

# Show the menu and prices for the chosen restaurant
if restaurant.lower() == "leo_pizza":
    print("Leo Pizza menu:")
    for item, price in leo_pizza.items():
        print("-", item, ":", price)
elif restaurant.lower() == "burger":
    print("Burger menu:")
    for item, price in burger.items():
        print("-", item, ":", price)
elif restaurant.lower() == "kfc":
    print("KFC menu:")
    for item, price in kfc.items():
        print("-", item, ":", price)
elif restaurant.lower() == "kebab":
    print("Kebab menu:")
    for item, price in kebab.items():
        print("-", item, ":", price)
else:
    print("Invalid restaurant name")

# Ask the user to order items from the menu
order = []
order_price = 0

while True:
    item = input("Please choose an item from the menu (or enter 'done' to finish ordering): ")
    if item.lower() == "done":
        print('\nGreat, I got your orders, will make them with heart')
        break
    elif restaurant.lower() == "leo_pizza":
        if item in leo_pizza:
            order.append(item)
            order_price += leo_pizza[item]
        else:
            print("Invalid item name")
    elif restaurant.lower() == "burger":
        if item in burger:
            order.append(item)
            order_price += burger[item]
        else:
            print("Invalid item name")
    elif restaurant.lower() == "kfc":
        if item in kfc:
            order.append(item)
            order_price += kfc[item]
        else:
            print("Invalid item name")
    elif restaurant.lower()=="kebab":
        if item in kebab:
            order.append(item)
            order_price+= kebab[item]
        else:
            print("Invalid item name")
import re
phone_number_pattern = re.compile(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$')
membership_card_pattern = re.compile(r'^[A-Z]{2}[0-9]{4}$')


# Now ask if the customer has discount coupon or membership card


while True:
    ask= input('\nDo you have a discount coupon or a membership card? (yes/no)')
    if ask=='no':
        break
    else:
        ask_discount=input('\nGreat, which one do you have discount coupon (dc) or membership card (mc) ')
        
        
        count=0
        while count!=3:
                    
             if ask_discount=='dc':
                  phone_number=input("\nPlease, write your phone number to confirm your Coupon:")
                              
                  if phone_number_pattern.search(phone_number):
                     order_price= order_price- order_price*0.1
                     print("\nAccepted")
                     count=3
            
                  else:
                       print('\n Please, give a valid phone number') 
                       count=count+1
                       
             elif ask_discount=='mc':
                membership_card_number=input('\n Please, write membership card number to confirm: ')
                if membership_card_pattern.search(membership_card_number):
                    order_price = order_price - order_price * 0.05
                    count=3
                else:
                    print('\nPlease, give a valid membership card number')
                    count=count+1

        break
# final part, ask if he\she wants to eat out or inside of the restaurant
while True:
    place=input('\nWhere do you want to eat in (N) or eat out (T)')
    if place.upper()=='N':
        print('\nGreat, cant wait to see you here')
        break
    else:
        print('\nOkey, that sounds reasonable,delivery fee is 4000, your orders will be ready soon))')
        order_price=order_price+ 4000
        break
        
print(f'\nYour final order:{order}')
print(f'\nFinal estimated price: {order_price}')



       

        














