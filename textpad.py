from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import os, sys

root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("1200x680")

global open_status_name
open_status_name = False

global selected
selected = False

#-----------------------------------------------------Functions-----------------------------------------------------------------
#Create new file function
def new_file():
    my_text.delete("1.0", END)
    root.title('New File - TextPad!')
    status_bar.config(text="New File      ")
    global open_status_name
    open_status_name = False

#Create new file function
def open_file():
    # Clear Editor
    my_text.delete("1.0", END)
    global open_status_name
    # Grab File
    text_file = filedialog.askopenfilename(initialdir="", title="Open text File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*"),))
    if text_file:
        name = text_file
        open_status_name = name

        status_bar.config(text=f'{name}           ')
        root.title(f'{name} - TextPad!')

        # Open the file
        text_file = open(text_file, 'r')
        stuff = text_file.read()

        # Add file data tot he text box
        my_text.insert(END, stuff)
        # Close  file
        text_file.close()

def save_as_file():
    global open_status_name
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        name = text_file
        root.title(f'{name} - TextPad!')
        status_bar.config(text=f'Saved: {name}           ')

        # Save  the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        # Close the file
        text_file.close()

def save_file():
    global open_status_name
    if open_status_name:
        # Save  the file
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        # Close the file
        text_file.close()
        root.title(f'{open_status_name} - TextPad!')
        status_bar.config(text=f'Saved: {open_status_name}           ')
    else:
        save_as_file()

#Cut Text
def cut_text(e):
    global selected
    # To see if from keyboard
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            selected = my_text.selection_get()
            my_text.delete("sel.first", "sel.last")

#Copy Text
def copy_text(e):
    global selected
    # To see if from keyboard
    if e:
        selected = root.clipboard_get()

    if my_text.selection_get():
        selected = my_text.selection_get()
        # my_text.delete("sel.first", "sel.last")
        root.clipboard_clear()
        root.clipboard_append(selected)

#Paste Text
def paste_text(e):
    global selected
    # Check to see if keyboard shortcut cut
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)

# Bold it
def bold_it():
	bold_font = font.Font(my_text, my_text.cget("font"))
	bold_font.configure(weight="bold")

	my_text.tag_configure("bold", font=bold_font)

	current_tags = my_text.tag_names("sel.first")

	if "bold" in current_tags:
		my_text.tag_remove("bold", "sel.first", "sel.last")
	else:
		my_text.tag_add("bold", "sel.first", "sel.last")

# Italics it
def italics_it():
	italics_font = font.Font(my_text, my_text.cget("font"))
	italics_font.configure(slant="italic")

	my_text.tag_configure("italic", font=italics_font)

	current_tags = my_text.tag_names("sel.first")

	if "italic" in current_tags:
		my_text.tag_remove("italic", "sel.first", "sel.last")
	else:
		my_text.tag_add("italic", "sel.first", "sel.last")

# Selected Text Color
def text_color():
    my_color = colorchooser.askcolor()[1]

    if my_color:
        color_font = font.Font(my_text, my_text.cget("font"))
        my_text.tag_configure("colored", font=color_font, foreground=my_color)
        current_tags = my_text.tag_names("sel.first")
        if "colored" in current_tags:
            my_text.tag_remove("colored", "sel.first", "sel.last")
        else:
            my_text.tag_add("colored", "sel.first", "sel.last")

# Change background color
def bg_color():
	my_color = colorchooser.askcolor()[1]
	if my_color:
		my_text.config(bg=my_color)

# Change ALL Text Color
def all_text_color():
	my_color = colorchooser.askcolor()[1]
	if my_color:
		my_text.config(fg=my_color)

# Print file
def print_file():
    pass

# Select all
def select_all(e):
    my_text.tag_add('sel', '1.0', 'end')

#Clear All
def clear_all():
    my_text.delete(1.0, END)

# Turn on Night Mode
def night_on():
    main_color = "#000000"
    second_color = "#373737"
    text_color = "green"

    root.config(bg=main_color)
    status_bar.config(bg=main_color, fg=text_color)
    my_text.config(bg=second_color)
    toolbar_frame.config(bg=main_color)

    bold_button.config(bg=second_color)
    italics_button.config(bg=second_color)
    redo_button.config(bg=second_color)
    undo_button.config(bg=second_color)
    color_text_button.config(bg=second_color)

    file_menu.config(bg=main_color,fg=text_color)
    edit_menu.config(bg=main_color,fg=text_color)
    options_menu.config(bg=main_color,fg=text_color)
    color_menu.config(bg=main_color,fg=text_color)


# Turn off Night Mode
def night_off():
    main_color = "SystemButtonFace"
    second_color = "SystemButtonFace"
    text_color = "black"

    root.config(bg=main_color)
    status_bar.config(bg=main_color, fg=text_color)
    my_text.config(bg=second_color)
    toolbar_frame.config(bg=main_color)

    bold_button.config(bg=second_color)
    italics_button.config(bg=second_color)
    redo_button.config(bg=second_color)
    undo_button.config(bg=second_color)
    color_text_button.config(bg=second_color)

    file_menu.config(bg=main_color,fg=text_color)
    edit_menu.config(bg=main_color,fg=text_color)
    options_menu.config(bg=main_color,fg=text_color)
    color_menu.config(bg=main_color,fg=text_color)
#--------------------------------------------------------------------------------------------------------------
# Create a toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

# Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create our vertical scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Horizontal scroll bar
hor_scroll = Scrollbar(my_frame, orient="horizontal")
hor_scroll.pack(side=BOTTOM,fill=X)

# Text box
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, xscrollcommand=hor_scroll.set, wrap="none")
my_text.pack(pady=5)

# Configure our scroll bar
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)


my_menu = Menu(root)
root.config(menu=my_menu)

# File menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As",command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Print File",command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command= root.quit)

# Add Edit menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut",accelerator="cmd+x", command=lambda: cut_text(False))
edit_menu.add_command(label="Copy", accelerator="cmd+c",command=lambda: copy_text(False))
edit_menu.add_command(label="Paste ", accelerator="cmd+v", command=lambda: paste_text(False))
edit_menu.add_separator()
edit_menu.add_command(label="Undo", accelerator="cmd+z", command = my_text.edit_undo)
edit_menu.add_command(label="Redo", accelerator="cmd+y", command = my_text.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", accelerator="cmd+a", command = lambda : select_all(False))
edit_menu.add_command(label="Clear", command=clear_all)

# Add Color menu
color_menu = Menu(my_menu)
my_menu.add_cascade(label="Color", menu=color_menu)
color_menu.add_command(label="Change Selected", command=text_color)
color_menu.add_command(label="All Text", command=all_text_color)
color_menu.add_command(label="Background", command=bg_color)

# Add Options menu
options_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Dark Mode On", command=night_on)
options_menu.add_command(label="Dark Mode Off", command=night_off)

# Add Status Bar
status_bar = Label(root, text='Ready         ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=15)

# Create a Bold button
bold_button = Button(toolbar_frame, text="Bold", command=bold_it)
bold_button.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Italics Button
italics_button = Button(toolbar_frame, text="Italics", command=italics_it)
italics_button.grid(row=0, column=1, padx=5, pady=5)

# Undo Buttons
undo_button = Button(toolbar_frame, text="Undo", command=my_text.edit_undo)
undo_button.grid(row=0, column=2, padx=5, pady=5)

# Redo Buttons
redo_button = Button(toolbar_frame, text="Redo", command=my_text.edit_redo)
redo_button.grid(row=0, column=3, padx=5, pady=5)

# Text color button
color_text_button = Button(toolbar_frame, text="Text Color", command=text_color)
color_text_button.grid(row=0, column=4, padx=5, pady=5)

# Edit Bindings
root.bind("<Control-Key-x>", cut_text)
root.bind("<Control-Key-c>", copy_text)
root.bind("<Control-Key-v>", paste_text)

# Select Binding
root.bind('<Control-A>', select_all)
root.bind('<Control-a>', select_all)
root.mainloop();
