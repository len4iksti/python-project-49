import prompt

from random import randint


random_number = randint(1, 100)


def is_even(random_number):
    return random_number % 2 == 0


print('Answer "yes" if the number is even, otherwise answer "no".')
print(f"Question: {random_number}")

user_answer = prompt.string('Your answer: ')
right_answer = is_even(random_number)
answer_1 = 'yes'
answer_2 = 'no'


if user_answer == 'yes' and right_answer is True:
    print('Correct!')
elif user_answer == 'no' and right_answer is False:
    print('Correct!')
else:
    if user_answer == 'yes':
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was 'no'.")
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was 'yes'.")
