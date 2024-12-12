import tkinter as tk
from tkinter import messagebox
import random

# Global variables
target_number = random.randint(1, 100)
attempts_left = 10

def check_guess():
    """Process the user's guess."""
    global target_number, attempts_left

    try:
        guess = int(entry_guess.get())
        entry_guess.delete(0, tk.END)  # Clear the input field after submitting

        if guess < 1 or guess > 100:
            label_feedback.config(text="Guess out of range! Try again.", fg="red")
            return

        if guess == target_number:
            messagebox.showinfo("Congratulations!", f"You guessed the number {target_number} correctly!")
            reset_game()
        elif guess < target_number:
            label_feedback.config(text="Too low! Try again.", fg="Black")
        else:
            label_feedback.config(text="Too high! Try again.", fg="Black")

        attempts_left -= 1
        label_attempts.config(text=f"Attempts Left: {attempts_left}")

        if attempts_left == 0:
            messagebox.showinfo("Game Over", f"You're out of attempts! The number was {target_number}.")
            reset_game()

    except ValueError:
        label_feedback.config(text="Invalid input! Enter a number.", fg="red")

def clear_feedback(event=None):
    """Clear feedback message when typing a new guess."""
    label_feedback.config(text="")

def reset_game():
    """Reset the game state."""
    global target_number, attempts_left
    target_number = random.randint(1, 100)
    attempts_left = 10
    label_feedback.config(text="")
    label_attempts.config(text=f"Attempts Left: {attempts_left}")
    entry_guess.delete(0, tk.END)

# Create the main Tkinter window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.configure(bg="white")

# Bind Enter key to check_guess function
root.bind('<Return>', lambda event: check_guess())

# UI Elements
label_title = tk.Label(root, text="Guess the Number!", font=("Arial", 16), bg="white", fg="black")
label_title.pack(pady=10)

label_instruction = tk.Label(root, text="Enter a number between 1 and 100:", font=("Arial", 12), bg="white", fg="black")
label_instruction.pack()

entry_guess = tk.Entry(root, font=("Arial", 12), bg="gray", fg="black", justify="center")
entry_guess.pack(pady=10)

# Bind any keypress on the entry field to clear previous feedback
entry_guess.bind('<Key>', clear_feedback)

button_submit = tk.Button(root, text="Submit Guess", font=("Arial", 12), bg="white", fg="black", command=check_guess)
button_submit.pack(pady=10)

label_feedback = tk.Label(root, text="", font=("Arial", 12), bg="white", fg="black")
label_feedback.pack(pady=10)

label_attempts = tk.Label(root, text=f"Attempts Left: {attempts_left}", font=("Arial", 12), bg="white", fg="black")
label_attempts.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()