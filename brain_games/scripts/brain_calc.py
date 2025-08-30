from brain_games.engine import start_game
from brain_games.games.calc import is_user_correct, print_question


def main():
    start_game('What is the result of the expression?', 
               is_user_correct, print_question)
