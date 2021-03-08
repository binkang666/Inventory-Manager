from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
import dbCommandsPool

root = tk.Tk()
root.title('CECS 445 Inventory Manager by Yiang Shen')
root.geometry("900x700")

conn = sqlite3.connect('Hiccups.db') # create a DB if there is not one
c = conn.cursor()


def query():
    conn = sqlite3.connect('Hiccups.db')
    c = conn.cursor()
    # Query DB
    c.execute("SELECT * FROM products")
    records = c.fetchall()

    for row in displayContentTree.get_children():
        displayContentTree.delete(row)

    for row in records:
        print(row)
        displayContentTree.insert("", tk.END, values=row)
    conn.commit()
    conn.close()


# Add item to product button function
def addProduct():
    conn = sqlite3.connect('Hiccups.db')
    c = conn.cursor()

    c.execute("INSERT INTO products VALUES (:code, :desc,:vendor,:cata)",
              {
                  'code': box1.get(),
                  'desc': box2.get(),
                  'vendor': box3.get(),
                  'cata': box4.get(),
              })

    conn.commit()
    conn.close()

# This option is for products from now
def optionSetUp():
    option_Frame = Frame(root)
    option_Frame.grid(row=1, column=0, padx=20, pady=(10, 0))
    # Create text boxes for products
    global box1
    box1 = Entry(option_Frame, width=30) # product Code
    box1.grid(row=1, column=1, padx=20, pady=(10, 0))
    global box2
    box2 = Entry(option_Frame, width=30)  # product Desc
    box2.grid(row=2, column=1, padx=20, pady=(10, 0))
    global box3
    box3 = Entry(option_Frame, width=30)  # vender
    box3.grid(row=3, column=1, padx=20, pady=(10, 0))
    global box4
    box4 = Entry(option_Frame, width=30)  # category
    box4.grid(row=4, column=1, padx=20, pady=(10, 0))
    # Create labels for display
    box1_label = Label(option_Frame, text="Product Code")
    box1_label.grid(row=1, column=0, pady=(10, 0))
    box2_label = Label(option_Frame, text="Product Desc")
    box2_label.grid(row=2, column=0)
    box3_label = Label(option_Frame, text="Vendor")
    box3_label.grid(row=3, column=0)
    box4_label = Label(option_Frame, text="Category")
    box4_label.grid(row=4, column=0)

    option_Add_btn = Button(option_Frame, text="Add Item to Products", command=addProduct)
    option_Add_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=1, ipadx=100)




def displayWindowSetUp():
    global displayContentTree
    displayContentTree= ttk.Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings')
    displayContentTree.column("#1", width=250, minwidth=150, anchor=tk.W)
    displayContentTree.heading("#1", text="Product Code")
    displayContentTree.column("#2", width=180, minwidth=80, anchor=tk.CENTER)
    displayContentTree.heading("#2", text="Product Desc")
    displayContentTree.column("#3", width=140, minwidth=100, anchor=tk.CENTER)
    displayContentTree.heading("#3", text="Vendor")
    displayContentTree.column("#4", width=140, minwidth=100, anchor=tk.CENTER)
    displayContentTree.heading("#4", text="Category")
    displayContentTree.grid(row=0, column=0, padx=50, pady=20)



optionSetUp()
displayWindowSetUp()
query()
# Commit our command
conn.commit()

# Close our connection
conn.close()

root.mainloop()
