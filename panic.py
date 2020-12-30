from tkinter import *
from PIL import ImageTk, Image
from datetime import date

root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

panic = Label(root, text="DON'T PANIC!", font=("Helvetica", 42), bg="black", fg="green")
panic.pack(pady=20, ipadx=10, ipady=10)

today = date.today()
f_today=today.strftime("%A - %B %d, %Y")

today_label = Label(root, text=f_today)
today_label.pack(pady=20)



root.mainloop();
