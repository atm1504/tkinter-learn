from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import font


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("800x800")

def open_txt():
    text_file = filedialog.askopenfilename(initialdir="", title="Open text File", filetypes=(("Text Files", "*.txt"),))
    name = text_file
    text_file = open(text_file, "r")
    stuff = text_file.read()

    my_text.insert(END,stuff)
    text_file.close()

    root.title(f'{name} - Textpad')

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

def select():
    selected = my_text.selection_get()
    myLabel.config(text=selected)

def bolder():
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")

    my_text.tag_configure("bold", font=bold_font)
    current_tags = my_text.tag_names("sel.first")

    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")


def italics_it():
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")

    my_text.tag_configure("italic", font=italics_font)
    current_tags = my_text.tag_names("sel.first")

    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")

my_frame = Frame(root)
my_frame.pack(pady=10)

# Create Scrollbar
textScroll = Scrollbar(my_frame)
textScroll.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width=40, height=10, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", yscrollcommand=textScroll.set, undo=True)
my_text.pack(pady=20)

# Configure scrollbar
textScroll.config(command=my_text.yview)

open_button = Button(root, text="Open text file", command=open_txt)
open_button.pack(pady=20)

save_button = Button(root, text="Save File", command=save_txt)
save_button.pack(pady=20)

image_button = Button(root, text="Add Image", command=add_image)
image_button.pack(pady=10)

select_button = Button(root, text="Select Text", command=select)
select_button.pack(pady=5)

bold_button = Button(root, text="Bold", command=bolder)
bold_button.pack(pady=5)

italics_button = Button(root, text="Italics", command=italics_it)
italics_button.pack(pady=5)

bold_button.pack(pady=5)

myLabel = Label(root, text='')
myLabel.pack(pady=5)

redo_button = Button(root, text="Redo", command=my_text.edit_redo)
redo_button.pack(pady=10)

undo_button = Button(root, text="Undo", command=my_text.edit_undo)
undo_button.pack(pady=10)

root.mainloop();
