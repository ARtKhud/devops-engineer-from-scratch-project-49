import prompt


def is_user_correct(result, user_ans):
    if user_ans == result:
        print("Correct!", end="\n")
        return True
    else:
        print(
            f"'{user_ans}' is wrong answer ;(. Correct answer was '{result}'.",
              end="\n"
        )
        return False


def start(game):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")

    print(game.get_condition_string(), end="\n")
    GAME_LAPS = 3
    for _ in range(GAME_LAPS):
        (condition, result) = game.get_condition_with_result()
        print(f"Question: {condition}")
        user_answer = prompt.string("Your answer: ")
        is_correct = is_user_correct(result, user_answer)
        if not is_correct:
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f"Congratulations, {user_name}!")
