from tkinter import *
from PIL import ImageTk, Image
import mysql.connector


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="11312113"
)

print(mydb)

mainloop();
