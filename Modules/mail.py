import requests  # For sending emails.


def email_stock_message(indices, friends, stock_message):
    """Sends an email to a friend with an stock message chosen by the user from text file, messages.txt."""

    if len(indices) == 0:
        print("Nothing will be sent.")

    else:
        for index in indices:
            first_name = friends[index][0]
            email = friends[index][2]

        print('Email was sent.')

        return requests.post(
            "https://api.mailgun.net/v3/kevinnourian.com/messages",
            auth=("api", "4b7b75a9a7f02aac454b73da2159dc9c-468bde97-d0866e74"),
            data={"from": "Kevin Nourian <kevin@kevinnourian.com>",
                  "to": [email],
                  "subject": "Happy Birthday!!!",
                  "text": "Dear " + first_name + "," + "\n\n" + stock_message[4:]})


def email_personal_message(indices, friends, personal_message):
    """Sends an email to a friend with a persoanl message entered by the user."""

    if len(indices) == 0:
        print("Nothing will be sent.")

    else:
        for index in indices:
            first_name = friends[index][0]
            email = friends[index][2]

        print('\nEmail was sent.')

        return requests.post(
            "https://api.mailgun.net/v3/kevinnourian.com/messages",
            auth=("api", "4b7b75a9a7f02aac454b73da2159dc9c-468bde97-d0866e74"),
            data={"from": "Kevin Nourian <kevin@kevinnourian.com>",
                  "to": [email],
                  "subject": "Happy Birthday!!!",
                  "text": "Dear " + first_name + "," + "\n\n" + personal_message[0]})


def email_combined_message(indices, friends, stock_message, personal_message):

    if len(indices) == 0:
        print("Nothing will be sent.")

    else:
        for index in indices:
            first_name = friends[index][0]
            email = friends[index][2]

        print('\nEmail was sent.')

        return requests.post(
            "https://api.mailgun.net/v3/kevinnourian.com/messages",
            auth=("api", "4b7b75a9a7f02aac454b73da2159dc9c-468bde97-d0866e74"),
            data={"from": "Kevin Nourian <kevin@kevinnourian.com>",
                  "to": [email],
                  "subject": "Happy Birthday!!!",
                  "text": "Dear " + first_name + "," + "\n\n" + stock_message[4:] + "\n" + personal_message[0]})
