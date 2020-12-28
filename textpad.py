from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("1200x660")

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
        


#--------------------------------------------------------------------------------------------------------------
# Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create our scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Text box
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none")
my_text.pack(pady=5)

# Configure our scroll bar
text_scroll.config(command=my_text.yview)

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
file_menu.add_command(label="Exit", command= root.quit)

# Add Edit menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut         ",accelerator="cmd+x", command=lambda: cut_text(False))
edit_menu.add_command(label="Copy        ", accelerator="cmd+c",command=lambda: copy_text(False))
edit_menu.add_command(label="Paste       ", accelerator="cmd+v", command=lambda: paste_text(False))
edit_menu.add_separator()
edit_menu.add_command(label="Und         ", accelerator="cmd+z", command = my_text.edit_undo)
edit_menu.add_command(label="Redo        ", accelerator="cmd+y", command = my_text.edit_redo)
edit_menu.add_separator()

# Add Status Bar
status_bar = Label(root, text='Ready         ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)


# Edit Bindings
root.bind("<Control-Key-x>", cut_text)
root.bind("<Control-Key-c>", copy_text)
root.bind("<Control-Key-v>", paste_text)

root.mainloop();
