import prompt


def start_game(condition_string, predicateFn, questionFn):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")

    print(condition_string, end="\n")

    attempts = 1
    number = questionFn()
    answer = prompt.string("Your answer: ")

    is_correct = predicateFn(number, answer)
    while attempts < 3 and is_correct:
        number = questionFn()
        answer = prompt.string("Your answer: ")
        is_correct = predicateFn(number, answer)
        if not is_correct:
            break
        attempts += 1

    if attempts == 3:
        print(f"Congratulations, {user_name}!")
    else:
        print(f"Let's try again, {user_name}!")