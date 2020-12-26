from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")


myPic = PhotoImage(file="images/1.jpg")
myLabel = Label(root, image=myPic)
myLabel.pack(pady=20)


root.mainloop();
