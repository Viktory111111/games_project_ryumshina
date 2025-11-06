import random

from VD_games.VD_games.cli import run_game, welcome_user


def generate_calc_question():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(['+', '-', '*'])

    match operator:
        case '+':
            correct_answer = str(num1 + num2)
        case '-':
            correct_answer = str(num1 - num2)
        case '*':
            correct_answer = str(num1 * num2)

    question = f"{num1} {operator} {num2}"
    return question, correct_answer


def main():
    name = welcome_user()
    print("What is the result of the expression?")
    run_game(name, generate_calc_question, "Calc")


if __name__ == '__main__':
    main()
