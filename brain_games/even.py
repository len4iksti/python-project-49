from random import randint


random_number = randint(1, 100)

import prompt


def is_even(random_number):
    return random_number %2 == 0

print('Answer "yes" if the number is even, otherwise answer "no".')
print(f"Question: {random_number}")

answer = prompt.string('Your answer: ')
