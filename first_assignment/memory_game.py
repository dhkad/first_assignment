"""This is a simple test memory game"""
import tkinter as tk
from tkinter import messagebox
import random


root = tk.Tk()
root.title("Memory Game")
root.geometry("500x300")
root.configure(bg="lightblue")

label_info = tk.Label(root, text="Click 'Start Game' to begin", font=("Arial", 12), fg="blue")
label_info.pack(pady=20)


sequence = []   # Correct order
shuffled = []   # Shuffled version
buttons = []    # Button to put the letters on them
guess = []      # Player's guess


def start_game():
    global sequence, shuffled, buttons, guess #we use global so we can access them outside the fn. 
    guess = []  
    
    # Remove old buttons if there is any
    for b in buttons:
        b.destroy()
    buttons = []
    
    # Choose sequence length (3-5 random letters)
    length = random.choice([3, 4, 5])
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sequence = random.sample(letters, length)
    
    # Show the sequence to the player
    label_info.config(text=f"Remember this order:\n{' '.join(sequence)}")
    root.after(4000, show_shuffled) #run the shuffled fn. after 4 sec 

btn_start = tk.Button(root, text="Start Game", command=start_game, width=10, height=3, font=("Arial", 12), fg="blue")
btn_start.pack(pady=10)

# Show shuffled sequence
def show_shuffled():
    global shuffled, buttons
    label_info.config(text="Click the letters in the correct order")
    
    # Shuffle the sequence
    shuffled = sequence[:]
    random.shuffle(shuffled)
    

    x = 130 #start button at x =130
    for ch in shuffled:
        btn = tk.Button(root, text=ch, width=4, height=2, fg="blue")
        btn.config(command=lambda c=ch, b=btn: choose_letter(c, b))
        btn.place(x=x, y=200)
        buttons.append(btn)
        x += 60  # spacing between buttons
        btn_start.config(state="disabled")


# player choice
def choose_letter(char, button):
    global guess
    guess.append(char)
    button.config(state="disabled")  # disable the clicked button
    
    # When player has chosen all letters
    if len(guess) == len(sequence):
        if guess == sequence:
            messagebox.showinfo("Congratulations", "You remembered correctly")
        else:
            messagebox.showerror("Oops!", f"Wrong order.\nCorrect was: {' '.join(sequence)}")
        btn_start.config(state='active',fg='blue')

# Run the application
root.mainloop()
