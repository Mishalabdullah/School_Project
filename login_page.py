

from tkinter import *
from PIL import ImageTk 
from tkinter import messagebox
from functions import login_check


root=Tk()
def login_function():
    for i in login_check():
        if i[0] == txt_user.get() and i[1]==txt_pass.get():
            root.destroy()
            import application
        else:
            messagebox.showinfo("Invalid User",parent=root)
    
def window():
    global txt_user
    global txt_pass
    root.title("Login System")
    root.geometry('800x640')
    root.resizable(False,False)
    bg=ImageTk.PhotoImage(file="Assests/download2.jpeg")
    bg_image=Label(root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
    Frame_login=Frame(root,bg="white")
    Frame_login.place(x=150,y=175,height=340,width=500)
    title=Label(Frame_login,text="Login Here",font=("helventica",35,"bold"),fg="#d77337",bg='white').place(x=90,y=30)
    lbl_user=Label(Frame_login,text="Login To Continue",fg='#d77337').place(x=90,y=100)
    txt_user=Entry(Frame_login,font=("times new roman",15))
    txt_user.place(x=90,y=170,width=350,height=35)
    lbl_pass=Label(Frame_login,text="Password",fg='#d77337').place(x=90,y=210)
    txt_pass=Entry(Frame_login,font=("times new roman",15))
    txt_pass.place(x=90,y=210,width=350,height=35)
    Login_btn=Button(root,command=login_function,cursor="hand2",text="Login",fg="white",bg="#d77337",font=("times new roman",15)).place(x=390,y=450,width=180,height=40) 
    root.mainloop()

window()
