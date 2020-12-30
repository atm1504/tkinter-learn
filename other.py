from tkinter import *
from PIL import ImageTk, Image
from namer import wish

root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

greet = wish("Anam")

def submit_name():
    greet = wish(my_box.get())
    my_label.config(text=greet)

my_box = Entry(root)
my_box.pack(pady=20)

my_label = Label(root, text=greet, font=("Helvetics", 18))
my_label.pack(pady=10)

my_button = Button(root, text="Submit  Name", command=submit_name)
my_button.pack(pady=20)


root.mainloop();
