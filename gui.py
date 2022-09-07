from tkinter import *
from tkinter import ttk
from  functionprintworld  import *
root = Tk()
frm = ttk.Frame(root, padding=30)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Print World", command=printhello).grid(column=0, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
root.mainloop()
