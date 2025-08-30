import prompt

user_name = ""


def welcome_user():
    global user_name
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")


def print_user_answer():
    answer = prompt.string("Your answer: ")
    return answer


def print_end_result(attempts):
    if attempts == 3:
        print(f"Congratulations, {user_name}")
    else:
        print(f"Let's try again, {user_name}")


def start_game(condition_string, predicateFn, questionFn):
    welcome_user()

    print(condition_string, end="\n")

    attempts = 1
    number = questionFn()
    answer = print_user_answer()
    is_correct = predicateFn(number, answer)
    while attempts < 3 and is_correct:
        number = questionFn()
        answer = print_user_answer()
        is_correct = predicateFn(number, answer)
        if not is_correct:
            break
        attempts += 1

    print_end_result(attempts)