from random import randint


def print_question():
    question_number = randint(1, 100)
    print(f"Question: {question_number}")
    return question_number


def is_user_correct(number, answer):
    if number % 2 == 0 and answer == "yes":
        print("Correct!", end="\n")
        return True
    elif number % 2 == 1 and answer == "no":
        print("Correct!", end="\n")
        return True
    elif number % 2 == 0 and answer == "no":
        print("'no' is wrong answer ;(. Correct answer was 'yes'.", end="\n")
        return False
    elif number % 2 == 1 and answer == "yes":
        print("'yes' is wrong answer ;(. Correct answer was 'no'.", end="\n")
        return False
    else:
        print("The answer must be 'yes' or 'no'")
        return False
