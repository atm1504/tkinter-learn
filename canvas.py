from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

myCanvas = Canvas(root, width=300, height=200, bg="white", bd=5)
myCanvas.pack(pady=20)

# Create a straight line
myCanvas.create_line(0, 100, 300, 100, fill="red")
myCanvas.create_line(150, 0, 150, 200, fill="red")

# Create a rectangle
myCanvas.create_rectangle(50, 150, 250, 50, fill="pink")

# Create oval
myCanvas.create_oval(50,150,250,50, fill="cyan")

root.mainloop();
