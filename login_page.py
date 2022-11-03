from tkinter import *
from PIL import ImageTk 
class Login:
    def_init_(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("700X350")
        self.root.resizable(False,False)

        self.bg=ImageTk.PhotoImage(file="Assests\download.jpeg")
        self.bg_image=Label(self.root,image=self.bg)place(x=0,y=0,relwidth=1,relheight=1)

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=175,height=340,width=500)

        title=Label(Frame_login,text="Login Here",font=("helventica",35,"bold")fg="#d77337").place(x=90,y=30)

        lbl_user=Label(Frame_login,texts="Username",fg='#d77337').place(x=90,y=100)
        self.txt_user=Entry(Frame_login,font=("times new roman",15))
        self.txt_user.place=(x=90,y=170,width=350,height=35)
        lbl_pass=Label(Frame_login,texts="Password",fg='#d77337').place(x=90,y=130)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15))
        self.txt_pass.place=(x=90,y=210,width=350,height=35)

        forget=button(Frame_login,text="Forget password?",bg="white",fg="#d77337",font=("times new roman",12)).place(x=90,y=)







