from tkinter import *
from tkinter import ttk 
from tkinter.messagebox import *
from PIL import ImageTk

import connection
import main


class main_login:

    def __init__(self):
        self.root=Tk()
        self.root.state("zoomed")
        self.root.title("Login")
        
        self.back_pic=ImageTk.PhotoImage(file="carparkbg2.png")
        self.logo_icon=ImageTk.PhotoImage(file="logicon1.png")
        self.user_icon=ImageTk.PhotoImage(file="usericon1.png")
        self.pass_icon=ImageTk.PhotoImage(file="passicon1.png")
        
        
        Label(self.root,image=self.back_pic,bd=0).place(x=0,y=0)
        Label(self.root,text="***** Login Screen *****",foreground="steel blue",bg="black",font="rockwell 38 bold ").pack(fill=X,pady=1)
        
        Label(self.root,image=self.logo_icon,relief=SOLID,bd=10,bg="gold3",highlightbackground="orange",highlightthickness=6,highlightcolor="red",cursor="heart").pack(ipadx=20,ipady=10,pady=60)
        #logolbl.grid(row=0,columnspan=3,pady=20)
        

        self.f1=Frame(self.root,bg="steel blue",relief=RIDGE,bd=10)
        
        Label(self.f1,image=self.user_icon,compound=LEFT,text=" Enter Email:       ",font="arial 15 bold",bg="cyan").grid(row=0,column=1,padx=10,pady=10,sticky="w")
        self.txt1=Entry(self.f1,font="arial 10 bold",width=50)
        self.txt1.grid(row=0,column=2,padx=10)
        
        
        Label(self.f1,image=self.pass_icon,compound=LEFT, text=" Enter Password:",font="arial 15 bold",bg="cyan").grid(row=1, column=1,padx=10,pady=10,sticky="w")
        self.txt2 = Entry(self.f1,font="times 10 bold", width=50,show='*')
        self.txt2.grid(row=1, column=2,padx=10)

        self.f1.pack(ipadx=10,ipady=10,pady=5)
        
        self.bt1=Button(self.root,text="Press to Login",command=self.checkLogin,font="cambria 13 bold", fg="darkgreen",bg="lime green",activebackground="green",cursor="hand2")
        self.bt1.bind("<Return>",self.checkLogin)
        #self.bt1.grid(row=2,column=1,pady=10)
        self.bt2=Button(self.root,text="Exit the Screen",command=lambda: self.root.destroy(),font="cambria 13 bold", fg="darkred",bg="firebrick1",activebackground="darkred",cursor="hand2")
        
        self.bt1.pack(ipadx=3,pady=5)
        self.bt2.pack(pady=5)

        self.root.mainloop()

    
    def checkLogin(self,event=None):
        self.email=self.txt1.get()
        self.password=self.txt2.get()
        #print(self.password)
        conn=connection.Connect()

        if self.email=="" or self.password=="":
            showerror("Error", " All fields required ")
        else:
            cr=conn.cursor()
            q=f"select * from admin where email='{self.email}' and password='{self.password}' "
            #print(q)
            cr.execute(q)
            result=cr.fetchone()
            #print(result)
        
            if result==None:
                showerror("Error","Invalid username/Password ")
            else:
                #showinfo("Welcome","Login Successful")
                self.root.destroy()
                #print(self.email)
                main.main(email=self.email)
    
main_login()


# if __name__=="__main__":
#     obj=main_login()
#     print(__name__)
