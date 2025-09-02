from secrets import randbelow


def get_condition_string():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_condition_with_result():
    condition = randbelow(999) + 1
    if condition < 2:
        return (condition, 'no')
    if condition in (2, 3):
        return (condition, 'yes')
    if condition % 2 == 0 or condition % 3 == 0:
        return (condition, 'no')
    i = 5
    while i * i <= condition:
        if condition % i == 0 or condition % (i + 2) == 0:
            return (condition, 'no')
        i += 6
    return (condition, 'yes')
