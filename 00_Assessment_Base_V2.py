# import pandas
# Print introduction
print("************** INTRODUCTION *****************\n\n\n"


      "Welcome to the Recipe Cost Calculator!\n"
      "This calculator is a simple and easy to use tool for calculating a list of things\n"
      "you need to produce things like cakes or meals. Instructions have been created to\n"
      "to show you how to use it. If you'd like to view the instructions, please answer\n"
      "the next question with a yes. If you'd like to give it a go without reading the\n"
      "the instructions, then simply say no to the next question. I hope you enjoy using\n"
      "my calculator!\n\n\n"


      "************ READ INSTRUCTIONS? *************\n\n")


# number checker
def num_check(question, error, num_type):

    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# yes no checker cause pro
def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("INCORRECT RESPONSE: Please correct your response in order to proceed. "
              "Missing argument: yes (y) / no (n). \n")


def currency(x):
    return f"${x:.2f}"


# main routine goes here
want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    print('''\n
    ****** Instructions ******

    Thank you for using my Recipe Cost Calculator!

    Using the calculator is simple! All you need to do is provide how many people you are serving,
    the names of the ingredients you are using (one by one, not all at once) and how much they are!
    It's essential that you provide the unit for each ingredient (i.e. flour; kg;) and the price of
    the item per unit (e.g $4 per kg), and the quantity of the ingredient (i.e. 4kgs of flour).

    The calculator will calculate all the provided information and will give you the total amount you'd
    need to produce whatever it is you are making for the amount of persons you have entered.
     The calculator will also write the information to a text file so it can be shared with other people.


    **************************
    ''')


# Ensures that the string isn't blank
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
