import random


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'

random_number = random.randint(1, 100)

def is_even(random_number):
    return random_number % 2 == 0

def get_game():
    right_answer = is_even()
    question = f'{random_number}'
    if is_even():
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return question, right_answer
