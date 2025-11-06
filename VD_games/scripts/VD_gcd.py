import math
import random

from VD_games.VD_games.cli import run_game, welcome_user


def generate_gcd_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))

    return question, correct_answer


def main():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    run_game(name, generate_gcd_question, "GCD")


if __name__ == '__main__':
    main()
