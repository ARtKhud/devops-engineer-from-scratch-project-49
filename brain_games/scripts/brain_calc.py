from brain_games.engine import start_game
from brain_games.games.calc import QUESTION, is_user_correct, print_question


def main():
    start_game(QUESTION, is_user_correct, print_question)
