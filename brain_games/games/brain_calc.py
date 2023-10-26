import prompt

from random import randint, choice


number_1 = randint(1, 100)
number_2 = randint(1, 100)
operator = choice(['+', '-', '*'])


def calculate_expression(number_1, operator, number_2):
    if operator == '+':
        return number_1 + number_2
    elif operator == '-':
        return number_1 - number_2
    else:
        return number_1 * number_2


print('What is the result of the expression?')


print(f"Question: {number_1} {operator} {number_2}")


right_answer = calculate_expression(number_1, operator, number_2)
user_answer = prompt.integer('Your answer: ')

if user_answer == right_answer:
    print('Correct!')
else:
    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
