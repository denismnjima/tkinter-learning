'''
Tkinter alows you to add paddig
with padx and pady
'''

import tkinter as tk

root = tk.Tk()

# Create a button with padding
button = tk.Button(root, text="Click Me", padx=100, pady=40,bg='red')
button.pack()

root.mainloop()