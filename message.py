from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")

def popup():
    res = messagebox.askyesno("This is my pop up", "Hello World!")
    Label(root, text=res).pack()
    if res == 1:
        Label(root, text="You clicked Yes!").pack()
    else:
        Label(root, text="You clicked No!").pack()

    return

Button(root, text="Popup", command=popup).pack()


mainloop();
