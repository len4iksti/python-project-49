import prompt

from random import randint


number_1 = randint(1, 100)
number_2 = randint(1, 100)

print('Find the greatest common divisor of given numbers.')
print(f"Question: {number_1} {number_2}")
user_answer = prompt.iteger('Your answer: ')


def make_list_1(number_1):
    counter = 1
    list_1 = []
    while counter <= number_1:
        if number_1 % counter == 0:
            list_1.append(counter)
        counter += 1
    return list_1


def make_list_2(number_2):
    counter = 1
    list_2 = []
    while counter <= number_2:
        if number_2 % counter == 0:
            list_2.append(counter)
        counter += 1
    return list_2


def gcd(number_1, number_2):
    common = set(make_list_1(number_1)) & set(make_list_2(number_2))
    max_number = max(common)
    if user_answer == max_number:
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{max_number}'.")
