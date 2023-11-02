import random

GAME_RULE = 'What number is missing in the progression?'


def is_progression():
    first_number = random.randint(1, 20)
    progression = [first_number]
    progression_length = random.randint(4, 9)
    step = random.randint(2, 10)

    while len(progression) <= progression_length:
        next_number = progression[-1] + step
        progression.append(next_number)

    return progression


def get_game():
    progression = is_progression()
    answer = random.choice(progression)

    index = progression.index(answer)
    progression[index] = '..'

    question = ' '.join(map(str, progression))
    right_answer = str(answer)

    return question, right_answer
