from tkinter import *
from tkinter import ttk
from  functions  import *


root = Tk()
frm = ttk.Frame(root, padding=0)
frm.grid()
def check_Tick(): # The Funciton is for changing the colour of the boxes
    l = attendence()
    for i in l:
        print(i)
        if i[0] == 1:
            if i [1] == 1:
                canvas = Canvas(frm)
                canvas.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas.grid(column=1,row=2)
        if i[0] == 2:
            if i[1] == 1:
                canvas2 = Canvas(frm)
                canvas2.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas2.grid(column=2,row=2)
        if i[0] == 3:
            if i [1] == 1:    
                canvas3 = Canvas(frm)
                canvas3.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas3.grid(column=3,row=2)
        if i[0] == 4:
            if i[1] == 1:
                    canvas4 = Canvas(frm)
                    canvas4.create_rectangle(50, 50,10, 10, fill="#f50")
                    canvas4.grid(column=1,row=3)
        if i[0] == 5:
            if i[1] ==1:
                canvas5 = Canvas(frm)
                canvas5.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas5.grid(column=2,row=3)
        if i[0] == 6:
            if i[1] ==1:
                canvas6 = Canvas(frm)
                canvas6.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas6.grid(column=3,row=5)
        if i[0] == 7:
            if i[1] ==1:        
                canvas7 = Canvas(frm)
                canvas7.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas7.grid(column=1,row=6)
        if i[0] == 8:
            if i[1] ==1:
                canvas8 = Canvas(frm)
                canvas8.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas8.grid(column=2,row=6)

        if i[0] == 9:
                canvas9 = Canvas(frm)
                canvas9.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas9.grid(column=3,row=6)
        if i[0] == 10:
            if i[1] ==1:
                canvas10 = Canvas(frm)
                canvas10.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas10.grid(column=1,row=7)
        if i[0] == 11:
            if i[1] ==1:
                canvas11 = Canvas(frm)
                canvas11.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas11.grid(column=2,row=7)
        if i[0] == 12:
            if i[1] ==1:
                canvas12 = Canvas(frm)
                canvas12.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas12.grid(column=3,row=7)
        if i[0] == 13:
            if i[1] ==1:
                canvas13 = Canvas(frm)
                canvas13.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas13.grid(column=1,row=8)
        if i[0] == 14:
            if i[1] ==1:
                canvas14 = Canvas(frm)
                canvas14.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas14.grid(column=2,row=8)
        if i[0] == 15:
            if i[1] ==1:    
                canvas15 = Canvas(frm)
                canvas15.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas15.grid(column=3,row=8)
        if i[0] == 16:
            if i[1] ==1:          
                canvas16 = Canvas(frm)
                canvas16.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas16.grid(column=1,row=9)
        if i[0] == 17:
            if i[1] ==1:
                canvas17 = Canvas(frm)
                canvas17.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas17.grid(column=2,row=9)
        if i[0] == 18:
            if i[1] ==1:
                canvas18 = Canvas(frm)
                canvas18.create_rectangle(50, 50,10, 10, fill="#f50")
                canvas18.grid(column=3,row=9)

# the below code is for the boxes feel free to skip to the last part

canvas = Canvas(frm)
canvas.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas.grid(column=1,row=2)
canvas2 = Canvas(frm)
canvas2.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas2.grid(column=2,row=2)
canvas3 = Canvas(frm)
canvas3.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas3.grid(column=3,row=2)
canvas4 = Canvas(frm)
canvas4.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas4.grid(column=1,row=3)
canvas5 = Canvas(frm)
canvas5.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas5.grid(column=2,row=3)
canvas6 = Canvas(frm)
canvas6.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas6.grid(column=3,row=3)
canvas7 = Canvas(frm)
canvas7.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas7.grid(column=1,row=4)
canvas8 = Canvas(frm)
canvas8.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas8.grid(column=2,row=4)
canvas9 = Canvas(frm)
canvas9.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas9.grid(column=3,row=4)
canvas10 = Canvas(frm)
canvas10.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas10.grid(column=1,row=5)
canvas11 = Canvas(frm)
canvas11.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas11.grid(column=2,row=5)
canvas12 = Canvas(frm)
canvas12.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas12.grid(column=3,row=5)
canvas13 = Canvas(frm)
canvas13.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas13.grid(column=1,row=6)
canvas14 = Canvas(frm)
canvas14.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas14.grid(column=2,row=6)
canvas15 = Canvas(frm)
canvas15.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas15.grid(column=3,row=6)
canvas16 = Canvas(frm)
canvas16.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas16.grid(column=1,row=7)
canvas17 = Canvas(frm)
canvas17.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas17.grid(column=2,row=7)
canvas18 = Canvas(frm)
canvas18.create_rectangle(50, 50,10, 10, fill="#fb0")
canvas18.grid(column=3,row=7)

## The above part is just the code for the boxes 

check_Tick()
ttk.Label(frm, text="QR Code Scanner").grid(column=2, row=0)
ttk.Button(frm, text="Scan Me", command=attender).grid(column=1, row=1, pady=15)
ttk.Button(frm, text="reset", command=payed_fees).grid(column=2, row=1, pady=15)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=1, pady=15)
ttk.Button(frm, text="check", command=check_Tick).grid(column=4, row=1, pady=15)


root.mainloop()

