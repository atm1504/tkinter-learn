from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

my_menu = Menu(root)
root.config(menu=my_menu)

def our_command():
    my_label=Label(root,text="You clicked on a menu item").pack()
    pass

def file_new():
    file_new_frame.pack(fill="both", expand=1)
    

# Create items for menu
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=file_new)
file_menu.add_separator()
file_menu.add_command(label="Exit...", command=root.quit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut...", command=our_command)
# edit_menu.add_separator()
edit_menu.add_command(label="Copy...", command=our_command)


option_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Find", command=our_command)
option_menu.add_command(label="Find Next", command=our_command)

file_new_frame = Frame(root, width=400, height=400, bg="red")


mainloop();
