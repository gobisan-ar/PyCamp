from random import randint

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


# compare answer and user guess
def check_guess(guess, answer, attempts):
    """
    Checks answer against guess.
    Returns the number of turns remaining.
    """
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}.")


# set difficulty
def set_difficulty():
    difficulty = input("Choose a difficulty, Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    # choose a random number
    answer = randint(1, 100)
    attempts = set_difficulty()

    # repeat guessing
    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts to guess the number.")

        # guess a number
        guess = int(input("Make a guess: "))
        attempts = check_guess(guess, answer, attempts)

        if attempts == 0:
            print("You've run out of guess, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
