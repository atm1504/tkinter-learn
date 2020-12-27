from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

def buttonHover(e):
    myButton["bg"] = "white"
    statusLabel.config(text="I'm Hovering over the Button!")

def buttonHoverLeave(e):
    myButton["bg"] = "SystemButtonFace"
    statusLabel.config(text="")

myButton = Button(root, text="Click Me", font=("Helvetica", 28))
myButton.pack(pady=50)

statusLabel = Label(root, text='test', bd=1, relief=SUNKEN, anchor=E)
statusLabel.pack(fill=X, side=BOTTOM, ipady=2)

myButton.bind("<Enter>", buttonHover)
myButton.bind("<Leave>", buttonHoverLeave)


root.mainloop();
