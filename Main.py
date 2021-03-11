from New_UI import NewerVersion
from Dashboard import Dashboard
from sqlite3.dbapi2 import DatabaseError
from Inventory import InventoryTab

import tkinter as tk                     
from tkinter import ttk 
  
  
root = tk.Tk() 
root.geometry("900x600")
root.title("Tab Widget") 
tabControl = ttk.Notebook(root) 
  
tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 
tab3 = ttk.Frame(tabControl)
  
tabControl.add(tab1, text ='Inventory') 
tabControl.add(tab2, text ='Dashboard') 
tabControl.add(tab3, text = 'Invent_V2')
tabControl.grid(row= 0, column=0) 
  
InventoryTab(tab1) 
Dashboard(tab2)
NewerVersion(tab3)

root.mainloop()