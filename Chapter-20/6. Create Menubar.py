import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Menubar')

# ******************************* simple menu bar ***********************
# def save():
#     print('Save Clicked')
# menubar = tk.Menu(window)
# menubar.add_command(label='Save', command=save)
# menubar.add_command(label='Save As', command=save)
# menubar.add_command(label='Copy', command=save)
# menubar.add_command(label='Paste', command=save)
# window.config(menu=menubar)

def func():
    print('Clicked')
main_menu = tk.Menu(window)
file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label='New File', command=func)
file_menu.add_command(label='New Window', command=func)
file_menu.add_separator()
file_menu.add_command(label='Save File', command=func)

edit_menu = tk.Menu(main_menu, tearoff=0)
edit_menu.add_command(label='Undo', command=func)
edit_menu.add_command(label='Redo', command=func)

main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='Edit', menu=edit_menu)

window.config(menu=main_menu)

window.mainloop()