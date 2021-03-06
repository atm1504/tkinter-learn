from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("800x600")

w = 600
h = 400
x = w // 2
y = h // 2

myCanvas = Canvas(root, width=w, height=h, bg="white")
myCanvas.pack(pady=20)

# myCircle = myCanvas.create_oval(x, y, x + 10, y + 10)

img = PhotoImage(file="images/me.png")

myImage = myCanvas.create_image(0, 0, anchor=NW, image=img)


def left(event):
    x = -10
    y = 0
    myCanvas.move(myImage, x, y)

def right(event):
    x = 10
    y = 0
    myCanvas.move(myImage, x, y)

def up(event):
    x = 0
    y = -10
    myCanvas.move(myImage, x, y)

def down(event):
    x = 0
    y = 10
    myCanvas.move(myImage, x, y)

def pressing(event):
    x = 0
    y = 0
    if event.char == "a": x = -10
    if event.char == "d": x = 10
    if event.char == "r": y = -10
    if event.char == "x": y = 10
    myCanvas.move(myImage, x, y)


root.bind("<Key>",pressing)

root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

root.mainloop();
