from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")

def openW():
    global my_img
    top = Toplevel()
    # lbl = Label(top, text="Hello World!").pack()

    my_img = ImageTk.PhotoImage(Image.open("./images/1.jpg"))
    my_label = Label(top, image=my_img).pack()

    btn= Button(top,text="Close Second Window",command=top.destroy).pack()


btn= Button(root,text="Open Second Window",command=openW).pack()

mainloop();
