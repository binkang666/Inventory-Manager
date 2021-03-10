from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
import dbCommandsPool

root = tk.Tk()
root.title('CECS 445 Inventory Manager by Yiang Shen')
root.geometry("1200x700")

conn = sqlite3.connect('Hiccups.db')  # create a DB if there is not one
c = conn.cursor()

'''
c.execute("SELECT * FROM products")
display1 = c.fetchall()
print(display1)
'''
global currentSelectedTable

# main option frame declare
mainOptionFrame = Frame(root)
mainOptionFrame.grid(row=0, column=1, padx=20, pady=(10, 0))
# All pop up window
global productAdd
global vendorAdd
global ordersAdd
global InventoryAdd
# Global tree tables


# Main screen Combo Drop down
mainList = ["Products", "Vendors", "Orders", "Inventory"]
mainComboDropdown = ttk.Combobox(mainOptionFrame, value=mainList)
mainComboDropdown.current(0)
mainComboDropdown.bind("<<ComboboxSelected>>")
# print(mainComboDropdown.get())
mainComboDropdown.grid(row=1, column=1, pady=1, padx=1)

# addDataComandList in main Screen
def addCommand():
    currentSelectedTable=mainComboDropdown.get()
    print("In ADD table " + currentSelectedTable)
    if(currentSelectedTable == "Products"):  # if dropdown selected table then
        print("Yes Products Add is selected")
        productsAddWindowPopup()
    elif(currentSelectedTable == "Vendors"):
        print("Yes Vendors Add is selected")
        vendorsAddWindowPopup()
    elif (currentSelectedTable == "Orders"):
        print("Yes Orders Add is selected")
        ordersAddWindowPopup()
    elif (currentSelectedTable == "Inventory"):
        print("Yes Inventory Add is selected")
        inventoryAddWindowPopup()

def treeRemove():
    currentSelectedTable = mainComboDropdown.get()
    if (currentSelectedTable !="Products"):
        try:
            display_Products_ContentTree.destroy()
        except:
            print("Tree not defined")
    if (currentSelectedTable !="Orders"):
        try:
            display_Orders_ContentTree.destroy()
        except:
            print("Tree not defined")
    if (currentSelectedTable !="Inventory"):
        try:
            display_Inventory_ContentTree.destroy()
        except:
            print("Tree not defined")

    if (currentSelectedTable !="Vendors"):
        try:
            display_Vendors_ContentTree.destroy()
        except:
            print("Tree not defined")

def displayCommand():
    currentSelectedTable = mainComboDropdown.get()
    print("In Display table " + currentSelectedTable)
    if (currentSelectedTable == "Products"):  # if dropdown selected table then
        print("Yes Products display is selected")
        treeRemove()
        displayProductsWindowSetUp()
        queryProducts()
    elif (currentSelectedTable == "Vendors"):
        print("Yes Vendors display is selected")
        treeRemove()
        displayVendorsWindowSetUp()
        queryVendors()
    elif (currentSelectedTable == "Orders"):
        print("Yes Orders display is selected")
        treeRemove()
        displayOrdersWindowSetUp()
        queryOrders()
    elif (currentSelectedTable == "Inventory"):
        print("Yes Inventory display is selected")
        treeRemove()
        displayInventoryWindowSetUp()
        queryInventory()

def queryProducts():
    conn = sqlite3.connect('Hiccups.db')
    c = conn.cursor()
    # Query DB
    c.execute("SELECT * FROM products")
    records = c.fetchall()

    for row in display_Products_ContentTree.get_children():
        display_Products_ContentTree.delete(row)

    for row in records:
        print(row)
        display_Products_ContentTree.insert("", tk.END, values=row)
    conn.commit()
    conn.close()

def queryVendors():
    conn = sqlite3.connect('Hiccups.db')
    c = conn.cursor()
    # Query DB
    c.execute("SELECT * FROM vendors")
    records = c.fetchall()

    for row in display_Vendors_ContentTree.get_children():
        display_Vendors_ContentTree.delete(row)

    for row in records:
        print(row)
        display_Vendors_ContentTree.insert("", tk.END, values=row)
    conn.commit()
    conn.close()

def queryOrders():
    conn = sqlite3.connect('Hiccups.db')
    c = conn.cursor()
    # Query DB
    c.execute("SELECT * FROM orders")
    records = c.fetchall()

    for row in display_Orders_ContentTree.get_children():
        display_Orders_ContentTree.delete(row)

    for row in records:
        print(row)
        display_Orders_ContentTree.insert("", tk.END, values=row)
    conn.commit()
    conn.close()

def queryInventory():
    conn = sqlite3.connect('Hiccups.db')
    c = conn.cursor()
    # Query DB
    c.execute("SELECT * FROM inventory")
    records = c.fetchall()

    for row in display_Inventory_ContentTree.get_children():
        display_Inventory_ContentTree.delete(row)

    for row in records:
        print(row)
        display_Inventory_ContentTree.insert("", tk.END, values=row)
    conn.commit()
    conn.close()
# Add item to product button function
def submitAddProduct():
    conn = sqlite3.connect('Hiccups.db')
    c = conn.cursor()

    c.execute("INSERT INTO products VALUES (:code, :desc,:vendor,:cata,:vendorF,:cataF)",
              {
                  'code': productbox1.get(),
                  'desc': productbox2.get(),
                  'vendor': productbox3.get(),
                  'cata': productbox4.get(),
                  'vendorF': productbox3.get(),
                  'cataF': productbox4.get(),
              })

    conn.commit()
    conn.close()

def submitAddVendor():
    conn = sqlite3.connect('Hiccups.db')
    c = conn.cursor()

    c.execute("INSERT INTO vendors VALUES (:name, :phone,:email,:address,:URL)",
              {
                  'name': vendorbox1.get(),
                  'phone': vendorbox2.get(),
                  'email': vendorbox3.get(),
                  'address': vendorbox4.get(),
                  'URL': vendorbox5.get(),
              })

    conn.commit()
    conn.close()
def submitAddOrder():
    conn = sqlite3.connect('Hiccups.db')
    c = conn.cursor()
    c.execute("INSERT INTO orders VALUES (:id, :date,:vendor)",
              {
                  'id': orderbox1.get(),
                  'date': orderbox2.get(),
                  'vendor': orderbox3.get(),
              })

    conn.commit()
    conn.close()

def submitAddInventory():
    conn = sqlite3.connect('Hiccups.db')
    c = conn.cursor()

    c.execute("INSERT INTO inventory VALUES (:unit, :quantity,:level,:code)",
              {
                  'unit': inventorybox1.get(),
                  'quantity': inventorybox2.get(),
                  'level': inventorybox3.get(),
                  'code': inventorybox4.get(),
              })

    conn.commit()
    conn.close()

def productsAddWindowPopup():
    productAdd = Tk()
    productAdd.title("Add data to product table")
    productAdd.geometry("400x250")
    conn = sqlite3.connect('Hiccups.db')
    c = conn.cursor()

    global productbox1
    productbox1 = Entry(productAdd, width=30)  # product Code
    productbox1.grid(row=2, column=1, padx=20, pady=(10, 0))
    global productbox2
    productbox2 = Entry(productAdd, width=30)  # product Desc
    productbox2.grid(row=3, column=1, padx=20, pady=(10, 0))
    global productbox3
    productbox3 = Entry(productAdd, width=30)  # vendor
    productbox3.grid(row=4, column=1, padx=20, pady=(10, 0))
    global productbox4
    productbox4 = Entry(productAdd, width=30)  # category
    productbox4.grid(row=5, column=1, padx=20, pady=(10, 0))
    # Create labels for display
    box1_label = Label(productAdd, text="Product Code")
    box1_label.grid(row=2, column=0, padx=20, pady=(10, 0))
    box2_label = Label(productAdd, text="Product Desc")
    box2_label.grid(row=3, column=0, padx=20)
    box3_label = Label(productAdd, text="Vendor")
    box3_label.grid(row=4, column=0, padx=20)
    box4_label = Label(productAdd, text="Category")
    box4_label.grid(row=5, column=0, padx=20)

    option_Add_btn = Button(productAdd, text="Add Product", command=submitAddProduct)
    option_Add_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=20, ipadx=100)

    conn.commit()
    conn.close()

def vendorsAddWindowPopup():
    vendorAdd = Tk()
    vendorAdd.title("Add New Vendor")
    vendorAdd.geometry("400x250")
    conn = sqlite3.connect('Hiccups.db')
    c = conn.cursor()

    global vendorbox1
    vendorbox1 = Entry(vendorAdd, width=30)  # product Code
    vendorbox1.grid(row=2, column=1, padx=20, pady=(10, 0))
    global vendorbox2
    vendorbox2 = Entry(vendorAdd, width=30)  # product Desc
    vendorbox2.grid(row=3, column=1, padx=20, pady=(10, 0))
    global vendorbox3
    vendorbox3 = Entry(vendorAdd, width=30)  # vendor
    vendorbox3.grid(row=4, column=1, padx=20, pady=(10, 0))
    global vendorbox4
    vendorbox4 = Entry(vendorAdd, width=30)  # category
    vendorbox4.grid(row=5, column=1, padx=20, pady=(10, 0))
    global vendorbox5
    vendorbox5 = Entry(vendorAdd, width=30)  # category
    vendorbox5.grid(row=6, column=1, padx=20, pady=(10, 0))
    # Create labels for display
    vendorbox1_label = Label(vendorAdd, text="Product Code")
    vendorbox1_label.grid(row=2, column=0, padx=20, pady=(10, 0))
    vendorbox2_label = Label(vendorAdd, text="Product Desc")
    vendorbox2_label.grid(row=3, column=0, padx=20)
    vendorbox3_label = Label(vendorAdd, text="Vendor")
    vendorbox3_label.grid(row=4, column=0, padx=20)
    vendorbox4_label = Label(vendorAdd, text="Category")
    vendorbox4_label.grid(row=5, column=0, padx=20)
    vendorbox5_label = Label(vendorAdd, text="Category")
    vendorbox5_label.grid(row=6, column=0, padx=20)

    option_Add_btn = Button(vendorAdd, text="Add Vendor info", command=submitAddVendor)
    option_Add_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=20, ipadx=100)

    conn.commit()
    conn.close()

def ordersAddWindowPopup():
    ordersAdd = Tk()
    ordersAdd.title("Add record to orders")
    ordersAdd.geometry("400x250")
    conn = sqlite3.connect('Hiccups.db')
    c = conn.cursor()

    global orderbox1
    orderbox1 = Entry(ordersAdd, width=30)  # product Code
    orderbox1.grid(row=2, column=1, padx=20, pady=(10, 0))
    global orderbox2
    orderbox2 = Entry(ordersAdd, width=30)  # product Desc
    orderbox2.grid(row=3, column=1, padx=20, pady=(10, 0))
    global orderbox3
    orderbox3 = Entry(ordersAdd, width=30)  # vendor
    orderbox3.grid(row=4, column=1, padx=20, pady=(10, 0))
    # Create labels for display
    orderbox1_label = Label(ordersAdd, text="Order ID")
    orderbox1_label.grid(row=2, column=0, padx=20, pady=(10, 0))
    orderbox2_label = Label(ordersAdd, text="Order Date")
    orderbox2_label.grid(row=3, column=0, padx=20)
    orderbox3_label = Label(ordersAdd, text="Vendor")
    orderbox3_label.grid(row=4, column=0, padx=20)

    option_Add_btn = Button(ordersAdd, text="Add record to Orders", command=submitAddOrder)
    option_Add_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=20, ipadx=100)

    conn.commit()
    conn.close()


def inventoryAddWindowPopup():
    inventoryAdd = Tk()
    inventoryAdd.title("Add record to Inventory")
    inventoryAdd.geometry("400x250")
    conn = sqlite3.connect('Hiccups.db')
    c = conn.cursor()

    global inventorybox1
    inventorybox1 = Entry(inventoryAdd, width=30)  # product Code
    inventorybox1.grid(row=2, column=1, padx=20, pady=(10, 0))
    global inventorybox2
    inventorybox2 = Entry(inventoryAdd, width=30)  # product Desc
    inventorybox2.grid(row=3, column=1, padx=20, pady=(10, 0))
    global inventorybox3
    inventorybox3 = Entry(inventoryAdd, width=30)  # vender
    inventorybox3.grid(row=4, column=1, padx=20, pady=(10, 0))
    global inventorybox4
    inventorybox4 = Entry(inventoryAdd, width=30)  # vender
    inventorybox4.grid(row=5, column=1, padx=20, pady=(10, 0))
    # Create labels for display
    inventorybox1_label = Label(inventoryAdd, text="Unit In Stock")
    inventorybox1_label.grid(row=2, column=0, padx=20, pady=(10, 0))
    inventorybox2_label = Label(inventoryAdd, text="Reorder Quantity")
    inventorybox2_label.grid(row=3, column=0, padx=20)
    inventorybox3_label = Label(inventoryAdd, text="Reorder Level")
    inventorybox3_label.grid(row=4, column=0, padx=20)
    inventorybox4_label = Label(inventoryAdd, text="Product Code")
    inventorybox4_label.grid(row=5, column=0, padx=20)

    option_Add_btn = Button(inventoryAdd, text="Add to Inventory", command=submitAddInventory)
    option_Add_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=20, ipadx=100)

    conn.commit()
    conn.close()

def displayProductsWindowSetUp():
    global display_Products_ContentTree
    display_Products_ContentTree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings')
    display_Products_ContentTree.column("#1", width=250, minwidth=150, anchor=tk.W)
    display_Products_ContentTree.heading("#1", text="Product Code")
    display_Products_ContentTree.column("#2", width=180, minwidth=80, anchor=tk.CENTER)
    display_Products_ContentTree.heading("#2", text="Product Desc")
    display_Products_ContentTree.column("#3", width=140, minwidth=100, anchor=tk.CENTER)
    display_Products_ContentTree.heading("#3", text="Vendor")
    display_Products_ContentTree.column("#4", width=140, minwidth=100, anchor=tk.CENTER)
    display_Products_ContentTree.heading("#4", text="Category")

    display_Products_ContentTree.grid(row=0, column=0, padx=50, pady=20)

def displayVendorsWindowSetUp():
    global display_Vendors_ContentTree
    display_Vendors_ContentTree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5"), show='headings')
    display_Vendors_ContentTree.column("#1", width=100, minwidth=100, anchor=tk.W)
    display_Vendors_ContentTree.heading("#1", text="Vendor Name")
    display_Vendors_ContentTree.column("#2", width=150, minwidth=100, anchor=tk.CENTER)
    display_Vendors_ContentTree.heading("#2", text="Phone Number")
    display_Vendors_ContentTree.column("#3", width=180, minwidth=100, anchor=tk.CENTER)
    display_Vendors_ContentTree.heading("#3", text="Email")
    display_Vendors_ContentTree.column("#4", width=180, minwidth=100, anchor=tk.CENTER)
    display_Vendors_ContentTree.heading("#4", text="Address")
    display_Vendors_ContentTree.column("#5", width=200, minwidth=100, anchor=tk.CENTER)
    display_Vendors_ContentTree.heading("#5", text="Web URL")

    display_Vendors_ContentTree.grid(row=0, column=0, padx=50, pady=20)


def displayOrdersWindowSetUp():
    global display_Orders_ContentTree
    display_Orders_ContentTree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')
    display_Orders_ContentTree.column("#1", width=250, minwidth=150, anchor=tk.W)
    display_Orders_ContentTree.heading("#1", text="order ID")
    display_Orders_ContentTree.column("#2", width=180, minwidth=80, anchor=tk.CENTER)
    display_Orders_ContentTree.heading("#2", text="Order Date")
    display_Orders_ContentTree.column("#3", width=140, minwidth=100, anchor=tk.CENTER)
    display_Orders_ContentTree.heading("#3", text="Vendor")
    '''display_Orders_ContentTree.column("#4", width=140, minwidth=100, anchor=tk.CENTER)
    display_Orders_ContentTree.heading("#4", text="Price")'''

    display_Orders_ContentTree.grid(row=0, column=0, padx=50, pady=20)

def displayInventoryWindowSetUp():
    global display_Inventory_ContentTree
    display_Inventory_ContentTree = ttk.Treeview(root, column=("c1", "c2", "c3","c4"), show='headings')
    display_Inventory_ContentTree.column("#1", width=250, minwidth=150, anchor=tk.W)
    display_Inventory_ContentTree.heading("#1", text="Units in stock")
    display_Inventory_ContentTree.column("#2", width=180, minwidth=80, anchor=tk.CENTER)
    display_Inventory_ContentTree.heading("#2", text="Reorder Quantity")
    display_Inventory_ContentTree.column("#3", width=140, minwidth=100, anchor=tk.CENTER)
    display_Inventory_ContentTree.heading("#3", text="Reorder Level")
    display_Inventory_ContentTree.column("#4", width=140, minwidth=100, anchor=tk.CENTER)
    display_Inventory_ContentTree.heading("#4", text="Product Code")
    display_Inventory_ContentTree.grid(row=0, column=0, padx=50, pady=20)


# Main Screen Labels
main_table_label = Label(mainOptionFrame,text="Choose Table")
main_table_label.grid(row=1, column=0, pady=10, padx=1)

# Insert data button in Main screen
main_insert_button = Button(mainOptionFrame, text="Add Data", command=addCommand)
main_insert_button.grid(row=2, column=0, columnspan=2, pady=10, padx=1, ipadx=95)
# Display table button in Main screen
main_select_display = Button(mainOptionFrame, text="Display", command=displayCommand)
main_select_display.grid(row=3, column=0, columnspan=2, pady=10, padx=1, ipadx=103)

# Initial display products
displayProductsWindowSetUp()
queryProducts()

# Commit our command
conn.commit()

# Close our connection
conn.close()

root.mainloop()
