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

#start countdown
x = 6

# function that starts the game
def start_game(event):
    global time_left
    e.config(state= "disabled")
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
    global time_left, x
    if x > 0:
        x = x - 1
        time_label.config(text="Game will start in: " + str(x))
        time_label.after(1000, countdown)
    else:
        e.config(state= "enabled")
        if time_left > 0:
            time_left -= 1
            time_label.config(text="Time left: " + str(time_left))
            time_label.after(1000, countdown)
        else:
            game_over_label.config(text="Game Over! Final Score: " + str(score))

# function to restart the game
def restart_game():
    e.config(state= "disabled")
    global score
    global time_left, x
    score = 0
    x = 6
    time_left = 60
    score_label.config(text="Game will start automatically")
    game_over_label.config(text="")
    e.delete(0, tkinter.END)


def dark_toggle():
    
    if toggle_button.config('text')[-1] == 'Dark Mode':
        toggle_button.config(text='Light Mode')
        for widget in root.winfo_children():
            if widget != label:
                widget.config(foreground="white", background = "#121212")
            else:
                widget.config(background = "#121212")
            if widget == e:
                widget.config(foreground="#121212", background = "white")
            root.config(background="#121212")
    else:
        toggle_button.config(text='Dark Mode')
        for widget in root.winfo_children():
            if widget != label:    
                widget.config(foreground="#121212", background = "white")
            else:
                widget.config(background = "white")
            if widget == e:
                widget.config(background = "#121212")
            root.config(background="white")


# create a GUI window
root = tkinter.Tk()

style = ttk.Style(root)
root.tk.call('source', 'azure/azure.tcl')
style.theme_use('azure')

# set the title 
root.title("Color Game")

# set the size
root.geometry("520x520")
root.minsize(400, 400)
root.maxsize(600, 600)

# can be resizable
root.resizable(True, True)

font = tkFont.Font(family="Segoe UI", size=60, weight="bold")

# add an instructions label
instructions_label = ttk.Label(root, text="Type in the colour of the words, and not the word text!", style="TLabel")
instructions_label.grid(row=0, column=0, pady=10)

# add a score label
score_label = ttk.Label(root, text="Press enter to start", style="TLabel")
score_label.grid(row=1, column=0, pady=10)

# add a time left label
time_label = ttk.Label(root, text="Time left: " + str(time_left), style="TLabel")
time_label.grid(row=2, column=0, pady=10)

# add a label for displaying the colours
label = tkinter.Label(root, font=font)
label.grid(row=3, column=0, padx=10, pady=10)

# add a game over label
game_over_label = ttk.Label(root, style="TLabel")
game_over_label.grid(row=4, column=0, pady=10)

# add a text entry box for typing in colours
e = ttk.Entry(root,style="TEntry")
e.grid(row=5, column=0, pady=10)
# run the 'start_game' function when the enter key is pressed
root.bind('<Return>', start_game)

# add a restart button
restart_button = ttk.Button(root, text="Restart",style="Togglebutton", command=restart_game)
restart_button.grid(row=6, column=0, padx=10, pady=10)

# add a switch button
toggle_button = ttk.Checkbutton(root, text="Light Mode", style="Switch",width=10, command=dark_toggle)
toggle_button.grid(column= 3, row = 6, pady=10)

# add the sizegrip
sg = ttk.Sizegrip(root, style="TSizegrip")
sg.grid(column=4, row=6, sticky=(tkinter.S, tkinter.E), padx=5, pady=5, ipadx=5, ipady=5)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# set focus on the entry box
e.focus_set()

# start the GUI
root.mainloop()