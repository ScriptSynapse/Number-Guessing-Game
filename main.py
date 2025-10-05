import random

def number_guessing_game_with_limit():
    print("Welcome to the Number Guessing Game! 🔢")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)

    max_guesses = 10
    guess_count = 0

    while guess_count < max_guesses:
        remaining_guesses = max_guesses - guess_count
        print(f"You have {remaining_guesses} guesses left.")

        try:
            guess = int(input("What's your guess? "))
            guess_count += 1

            if guess < secret_number:
                print("Too low! Try again. 👇")
            elif guess > secret_number:
                print("Too high! Try again. 👆")
            else:
                print(f"🎉 You got it in {guess_count} guesses! The number was {secret_number}. 🎉")
                return  # Exit the function and end the game

        except ValueError:
            print("Oops! That's not a valid number. Please enter an integer.")

    # NEW: This code runs only if the while loop finishes (i.e., user runs out of guesses)
    print(f"😢 Sorry, you ran out of guesses. The secret number was {secret_number}.")


number_guessing_game_with_limit()
