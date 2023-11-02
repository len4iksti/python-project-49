import prompt


NUMBER_OF_ROUNDS = 3


def launch_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.GAME_RULE)

    for _ in range(NUMBER_OF_ROUNDS):
        question, right_answer = game.get_game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        error_message = ' is wrong answer ;(. Correct answer was '

        if user_answer == str(right_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}{error_message}{right_answer}'.")
            print(f"Let's try again, {name}!")
            return
    return print(f'Congratulations, {name}!')
