'''
font is a mthon in labels, it has properties like
 ->font-name
 ->font-size
 ->additional styles like bold and italics
'''

import tkinter as tk

root = tk.Tk()

label = tk.Label(root,text='Hello Tkinter', font=("Cursive",16,"bold italic"))
label.pack()

root.mainloop()