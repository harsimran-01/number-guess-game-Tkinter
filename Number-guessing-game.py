from tkinter import *
import random

random_number = random.randint(1, 100)
print(random_number)

def check_num():
    if number_value.get() < random_number:
        message_label.config(text="Too Low!!! Try Again")
    elif number_value.get() > random_number:
        message_label.config(text="Too High!!! Try Again")
    elif number_value.get() == random_number:
        message_label.config(text="Great!!! You Guessed Correct")        

def play_again():
    message_label.config(text="")
    number_value.set("")

def exit():
    window.quit()

window = Tk()
window.title("Number-Guessing-Game")
window.geometry("480x300")

frame = Frame(window, height=300, width=500, bg="light coral")
frame.place(x=0, y=0)

label = Label(text="Number Guessing Game", font=("Times New Roman", 24, "bold"),bg="light salmon")
label.place(x=65, y=20)

number_value = IntVar()
number_value.set("")
entry = Entry(frame, width=25, border=2, relief="solid", textvariable=number_value, font=("Helvetica", 8, "bold"))
entry.place(x=90, y=110)

button_guess = Button(text="Guess", font=("Helvetica", 11, "bold"),bg="black", fg="white" ,width=10, command=check_num)
button_guess.place(x=260, y=106)

message_label = Label(frame,text="",font=("Helvetica", 16, "bold"), bg="light coral")
message_label.place(x=100, y=160)

button_play = Button(text="Play Again", font=("Helvetica", 11, "bold"),bg="black", fg="white" ,width=10, command=play_again)
button_play.place(x=120, y=220)

button_exit = Button(text="Exit Game", font=("Helvetica", 11, "bold"),bg="red", fg="black" ,width=10, command=quit)
button_exit.place(x=240, y=220)


window.mainloop()