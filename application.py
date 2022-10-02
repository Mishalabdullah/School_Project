from tkinter import *
from tkinter import ttk
from  functions  import *
from PIL import ImageTk,Image


'''def check_Tick():
    attendence()
    for i in l:
	    if i[1] == 1:
            #print()'''


root = Tk()
frm = ttk.Frame(root, padding=30)
frm.grid()
ttk.Label(frm, text="QR Code Scanner").grid(column=1, row=0)
ttk.Button(frm, text="Scan Me", command=qrcodescanner).grid(column=0, row=5, pady=15)
ttk.Button(frm, text="reset", command=payed_fees).grid(column=1, row=5)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=5)

my_img = ImageTk.PhotoImage(Image.open("Group 2.png"))
my_label = Label(image=my_img)
my_label.grid(column=0, row=8)
my_img_fill = ImageTk.PhotoImage(Image.open("Group 2fill.png"))
my_label_fill = Label(image=my_img_fill)
my_label_fill.grid(column=1, row=8 )
my_label_fill.grid(column=2, row=5)

root.mainloop()
