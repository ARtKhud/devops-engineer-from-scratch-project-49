from random import randint

CONDITION_STR = "What is the result of the expression?"


def get_condition_with_result():
    OPERATORS = ["+", "-", "*"]
    number_one = randint(1, 30)
    number_two = randint(1, 30)
    random_index = randint(0, 2)
    condition = f"{number_one} {OPERATORS[random_index]} {number_two}"
    result = None
    if OPERATORS[random_index] == "+":
        result = number_one + number_two
    elif OPERATORS[random_index] == "-":
        result = number_one - number_two
    else:
        result = number_one * number_two
    return (condition, str(result))
