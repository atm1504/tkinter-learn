from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("700x700")

style = ttk.Style()
style.theme_use("default")
style.configure("TreeView",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3"
)
# Change selected color
style.map('Treeview',
	background=[('selected', 'blue')])

my_tree = ttk.Treeview(root)

# Define our columns
my_tree['columns'] = ("Name", "ID", "Favorite Pizza")

# Formate our columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=80)
my_tree.column("Favorite Pizza", anchor=W, width=140)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favorite Pizza", text="Favorite Pizza", anchor=W)

# Datas
data = [
	["John", 1, "Pepperoni"],
	["Mary", 2, "Cheese"],
	["Tim", 3, "Mushroom"],
	["Erin", 4, "Ham"],
	["Bob", 5, "Onion"],
	["Steve", 6, "Peppers"],
	["Tina", 7, "Cheese"],
	["Mark", 8, "Supreme"],
	["John", 1, "Pepperoni"],
	["Mary", 2, "Cheese"],
	["Tim", 3, "Mushroom"],
	["Erin", 4, "Ham"],
	["Bob", 5, "Onion"],
	["Steve", 6, "Peppers"],
	["Tina", 7, "Cheese"],
	["Mark", 8, "Supreme"],
	["John", 1, "Pepperoni"],
	["Mary", 2, "Cheese"],
	["Tim", 3, "Mushroom"],
	["Erin", 4, "Ham"],
	["Bob", 5, "Onion"],
	["Steve", 6, "Peppers"],
	["Tina", 7, "Cheese"],
	["Mark", 8, "Supreme"],
	["Ruth", 9, "Vegan"]
]

# data = [
# 	["John", 1, "Pepperoni"],
# 	["Mary", 2, "Cheese"],
# 	["Tim", 3, "Mushroom"],
# 	["Erin", 4, "Ham"],
# 	["Bob", 5, "Onion"],
# 	["Steve", 6, "Peppers"],
# 	["Tina", 7, "Cheese"],
# 	["Mark", 8, "Supreme"]
# ]

# Create striped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

global count
count = 0
for record in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index=END, iid=count, text="Parent", values=(record[0], record[1], record[2]), tags=("evenrow",))
    else:
        my_tree.insert(parent='', index=END, iid=count, text="Parent", values=(record[0], record[1], record[2]), tags=("oddrow",))
    count += 1

my_tree.pack(pady=20)

add_frame = Frame(root)
add_frame.pack(pady=20)

# Name label
nl = Label(add_frame, text="Name")
nl.grid(row=0, column=0)

# ID label
il = Label(add_frame, text="ID")
il.grid(row=0, column=1)

# Topping label
tl = Label(add_frame, text="Topping")
tl.grid(row=0, column=2)

# Entry boxes
name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

id_box = Entry(add_frame)
id_box.grid(row=1, column=1)

topping_box = Entry(add_frame)
topping_box.grid(row=1, column=2)

# Add child
# my_tree.insert(parent='', index=END, iid=6, text="Child", values=("Steve", 7, "wetryuio"))
# my_tree.move('6', '0', '0')

def add_record():
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    global count
    if count % 2 == 0:
        my_tree.insert(parent='', index=END, iid=count, text="Child", values=(name_box.get(), id_box.get(), topping_box.get()), tags=("evenrow",))
    else:
        my_tree.insert(parent='', index=END, iid=count, text="Child", values=(name_box.get(), id_box.get(), topping_box.get()), tags=("oddrow",))
    count += 1

    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)

def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)

def remove_one():
    rec = my_tree.selection()[0]
    my_tree.delete(rec)

def remove_many():
    records = my_tree.selection()
    for rec in records:
        my_tree.delete(rec)


# Add an item Buttons
add_record = Button(root, text="Add Record", command=add_record)
add_record.pack(pady=20)

# Remove all elements
remove_all = Button(root, text="Remove All", command=remove_all)
remove_all.pack(pady=10)

# Remove many elements
remove_many = Button(root, text="Remove Many Selected", command=remove_many)
remove_many.pack(pady=10)

# Remove one elements
remove_one = Button(root, text="Remove One", command=remove_one)
remove_one.pack(pady=10)

root.mainloop();
