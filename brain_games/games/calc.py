from random import randint


def get_condition_string():
    return "What is the result of the expression?"


def get_condition_data():
    OPERATORS = ["+", "-", "*"]
    number_one = randint(1, 30)
    number_two = randint(1, 30)
    random_operator = randint(0, 2)
    return f"Question: {number_one} {OPERATORS[random_operator]} {number_two}"


def get_correct_answer(data: str):
    data_list = data.split(" ")
    num_one = int(data_list[1])
    operator = data_list[2]
    num_two = int(data_list[3])
    if operator == "+":
        return num_one + num_two
    elif operator == "-":
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
