from secrets import randbelow


def get_condition_string():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_condition_data():
    question_number = randbelow(999) + 1
    return question_number


def get_correct_answer(data):
    if data < 2:
        return False
    if data in (2, 3):
        return True
    if data % 2 == 0 or data % 3 == 0:
        return False
    i = 5
    while i * i <= data:
        if data % i == 0 or data % (i + 2) == 0:
            return False
        i += 6
    return True


def is_user_correct(is_prime, answer):
    if is_prime and answer == "yes":
        print("Correct!", end="\n")
        return True
    elif not is_prime and answer == "no":
        print("Correct!", end="\n")
        return True
    elif is_prime and answer == "no":
        print("'no' is wrong answer ;(. Correct answer was 'yes'.", end="\n")
        return False
    elif not is_prime and answer == "yes":
        print("'yes' is wrong answer ;(. Correct answer was 'no'.", end="\n")
        return False
    else:
        print("The answer must be 'yes' or 'no'")
        return False
