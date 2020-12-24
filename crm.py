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
# my_cursor.execute("CREATE TABLE IF NOT EXISTS customers( first_name VARCHAR(255), last_name VARCHAR(255) , zipcode int(10), price_paid DECIMAL(10, 2), user_id INT AUTO_INCREMENT PRIMARY KEY) ")

# Altered the table to add more fields
# my_cursor.execute("ALTER TABLE customers ADD (\
#     email VARCHAR(255), \
#     address_1 VARCHAR(255), \
#     address_2 VARCHAR(255), \
#     city VARCHAR(50), \
#     state VARCHAR(50), \
#     country VARCHAR(250), \
#     phone VARCHAR(100), \
#     payment_method VARCHAR(50), \
#     discount_code VARCHAR(255))")

## Shows all the column headers of the table
my_cursor.execute("SELECT * FROM customers")

for m in my_cursor.description:
    print(m)
# print(my_cursor.description)

mainloop();
