'''
Tkinter allows you to add foregoround (fg)
and background (bg)
'''


import tkinter as tk

root = tk.Tk()

label = tk.Label(root,text='Hello Tkinter', font=("Cursive",16,"bold italic"),fg='yellow',bg='black')
label.pack()

root.mainloop()