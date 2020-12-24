from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

# Dropdown boxes
options = ["Monday", "Tueday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

clicked = StringVar()
clicked.set(options[1])

def show():
    Label(root,text=clicked.get()).pack()

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

mainloop();
