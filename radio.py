from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")

# r = IntVar()
# r.set(2)

TOPPINGS = [("Pepperoni", "Pepperoni"), ("Cheese", "Cheese"), ("Mushroom", "Mushroom"), ("Onion", "Onion")]

pizza = StringVar()
pizza.set("Pepperoni")

for text, tops in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=tops).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

# Radiobutton(root, text="Option 1", variable=r, value=1).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2).pack()

myButton = Button(root, text="CLick me", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()