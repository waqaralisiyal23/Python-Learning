# Notebook -- contain two pages
# page1 -- widgets
# page2 -- widgets

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Tabbed Control Widget')

notebook = ttk.Notebook(window)

page1 = ttk.Frame(notebook)
page2 = ttk.Frame(notebook)

notebook.add(page1, text='One')
notebook.add(page2, text='Two')
# notebook.grid(row=0, column=0)
notebook.pack(expand=True, fill='both')    # expand jo hai wo expand krega or both mtlb horizontally bhi vertically bhi

label1 = ttk.Label(page1, text='This is label : ')
label1.grid(row=0, column=0)

entry1 = ttk.Entry(page1, width=26)
entry1.grid(row=0, column=1)

label2 = ttk.Label(page2, text='This is label : ')
label2.grid(row=0, column=0)

window.mainloop()