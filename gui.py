from tkinter import *
from tkinter import ttk
from  functionprintworld  import *
root = Tk()
frm = ttk.Frame(root, padding=30)
frm.grid()
ttk.Label(frm, text="QR Code Scanner").grid(column=0, row=0)
ttk.Button(frm, text="Scan Me", command=qrcodescanner).grid(column=0, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
root.mainloop()
