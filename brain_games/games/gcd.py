import secrets


def get_condition_string():
    return "Find the greatest common divisor of given numbers."


def get_condition_data():
    number_one = secrets.randbelow(100) + 1
    number_two = secrets.randbelow(100) + 1
    return f"Question: {number_one} {number_two}"


def get_correct_answer(data: str):
    data_list = data.split(" ")
    a = int(data_list[1])
    b = int(data_list[2])
    temp = a
    while b != 0:
        a = b
        b = temp % b
        temp = a
    return a


def is_user_correct(correct, answer):
    to_int = int(answer)
    if to_int == correct:
        print("Correct!", end="\n")
        return True
    else:
        print(f"'{to_int}' is wrong answer ;(. Correct answer was '{correct}'.",
               end="\n")
        return False
