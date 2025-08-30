from random import randint

OPERATORS = ['+', '-', '*']
QUESTION = 'What is the result of the expression?'


def print_question():
    number_one = randint(1, 30)
    number_two = randint(1, 30)
    random_operator = randint(0, 2)
    print(f"Question: {number_one} {OPERATORS[random_operator]} {number_two}")
    return calculate_expression(OPERATORS[random_operator],
                                 number_one, number_two)


def calculate_expression(operator, num_one, num_two):
    if operator == '+':
        return num_one + num_two
    elif operator == '-':
        return num_one - num_two
    else:
        return num_one * num_two
    

def is_user_correct(num, ans):
    to_int = int(ans)
    if num == to_int:
        print("Correct!", end="\n")
        return True
    else:
        print(
            f"'{to_int}' is wrong answer ;(. Correct answer was '{num}'.",
               end="\n")
        return False
