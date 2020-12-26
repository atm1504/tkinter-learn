from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import time


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

def step():
    # myProgress['value'] += 20
    # myProgress.start(10)
    for x in range(5):
        myProgress['value'] += 20
        root.update_idletasks()
        time.sleep(1)
        myLabel.config(text=myProgress['value'])

def stop():
    myProgress.stop()

myProgress = ttk.Progressbar(root,orient=HORIZONTAL, length=300, mode='determinate')
myProgress.pack(pady=10)

myButton = Button(root, text="Progress", command=step)
myButton.pack(pady=20)

myButton = Button(root, text="Stop", command=stop)
myButton.pack(pady=20)

myLabel = Label(root, text="")
myLabel.pack(pady=20)


root.mainloop();
