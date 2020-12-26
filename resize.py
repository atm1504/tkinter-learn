from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

myPic = Image.open("images/aspen.png")
# resize the image
resized = myPic.resize((300, 225), Image.ANTIALIAS)


# myPic = ImageTk.PhotoImage(file="images/aspen.png")
newPic = ImageTk.PhotoImage(resized)

# Image Size
myLabel = Label(root, image=newPic)
myLabel.pack(pady=20)


root.mainloop();
