from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")


def grab():
	my_label.config(text=my_box.get())


my_box = Entry(root, font=("Helvetica", 28))
my_box.pack(pady=20)

my_button = Button(root, text="Grab Text From Box", command=grab)
my_button.pack(pady=20)


my_label = Label(root, text="")
my_label.pack(pady=20)


root.mainloop()
