from secrets import randbelow


CONDITION_STRING = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return 'no'
    if num in (2, 3):
        return 'yes'
    if num % 2 == 0 or num % 3 == 0:
        return 'no'
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return 'no'
        i += 6
    return 'yes'

def get_condition_with_result():
    condition = randbelow(999) + 1
    return (condition, is_prime(condition))
    
