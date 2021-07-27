from datetime import date


def todays_date():
    """Returns today's date in string format."""

    today = date.today()

    today = today.strftime("%B %d, %Y")  # Textual month, day and year

    return today
