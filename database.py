from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("800x800")

# database

# # create a database or connect to one
# conn = sqlite3.connect("address_book.db")

# # Create Cursor
# c = conn.cursor()

def submit():
    # create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create Cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name , :address, :city, :state, :zipcode)",
    {
        'f_name': f_name.get(),
        'l_name': l_name.get(),
        'address': address.get(),
        'city': city.get(),
        'state': state.get(),
        'zipcode': zipcode.get()
    })

    # Commit changes
    conn.commit()
    # Close Connection
    conn.close()

    # Clear the Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    # create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create Cursor
    c = conn.cursor()

    c.execute("SELECT *, oid from addresses ")
    records = c.fetchall();

    all_records = ""
    for rec in records:
        all_records += str(rec[0]) + " " + str(rec[1]) + " " + str(rec[6]) + "\n"

    show_label = Label(root, text=all_records)
    show_label.grid(row=20, column=0, columnspan=3)

    # Commit changes
    conn.commit()
    # Close Connection
    conn.close()

# Delete record
def delete():
    conn = sqlite3.connect("address_book.db")
    # Create Cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from addresses WHERE oid=" + delete_box.get())

    # Commit changes
    conn.commit()
    # Close Connection
    conn.close()

def update(ids):
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    global editor

    conn = sqlite3.connect("address_book.db")
    # Create Cursor
    c = conn.cursor()

    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        WHERE oid= :oid """,
        {
            'first': f_name_editor.get(),
            'last': l_name_editor.get(),
            'address': address_editor.get(),
            'city': city_editor.get(),
            'state': state_editor.get(),
            'zipcode': zipcode_editor.get(),
            'oid': ids
        }
    );

    # Commit changes
    conn.commit()
    # Close Connection
    conn.close()
    editor.destroy()


# A function to update record
def edit():
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    global editor

    record_id = select_box.get()
    conn = sqlite3.connect("address_book.db")
    # Create Cursor
    c = conn.cursor()

    c.execute("SELECT * from addresses where oid= " + record_id)
    records = c.fetchall();

    # Decorate
    editor = Tk()
    editor.title("Update Database")
    editor.iconbitmap("./images/quality.ico")
    editor.geometry("800x800")

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10,0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    f_name_label_editor = Label(editor, text="First Name: ")
    f_name_label_editor.grid(row=0, column=0, pady=(10,0))
    l_name_label_editor = Label(editor, text="Last Name: ")
    l_name_label_editor.grid(row=1, column=0)
    address_label_editor = Label(editor, text="Address: ")
    address_label_editor.grid(row=2, column=0)
    city_label_editor = Label(editor, text="City: ")
    city_label_editor.grid(row=3, column=0)
    state_label_editor = Label(editor, text="State: ")
    state_label_editor.grid(row=4, column=0)
    zipcode_label_editor = Label(editor, text="Zipcode: ")
    zipcode_label_editor.grid(row=5, column=0)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Commit changes
    conn.commit()
    # Close Connection
    conn.close()

    submit_btn_editor = Button(editor, text="Save Edited Record", command=lambda: update(record_id))
    submit_btn_editor.grid(row=6, column=0, columnspan=2, padx=10, ipadx=100)

# create table
# c.execute("""
# CREATE TABLE addresses (
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer
#     )
# """)

# Take input
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)


# Box for deleting
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

select_box = Entry(root, width=30)
select_box.grid(row=11, column=1)

# Create text box labels
f_name_label = Label(root, text="First Name: ")
f_name_label.grid(row=0, column=0, pady=(10,0))

l_name_label = Label(root, text="Last Name: ")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address: ")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City: ")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State: ")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode: ")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Delete ID: # ")
delete_box_label.grid(row=9, column=0)

select_box_label = Label(root, text="Select ID: # ")
select_box_label.grid(row=11, column=0)

# Create Submit Button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, ipadx=100)

# Create Query Button
query_btn = Button(root, text="Show Record from Database", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# Create a delete button
delete_btn = Button(root, text="Delete from Database", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# Create a Update button
update_btn = Button(root, text="Update Database", command=edit)
update_btn.grid(row=14, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

mainloop();