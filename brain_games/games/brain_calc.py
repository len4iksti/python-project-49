import random


GAME_RULE = 'What is the result of the expression?'


def calculate_expression(number_1: int, random_operator: str, number_2: int):
    if random_operator == '+':
        return number_1 + number_2

    if random_operator == '-':
        return number_1 - number_2

    return number_1 * number_2


def get_game():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    operator = ['+', '-', '*']
    random_operator = random.choice(operator)
    right_answer = calculate_expression()
    question = f'{number_1} {random_operator} {number_2}'
    return question, right_answer
