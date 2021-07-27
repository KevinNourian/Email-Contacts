import sys
import yaml

config_file_path = (r'C:\Birthday\Config\config.yml')

def yaml_loader(config_file_path):
    with open (config_file_path, "r") as file_descriptor:
        data = yaml.load (file_descriptor, Loader=yaml.FullLoader)

    return data

data = yaml_loader (config_file_path)

files = data.get('files')

base_path = (files['base_path'])

modules_path = (files['modules_path'])

sys.path.append(modules_path) # Pythons finds modules in the indicated directory.


def choice_0 ():
    indices, label = display.find_all_friends (friends)
    display.display_search_results(indices, friends)
    save.save_search_results (base_path, today, indices, friends, label)

def choice_1 ():
    indices, label = search.full_name_search (friends)
    display.display_search_results(indices, friends)
    save.save_search_results (base_path, today, indices, friends, label)

def choice_2 ():
    indices, label = search.first_name_search (friends)
    display.display_search_results(indices, friends)
    save.save_search_results (base_path, today, indices, friends, label)

def choice_3 ():
    indices, label = search.last_name_search(friends)
    display.display_search_results(indices, friends)
    save.save_search_results (base_path, today, indices, friends, label)

def choice_4 ():
    indices, label = search.close_matches(friends)
    display.display_search_results(indices, friends)
    save.save_search_results (base_path, today, indices, friends, label)

def choice_5 ():
    indices, label = search.month_search(friends)
    display.display_search_results(indices, friends)
    save.save_search_results (base_path, today, indices, friends, label)

def choice_6 ():
    display.display_messages(messages)

def choice_7 ():
    indices, label = search.full_name_search (friends)
    stock_message = message.choose_stock_message (indices, friends, base_path)
    indices = save.save_stock_message (base_path, today, indices, friends, stock_message)
    mail.email_stock_message (indices, friends, stock_message)

def choice_8 ():
    indices, label = search.full_name_search (friends)
    personal_message = message.input_personal_message (indices, friends)
    indices = save.save_personal_message (base_path, today, indices, friends, personal_message)
    mail.email_personal_message (indices, friends, personal_message)

def choice_9 ():
    indices, label = search.full_name_search (friends)
    stock_message = message.choose_stock_message (indices, friends, base_path)
    personal_message = message.input_personal_message (indices, friends)
    indices = save.save_combined_message (base_path, today, indices, friends, stock_message, personal_message)
    mail.email_combined_message (indices, friends, stock_message, personal_message)




if __name__ == '__main__':

    import search
    import display
    import save
    import database
    import date
    import message
    import mail

    friends = database.friends_data_base (base_path)

    messages = database.messages_data_base (base_path)

    today = date.todays_date()

    print("\n" + "Today's date is:", date.todays_date())

    print ("This is the birthday app.")

    print ("What would you like to do?")


    choice_dict = {'0' : choice_0, '1' : choice_1, '2' : choice_2, '3' : choice_3, '4' : choice_4 , '5' : choice_5,
                   '6' : choice_6, '7' : choice_7, '8' : choice_8, '9' : choice_9}


    choice = ''

    while choice != 'quit':

        choice = input ("\n\nEnter your choice, help to see available options, quit to exit: ")

        if choice == 'help':
            print ('\n\n')
            prompt = "\tEnter 0 for a list of all your friends.\n"
            prompt = prompt + "\tEnter 1 to search by first and last name.\n"
            prompt = prompt + "\tEnter 2 to search by first name only.\n"
            prompt = prompt + "\tEnter 3 to search by last name only.\n"
            prompt = prompt + "\tEnter 4 to search using a few letters of the name.\n"
            prompt = prompt + "\tEnter 5 to search by month of birthday.\n"
            prompt = prompt + "\tEnter 6 to display inspriational messages.\n"
            prompt = prompt + "\tEnter 7 to email an stock message.\n"
            prompt = prompt + "\tEnter 8 to email a personal message.\n"
            prompt = prompt + "\tEnter 9 to email a combined message.\n"
            prompt = prompt + "\tEnter quit to exit the program.\n"
            print (prompt)
            print ('\n\n')


        elif choice == "0":
            choice_dict ['0']()

        elif choice == "1":
            choice_dict ['1']()

        elif choice == "2":
            choice_dict ['2']()

        elif choice == "3":
            choice_dict ['3']()

        elif choice == "4":
            choice_dict ['4']()

        elif choice == "5":
            choice_dict ['5']()

        elif choice == "6":
            choice_dict ['6']()

        elif choice == "7":
            choice_dict ['7']()

        elif choice == "8":
            choice_dict ['8']()

        elif choice == "9":
            choice_dict ['9']()

        elif choice == "quit":
            print ("You have exited the program.\n\n")
            exit ()

        else:
            print ("invalid entry. Try again.")
