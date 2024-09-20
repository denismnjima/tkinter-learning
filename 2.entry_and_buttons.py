import tkinter as tk

root = tk.Tk()

label = tk.Label(root,text='Hello Tkinter')
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root,text='Submit', command=lambda :print(f'The name is: {entry.get()} '))
button.pack()

root.mainloop()