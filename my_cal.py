from tkinter import *
from PIL import ImageTk, Image
from tkcalendar import *

# Install tkcalendar
# pip install tkcalendar

root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

cal = Calendar(root, selectmode="day", year=2020, month=5, day=22)
cal.pack(pady=20, fill="both", expand=True)

def grabDate():
    myLabel.config(text=cal.get_date())


myButton = Button(root, text="Get Date",command=grabDate)
myButton.pack(pady=20)

myLabel = Label(root, text="")
myLabel.pack(pady=20)

root.mainloop();
