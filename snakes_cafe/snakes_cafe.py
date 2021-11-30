import sys

menu = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************"""
print(menu)

def orderStuff():
    meal = []
    while True:
        orderedItem = input(">")
        if orderedItem.lower() == "quit":
            print(f"You ordered: {meal}")
            sys.exit()
        elif orderedItem not in meal:
            print(f"** 1 order of {orderedItem} have been added to your meal **")
            meal.append(orderedItem)
        elif orderedItem in meal:
            order = meal.count(orderedItem) + 1
            print(f"** {order} orders of {orderedItem} have been added to your meal **")
            meal.append(orderedItem)

orderStuff()