#dictionary front end.

#to connect it form the backend file.
from dictApp import *

#to import the tkinter module.
import tkinter
from tkinter import *


def user_input():
    word = user_word.get()
    dict(word)

def user_output():
    t1.insert(END, item)

#main window.
main_window = tkinter.Tk()
user_word = StringVar()
#widgets.
l1 = Label(main_window, text = "Enter Word")
l1.place(x = 5, y = 10)

#to take word form the user.
e1 = Entry(main_window, textvariable = user_word)
e1.place(x = 70, y = 10)

#to display the output.
t1 = Text(main_window, height = 5, width = 22)
t1.place(x = 10, y = 50)

#to call the dictionary method.
b1 = Button(main_window, text = "GO", command = user_input)
b1.place(x = 70, y = 150)

main_window.mainloop()

# TODO: improve GUI
# TODO: make GUI for wrong answer.
