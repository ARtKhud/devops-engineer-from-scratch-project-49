from random import randint

TEXT = "What number is missing in the progression?"


def print_question():
    generated_progression = generate_progression()
    progression_with_ommited_number = ommit_random_number(generated_progression)
    print(f"Question: {' '.join(
        [str(item) for item in progression_with_ommited_number['result']]
        )}")
    return progression_with_ommited_number['ommited_item']


def generate_progression():
    steps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    step_index = randint(1, 10)
    prog_len = randint(5, 10)
    start = randint(1, 999)
    result = []
    for i in range(prog_len):
        currentElement = start + i * steps[step_index]
        result.append(currentElement)
    return result
    

def ommit_random_number(progression):
    ommited_index = randint(0, len(progression) - 1)
    result = []
    ommited_item = 0
    for i, item in enumerate(progression):
        if i == ommited_index:
            ommited_item = item
            result.append('..')
            continue
        result.append(item)
    return {
        "result": result,
        "ommited_item": ommited_item
        }


def is_user_correct(num, answer):
    to_int = int(answer)
    if to_int == num:
        print("Correct!", end="\n")
        return True
    else:
        print(
            f"'{to_int}' is wrong answer ;(. Correct answer was '{num}'.",
               end="\n")
        return False
