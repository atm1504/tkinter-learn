from tkinter import *
from PIL import ImageTk, Image
import pyttsx3


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

def talk():
    engine = pyttsx3.init()
    engine.say(myEntry.get())
    engine.runAndWait()
    myEntry.delete(0, END)

myEntry = Entry(root, font=("Helvetica", 28))
myEntry.pack(pady=20)

myButton = Button(root, text="Speak", command=talk)
myButton.pack(pady=20)

root.mainloop();
