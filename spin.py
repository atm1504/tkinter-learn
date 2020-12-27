from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

def grab():
    my_label.config(text=my_spin.get())
    


# my_spin = Spinbox(root, from_=0, to=10, increment=1, font=("Helvetica", 20))
names = ("John", "Tim", "Mary", "Tina")

my_spin = Spinbox(root, values=names, font=("Helvetica", 20))
my_spin.pack(pady=20)

my_button = Button(root, text="Submit",command=grab)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)


root.mainloop();
