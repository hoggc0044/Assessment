# Ask the user for the item name
item_name = input("What is the item name? ")

# Ask the user for the quantity
quantity = int(input("How many items would you like? "))

# Ask the user for the price
price = float(input("What is the price of each item? "))

# Calculate the total cost
total_cost = quantity * price

# Create a list of the item details
item_details = [item_name, quantity, price, total_cost]

# Print the list in a formatted way
print("| Item Name | Quantity | Price | Total |")
for item_detail in item_details:
    print("| {} | {} | {} | {} |".format(item_detail, item_detail, item_detail, item_detail))
