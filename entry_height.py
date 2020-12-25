from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack(pady=10)
    

e = Entry(root, width=50, font=('Helvetica', 24))

e.pack(padx=10, pady=10)


myButton = Button(root, text="Enter Your name", command=myClick)
myButton.pack(pady=10)


mainloop();
