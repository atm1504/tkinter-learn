from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

my_notebook = ttk.Notebook(root)
my_notebook.pack()

def hide():
    my_notebook.hide(1)

def show():
    my_notebook.add(my_frame2, text="Red Tab")

def select():
    my_notebook.select(1)

my_frame1 = Frame(my_notebook, width=500, height=500, bg="blue")
my_frame2 = Frame(my_notebook, width=500, height=500, bg="red")

my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)

my_notebook.add(my_frame1,text="Blue Tab")
my_notebook.add(my_frame2, text="Red Tab")

my_button = Button(my_frame1, text="Hide Tab 2", command=hide).pack(pady=10)
my_button2 = Button(my_frame1, text="Show Tab 2", command=show).pack(pady=10)
my_button3 = Button(my_frame1, text="Show Tab 2", command=select).pack(pady=10)

root.mainloop();