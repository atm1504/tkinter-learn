from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("300x300")

# messagebox.showinfo("showinfo", "Information")

def choice(option):
    pop.destroy()
    if option == "yes":
        temp_label.config(text="You clicked YES")
    else:
        temp_label.config(text="You clicked No")

def clicker():
    global pop
    pop = Toplevel(root)
    pop.title("My popup")
    pop.geometry("250x150")
    pop.config(bg="green")

    global me
    me = PhotoImage(file="images/me_head_gr.png")

    pop_label = Label(pop, text="Would you like to Proceed?", bg="green", fg="white", font=("Helvetica", 12))
    pop_label.pack(pady=10)

    my_frame = Frame(pop, bg="green")
    my_frame.pack(pady=5)

    me_pic = Label(my_frame, image=me, borderwidth=0)
    me_pic.grid(row=0, column=0, padx=10)

    yes = Button(my_frame, text="YES", command=lambda: choice("yes"))
    yes.grid(row=0, column=1, padx=10)
    
    no = Button(my_frame, text="NO", command=lambda: choice("no"))
    no.grid(row=0, column=2, padx=10)


my_button = Button(root, text="Click Me!", command=clicker)
my_button.pack(pady=50)

temp_label = Label(root, text='')
temp_label.pack(pady=20)

root.mainloop();
