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
