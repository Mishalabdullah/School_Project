from tkinter import *
from PIL import ImageTk 
from tkinter import messagebox
root=Tk()
def login_function():
        #print(Login_funtion)
        if txt_pass.get()=="" or txt_user.get()=="":
            messagebox.showerror("error, all fields are required",parent=root)
        elif txt_user.get()=="project" or txt_pass.get()=="cs2023":
            messagebox.showerror("Invalid username or password",parent=root)
        else:
            messagebox.showinfo("Welcome","welcome {self.txt.user.get()}\nyour Password: {self.txt.pass.get()}",parent=root)

def window():
    global txt_user
    global txt_pass
    root.title("Login System")
    root.geometry('1280x640')
    root.resizable(False,False)
    bg=ImageTk.PhotoImage(file="Assests/download2.jpeg")
    bg_image=Label(root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
    Frame_login=Frame(root,bg="white")
    Frame_login.place(x=150,y=175,height=340,width=500)
    title=Label(Frame_login,text="Login Here",font=("helventica",35,"bold"),fg="#d77337",bg='white').place(x=90,y=30)
    lbl_user=Label(Frame_login,text="Username",fg='#d77337').place(x=90,y=100)
    txt_user=Entry(Frame_login,font=("times new roman",15))
    txt_user.place(x=90,y=170,width=350,height=35)
    lbl_pass=Label(Frame_login,text="Password",fg='#d77337').place(x=90,y=210)
    txt_pass=Entry(Frame_login,font=("times new roman",15))
    txt_pass.place(x=90,y=210,width=350,height=35)
    forget_btn=Button(Frame_login,text="Forget password?",cursor="hand2",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=280)
    Login_btn=Button(root,command=login_function,cursor="hand2",text="Login",fg="white",bg="#d77337",font=("times new roman",15)).place(x=390,y=450,width=180,height=40) 
    root.mainloop()

window()

