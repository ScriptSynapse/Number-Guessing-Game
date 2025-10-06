import tkinter as tk
import random

# You can adjust these settings
NUMBER_RANGE_MIN = 1
NUMBER_RANGE_MAX = 100
MAX_GUESSES = 10


class GuessingGameGUI:
    """
    A GUI for the Number Guessing Game using Tkinter.
    """

    def __init__(self, master):
        """
        Initializes the GUI window and its widgets.
        'master' is the main window object (tk.Tk()).
        """
        # 1. Set up the main window
        self.master = master
        master.title("Number Guessing Game 🔢")
        master.geometry("350x200")  # Set window size

        # Initialize game state variables
        self.secret_number = 0
        self.guess_count = 0

        # 2. Create and arrange the widgets
        # A Label for instructions and feedback
        self.feedback_text = tk.StringVar()
        self.feedback_label = tk.Label(master, textvariable=self.feedback_text, font=("Helvetica", 12), wraplength=300)
        self.feedback_label.pack(pady=10)  # pady adds some vertical space

        # An Entry widget for user input
        self.entry = tk.Entry(master, font=("Helvetica", 14), width=10)
        self.entry.pack(pady=5)

        # A Button to submit the guess
        self.guess_button = tk.Button(master, text="Submit Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        # A Button to start a new game
        self.new_game_button = tk.Button(master, text="New Game", command=self.start_new_game)
        self.new_game_button.pack(pady=5)

        # 3. Start the first game automatically
        self.start_new_game()

    def start_new_game(self):
        """Resets the game state for a new round."""
        self.secret_number = random.randint(NUMBER_RANGE_MIN, NUMBER_RANGE_MAX)
        self.guess_count = 0

        # Update UI for the new game
        self.feedback_text.set(
            f"I'm thinking of a number between {NUMBER_RANGE_MIN} and {NUMBER_RANGE_MAX}.\nYou have {MAX_GUESSES} guesses.")
        self.entry.delete(0, 'end')  # Clear the entry box
        self.guess_button.config(state='normal')  # Re-enable the guess button
        self.entry.focus_set()  # Place the cursor in the entry box

    def check_guess(self):
        """Handles the logic of checking the user's guess."""
        try:
            # Get the guess from the entry box
            guess = int(self.entry.get())
            self.guess_count += 1
            remaining_guesses = MAX_GUESSES - self.guess_count

            # The core game logic
            if guess < self.secret_number:
                feedback = f"Too low! 👇 You have {remaining_guesses} guesses left."
            elif guess > self.secret_number:
                feedback = f"Too high! 👆 You have {remaining_guesses} guesses left."
            else:
                feedback = f"🎉 You got it in {self.guess_count} guesses! The number was {self.secret_number}."
                self.guess_button.config(state='disabled')  # Disable button on win

            # Check for game over (out of guesses)
            if self.guess_count >= MAX_GUESSES and guess != self.secret_number:
                feedback = f"😢 Out of guesses. The number was {self.secret_number}."
                self.guess_button.config(state='disabled')  # Disable button on loss

            self.feedback_text.set(feedback)
            self.entry.delete(0, 'end')  # Clear the entry box for the next guess

        except ValueError:
            # Handle cases where input is not a number
            self.feedback_text.set("That's not a number! Please enter an integer.")


# --- Main script execution ---
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window instance
    game_gui = GuessingGameGUI(root)  # Create our game object
    root.mainloop()  # Start the Tkinter event loop