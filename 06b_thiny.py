payment_list = ["QSlot", "ESlot", "GSlot"]


def string_checker(question, num_letters, valid_responses):

    error = "INCORRECT RESPONSE"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item:
                return item

        print(error)


for case in range(0, 2):
    pay_method = string_checker("Enter a response (SlotOne, SlotTwo, SlotThree):", 1, payment_list)

    print("you chose", pay_method)