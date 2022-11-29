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

Label(frm, text="Analytics",font=("Helvetica", 24),bg='#d9ecf0',fg="#000000").grid(column=2, row=0,pady=10)
Label(frm, text="Number Of Visits In A Month",font=("Helvetica", 20),bg='#d9ecf0',fg="#000000").grid(column=2, row=1)
Button(frm, text="Quit", command=root.destroy,font=("times new roman",15),bg="#043565",fg='white').grid(column=2, row=10,padx=55)


root.mainloop()