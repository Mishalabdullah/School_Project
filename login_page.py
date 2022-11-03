from tkinter import *
from PIL import ImageTk 
from tkinter import messagebox
class Login:
    def _init_(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1199X600+100+50")
        self.root.resizable(False,False)

        self.bg=ImageTk.PhotoImage(file="Assests\download.jpeg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
    

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=175,height=340,width=500)

        title=Label(Frame_login,text="Login Here",font=("helventica",35,"bold"),fg="#d77337",bg='white').place(x=90,y=30)

        lbl_user=Label(Frame_login,texts="Username",fg='#d77337').place(x=90,y=100)
        self.txt_user=Entry(Frame_login,font=("times new roman",15))
        self.txt_user.place(x=90,y=170,width=350,height=35)
        lbl_pass=Label(Frame_login,texts="Password",fg='#d77337').place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15))
        self.txt_pass.place(x=90,y=210,width=350,height=35)


        forget_btn=Button(Frame_login,text="Forget password?",cursor="hand2",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=280)
        Login_btn=Button(self.root,command=self.login_function,cursor="hand2",text="Login",fg="white",bg="#d77337",font=("times new roman",15)).place(x=300,y=470,width=180,height=40) 

    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("error, all fields are required",parent=self.root)
        elif self.txt_user.get()=="project" or self.txt_pass.get()=="cs2023":
            messagebox.showerror("Invalid username or password",parent=self.root)
        else:
            messagebox.showinfo("Welcome","welcome {self.txt.user.get()}\nyour Password: {self.txt.pass.get()}",parent=self.root)

root=Tk()
#Before
# obj=Login(root)
#The change i have made
obj=Login()
root.mainloop()




