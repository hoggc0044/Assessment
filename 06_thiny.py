unit_list = ["gram", "kilogram", "miliLitre", "Litre"]


def string_checker(question, num_letters, valid_responses):

    error = "ERROR: INCORRECT RESPONSE"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


for case in range(0, 5):
    unit = string_checker("Please enter the measurement unit (g, kg, mL, L):", 1, unit_list)

    print("Unit selected:", unit, "s")

