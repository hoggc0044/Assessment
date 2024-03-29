# functions go here
def unit_checker(question):

    while True:
        response = input(question).lower()

        if response == "grams" or response == "g":
            return "grams"
        elif response == "kilograms" or response == "kg":
            return "kilograms"
        elif response == "mililitres" or response == "mL":
            return "mililitres"
        elif response == "litres" or response == "litres":
            return "litres"
        elif response == "xxx":
            return "Next Question"
        else:
            print("INCORRECT RESPONSE: Please correct your response in order to proceed.")


# main routine goes here
want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "xxx":
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


print("we are done")
