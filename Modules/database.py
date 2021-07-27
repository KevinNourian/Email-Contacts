import pathlib
import csv  # Read csv file
import os  # File directory manipulations


def friends_data_base(base_path):
    """From rows of the csv table, creates lists for each friends' data and places them within another list."""

    friends = []

    file_name = r'Birthdays.csv'
    path = os.path.join(base_path, file_name)  # Concatenates file directory paths.

    with open(path) as birthday_file:
        reader = csv.reader(birthday_file)
        headers = next(reader)  # Eliminates the header from the csv file to enter the list.
        for row in reader:
            friends.append(row)

    return friends


def messages_data_base(base_path):
    """Returns all messages from the text file, messages.txt."""

    file_name = r'messages.txt'
    path = os.path.join(base_path, file_name)  # Concatenates file directory paths.

    with open(path) as file_object:

        messages = file_object.readlines()

    return messages
