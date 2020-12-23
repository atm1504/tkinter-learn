from tkinter import *

root = Tk()

# Method -1: Create Components idividually and render individually
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Hello World! We are Anam!! We will conquer the world!")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)

# Method -2: Component creation nd redering inline
myLabel3 = Label(root, text="Hello World! We are the Best!").grid(row=1, column=0)
myLabel4 = Label(root, text="Hello World! We are Anam!! We will conquer the world!").grid(row=1, column=1)


root.mainloop()