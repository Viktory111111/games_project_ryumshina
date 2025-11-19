import random

GAME_RULES = "What is the result of the expression?"


def generate_round():
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
