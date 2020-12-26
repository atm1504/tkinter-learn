from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

def number():
    try:
        print(int(myBox.get()))
        answer.config(text="That is a number")
    except ValueError:
        answer.config(text="That is a string")


myLabel = Label(root, text="Enter a number")
myLabel.pack(pady=20)

myBox = Entry(root)
myBox.pack(pady=10)

myButton = Button(root, text="Enter a number", command=number)
myButton.pack(pady=5)

answer = Label(root, text='')
answer.pack(pady=20)


root.mainloop();
