from secrets import randbelow

TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def print_question():
    question_number = randbelow(999) + 1
    print(f"Question: {question_number}")
    return is_number_prime(question_number)


def is_number_prime(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
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