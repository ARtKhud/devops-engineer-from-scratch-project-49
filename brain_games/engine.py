import prompt


def start(game):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")

    print(game.get_condition_string(), end="\n")

    for _ in range(3):
        condition_data = game.get_condition_data()
        print(f"Question: {condition_data}")
        correct_ans = game.get_correct_answer(condition_data)
        answer = prompt.string("Your answer: ")
        is_correct = game.is_user_correct(correct_ans, answer)
        if not is_correct:
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f"Congratulations, {user_name}!")
