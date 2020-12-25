from tkinter import *
from PIL import ImageTk, Image
import mysql.connector


root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("400x800")

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
# my_cursor.execute("SELECT * FROM customers")

# for m in my_cursor.description:
#     print(m)
# print(my_cursor.description)

# Clear Text Fields
def clearFields():
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    address1_box.delete(0, END)
    address2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    zipcode_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    email_box.delete(0, END)
    username_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)

# Submit Customer Database
def addCustomer():
    sql_commands = "INSERT INTO customers (first_name, last_name, zipcode,  price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)";
    values = (first_name_box.get(), last_name_box.get(), zipcode_box.get(), price_paid_box.get(), email_box.get(), address1_box.get(), address2_box.get(), city_box.get(), state_box.get(), country_box.get(), phone_box.get(), payment_method_box.get(), discount_code_box.get())
    my_cursor.execute(sql_commands, values)

    mydb.commit()
    clearFields()

# Create label boxes
#----------------------------------------------------------------
title_label = Label(root, text="Customer Database", font=("Helvetica", 16))
title_label.grid(row=60, column=0, columnspan=2, pady="10")

first_name_label = Label(root, text="First Name").grid(row=1, column=0, sticky=W, padx=10)
last_name_label = Label(root, text="Last Name").grid(row=2, column=0, sticky=W, padx=10)
address1_label = Label(root, text="Address 1 Box").grid(row=3, column=0, sticky=W, padx=10)
address2_label = Label(root, text="Address 2 Box").grid(row=4, column=0, sticky=W, padx=10)
city_label = Label(root, text="City").grid(row=5, column=0, sticky=W, padx=10)
state_label = Label(root, text="State").grid(row=6, column=0, sticky=W, padx=10)
zipcode_label = Label(root, text="Zipcode").grid(row=7, column=0, sticky=W, padx=10)
country_label = Label(root, text="Country").grid(row=8, column=0, sticky=W, padx=10)
phone_label = Label(root, text="Phone").grid(row=9, column=0, sticky=W, padx=10)
email_label = Label(root, text="Email").grid(row=10, column=0, sticky=W, padx=10)
username_label = Label(root, text="Username").grid(row=11, column=0, sticky=W, padx=10)
payment_method_label = Label(root, text="Payment Method").grid(row=12, column=0, sticky=W, padx=10)
discount_code_label = Label(root, text="Discount Code").grid(row=13, column=0, sticky=W, padx=10)
price_paid_label = Label(root, text="Price Paid").grid(row=14, column=0, sticky=W, padx=10)

# Create input text boxes
#----------------------------------------------------------------
first_name_box = Entry(root)
first_name_box.grid(row=1, column=1, pady=5)

last_name_box = Entry(root)
last_name_box.grid(row=2, column=1, pady=5)

address1_box = Entry(root)
address1_box.grid(row=3, column=1, pady=5)

address2_box = Entry(root)
address2_box.grid(row=4, column=1, pady=5)

city_box = Entry(root)
city_box.grid(row=5, column=1, pady=5)

state_box = Entry(root)
state_box.grid(row=6, column=1, pady=5)

zipcode_box = Entry(root)
zipcode_box.grid(row=7, column=1, pady=5)

country_box = Entry(root)
country_box.grid(row=8, column=1, pady=5)

phone_box = Entry(root)
phone_box.grid(row=9, column=1, pady=5)

email_box = Entry(root)
email_box.grid(row=10, column=1, pady=5)

username_box = Entry(root)
username_box.grid(row=11, column=1, pady=5)

payment_method_box = Entry(root)
payment_method_box.grid(row=12, column=1, pady=5)

discount_code_box = Entry(root)
discount_code_box.grid(row=13, column=1, pady=5)

price_paid_box = Entry(root)
price_paid_box.grid(row=14, column=1, pady=5)

# Create buttons
#----------------------------------------------------------------
add_customer_button = Button(root, text="Add customer to database", command=addCustomer)
add_customer_button.grid(row=15, column=0, padx=10, pady=10)

clear_fields_button = Button(root, text="Clear Fields", command=clearFields)
clear_fields_button.grid(row=15, column=1, padx=10, pady=10)


my_cursor.execute("SELECT * from customers");
results= my_cursor.fetchall()
print(results)

mainloop();
