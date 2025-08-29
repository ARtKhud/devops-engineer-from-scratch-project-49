from random import randint

import prompt

user_name = ''


def welcome_user():
    global user_name
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')


def print_user_answer():
    answer = prompt.string('Your answer: ')
    return answer


def print_random_number():
    number = randint(1, 100)
    print(f"Question: {number}")
    return number


def is_user_correct(number, answer):
    if number % 2 == 0 and answer == 'yes':
        print('Correct!', end='\n')
        return True
    elif number % 2 == 1 and answer == 'no':
        print('Correct!', end='\n')
        return True
    elif number % 2 == 0 and answer == 'no':
        print("'no' is wrong answer ;(. Correct answer was 'yes'.", end='\n')
        return False
    elif number % 2 == 1 and answer == 'yes':
        print("'yes' is wrong answer ;(. Correct answer was 'no'.", end='\n')
        return False
    else:
        print("The answer must be 'yes' or 'no'")
        return False


def print_end_resilt(attempts):
    if attempts == 3:
        print(f'Congratulations {user_name}')
    else:
        print(f"Let's try again, {user_name}")


def start_game():
    welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".', end='\n')

    attempts = 1
    number = print_random_number()
    answer = print_user_answer()
    is_correct = is_user_correct(number, answer)
    while attempts < 3 and is_correct:
        number = print_random_number()
        answer = print_user_answer()
        is_correct = is_user_correct(number, answer)
        attempts += 1
    
    print_end_resilt(attempts)


def main():
    start_game()
