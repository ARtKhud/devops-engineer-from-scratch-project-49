from random import randint

TEXT = "Find the greatest common divisor of given numbers."

def print_question():
    number_one = randint(1, 100)
    number_two = randint(1, 100)
    print(f"Question: {number_one} {number_two}")
    return calc_nod(number_one, number_two)


def calc_nod(num_one, num_two):
    a = num_one
    b = num_two
    temp = a
    while b != 0:
        a = b
        b = temp % b
        temp = a
    return a

def is_user_correct(num, answer):
    to_int = int(answer)
    if to_int == num:
        print("Correct!", end="\n")
        return True
    else:
        print(
            f"'{to_int}' is wrong answer ;(. Correct answer was '{num}'.",
               end="\n")
        return False