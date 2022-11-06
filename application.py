from tkinter import *
from  functions  import *
import tkinter.font as font
from PIL import ImageTk, Image




root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()

bg = ImageTk.PhotoImage(file='Assests/water.jpeg')
my_label = Label(frm,image=bg)
my_label.place(x=0,y=0,relheight=1,relwidth=1 ,bordermode=OUTSIDE)

def check_Tick(): # The Funciton is for changing the colour of the boxes
    l = attendence()
    for i in l:
        print(i)
        if i[0] == 1:
            if i [1] == 1:
                canvas = Canvas(frm,width=50,height=50,bg='#b0e2f9',borderwidth=0)
                canvas.create_rectangle(50, 50,0, 0, fill="#f50")
                canvas.grid(column=1,row=3,pady=10)
            else:
                canvas = Canvas(frm,width=50,height=50,bg='#b0e2f9',borderwidth=0)
                canvas.create_rectangle(50, 50,0, 0, fill="#fb0")
                canvas.grid(column=1,row=3,pady=10)
        if i[0] == 2:
            if i[1] == 1:
                canvas2 = Canvas(frm,width=50,height=50,bd=0,bg='#b2e2f9',borderwidth=0)
                canvas2.create_rectangle(50, 50,0, 0, fill="#f50")
                canvas2.grid(column=2,row=3,pady=10)
            else:
                canvas2 = Canvas(frm,width=50,height=50,bg='#b0e2f9',borderwidth=0)
                canvas2.create_rectangle(50, 50,0, 0, fill="#fb0")
                canvas2.grid(column=2,row=3,pady=10)
        if i[0] == 3:
            if i [1] == 1:    
                canvas3 = Canvas(frm,width=50,height=50,bg='#b0e2f9')
                canvas3.create_rectangle(50, 50,0, 0, fill="#f50")
                canvas3.grid(column=3,row=3,pady=10)
            else:
                canvas3 = Canvas(frm,width=50,height=50,bg='#b0e2f9')
                canvas3.create_rectangle(50, 50,0, 0, fill="#fb0")
                canvas3.grid(column=3,row=3,pady=10)
        if i[0] == 4:
            if i[1] == 1:
                    canvas4 = Canvas(frm,width=50,height=50,bg='#b0e2f9',bd=0)
                    canvas4.create_rectangle(50, 50,0, 0, fill="#f50")
                    canvas4.grid(column=1,row=4,pady=10)
            else:
                canvas4 = Canvas(frm,width=50,height=50,bg='#b0e2f9',bd=0)
                canvas4.create_rectangle(50, 50,0, 0, fill="#fb0")
                canvas4.grid(column=1,row=4,pady=10)
        if i[0] == 5:
            if i[1] ==1:
                canvas5 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9')
                canvas5.create_rectangle(50, 50,0, 0, fill="#f50")
                canvas5.grid(column=2,row=4,pady=10)
            else:
                canvas5 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9')
                canvas5.create_rectangle(50, 50,0, 0, fill="#fb0")
                canvas5.grid(column=2,row=4,pady=10)
        if i[0] == 6:
            if i[1] ==1:
                canvas6 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9')
                canvas6.create_rectangle(50, 50,0, 0, fill="#f50")
                canvas6.grid(column=3,row=4,pady=10)
            else:
                canvas6 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9')
                canvas6.create_rectangle(50, 50,0, 0, fill="#fb0")
                canvas6.grid(column=3,row=4,pady=10)
        if i[0] == 7:
            if i[1] ==1:        
                canvas7 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9')
                canvas7.create_rectangle(50, 50,0, 0, fill="#f50")
                canvas7.grid(column=1,row=5,pady=10)
            else:   
                canvas7 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9')
                canvas7.create_rectangle(50, 50,0, 0, fill="#fb0")
                canvas7.grid(column=1,row=5,pady=10)
        if i[0] == 8:
            if i[1] ==1:
                canvas8 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9')
                canvas8.create_rectangle(50, 50,0, 0, fill="#f50")
                canvas8.grid(column=2,row=5,pady=10)
            else:
                canvas8 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9')
                canvas8.create_rectangle(50, 50,0, 0, fill="#fb0")
                canvas8.grid(column=2,row=5,pady=10)
        if i[0] == 9:
            if i[1] ==1:
                canvas9 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9')
                canvas9.create_rectangle(50, 50,0, 0, fill="#f50")
                canvas9.grid(column=3,row=5,pady=10)
            else:
                canvas9 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9')
                canvas9.create_rectangle(50, 50,0, 0, fill="#fb0")
                canvas9.grid(column=3,row=5,pady=10)
        if i[0] == 10:
            if i[1] ==1:
                canvas10 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9')
                canvas10.create_rectangle(50, 50,0, 0, fill="#f50")
                canvas10.grid(column=1,row=6,pady=10)
            else:
                canvas11 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9')
                canvas11.create_rectangle(50, 50,0, 0, fill="#fb0")
                canvas11.grid(column=1,row=6,pady=10)
        if i[0] == 11:
            if i[1] ==1:
                canvas11 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9')
                canvas11.create_rectangle(50, 50,0, 0, fill="#f50")
                canvas11.grid(column=2,row=6,pady=10)
            else:
                canvas11 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9')
                canvas11.create_rectangle(50, 50,0, 0, fill="#fb0")
                canvas11.grid(column=2,row=6,pady=10)
        if i[0] == 12:
            if i[1] ==1:
                canvas12 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9')
                canvas12.create_rectangle(50, 50,0, 0, fill="#f50")
                canvas12.grid(column=3,row=6,pady=10)
            else:
                canvas12 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9' )
                canvas12.create_rectangle(50, 50,0, 0, fill="#fb0")
                canvas12.grid(column=3,row=6,pady=10)
        if i[0] == 13:
            if i[1] ==1:
                canvas13 = Canvas(frm,width=50,height=50,bd=0)
                canvas13.create_rectangle(50, 50,0, 0, fill="#f50")
                canvas13.grid(column=1,row=7,pady=10)
            else:
                canvas13 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9' )
                canvas13.create_rectangle(50, 50,0, 0, fill="#fb0")
                canvas13.grid(column=1,row=7,pady=10)
        if i[0] == 14:
            if i[1] ==1:
                canvas14 = Canvas(frm,width=50,height=50,bd=0)
                canvas14.create_rectangle(50, 50,0, 0, fill="#f50")
                canvas14.grid(column=2,row=7,pady=10)
            else:
                canvas14 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9' )
                canvas14.create_rectangle(50, 50,0, 0, fill="#fb0")
                canvas14.grid(column=2,row=7,pady=10)
        if i[0] == 15:
            if i[1] ==1:    
                canvas15 = Canvas(frm,width=50,height=50,bd=0)
                canvas15.create_rectangle(50, 50,0, 0, fill="#f50")
                canvas15.grid(column=3,row=7,pady=10)
            else:
                canvas15 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9' )
                canvas15.create_rectangle(50, 50,0, 0, fill="#fb0")
                canvas15.grid(column=3,row=7,pady=10)
        if i[0] == 16:
            if i[1] ==1:          
                canvas16 = Canvas(frm,width=50,height=50,bd=0)
                canvas16.create_rectangle(50, 50,0, 0, fill="#f50")
                canvas16.grid(column=1,row=8,pady=10)
            else:
                canvas16 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9' )
                canvas16.create_rectangle(50, 50,0, 0, fill="#fb0")
                canvas16.grid(column=1,row=8,pady=10)
        if i[0] == 17:
            if i[1] ==1:
                canvas17 = Canvas(frm,width=50,height=50,bd=0)
                canvas17.create_rectangle(50, 50,0, 0, fill="#f50")
                canvas17.grid(column=2,row=8,pady=10)
            else:
                canvas17 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9' )
                canvas17.create_rectangle(50, 50,0, 0, fill="#fb0")
                canvas17.grid(column=2,row=8,pady=10)
        if i[0] == 18:
            if i[1] ==1:
                canvas18 = Canvas(frm,width=50,height=50,bd=0)
                canvas18.create_rectangle(50, 50,0, 0, fill="#f50")
                canvas18.grid(column=3,row=8,pady=10)
            else:
                canvas18 = Canvas(frm,width=50,height=50,bd=0,bg='#b0e2f9' )
                canvas18.create_rectangle(50, 50,0, 0, fill="#fb0")
                canvas18.grid(column=3,row=8,pady=10)
 
 

check_Tick()
ttk.Label(frm, text="LIFE",font=("Helvetica", 24)).grid(column=2, row=0)
ttk.Label(frm, text="Scan The QRCode To Enter",font=("Helvetica", 20)).grid(column=2, row=1)
ScanMeButton = Button(frm,text="Click To Scan",bg='#0688d4',fg="#ffffff",font=('Helvetica',18),command=attender,border=0)
ScanMeButton.grid(column=2, row=2, pady=15)
ttk.Button(frm, text="reset", command=payed_fees).grid(column=3, row=10, pady=15)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=10,padx=55)
ttk.Button(frm, text="check", command=check_Tick).grid(column=1, row=10)


root.mainloop()