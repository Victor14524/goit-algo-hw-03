from random import randint


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """

    :param min: the minimum possible number in the set (at least 1)
    :param max: the maximum possible number in the set (no more than 1000)
    :param quantity: the number of numbers to choose
    :return: a list of unique random numbers for lotteries
    """
    set_of_lottery = set()
    if min <= 1 and max <= 1000 and min < max and min < quantity < max:
        while len(set_of_lottery) < quantity:
            set_of_lottery.add(randint(min, max))
    return sorted(set_of_lottery)


print(get_numbers_ticket(1, 49, 6))
