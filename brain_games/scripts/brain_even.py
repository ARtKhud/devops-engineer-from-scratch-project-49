from brain_games.engine import start_game
from brain_games.games.even import is_user_correct, print_question 


def main():
    start_game('Answer "yes" if the number is even, otherwise answer "no".',
                is_user_correct, print_question)
