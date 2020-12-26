from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

def something():
    my_label.config(text="This is new text!")
    root.config(bg="blue")
    my_button.config(text="You've been configured!")


global my_label
my_label = Label(root, text='This is my text', font=("Helvetica", 18))
my_label.pack(pady=10)

my_button = Button(root, text="Click Me", command=something)
my_button.pack(pady=10)

root.mainloop();
