import prompt


def start(game):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")

    print(game.CONDITION_STR, end="\n")
    GAME_LAPS = 3
    for _ in range(GAME_LAPS):
        (condition, result) = game.get_condition_with_result()
        print(f"Question: {condition}")
        user_ans = prompt.string("Your answer: ")
        if user_ans == result:
            print("Correct!", end="\n")
        else:
            print(
            f"'{user_ans}' is wrong answer ;(. Correct answer was '{result}'.",
              end="\n"
            )
            print(f"Let's try again, {user_name}!")
            break
            
    else:
        print(f"Congratulations, {user_name}!")
