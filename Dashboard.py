from tkinter import *
from tkinter import ttk
import sqlite3

from matplotlib.figure import Figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

conn = sqlite3.connect('invetory.db')  # create a DB if there is not one
c = conn.cursor()
c.execute("SELECT product_name, price FROM products;")
product_labels = []
prices = []
records = c.fetchall()
for r in records:
    product_labels.append(r[0])
    prices.append(r[1])

size_of_groups=[12,11,3,30]
names=['groupA', 'groupB', 'groupC', 'groupD']

fig = Figure()
ax = fig.add_subplot(111)
ax.set(title='Inventory')
ax.pie(prices, radius=1, labels=product_labels, shadow=True)

circle=matplotlib.patches.Circle((0,0), 0.7, color='white')
ax.add_artist(circle)

def Dashboard(Tab):
    
    option_frame = ttk.Frame(Tab)
    option_frame.grid(row=5, column=7, padx=20, pady=(10, 0))
    w = Button(option_frame, text="Add Inventory Item")
    w.grid(row=9, column=9)

    chart1 = FigureCanvasTkAgg(fig,Tab)
    chart1.get_tk_widget().grid()