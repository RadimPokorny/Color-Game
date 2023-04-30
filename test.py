import tkinter
import random
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont

# list of possible colours
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'Purple', 'Brown']

# game score
score = 0

# time left, initially 60 seconds
time_left = 60

# function that starts the game
def start_game(event):
    global time_left
    if time_left == 60:
        countdown()
    next_colour()

# function to choose and display the next colour
def next_colour():
    global score, style
    global time_left
    if time_left > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]), font=('Segoe UI', 60))
        score_label.config(text="Score: " + str(score))

# countdown timer function
def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_label.config(text="Time left: " + str(time_left))
        time_label.after(1000, countdown)
    else:
        game_over_label.config(text="Game Over! Final Score: " + str(score))

# function to restart the game
def restart_game():
    global score
    global time_left
    score = 0
    time_left = 60
    score_label.config(text="Press enter to start")
    time_label.config(text="Time left: " + str(time_left))
    game_over_label.config(text="")
    e.delete(0, tkinter.END)

# create a GUI window
root = tkinter.Tk()

style = ttk.Style(root)
root.tk.call('source', 'azure/azure.tcl')
style.theme_use('azure')

# set the title 
root.title("Color Game")

# set the size
root.geometry("400x250")

font = tkFont.Font(family="Segoe UI", size=60, weight="bold")


# add an instructions label
instructions_label = ttk.Label(root, text="Type in the colour of the words, and not the word text!", style="TLabel")
instructions_label.pack()

# add a score label
score_label = ttk.Label(root, text="Press enter to start", style="TLabel")
score_label.pack()

# add a time left label
time_label = ttk.Label(root, text="Time left: " + str(time_left), style="TLabel")
time_label.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font=font)
label.pack()

# add a game over label
game_over_label = ttk.Label(root, style="TLabel")
game_over_label.pack()

# add a text entry box for typing in colours
e = ttk.Entry(root, style="TEntry")

# run the 'start_game' function when the enter key is pressed
root.bind('<Return>', start_game)
e.pack()

# set focus on the entry box
e.focus_set()

# add a restart button
restart_button = ttk.Button(root, text="Restart",style="Accentbutton", command=restart_game)
restart_button.pack()

# start the GUI
root.mainloop()