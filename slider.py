from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

vertical=Scale(root, from_=0, to=200)
vertical.pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()

horizontal=Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

myButton= Button(root,text="Click Me!", command=slide).pack()

mainloop();
