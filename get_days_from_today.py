from datetime import datetime


def get_days_from_today(date: str) -> int:
    """

    :param date: a string representing a date in 'YYYY-MM-DD' format
    :return:an integer that indicates the number of days from the given date to the current date

    Exception:
    ValueError: If the input date is in an incorrect format.
    """
    try:
        given_date = datetime.strptime(date, '%Y-%m-%d')
        today = datetime.today()
        delta = given_date - today
        return delta.days

    except ValueError:
        raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")


print(get_days_from_today('2021-10-09'))
