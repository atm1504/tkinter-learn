from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("1200x400")

my_entries = []

def something():
    entry_list=""
    for entries in my_entries:
        entry_list += str(entries.get()) + "\n"
        myLabel.config(text=entry_list)

for y in range(5):
    for x in range(5):
        my_entry = Entry(root, bd=4)
        my_entry.grid(row=y, column=x, pady=20, padx=5)
        my_entries.append(my_entry)

myButton = Button(root, text="Click Me!", command=something)
myButton.grid(row=6, column=0, pady=10)


myLabel = Label(root, text="")
myLabel.grid(row=7, column=0, pady=20)

root.mainloop();
