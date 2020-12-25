from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

# myLabel = Label(root, text="42" + u'\u00A9', font=("Halvetica", 32)).pack(pady=10)

def states():
    hide_all_frames()
    state_frame.pack(fill="both", expand=1)
    my_label = Label(state_frame, text="States").pack()

def state_capitals():
    hide_all_frames()
    state_capital_frame.pack(fill="both", expand=1)
    my_label = Label(state_capital_frame, text="Capitals").pack()

def hide_all_frames():

    for widget in state_frame.winfo_children():
        widget.destroy()
    
    for widget in state_capital_frame.winfo_children():
        widget.destroy()

    state_frame.pack_forget()
    state_capital_frame.pack_forget()

# Create our own menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create menu items
states_menu = Menu(my_menu)
my_menu.add_cascade(label="Geography", menu=states_menu)
states_menu.add_command(label="States", command=states)
states_menu.add_command(label="Capitals", command=state_capitals)
states_menu.add_separator()
states_menu.add_command(label="Exit", command=root.quit)

# Create Frames
state_frame = Frame(root, width=500, height=500)
state_capital_frame = Frame(root, width=500, height=500)



root.mainloop();
