from secrets import randbelow

CONDITION_STR = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return True
    if num in (2, 3):
        return False
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def get_condition_with_result():
    condition = randbelow(999) + 1
    return (condition, 'yes' if is_prime(condition) else 'no')
    
