from secrets import randbelow

CONDITION_STR = "What number is missing in the progression?"


def get_condition_with_result():
    generated_progression = generate_progression()
    index = randbelow(len(generated_progression) - 1)
    result = [*generated_progression]
    result[index] = ".."
    return (" ".join(str(item) for item in result),
             str(generated_progression[index]))


def generate_progression():
    STEPS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    step_index = randbelow(len(STEPS) - 1)
    prog_len = randbelow(6) + 5
    start = randbelow(999) + 1
    end = start + prog_len * STEPS[step_index]
    result = list(range(start, end, STEPS[step_index]))
    return result