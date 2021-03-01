# Python tkinter tutorial

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Python GUI')

# widgets ---> labels, buttons, radio buttons     - tk, ttk
# Create Labels
# two ways to add label on window - pack, grid
# name_label = ttk.Label(window, text='Enter your name: ')
# name_label.pack()
name_label = ttk.Label(window, text='Enter your name: ')
name_label.grid(row=0, column=0, sticky=tk.W)

email_label = ttk.Label(window, text='Enter your email: ')
email_label.grid(row=1, column=0, sticky=tk.W)

age_label = ttk.Label(window, text='Enter your age: ')
age_label.grid(row=2, column=0, sticky=tk.W)

gender_label = ttk.Label(window, text='Select your gender: ')
gender_label.grid(row=3, column=0, sticky=tk.W)

# Create Entry Boxes
name_var = tk.StringVar()
name_entrybox = ttk.Entry(window, width=16, textvariable=name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()

email_var = tk.StringVar()
email_entrybox = ttk.Entry(window, width=16, textvariable=email_var)
email_entrybox.grid(row=1, column=1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(window, width=16, textvariable=age_var)
age_entrybox.grid(row=2, column=1)

# Create Combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(window, width=13, textvariable=gender_var, state='readonly')
gender_combobox['values'] = ('Male', 'Female', 'Other')
gender_combobox.current(0)              # sets the default value at index 0
gender_combobox.grid(row=3, column=1)

# Create Radiobutton
user_type = tk.StringVar()
radio_btn1 = ttk.Radiobutton(window, text='Student', value='Student', variable=user_type)        # jo value di hai wo variable ke andr chli jyegi jb ye radio button select huga
radio_btn1.grid(row=4, column=0)

radio_btn2 = ttk.Radiobutton(window, text='Teacher', value='Teacher', variable=user_type)
radio_btn2.grid(row=4, column=1)

# Create Checkbutton
checkbtn_var = tk.IntVar()
check_btn = ttk.Checkbutton(window, text='Check if you want to subscribe our newsletter', variable=checkbtn_var)      # 0 means unchecked, 1 means checked
check_btn.grid(row=5, columnspan=3)

# Create Button
def submit_button_action():
    name = name_var.get()
    email= email_var.get()
    age = age_var.get()
    gender = gender_var.get()
    usertype = user_type.get()
    checked = checkbtn_var.get()
    print(f'Name: {name}')
    print(f'Email: {email}')
    print(f'Age: {age}')
    print(f'Gender: {gender}')
    print(f'Type: {usertype}')
    print(f'Checked: {checked}')

    # Clear entry boxes
    name_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)

    # chnage color of label
    # name_label.configure(foreground='Blue')      # python mn kuc colors hain ab agy ye dekhein apna color kese add kr skte hain
    name_label.configure(foreground='#b388ff')

submit_button = ttk.Button(window, text='Submit', command=submit_button_action)
submit_button.grid(row=6, column=0)

window.mainloop()