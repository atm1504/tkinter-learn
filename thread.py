from tkinter import *
from PIL import ImageTk, Image
import time
from random import randint
import threading


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

def five_seconds():
    time.sleep(5)
    my_label.config("5 seconds is up")

def rando():
    random_label.configure(text=f'Random Number: {randint(1,100)}')


my_label = Label(root, text="Hello There!")
my_label.pack(pady=20)

my_button1 = Button(root, text="5 Seconds", command=threading.Thread(target=five_seconds).start())
my_button1.pack(pady=20)

my_button2 = Button(root, text="Pick a random number", command=rando)
my_button2.pack(pady=20)

random_label = Label(root, text='')
random_label.pack(pady=20)

threading.Thread(target=five_seconds).start()

root.mainloop();
