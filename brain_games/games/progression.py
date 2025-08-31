from secrets import randbelow


def get_condition_string():
    return "What number is missing in the progression?"


def get_condition_data():
    generated_progression = generate_progression()
    progression_with_omitted_number = omit_random_number(generated_progression)
    return progression_with_omitted_number


def get_correct_answer(progression_str: str):
    progression_list = [
        item if item == ".." else int(item) for 
        item in progression_str.split(" ")
    ]
    omitted_i = progression_list.index("..")
    ommited_value = 0
    if omitted_i != 0:
        ommited_value = (
            progression_list[omitted_i + 1] - progression_list[omitted_i - 1]
        ) / 2 + progression_list[omitted_i - 1]
    else:
        ommited_value = progression_list[omitted_i + 1] - (
            progression_list[omitted_i + 2] - progression_list[omitted_i + 1]
        )
    return int(ommited_value)


def generate_progression():
    steps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    step_index = randbelow(len(steps) - 1)
    prog_len = randbelow(10) + 5
    start = randbelow(999) + 1
    result = []
    for i in range(prog_len):
        currentElement = start + i * steps[step_index]
        result.append(currentElement)
    return result


def omit_random_number(progression):
    index = randbelow(len(progression) - 1)
    result = [*progression]
    result[index] = ".."
    return " ".join(str(item) for item in result)


def is_user_correct(correct, answer):
    int_ans = int(answer)
    if correct == int_ans:
        print("Correct!", end="\n")
        return True
    else:
        print(
            f"'{int_ans}' is wrong answer ;(. Correct answer was '{correct}'.",
              end="\n"
        )
        return False
