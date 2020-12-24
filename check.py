from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="Would you like SuperSize? Click Here!", variable=var, onvalue="SuperSize", offvalue="RegularSize")
c.deselect()
c.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

mainloop();
