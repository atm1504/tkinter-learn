from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

myLabel = Label(root)

def myDelete():
    myLabel.grid_forget()
    myButton['state'] = NORMAL

def myClick():
    global myLabel
    myLabel = Label(root)
    myLabel.destroy()

    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, 'end')
    myLabel.grid(row=3, column=0, pady=10)
    # myButton['state'] = DISABLED

e = Entry(root, width=50, font=('Helvetica', 30))
e.grid(row=0, column=0, padx=10, pady=10)

myButton = Button(root, text="Enter your name!", command=myClick)
myButton.grid(pady=10,row=1,column=0)

deleteButton = Button(root, text="Delete Text", command=myDelete)
deleteButton.grid(pady=10, row=2, column=0)


mainloop();
