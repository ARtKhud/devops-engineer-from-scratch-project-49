import secrets

CONDITION_STR = "Find the greatest common divisor of given numbers."


def get_condition_with_result():
    number_one = secrets.randbelow(100) + 1
    number_two = secrets.randbelow(100) + 1
    condition = f"{number_one} {number_two}"
    temp = number_one
    while number_two != 0:
        number_one = number_two
        number_two = temp % number_two
        temp = number_one
    return (condition, str(number_one))
