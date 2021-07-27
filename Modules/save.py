import os # For concatenating file directory paths.
import pathlib


def save_search_results (base_path, today, indices, friends, label):
    '''Saves the results of the search in text file, searches.txt.'''

    file_name = r'searches.txt'

    if len (indices) == 0:
        print ("Nothing will be recorded in file 'searches.txt.'")

    else:
        path = os.path.join(base_path, file_name) # Concatenates file directory paths.

        with open (path, 'a' ) as file_object:

            file_object.write("\n\n" + today)
            file_object.write(label + "\n")

            for index in indices:
                file_object.write("\n" + friends [index][0] + " ")
                file_object.write(friends [index][1] + "\n")
                file_object.write("\t" + "Email: " + friends [index][2] + "\n")
                file_object.write("\t" + "Telephone: " + friends [index][3] + "\n")
                file_object.write("\t" + "Day: " + friends [index][4] + "\n")
                file_object.write("\t" + "Month: " + friends [index][5] + "\n")

        print ("The result of your seach has been recorded in file, 'searches.txt'.")


def save_stock_message (base_path, today, indices, friends, stock_message):
    '''Saves today's date, friend's name and the content of the email sent in the text file, sent.txt.'''

    file_name = r'sent.txt'
    label = "\n" + 'Email sent: '

    if len (indices) == 0:
        print ("Nothing will be saved.")

    else:
        print ("An email will be sent to your friend and a record is kept in file sent.txt")
        path = os.path.join(base_path, file_name) # Concatenates file directory paths.

        for index in indices:
            first_name = friends [index][0]
            last_name = friends [index][1]
            name = first_name + " "  + last_name

        with open (path, 'a' ) as file_object:
            file_object.write("\n" + today + "\n")
            file_object.write("To: " + name)
            file_object.write("\t" + label + "\n")
            file_object.write("\t" + "Message number: " + stock_message[0:2] + "\n")
            file_object.write("\t" + stock_message [4:] + "\n")

    return indices


def save_personal_message (base_path, today, indices, friends, personal_message):
    '''Saves today's date, friend's name and the content of the email sent in the text file, sent.txt.'''

    file_name = r'sent.txt'
    label = "\n" + 'Email sent: '

    if len (indices) == 0:
        print ("Nothing will be saved.")

    else:
        print ("An email will be sent to your friend and a record is kept in file sent.txt")
        path = os.path.join(base_path, file_name) # Concatenates file directory paths.

        for index in indices:
            first_name = friends [index][0]
            last_name = friends [index][1]
            name = first_name + " "  + last_name

        with open (path, 'a' ) as file_object:
            file_object.write("\n" + today + "\n")
            file_object.write("To: " + name)
            file_object.write("\t" + label + "\n")
            file_object.write("\t" + personal_message[0] + "\n")

    return indices


def save_combined_message (base_path, today, indices, friends, stock_message, personal_message):
    '''Saves today's date, friend's name and the content of the email sent in the text file, sent.txt.'''

    file_name = r'sent.txt'
    label = "\n" + 'Email sent: '

    if len (indices) == 0:
        print ("\nNothing will be saved. \n")

    else:
        print ("An email will be sent to your friend and a record is kept in file sent.txt")
        path = os.path.join(base_path, file_name) # Concatenates file directory paths.

        for index in indices:
            first_name = friends [index][0]
            last_name = friends [index][1]
            name = first_name + " "  + last_name

        with open (path, 'a' ) as file_object:
            file_object.write("\n" + today + "\n")
            file_object.write("To: " + name)
            file_object.write("\t" + label + "\n")
            file_object.write("\t" + "Stock message number: " + stock_message[0:2] + "\n")
            file_object.write("\t" + stock_message [4:])
            file_object.write("\t" + "Personal message: " + "\n")
            file_object.write ("\t" + personal_message[0] + "\n")

    return indices
