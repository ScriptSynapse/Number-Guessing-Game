# Number Guessing Game 🔢

A classic command-line number guessing game built with Python. This project is a great starting point for beginners to learn fundamental programming concepts.

-----

## 📜 Description

This is a simple interactive game where the computer thinks of a random integer within a specified range (e.g., 1 to 100), and the player's objective is to guess that number. The program provides feedback after each guess, telling the player if their guess was "Too high\!" or "Too low\!". The game ends when the player correctly guesses the number or runs out of attempts.

-----

## ✨ Features

  * **Random Number Generation**: A secret number is randomly generated at the start of each game.
  * **User Input**: Prompts the user to enter their guess.
  * **Feedback System**: Informs the user if their guess is too high or too low.
  * **Guess Limiter**: The player has a limited number of attempts to guess the number, adding a layer of challenge.
  * **Input Validation**: Gracefully handles non-numeric input to prevent crashes.
  * **Win/Loss Conditions**: Displays a success message upon a correct guess or a "game over" message if the player runs out of attempts.

-----

## 🚀 How to Play

To run this game on your local machine, you'll need to have [Python](https://www.python.org/downloads/) installed.

1.  **Clone the repository** (or just download the `guessing_game.py` file):

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    ```

2.  **Navigate to the project directory**:

    ```bash
    cd your-repository-name
    ```

3.  **Run the Python script** from your terminal:

    ```bash
    python guessing_game.py
    ```

4.  Follow the on-screen instructions to play the game\!

-----

## 🛠️ Code Overview

The game logic is contained within a single Python script, `guessing_game.py`.

  * **`import random`**: This module is used to generate the secret number.
  * **`while` loop**: The core of the game is a `while` loop that continues as long as the player has guesses remaining.
  * **`input()` function**: This function captures the player's guess from the terminal.
  * **`if-elif-else` statements**: These are used to compare the player's guess to the secret number and provide the appropriate feedback.
  * **`try-except` block**: This is used for error handling, specifically to catch `ValueError` if the user enters text that cannot be converted to an integer.

-----

## 🔮 Future Enhancements

This project can be expanded with more features. Here are a few ideas:

  * **Difficulty Levels**: Implement 'Easy', 'Medium', and 'Hard' modes that adjust the number range and the number of allowed guesses.
  * **High Score**: Add a feature to save and display the best score (fewest guesses).
  * **Play Again**: Ask the user if they want to play another round after a game ends.
  * **GUI Implementation**: Rebuild the game with a graphical user interface using a library like `Tkinter` or `PyQt`.