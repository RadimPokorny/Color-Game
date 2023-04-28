import tkinter
import random
from tkinter import *
from tkinter import ttk

# list of possible colours
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']

# game score
score = 0

# time left, initially 30 seconds
time_left = 30

# function that starts the game
def start_game(event):
    global time_left
    if time_left > 0:
        countdown()
    next_colour()

# function to choose and display the next colour
def next_colour():
    global score
    global time_left
    if time_left > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]), font=('Helvetica', 60, 'bold'))
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
    time_left = 30
    score_label.config(text="Press enter to start")
    time_label.config(text="Time left: " + str(time_left))
    game_over_label.config(text="")
    e.delete(0, tkinter.END)
    label.config(fg="black", text="Welcome to the game!", font=('Helvetica', 60, 'bold'))

# function to update the time left when a new time is selected from the dropdown
def update_time(event):
    global time_left
    time_selected = int(time_dropdown.get())
    time_left = time_selected
    time_label.config(text="Time left: " + str(time_left))

# create a GUI window
root = tkinter.Tk()

# set the title
root.title("Color Game")

# set the size
root.geometry("1024x800")

root.configure(bg="#3D59AB")

# add an instructions label
instructions_label = tkinter.Label(root, text="Type in the colour of the words, and not the word text!", font=('Helvetica', 30, 'bold'), fg='white')
instructions_label.pack()

# add a score label
score_label = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 30, 'bold'), fg='white')
score_label.pack()

# add a time left label
time_label = tkinter.Label(root, text="Time left: " + str(time_left), font=('Helvetica', 30, 'bold'), fg='white')
time_label.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font=('Helvetica', 60, 'bold'))
label.pack()

# add a game over label
game_over_label = tkinter.Label(root, font=('Helvetica', 30, 'bold'), fg='red')
game_over_label.pack()

# set the background color of all the widgets to red
for widget in root.winfo_children():
    widget.config(bg="#3D59AB")

# add a dropdown menu for selecting the time
time_options = ["10", "30", "60", "120"]
selected_time = tkinter.StringVar(value=time_options[1])  # set the default value to 30 seconds
time_dropdown = tkinter.OptionMenu(root, selected_time, *time_options)
time_dropdown.config(font=('Helvetica', 20), bg='#3D59AB', fg='white', borderwidth=0)
time_dropdown.pack(pady=20)
selected_time_value = int(selected_time.get())

# add a text entry box for typing in colours
e = tkinter.Entry(root, font=('Helvetica', 30, 'bold'), borderwidth = 0, fg='#3D59AB')

# run the 'start_game' function when the enter key is pressed
root.bind('<Return>', start_game)
e.pack()

# set focus on the entry box
e.focus_set()

# add a frame to hold the restart button
button_frame = tkinter.Frame(root, bg="#3D59AB")
button_frame.pack(side=tkinter.BOTTOM, pady=20)

# add a restart button
restart_button = tkinter.Button(button_frame, text="Restart",font=('Helvetica', 30, 'bold') , fg='#3D59AB' ,bg='white', borderwidth = 0, command=restart_game)
restart_button.pack()

# start the GUI
root.mainloop()
