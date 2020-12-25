from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

def myDelete():
    myLabel.pack_forget()
    myButton['state'] = NORMAL

def myClick():
    global myLabel
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, 'end')
    myLabel.pack(pady=10)
    myButton['state'] = DISABLED

e = Entry(root, width=50, font=('Helvetica', 30))
e.pack(padx=10, pady=10)

myButton = Button(root, text="Enter your name!", command=myClick)
myButton.pack(pady=10)

deleteButton = Button(root, text="Delete Text", command=myDelete)
deleteButton.pack(pady=10)


mainloop();
