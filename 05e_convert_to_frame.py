import pandas as pd


# Function to ensure answer is not blank
def not_blank(question, error):
    while True:
        response = input(question)

        if response.strip() == "":
            print("{}. \n Please try again. \n".format(error))
        else:
            return response


# Function to get a valid number
def get_valid_number(question, error, num_type):
    while True:
        try:
            response = num_type(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


# Function to write DataFrame to a text file
def write_to_file(dataframe, file_name):
    with open(file_name, 'w') as file:
        file.write(dataframe.to_string(index=False))


# Set up lists to store data
recipe_names = []
ingredient_names = []
amounts = []
units = []
prices_per_unit = []
totals = []

while True:
    recipe_name = not_blank("Enter the recipe name (or 'NEXT' to stop): ", "Recipe name can't be blank.")
    if recipe_name.lower() == "next":
        break

    while True:
        ingredient_name = input("Enter the ingredient name (or 'NEXT' to move to the next recipe): ")
        if ingredient_name.lower() == "next":
            break
        if ingredient_name.strip() != "":
            unit = not_blank("Enter the unit for {} in {}: ".format(ingredient_name, recipe_name),
                             "Unit can't be blank.")
            amount = get_valid_number("Enter the amount for {} in {}: ".format(ingredient_name, recipe_name),
                                      "Amount must be a positive number.", float)
            price_per_unit = get_valid_number("Enter the price per unit for {} in {}: ".format(ingredient_name, recipe_name),
                                              "Price per unit must be a positive number.", float)

            # Calculate total cost for each ingredient
            total_cost = amount * price_per_unit

            # Append data to lists
            recipe_names.append(recipe_name)
            ingredient_names.append(ingredient_name)
            amounts.append(amount)
            units.append(unit)
            prices_per_unit.append(price_per_unit)
            totals.append(total_cost)

# Create a DataFrame from the collected data
recipe_data = pd.DataFrame({
    "Recipe": recipe_names,
    "Ingredient": ingredient_names,
    "Amount": amounts,
    "Unit": units,
    "PricePerUnit": prices_per_unit,
    "TotalCost": totals
})

# Write the DataFrame to a .txt file
output_file_name = "recipe_data.txt"
write_to_file(recipe_data, output_file_name)

print(f"\nRecipe data has been saved to '{output_file_name}'.")
