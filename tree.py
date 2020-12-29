from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Learning Tkinter")
root.iconbitmap("./images/quality.ico")
root.geometry("500x500")

my_tree = ttk.Treeview(root)

# Define our columns
my_tree['columns'] = ("Name", "ID", "Favorite Pizza")

# Formate our columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=W, width=120)
my_tree.column("ID", anchor=CENTER, width=80)
my_tree.column("Favorite Pizza", anchor=W, width=120)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favorite Pizza", text="Favorite Pizza", anchor=W)

# Datas
data = [
    ["John1", 1, "Pepperroni"],
    ["John2", 2, "Pepperroni"],
    ["John3", 3, "Pepperroni"],
    ["John4", 4, "Pepperroni"]
]

count = 0
for record in data:
    my_tree.insert(parent='', index=END, iid=count, text="Parent", values=(record[0], record[1], record[2]))
    count += 1

# Add Data
# my_tree.insert(parent='', index=END, iid=0, text="Parent", values=("John", 1, "Peperroni"))
# my_tree.insert(parent='', index=END, iid=1, text="Parent", values=("Tass1", 2, "yuexuiqn1"))
# my_tree.insert(parent='', index=END, iid=2, text="Parent", values=("Tass2", 3, "yuexuiqn2"))
# my_tree.insert(parent='', index=END, iid=3, text="Parent", values=("Tass3", 4, "yuexuiqn3"))
# my_tree.insert(parent='', index=END, iid=4, text="Parent", values=("Tass4", 5, "yuexuiqn4"))
# my_tree.insert(parent='', index=END, iid=5, text="Parent", values=("Tass5", 6, "yuexuiqn5"))
my_tree.pack(pady=20)

# Add child
my_tree.insert(parent='', index=END, iid=6, text="Child", values=("Steve", 7, "wetryuio"))
my_tree.move('6', '0', '0')



root.mainloop();
