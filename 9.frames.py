import  tkinter as tk

root = tk.Tk()

frame = tk.Frame(root,bg='lightblue',padx=20,pady=20)
frame.pack(pady=20)

label = tk.Label(frame,text='Label inside frame', font=('Arial',15))
label.pack()

label.mainloop()