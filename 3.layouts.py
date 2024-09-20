'''
pack - Arranges in a block, top to bottom
grid - arranges in either row or column manner
place - Allow placing at specific x-y cordinates
'''

import tkinter as tk

from sqlalchemy import column

root = tk.Tk()

label = tk.Label(root,text='Hello Tkinter')
label.grid(row=0,column=0)

entry = tk.Entry(root)
entry.grid(row=0,column=1)

button = tk.Button(root,text='Submit', command=lambda :print(f'The name is: {entry.get()} '))
button.grid(row=0,column=2)

root.mainloop()