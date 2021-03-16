from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
import dbCommandsPool

root = tk.Tk()
root.title('CECS 445 Inventory Manager by Yiang Shen')
root.geometry("1400x700")

conn = sqlite3.connect('Hiccups.db')  # create a DB if there is not one
c = conn.cursor()
c.execute("Delete from products where prodCode = 'Potato' ")
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
global vendorPriceAdd
# Global tree tables


# Main screen Tables Combo Drop down
mainList = ["Products", "Vendors", "Orders", "Vendor Price"]
mainComboDropdown = ttk.Combobox(mainOptionFrame, value=mainList)
mainComboDropdown.current(0)
mainComboDropdown.bind("<<ComboboxSelected>>")
# print(mainComboDropdown.get())
mainComboDropdown.grid(row=1, column=1, pady=1, padx=1)

# Main Screen sort-By Combo drop down
mainSortList = ["Price: Low to High", "Price: High to Low", "Alphabetical", "Newest"]
mainSortComboDropdown = ttk.Combobox(mainOptionFrame, value=mainSortList)
mainSortComboDropdown.current(0)
mainSortComboDropdown.bind("<<ComboboxSelected>>")
# print(mainComboDropdown.get())
mainSortComboDropdown.grid(row=6, column=1, pady=1, padx=1)

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
    elif (currentSelectedTable == "Vendor Price"):
        print("Yes Vendor Price Add is selected")
        vendorPricesAddWindowPopup()

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
    if (currentSelectedTable !="Vendor Price"):
        try:
            display_VendorPrices_ContentTree.destroy()
        except:
            print("Tree not defined")

    if (currentSelectedTable !="Vendors"):
        try:
            display_Vendors_ContentTree.destroy()
        except:
            print("Tree not defined")

def editCommand():
    currentSelectedTable = mainComboDropdown.get()
    print("In Edit table " + currentSelectedTable)
    if (currentSelectedTable == 'Products'):
        print("Product tuple is selected")
        editWindowPopup()
        updateProducts()
    # if table is balabala, then XXXX_EditWindowPopup()

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
    elif (currentSelectedTable == "Vendor Price"):
        print("Yes Vendor Price display is selected")
        treeRemove()
        displayVendorPricesWindowSetUp()
        queryVendorPrices()


def sortCommand(): ####################### Comand list for sort in certain type ################################
    return 0


def avgGetterCommand(): ####################### Comand list for get average price form vendors ################################
    return 0

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

def queryVendorPrices():
    conn = sqlite3.connect('Hiccups.db')
    c = conn.cursor()
    # Query DB
    c.execute("SELECT * FROM vendorPrices")
    records = c.fetchall()

    for row in display_VendorPrices_ContentTree.get_children():
        display_VendorPrices_ContentTree.delete(row)

    for row in records:
        print(row)
        display_VendorPrices_ContentTree.insert("", tk.END, values=row)
    conn.commit()
    conn.close()
# Add item to product button function
def submitAddProduct():
    conn = sqlite3.connect('Hiccups.db')
    c = conn.cursor()

    c.execute("INSERT INTO products VALUES (:code, :desc,:unitIn,:reQuantity,:reLevel,:cata)",
              {
                  'code': productbox1.get(),
                  'desc': productbox2.get(),
                  'unitIn': productbox3.get(),
                  'reQuantity': productbox4.get(),
                  'reLevel': productbox5.get(),
                  'cata': productbox6.get(),
              })
    # Clear the text box
    productbox1.delete(0, END)
    productbox2.delete(0, END)
    productbox3.delete(0, END)
    productbox4.delete(0, END)
    productbox5.delete(0, END)
    productbox6.delete(0, END)

    conn.commit()
    conn.close()
    displayCommand()

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
    # Clear the text box
    vendorbox1.delete(0, END)
    vendorbox2.delete(0, END)
    vendorbox3.delete(0, END)
    vendorbox4.delete(0, END)
    vendorbox5.delete(0, END)
    conn.commit()
    conn.close()
    displayCommand()

def updateProducts():
    try:
        conn = sqlite3.connect('Hiccups.db')
        c = conn.cursor()
        c.execute('''UPDATE products
                 SET prodDesc = :name,
                     unitsInStock = :stock,
                     reorderQuantity = :quantity,
                     reorderLevel = :level,
                     category = :cate
                 WHERE prodCode = :code''',
               {
                   'code': 'Broccoli',
                   'name': product_Desc_editor.get(),
                   'stock': stock_editor.get(),
                   'quantity': quantity_editor.get(),
                   'level': level_editor.get(),
                   'cate': cate_editor.get(),
               })
        queryP()
        conn.commit()
        product_Desc_editor.delete(0, END)
        stock_editor.delete(0, END)
        quantity_editor.delete(0, END)
        level_editor.delete(0, END)
        cate_editor.delete(0, END)
        c.close()
        displayCommand()
    except sqlite3.Error as e:
        print("Failed to update", e)

def queryP():
        conn = sqlite3.connect('Hiccups.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM products")
        records = c.fetchall()
        for row in display_Products_ContentTree.get_children():
            display_Products_ContentTree.delete(row)
        for row in records:
            display_Products_ContentTree.insert("", tk.END, values=row)
        conn.commit()
        conn.close()

def editWindowPopup():
    editor = Tk()
    editor.title("Update data to the tuple")
    editor.geometry("400x250")
    conn = sqlite3.connect('Hiccups.db')
    c = conn.cursor()

    global product_Desc_editor
    global stock_editor
    global quantity_editor
    global level_editor
    global cate_editor

    product_Desc_editor = Entry(editor, width=30)
    product_Desc_editor.grid(row=2, column=1, padx=20, pady=(10, 0))
    stock_editor = Entry(editor, width=30)
    stock_editor.grid(row=3, column=1)
    quantity_editor = Entry(editor, width=30)
    quantity_editor.grid(row=4, column=1)
    level_editor = Entry(editor, width=30)
    level_editor.grid(row=5, column=1)
    cate_editor = Entry(editor, width=30)
    cate_editor.grid(row=6, column=1)

    box2_label = Label(editor, text="Product Desc")
    box2_label.grid(row=2, column=0, padx=20)
    box3_label = Label(editor, text="Units In Stock")
    box3_label.grid(row=3, column=0, padx=20)
    box4_label = Label(editor, text="Reorder Quantity")
    box4_label.grid(row=4, column=0, padx=20)
    box3_label = Label(editor, text="Reorder Level")
    box3_label.grid(row=5, column=0, padx=20)
    box4_label = Label(editor, text="Category")
    box4_label.grid(row=6, column=0, padx=20)
    save_btn = Button(editor, text="Edit Product", command=updateProducts)
    save_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=20, ipadx=100)

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
    # Clear the text box
    orderbox1.delete(0, END)
    orderbox2.delete(0, END)
    orderbox3.delete(0, END)

    conn.commit()
    conn.close()
    displayCommand()

def submitAddVendorPrices():
    conn = sqlite3.connect('Hiccups.db')
    c = conn.cursor()

    c.execute("INSERT INTO vendorPrices VALUES (:price, :vendor,:product,:unitPrice, :timecheck)",
              {
                  'price': vendorPricebox1.get(),
                  'vendor': vendorPricebox2.get(),
                  'product': vendorPricebox3.get(),
                  'unitPrice': vendorPricebox4.get(),
                  'timecheck': vendorPricebox5.get(),
              })
    vendorPricebox1.delete(0, END)
    vendorPricebox2.delete(0, END)
    vendorPricebox3.delete(0, END)
    vendorPricebox4.delete(0, END)
    vendorPricebox5.delete(0, END)

    conn.commit()
    conn.close()
    displayCommand()

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
    productbox3 = Entry(productAdd, width=30)
    productbox3.grid(row=4, column=1, padx=20, pady=(10, 0))
    global productbox4
    productbox4 = Entry(productAdd, width=30)
    productbox4.grid(row=5, column=1, padx=20, pady=(10, 0))
    global productbox5
    productbox5 = Entry(productAdd, width=30)
    productbox5.grid(row=6, column=1, padx=20, pady=(10, 0))
    global productbox6
    productbox6 = Entry(productAdd, width=30)
    productbox6.grid(row=7, column=1, padx=20, pady=(10, 0))
    # Create labels for display
    box1_label = Label(productAdd, text="Product Code")
    box1_label.grid(row=2, column=0, padx=20, pady=(10, 0))
    box2_label = Label(productAdd, text="Product Desc")
    box2_label.grid(row=3, column=0, padx=20)
    box3_label = Label(productAdd, text="Units In Stock")
    box3_label.grid(row=4, column=0, padx=20)
    box4_label = Label(productAdd, text="Reorder Quantity")
    box4_label.grid(row=5, column=0, padx=20)
    box3_label = Label(productAdd, text="Reorder Level")
    box3_label.grid(row=6, column=0, padx=20)
    box4_label = Label(productAdd, text="Category")
    box4_label.grid(row=7, column=0, padx=20)
    option_Add_btn = Button(productAdd, text="Add Product", command=submitAddProduct)
    option_Add_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=20, ipadx=100)

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


def vendorPricesAddWindowPopup():
    vendorPriceAdd = Tk()
    vendorPriceAdd.title("Add record to VendorPrice")
    vendorPriceAdd.geometry("400x250")
    conn = sqlite3.connect('Hiccups.db')
    c = conn.cursor()

    global vendorPricebox1
    vendorPricebox1 = Entry(vendorPriceAdd, width=30)  # product Code
    vendorPricebox1.grid(row=2, column=1, padx=20, pady=(10, 0))
    global vendorPricebox2
    vendorPricebox2 = Entry(vendorPriceAdd, width=30)  # product Desc
    vendorPricebox2.grid(row=3, column=1, padx=20, pady=(10, 0))
    global vendorPricebox3
    vendorPricebox3 = Entry(vendorPriceAdd, width=30)  # vender
    vendorPricebox3.grid(row=4, column=1, padx=20, pady=(10, 0))
    global vendorPricebox4
    vendorPricebox4 = Entry(vendorPriceAdd, width=30)  # vender
    vendorPricebox4.grid(row=5, column=1, padx=20, pady=(10, 0))
    global vendorPricebox5
    vendorPricebox5 = Entry(vendorPriceAdd, width=30)  # vender
    vendorPricebox5.grid(row=6, column=1, padx=20, pady=(10, 0))
    # Create labels for display
    vendorPricebox1_label = Label(vendorPriceAdd, text="Unit In Stock")
    vendorPricebox1_label.grid(row=2, column=0, padx=20, pady=(10, 0))
    vendorPricebox2_label = Label(vendorPriceAdd, text="Reorder Quantity")
    vendorPricebox2_label.grid(row=3, column=0, padx=20)
    vendorPricebox3_label = Label(vendorPriceAdd, text="Reorder Level")
    vendorPricebox3_label.grid(row=4, column=0, padx=20)
    vendorPricebox4_label = Label(vendorPriceAdd, text="Product Code")
    vendorPricebox4_label.grid(row=5, column=0, padx=20)
    vendorPricebox5_label = Label(vendorPriceAdd, text="Product Code")
    vendorPricebox5_label.grid(row=6, column=0, padx=20)

    option_Add_btn = Button(vendorPriceAdd, text="Add to Vendor Price List", command=submitAddVendorPrices)
    option_Add_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=20, ipadx=100)

    conn.commit()
    conn.close()

def displayProductsWindowSetUp():
    global display_Products_ContentTree
    display_Products_ContentTree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings')
    display_Products_ContentTree.column("#1", width=150, minwidth=100, anchor=tk.CENTER)
    display_Products_ContentTree.heading("#1", text="Product Code")
    display_Products_ContentTree.column("#2", width=250, minwidth=150, anchor=tk.CENTER)
    display_Products_ContentTree.heading("#2", text="Product Desc")
    display_Products_ContentTree.column("#3", width=120, minwidth=100, anchor=tk.CENTER)
    display_Products_ContentTree.heading("#3", text="Unit In Stock")
    display_Products_ContentTree.column("#4", width=120, minwidth=100, anchor=tk.CENTER)
    display_Products_ContentTree.heading("#4", text="Reorder Quantity")
    display_Products_ContentTree.column("#5", width=120, minwidth=100, anchor=tk.CENTER)
    display_Products_ContentTree.heading("#5", text="Reorder Level")
    display_Products_ContentTree.column("#6", width=120, minwidth=100, anchor=tk.CENTER)
    display_Products_ContentTree.heading("#6", text="Category")

    display_Products_ContentTree.grid(row=0, column=0, padx=50, pady=20)
    root.geometry("1320x400")

def displayVendorsWindowSetUp():
    global display_Vendors_ContentTree
    display_Vendors_ContentTree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5"), show='headings')
    display_Vendors_ContentTree.column("#1", width=180, minwidth=100, anchor=tk.W)
    display_Vendors_ContentTree.heading("#1", text="Vendor Name")
    display_Vendors_ContentTree.column("#2", width=180, minwidth=100, anchor=tk.CENTER)
    display_Vendors_ContentTree.heading("#2", text="Phone Number")
    display_Vendors_ContentTree.column("#3", width=200, minwidth=100, anchor=tk.CENTER)
    display_Vendors_ContentTree.heading("#3", text="Email")
    display_Vendors_ContentTree.column("#4", width=200, minwidth=100, anchor=tk.CENTER)
    display_Vendors_ContentTree.heading("#4", text="Address")
    display_Vendors_ContentTree.column("#5", width=200, minwidth=100, anchor=tk.CENTER)
    display_Vendors_ContentTree.heading("#5", text="Web URL")

    display_Vendors_ContentTree.grid(row=0, column=0, padx=50, pady=20)
    root.geometry("1400x400")

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
    root.geometry("1000x400")

def displayVendorPricesWindowSetUp():
    global display_VendorPrices_ContentTree
    display_VendorPrices_ContentTree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5"), show='headings')
    display_VendorPrices_ContentTree.column("#1", width=250, minwidth=150, anchor=tk.W)
    display_VendorPrices_ContentTree.heading("#1", text="Vendor Price ID")
    display_VendorPrices_ContentTree.column("#2", width=180, minwidth=80, anchor=tk.CENTER)
    display_VendorPrices_ContentTree.heading("#2", text="Vendor")
    display_VendorPrices_ContentTree.column("#3", width=140, minwidth=100, anchor=tk.CENTER)
    display_VendorPrices_ContentTree.heading("#3", text="Product")
    display_VendorPrices_ContentTree.column("#4", width=140, minwidth=100, anchor=tk.CENTER)
    display_VendorPrices_ContentTree.heading("#4", text="Unit List Price")
    display_VendorPrices_ContentTree.column("#5", width=140, minwidth=100, anchor=tk.CENTER)
    display_VendorPrices_ContentTree.heading("#5", text="Time Checked")

    display_VendorPrices_ContentTree.grid(row=0, column=0, padx=50, pady=20)
    root.geometry("1300x400")

# Main Screen Labels
main_table_select_label = Label(mainOptionFrame, text="Choose Table")
main_table_select_label.grid(row=1, column=0, pady=10, padx=1)
main_sortBy_label = Label(mainOptionFrame, text="Sort by")
main_sortBy_label.grid(row=6, column=0)
# Insert data button in Main screen
main_insert_button = Button(mainOptionFrame, text="Add Data", command=addCommand)
main_insert_button.grid(row=2, column=0, columnspan=2, pady=10, padx=1, ipadx=95)
# Display table button in Main screen
main_select_display = Button(mainOptionFrame, text="Display", command=displayCommand)
main_select_display.grid(row=3, column=0, columnspan=2, pady=10, padx=1, ipadx=103)
# Edit button in Main Screen
main_edit_button = Button(mainOptionFrame, text="Edit Highlighted", command=editCommand)
main_edit_button.grid(row=5, column=0, columnspan=2, pady=10, padx=1, ipadx=78)
# Sort button in Main Screen
main_sort_button = Button(mainOptionFrame, text="Sort", command=sortCommand)
main_sort_button.grid(row=7, column=0, columnspan=2, pady=10, padx=1, ipadx=112) # row 6 is left for drop down
# Average Getter button
main_avgGetter_button = Button(mainOptionFrame, text="Calculate Average", command=avgGetterCommand)
main_avgGetter_button.grid(row=8, column=0, columnspan=2, pady=10, padx=1, ipadx=72)


# Initial display products
displayProductsWindowSetUp()
queryProducts()

# Commit our command
conn.commit()

# Close our connection
conn.close()

root.mainloop()
