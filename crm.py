from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
import csv
from tkinter import ttk

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

# my_cursor.execute("ALTER TABLE customers ADD(username VARCHAR(100))")

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
    sql_commands = "INSERT INTO customers (first_name, last_name, zipcode,  price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code,username) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)";
    values = (first_name_box.get(), last_name_box.get(), zipcode_box.get(), price_paid_box.get(), email_box.get(), address1_box.get(), address2_box.get(), city_box.get(), state_box.get(), country_box.get(), phone_box.get(), payment_method_box.get(), discount_code_box.get(), username_box.get())
    my_cursor.execute(sql_commands, values)

    mydb.commit()
    clearFields()

# Write to CSV
def writeToCSV(result):
    with open('customers.csv', 'a') as f:
        w = csv.writer(f, dialect='excel')
        for record in result:
            w.writerow(record)

# List customers
def listCustomers():
    list_customer_query = Tk()
    list_customer_query.title("List All Customers")
    list_customer_query.iconbitmap("./images/quality.ico")
    list_customer_query.geometry("800x800")

    my_cursor.execute("SELECT * from customers");
    result = my_cursor.fetchall()

    for index, x in enumerate(result):
        num = 0
        for y in x:
            lookup_label = Label(list_customer_query, text=y)
            lookup_label.grid(row=index, column=num)
            num += 1

    csv_button = Button(list_customer_query, text="Save to excel", command=lambda: writeToCSV(result))
    csv_button.grid(row=index + 1, column=0)

# Search customers in database
def searchCustomers():
    search_customers = Tk()
    search_customers.title("List of Customers Found")
    search_customers.iconbitmap("./images/quality.ico")
    search_customers.geometry("1300x800")

    def update():
        sql_command = """ UPDATE customers SET first_name=%s, last_name=%s, address_1 = %s ,  address_2=%s, city=%s, state=%s, zipcode=%s, country=%s,  phone=%s, email=%s, username=%s, payment_method=%s, discount_code=%s WHERE user_id=%s"""

        first_name = first_name_box2.get()
        last_name = last_name_box2.get()
        address1 = address1_box2.get()
        address2 = address2_box2.get()
        city = city_box2.get()
        state = state_box2.get()
        zipcode = zipcode_box2.get()
        country = country_box2.get()
        phone = phone_box2.get()
        email = email_box2.get()
        username = username_box2.get()
        payment_method = payment_method_box2.get()
        discount_code = discount_code_box2.get()
        id_value = id_box2.get()

        inputs = (first_name, last_name, address1, address2, city, state, zipcode, country, phone, email, username, payment_method, discount_code, id_value)

        my_cursor.execute(sql_command, inputs)
        mydb.commit()

        search_customers.destroy()


    def editNow(id, index):

        sql2 = "SELECT * FROM customers WHERE user_id = %s"
        name2 = (id,)
        result2 = my_cursor.execute(sql2, name2)
        result2 = my_cursor.fetchall()
        print(result2)

        first_name_label = Label(search_customers, text="First Name").grid(row=index + 1, column=0, sticky=W, padx=10)
        last_name_label = Label(search_customers, text="Last Name").grid(row=index + 2, column=0, sticky=W, padx=10)
        address1_label = Label(search_customers, text="Address 1 Box").grid(row=index + 3, column=0, sticky=W, padx=10)
        address2_label = Label(search_customers, text="Address 2 Box").grid(row=index + 4, column=0, sticky=W, padx=10)
        city_label = Label(search_customers, text="City").grid(row=index + 5, column=0, sticky=W, padx=10)
        state_label = Label(search_customers, text="State").grid(row=index + 6, column=0, sticky=W, padx=10)
        zipcode_label = Label(search_customers, text="Zipcode").grid(row=index + 7, column=0, sticky=W, padx=10)
        country_label = Label(search_customers, text="Country").grid(row=index + 8, column=0, sticky=W, padx=10)
        phone_label = Label(search_customers, text="Phone").grid(row=index + 9, column=0, sticky=W, padx=10)
        email_label = Label(search_customers, text="Email").grid(row=index + 10, column=0, sticky=W, padx=10)
        username_label = Label(search_customers, text="Username").grid(row=index + 11, column=0, sticky=W, padx=10)
        payment_method_label = Label(search_customers, text="Payment Method").grid(row=index + 12, column=0, sticky=W, padx=10)
        discount_code_label = Label(search_customers, text="Discount Code").grid(row=index + 13, column=0, sticky=W, padx=10)
        price_paid_label = Label(search_customers, text="Price Paid").grid(row=index + 14, column=0, sticky=W, padx=10)
        id_label = Label(search_customers, text="User Id").grid(row=index + 15, column=0, sticky=W, padx=10)

        # Create input text boxes
        #----------------------------------------------------------------
        global first_name_box2
        first_name_box2 = Entry(search_customers)
        first_name_box2.grid(row=index + 1, column=1, pady=10)
        first_name_box2.insert(0, result2[0][0])

        global last_name_box2
        last_name_box2 = Entry(search_customers)
        last_name_box2.grid(row=index + 2, column=1, pady=5)
        last_name_box2.insert(0, result2[0][1])

        global address1_box2
        address1_box2 = Entry(search_customers)
        address1_box2.grid(row=index + 3, column=1, pady=5)
        address1_box2.insert(0, result2[0][2])

        global address2_box2
        address2_box2 = Entry(search_customers)
        address2_box2.grid(row=index + 4, column=1, pady=5)
        address2_box2.insert(0, result2[0][3])

        global city_box2
        city_box2 = Entry(search_customers)
        city_box2.grid(row=index + 5, column=1, pady=5)
        city_box2.insert(0, result2[0][4])

        global state_box2
        state_box2 = Entry(search_customers)
        state_box2.grid(row=index + 6, column=1, pady=5)
        state_box2.insert(0, result2[0][5])

        global zipcode_box2
        zipcode_box2 = Entry(search_customers)
        zipcode_box2.grid(row=index + 7, column=1, pady=5)
        zipcode_box2.insert(0, result2[0][2])

        global country_box2
        country_box2 = Entry(search_customers)
        country_box2.grid(row=index + 8, column=1, pady=5)
        country_box2.insert(0, result2[0][10])

        global phone_box2
        phone_box2 = Entry(search_customers)
        phone_box2.grid(row=index + 9, column=1, pady=5)
        phone_box2.insert(0, result2[0][11])

        global email_box2
        email_box2 = Entry(search_customers)
        email_box2.grid(row=index + 10, column=1, pady=5)
        email_box2.insert(0, result2[0][5])

        global username_box2
        username_box2 = Entry(search_customers)
        username_box2.grid(row=index + 11, column=1, pady=5)
        username_box2.insert(0, result2[0][10])

        global payment_method_box2
        payment_method_box2 = Entry(search_customers)
        payment_method_box2.grid(row=index + 12, column=1, pady=5)
        payment_method_box2.insert(0, result2[0][12])

        global discount_code_box2
        discount_code_box2 = Entry(search_customers)
        discount_code_box2.grid(row=index + 13, column=1, pady=5)
        discount_code_box2.insert(0, result2[0][13])

        global price_paid_box2
        price_paid_box2 = Entry(search_customers)
        price_paid_box2.grid(row=index + 14, column=1, pady=5)
        price_paid_box2.insert(0, result2[0][3])

        global id_box2
        id_box2 = Entry(search_customers)
        id_box2.grid(row=index + 15, column=1, pady=5)
        id_box2.insert(0, id)

        global save_record
        save_record = Button(search_customers, text="Update Record", command=update)
        save_record.grid(row=index + 16, column=0, padx=10, pady=10)


    def searchNow():
        selected = drop.get()
        sql=""
        if selected == "Search by...":
            test = Label(search_customers, text="Hey! You forgot to pick a dropdown selection..")
            test.grid(row=2, column=0)
        elif selected == "Last Name":
            sql = "SELECT * FROM customers WHERE last_name=%s"
            # test = Label(search_customers, text="You picked Last Name..")
            # test.grid(row=2, column=0)
        elif selected == "Email Address":
            sql = "SELECT * FROM customers WHERE email=%s"
            # test = Label(search_customers, text="You picked Email Addresses...")
            # test.grid(row=2, column=0)
        elif selected == "Customer ID":
            sql = "SELECT * FROM customers WHERE user_id=%s"
            # test = Label(search_customers, text="You picked Customer ID...")
            # test.grid(row=2, column=0)

        searched = search_box.get()
        # sql = "SELECT * FROM customers WHERE last_name=%s"
        name = (searched,)
        result = my_cursor.execute(sql, name)
        result = my_cursor.fetchall()

        if not result:
            result = "Record not Found..."
            lookup_label = Label(search_customers, text=result)
            lookup_label.grid(row=3, column=0)
        else:
            for index, x in enumerate(result):
                num = 0
                index += 2
                id_reference = str(x[4])
                edit_button = Button(search_customers, text="Edit " + id_reference, command=lambda: editNow(id_reference,index))
                edit_button.grid(row=index,column=num)
                for y in x:
                    lookup_label = Label(search_customers, text=y)
                    lookup_label.grid(row=index, column=num+1)
                    num += 1
            csv_button = Button(search_customers, text="Save to excel", command=lambda: writeToCSV(result))
            csv_button.grid(row=index + 1, column=0)
        # searched_label = Label(search_customers, text=result)
        # searched_label.grid(row=4,column=0, padx=10, columnspan=2) 

    search_box = Entry(search_customers)
    search_box.grid(row=0, column=1, padx=10, pady=10)
    search_box_label = Label(search_customers, text="Search Customers: ")
    search_box_label.grid(row=0, column=0, padx=10, pady=10)

    search_button = Button(search_customers, text="Search Customers", command=searchNow, padx=5, pady=5)
    search_button.grid(row=1, column=0, padx=10, sticky=W)

    drop = ttk.Combobox(search_customers, value=["Search by...", "Last Name", "Email Address", "Customer ID"])
    drop.current(0)
    drop.grid(row=0, column=2)

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

list_customers_btn = Button(root, text="List Customers", command=listCustomers)
list_customers_btn.grid(row=16, column=0, padx=10, pady=10, sticky=W)

search_customers_btn = Button(root, text="Search/Edit Customers", command=searchCustomers)
search_customers_btn.grid(row=16, column=1, padx=10, pady=10, sticky=W)

mainloop();
