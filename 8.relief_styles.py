import tkinter as tk

root = tk.Tk()

# Create a label with a 'raised' border
label = tk.Label(root, text="Raised Border", relief="raised", borderwidth=5)
label.pack(pady=10)

# Create a label with a 'sunken' border
label2 = tk.Label(root, text="Sunken Border", relief="sunken", borderwidth=5)
label2.pack(pady=10)

root.mainloop()