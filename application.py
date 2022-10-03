from tkinter import *
from tkinter import ttk
from  functions  import *


root = Tk()
frm = ttk.Frame(root, padding=30)
frm.grid()
def check_Tick(): # The Funciton is for changing the colour of the boxes
    attendence()
    print(l)
    for i in l:
        print(i)
        if i[0] == 1:
            if i [1] == 1:
                canvas = Canvas(frm)
                canvas.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas.grid(column=1,row=4,padx=10,pady=5)
        if i[0] == 2:
            if i[1] == 1:
                canvas2 = Canvas(frm)
                canvas2.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas2.grid(column=2,row=4,padx=10,pady=5)
        if i[0] == 3:
            if i [1] == 1:    
                canvas3 = Canvas(frm)
                canvas3.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas3.grid(column=3,row=4,padx=10,pady=5)
        if i[0] == 4:
            if i[1] == 1:
                    canvas4 = Canvas(frm)
                    canvas4.create_rectangle(50, 50,10, 10, fill="#f50")
                    canvas4.grid(column=1,row=5,padx=10,pady=5)
        if i[0] == 5:
            if i[1] ==1:
                canvas5 = Canvas(frm)
                canvas5.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas5.grid(column=2,row=5,padx=10,pady=5)

# the below code is for the boxes feel free to skip to the last part

canvas = Canvas(frm)
canvas.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas.grid(column=1,row=4,padx=10,pady=5)
canvas2 = Canvas(frm)
canvas2.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas2.grid(column=2,row=4,padx=10,pady=5)
canvas3 = Canvas(frm)
canvas3.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas3.grid(column=3,row=4,padx=10,pady=5)
canvas4 = Canvas(frm)
canvas4.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas4.grid(column=1,row=5,padx=10,pady=5)
canvas5 = Canvas(frm)
canvas5.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas5.grid(column=2,row=5,padx=10,pady=5)

## The above part is just the code for the boxes 


ttk.Label(frm, text="QR Code Scanner").grid(column=1, row=0)
ttk.Button(frm, text="Scan Me", command=qrcodescanner).grid(column=0, row=3, pady=15)
ttk.Button(frm, text="reset", command=payed_fees).grid(column=1, row=3)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=3)
ttk.Button(frm, text="check", command=check_Tick).grid(column=3, row=3,padx=16)


root.mainloop()
