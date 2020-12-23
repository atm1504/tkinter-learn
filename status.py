from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Using Images")
root.iconbitmap("./images/quality.ico")

my_img0 = ImageTk.PhotoImage(Image.open("./images/quality.png"))
my_img1 = ImageTk.PhotoImage(Image.open("./images/1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("./images/2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("./images/3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("./images/4.jpg"))

image_list = [my_img0, my_img1, my_img2, my_img3, my_img4]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img0)
my_label.grid(row=0, column=0, columnspan=3)

# SHow the next image
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", padx=10, pady=10, command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", padx=10, pady=10, command=lambda: back(image_number - 1))

    if image_number == len(image_list):
        button_forward = Button(root, text=">>", padx=10, pady=10, state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

# Show the previous image
def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", padx=10, pady=10, command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", padx=10, pady=10, command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", padx=10, pady=10, state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

# initial setup
button_back = Button(root, text="<<", padx=10, pady=10, state=DISABLED)
button_exit = Button(root, text="EXIT PROGRAM", command=root.quit, pady=10, padx=10)
button_forward = Button(root, text=">>", padx=10, pady=10, command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

status.grid(row=2, column=0, columnspan=3, sticky=W + E)

root.mainloop()