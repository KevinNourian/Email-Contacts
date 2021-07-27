def display_search_results (indices, friends):
    """Displays the result of the search on the monitor."""

    if len (indices) == 0:
            print ("\nSearch does not exist.")

    else:
        for  index in indices:
            print ("\n" + friends [index][0], end = ' ')
            print (friends [index][1])
            print ("\t" + "Email: " , friends [index][2])
            print ("\t" + "Telephone: " , friends [index][3])
            print ("\t" + "Day: " , friends [index][4])
            print ("\t" + "Month: " , friends [index][5] + "\n")


def find_all_friends (friends):
    """Returns a list of index or indices of all the friends in the csv table. Returns a label to identify what is being saved in text file, searches.txt."""

    a = 0
    indices = []
    label = " \nAll friends search results:"

    for index in range (0, len(friends)):
            indices.append (index)

    return indices, label


def display_messages(messages):
    """Displays all the inspriational messages from text file, 'messages.txt' on the monitor."""

    s = "\n"
    s = s.join(messages)
    print (s)
