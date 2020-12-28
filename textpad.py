from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("1200x660")

#-----------------------------------------------------Functions-----------------------------------------------------------------
#Create new file function
def new_file():
    my_text.delete("1.0", END)
    root.title('New File - TextPad!')
    status_bar.config(text="New File      ")


#Create new file function
def open_file():
    # Clear Editor
    my_text.delete("1.0", END)
    # Grab File
    text_file = filedialog.askopenfilename(initialdir="", title="Open text File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*"),))
    name = text_file
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
file_menu.add_command(label="Save", command=save_as_file)
file_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Exit", command= root.quit)

# Add Edit menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_separator()

# Add Status Bar
status_bar = Label(root, text='Ready         ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)


root.mainloop();
