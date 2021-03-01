import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Label Frame')

label_frame = ttk.LabelFrame(window, text='Enter your details below')
label_frame.grid(row=0, column=0, padx=20, pady=0)

labels = ['Name: ', 'Age: ', 'Gender: ', 'State: ', 'City: ', 'Country: ']

for i in range(len(labels)):
    label = ttk.Label(label_frame, text=labels[i])
    label.grid(row=i, column=0, sticky=tk.W, padx=2, pady=2)

user_info = {
    'name': tk.StringVar(),
    'age': tk.StringVar(),
    'gender': tk.StringVar() ,
    'state': tk.StringVar(),
    'city': tk.StringVar(),
    'country': tk.StringVar(),
}

counter=0
for key in user_info:
    entry_box = ttk.Entry(label_frame, width=16, textvariable=user_info[key])
    entry_box.grid(row=counter, column=1, padx=2, pady=2)
    counter+=1

def submit_action():
    for key, value in user_info.items():
        print(f'{key} : {value.get()}')

submit_btn = ttk.Button(window, text='Submit', command=submit_action)
submit_btn.grid(row=1, columnspan=2)

for child in label_frame.winfo_children():
    child.grid_configure(padx=4, pady=4)       # second way to add padding to all widgets inside label_frame

window.mainloop()