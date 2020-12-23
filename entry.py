from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name: ") # kind of placeholder

def myClick():

    myLabel = Label(root, text="Your name is: " + e.get())
    myLabel.pack()


myButton = Button(root, text="Show your name?", padx=10, pady=10, command=myClick, fg="#000000", bg="black")
myButton.pack()


root.mainloop()