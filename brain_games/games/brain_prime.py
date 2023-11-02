import random

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(random_number):
    d = 2
    while random_number % d != 0:
        d += 1
    return d == random_number


def get_game():
    random_number = random.randint(1, 100)
    question = f'{random_number}'
    if is_prime(random_number):
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return question, right_answer
