from tkinter import *
from tkinter import ttk
from  functions  import *
root = Tk()
frm = ttk.Frame(root, padding=30)
frm.grid()
ttk.Label(frm, text="QR Code Scanner").grid(column=1, row=0)
ttk.Button(frm, text="Scan Me", command=qrcodescanner).grid(column=0, row=5, pady=15)
ttk.Button(frm, text="reset", command=payed_fees).grid(column=1, row=5)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=5)

# Check Box
var = IntVar()
c = Checkbutton(root,command=attendence,variable=var)
c.grid(column=0, row=6)
root.mainloop()
