from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("500x400")

# Create a main frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create a canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add a scrollbar to the canvas
my_scrollbarr = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbarr.pack(side=RIGHT, fill=Y)

# Configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbarr.set)
my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# Create Another FRAME inside the frame
second_frame = Frame(my_canvas)

# Add that new frame to a Window in the canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

for i in range(100):
    Button(second_frame, text=f'Button {i} Yo!', padx=10, pady=10).grid(row=i, column=0, pady=10, padx=10)

my_label = Label(second_frame, text="We are great!").grid(row=3, column=1)

root.mainloop();
