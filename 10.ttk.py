import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Create a styled button using ttk
button = ttk.Button(root, text="Styled Button")
button.pack(pady=10)

root.mainloop()