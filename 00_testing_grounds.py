def num_check(question, error, num_type=float):  # Add 'num_type' with a default value of float
    valid = False
    while not valid:
        try:
            response = num_type(input(question))
            if response <= 0:
                print("Please enter a valid positive number.")
            else:
                return response
        except ValueError:
            print(error)


def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)
        if response == "":
            print("{}\nPlease try again.".format(error))  # Removed the period from the error message
        else:
            return response


# Get recipe name
recipe_name = not_blank("Recipe name: ", "Please enter a valid response. Try again.")

# Get ingredient name
ingredient_name = not_blank("Ingredient name: ", "Please enter a valid response. Try again.")

# Get unit type
unit_type = not_blank("Unit type: ", "Please enter a valid response. Try again.")

# Get amount
amount = num_check("Ingredient Amount: ", "Please only enter positive numbers. Try again.")