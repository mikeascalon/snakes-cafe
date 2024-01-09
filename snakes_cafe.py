
print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("** To quit at any time, type \"quit\" **")
print("**************************************")

menu = {
    'appetizers': ['Wings', 'Cookies', 'Spring Rolls'],
    'entrees': ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
    'desserts': ['Ice Cream', 'Cake', 'Pie'],
    'drinks': ['Coffee', 'Tea', 'Unicorn Tears']
}

user_orders = {}

for category, items in menu.items():
    print(f"\n{category.capitalize()}")
    print("----------")
    for item in items:
        print(item)

print("\n" )

print("**************************************")
print("**    What would you like to order?   **")
print("**************************************")

while True:
    # Get user input for the order (help from chatGPT)
    user_order = input("> ")

    if user_order.lower() == "quit":
        break

    # Add the order to the user_orders dictionary (help from chatGPT)
    user_orders[user_order] = user_orders.get(user_order, 0) + 1

    # Print acknowledgment message ( help from chatGPT)
    order_count = user_orders[user_order]
    print(f"\n** {order_count} order{'s' if order_count > 1 else ''} of {user_order} "
          f"{'have' if order_count > 1 else 'has'} been added to your meal **")