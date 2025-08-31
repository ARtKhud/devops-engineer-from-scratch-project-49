import prompt


def start_game(module):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")

    print(module.get_condition_string(), end="\n")
    condition_data = module.get_condition_data()
    correct_ans = module.get_correct_answer(condition_data)
    print(f"Question: {condition_data}")
    answer = prompt.string("Your answer: ")

    is_correct = module.is_user_correct(correct_ans, answer)
    for _ in range(2):
        if not is_correct:
            print(f"Let's try again, {user_name}!")
            break
        condition_data = module.get_condition_data()
        correct_ans = module.get_correct_answer(condition_data)
        print(f"Question: {condition_data}")
        answer = prompt.string("Your answer: ")
        is_correct = module.is_user_correct(correct_ans, answer)
    else:
        print(f"Congratulations, {user_name}!")
