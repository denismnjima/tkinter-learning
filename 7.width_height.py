import tkinter as tk

root = tk.Tk()

# Create a button with specific width and height (in characters)
button = tk.Button(root, text="Wide Button", width=20, height=3)
button.pack()

root.mainloop()