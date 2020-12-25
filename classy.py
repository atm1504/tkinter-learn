from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

class Elder:
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.myButton = Button(root, text="Click Me!", command=self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print("Clicked!!.....")


e = Elder(root)



root.mainloop();
