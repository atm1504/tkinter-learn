from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

myLabel = Label(root, text="42" + u'\u00A9', font=("Halvetica", 32)).pack(pady=10)




root.mainloop();
