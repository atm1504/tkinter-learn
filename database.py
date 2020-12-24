from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x400")

# database

# create a database or connect to one
conn = sqlite3.connect("address_book.db")

# Create Cursor
c = conn.cursor()

c.execute("""
CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )
""")

# Commit changes
conn.commit()

# Close Connection
conn.close()

mainloop();
