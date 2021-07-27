from difflib import get_close_matches


def first_name_search (friends):
    '''Returns a list of index or indices corresponding to the location of the friend(s) matching the first name in the csv table. Returns a label to identify what is being saved in text file, searches.txt.'''

    first_name = input ("\nInput the first name: ")
    first_name = first_name.capitalize()

    a = 0
    indices = []
    label = " \nFirst name search results:"

    for index in range (0, len(friends)):
        if first_name == friends [index][int(a)]:
            indices.append (index)

    return indices, label


def last_name_search(friends):
    '''Returns a list of index or indices corresponding to the location of the friend(s) matching the last name in the csv table. Returns a label to identify what is being saved in text file, searches.txt.'''

    last_name = input ("Input the last name: ")
    last_name = last_name.capitalize()

    a = 1
    indices = []
    label = " \nLast name search results:"

    for index in range (0, len(friends)):
        if last_name == friends [index][int(a)]:
            indices.append (index)

    return indices, label


def close_matches(friends):
    '''Returns a list of index or indices corresponding to the location of the friend(s) closely matching the letters of the first name and last name in the csv table. Returns a label to identify what is being saved in text file, searches.txt.'''

    first_name = input ("\nInput at least three letters of the first name: ")
    first_name = first_name.capitalize()
    first_names = [index[int(0)] for index in friends] # List of the first names, in column 0 of the csv file.

    last_name = input ("Input at least three letters of the last name: ")
    last_name = last_name.capitalize()
    last_names = [index[int(1)] for index in friends] # List of the last names, in column 1 of the csv file.

    a = 0
    b = 1
    indices = []
    name = ''
    label = " \nClose match search results:"

    for name in get_close_matches(first_name, first_names):
        first_name = name

    for name in get_close_matches(last_name, last_names):
        last_name = name

    for index in range (0, len(friends)):
        if first_name == friends [index][int(a)] and last_name == friends [index][int(b)]:
            indices.append (index)

    return indices, label


def full_name_search (friends):
    '''Returns a list of index or indices corresponding to the location of the friend(s) matching the first name and last name in the csv table. Returns a label to identify what is being saved in text file, searches.txt.'''

    first_name = input ("\nInput the first name: ")
    first_name = first_name.capitalize()

    last_name = input ("Input the last name: ")
    last_name = last_name.capitalize()

    a = 0
    b = 1
    indices = []
    name = ''
    label = " \nFull name search results:"

    for index in range (0, len(friends)):
        if first_name == friends [index][int(a)] and last_name == friends [index][int(b)]:
            indices.append (index)

    return indices, label


def month_search(friends):
    '''Returns a list of index or indices corresponding to the location of the friend(s) mathcing the month in the csv table. Returns a label to identify what is being saved in text file, searches.txt.'''

    month = input ("Input month: ")
    month = month.capitalize()

    a = 5
    indices = []
    label = " \nBirthday month search results:"

    col = [index[int(a)] for index in friends]
    if month in col:
        for index in range (0, len(friends)):
            if month == friends [index][int(a)]:
                indices.append (index)

    return indices, label
