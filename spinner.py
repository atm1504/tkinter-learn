from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

def reset():
    var = IntVar()
    var.set(0)
    my_spin.config(textvariable=var)

var = IntVar()
var.set(0)


my_spin = Spinbox(root, from_=0, to=100, font=("Helvetica", 18), textvariable=var)
my_spin.pack(pady=20)

my_button = Button(root, text="Reset Button", command=reset)
my_button.pack(pady=20)

root.mainloop();
