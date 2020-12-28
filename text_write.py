from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("500x600")

def open_txt():
    text_file = filedialog.askopenfilename(initialdir="", title="Open text File", filetypes=(("Text Files", "*.txt"),))

    text_file = open(text_file, "r")
    stuff = text_file.read()

    my_text.insert(END,stuff)
    text_file.close()

# def save_txt():
#     text_file = filedialog.askopenfilename(initialdir="", title="Open Text File", filetypes=(("Text Files", "*.txt"),))
# 	text_file = open(text_file, 'w')
# 	text_file.write(my_text.get(1.0, END))

def save_txt():
    text_file = filedialog.askopenfilename(initialdir="", title="Open text file", filetypes=(("Text Files", "*.txt"),))
    text_file = open(text_file, 'a')
    text_file.write(my_text.get(1.0, END))

def add_image():
    # Add image
    global my_image
    my_image = PhotoImage(file="images/profile.png")
    position = my_text.index(INSERT)
    my_text.image_create(position, image=my_image)
    myLabel.config(text=position)


my_text = Text(root, width=40, height=10, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black")
my_text.pack(pady=20)

open_button = Button(root, text="Open text file", command=open_txt)
open_button.pack(pady=20)

save_button = Button(root, text="Save File", command=save_txt)
save_button.pack(pady=20)

image_button = Button(root, text="Add Image", command=add_image)
image_button.pack(pady=10)

myLabel = Label(root, text='')
myLabel.pack(pady=5)

root.mainloop();
