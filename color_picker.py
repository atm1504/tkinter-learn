from tkinter import *
from PIL import ImageTk, Image
from tkinter import colorchooser

root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

def color():
    my_color = colorchooser.askcolor()[1]
    my_label = Label(root, text= "You picked a color : " + my_color, bg=my_color).pack(pady=10)

# my_color = colorchooser.askcolor()
my_button = Button(root, text="Pick A Color", command=color).pack()

root.mainloop();
