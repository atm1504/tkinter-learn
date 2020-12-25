from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

def clicker(event):
    myLabel = Label(root, text="You clicked a key ->  " + event.keysym)
    print(event)
    myLabel.pack()

myButton = Button(root, text="Click Me!")
myButton.bind("<Key>", clicker)
myButton.pack(pady=20)


mainloop();
