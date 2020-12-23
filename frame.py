from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")

frame = LabelFrame(root, text="This is my Frame", padx=15, pady=15)
frame.pack(padx=20, pady=20)

b = Button(frame, text="I am a Button")
b.pack()

root.mainloop()