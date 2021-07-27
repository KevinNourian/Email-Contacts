import pathlib
import os


def choose_stock_message(indices, friends, base_path):
    """Checks if the friend is in the data base and returns the stock message entered by the user."""

    file_name = r'messages.txt'

    if len(indices) == 0:
        print('\nStock message machine says, "Check the name and try again."')

    else:
        for index in indices:
            first_name = friends[index][0]
            last_name = friends[index][1]
            name = first_name + " " + last_name

        print("\nThe friend you have chosen is: " + name)

        while True:
            choose_stock_message = input("Which message would you like to choose? Enter a number: ")

            try:
                stock_message = int(choose_stock_message)

            except ValueError:
                print("\nPlease enter a number!")

            else:
                stock_message = int(choose_stock_message) - 1

                path = os.path.join(base_path, file_name)  # Concatenates file directory paths.
                with open(path) as file_object:
                    messages = file_object.readlines()

                if 0 <= stock_message <= 50:
                    stock_message = messages.pop(stock_message)
                    print("\nYou chose message number: " + stock_message[0:3])
                    print("\nThe message is: \n" + stock_message[4:])
                    return stock_message
                    break

                else:
                    print("\nPlease choose a number from 1 - 50")


def input_personal_message(indices, friends):
    """Checks if the friend is in the data base and returns the personal message entered by the user."""

    if len(indices) == 0:
        print('\nPersonal message machine says, "Check the name and try again."')

    else:
        for index in indices:
            first_name = friends[index][0]
            last_name = friends[index][1]
            name = first_name + " " + last_name

        print("\nThis personal message is for: " + name)

        personal_message = input("Please enter your personal message: ")

        return personal_message, indices
