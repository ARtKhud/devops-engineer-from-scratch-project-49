from brain_games.engine import start_game
from brain_games.games.gcd import TEXT, is_user_correct, print_question


def main():
    start_game(TEXT, is_user_correct, print_question)