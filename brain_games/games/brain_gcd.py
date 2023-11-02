import random

from math import gcd

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_game():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f'{number_1} {number_2}'
    right_answer = gcd(number_1, number_2)
    return question, right_answer
