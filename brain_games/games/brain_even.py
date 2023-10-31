import random


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(random_number):
    return random_number % 2 == 0


def get_game():
    random_number = random.randint(1, 100)
    question = f'{random_number}'
    if is_even(random_number):
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return question, right_answer
