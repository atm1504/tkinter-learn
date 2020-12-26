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
myImage = myCanvas.create_image(260, 125, anchor=NW, image=img)


# def left(event):
#     x = -10
#     y = 0
#     myCanvas.move(myImage, x, y)

# def right(event):
#     x = 10
#     y = 0
#     myCanvas.move(myImage, x, y)

# def up(event):
#     x = 0
#     y = -10
#     myCanvas.move(myImage, x, y)

# def down(event):
#     x = 0
#     y = 10
#     myCanvas.move(myImage, x, y)

# def pressing(event):
#     x = 0
#     y = 0
#     if event.char == "a": x = -10
#     if event.char == "d": x = 10
#     if event.char == "r": y = -10
#     if event.char == "x": y = 10
#     myCanvas.move(myImage, x, y)

def move(e):
    global img
    myLabel.config(text="Coordinates: x: " + str(e.x) + " y: " + str(e.y))
    img = PhotoImage(file="images/me.png")
    myImage = myCanvas.create_image(e.x, e.y, anchor=NW, image=img)

# root.bind("<Key>",pressing)

# root.bind("<Left>", left)
# root.bind("<Right>", right)
# root.bind("<Up>", up)
# root.bind("<Down>", down)

myLabel = Label(root, text="")
myLabel.pack(pady=20)

myCanvas.bind('<B1-Motion>',move)

root.mainloop();
