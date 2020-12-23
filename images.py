from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Using Images")
root.iconbitmap("./images/quality.ico")

my_img = ImageTk.PhotoImage(Image.open("./images/quality.png"))
my_label = Label(image=my_img)
my_label.pack()


# quit button
button = Button(root, text="Exit Program", command=root.quit)
button.pack()


root.mainloop()