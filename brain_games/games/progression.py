from secrets import randbelow


def get_condition_string():
    return "What number is missing in the progression?"


def get_condition_with_result():
    generated_progression = generate_progression()
    index = randbelow(len(generated_progression) - 1)
    result = [*generated_progression]
    result[index] = ".."
    return (" ".join(str(item) for item in result),
             str(generated_progression[index]))


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