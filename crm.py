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
    passwd="11312113",
    database="codemy"
)

# Create a cursor and initialize it
my_cursor = mydb.cursor()

# Database created
# my_cursor.execute("CREATE DATABASE codemy");

# Table created
# my_cursor.execute("CREATE TABLE customers( first_name VARCHAR(255), last_name VARCHAR(255) , zipcode int(10), price_paid DECIMAL(10, 2), user_id INT AUTO_INCREMENT PRIMARY KEY) ")

my_cursor.execute("SELECT * FROM customers")
print(my_cursor.description)

mainloop();
