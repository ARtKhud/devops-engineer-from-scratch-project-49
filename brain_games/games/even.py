from random import randint

CONDITION_STR = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_condition_with_result():
    question_number = randint(1, 100)
    condition = f"{question_number}"
    is_even = 'yes' if question_number % 2 == 0 else 'no'
    return (condition, is_even)
