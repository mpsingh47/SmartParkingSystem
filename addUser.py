from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import connection
import re

class main:

    def __init__(self):
        self.root=Tk()
        self.root.geometry("550x500+0+0")
        self.root.title("Add User")
        self.root.config(bg="orange2")
        
        Label(self.root,text="Adding the User",font="rockwell 35 bold underline",fg="green",bg="seagreen2").pack(fill=X,pady=20)
        
        self.f1=Frame(self.root,bg="orange2")
        
        Label(self.f1,text="Enter email:",font="arial 15 bold",bg="seagreen2").grid(row=0,column=0,padx=5,sticky='w')
        self.txt1=Entry(self.f1,width=53)
        self.txt1.grid(row=0,column=1,pady=10,padx=10)
        
        Label(self.f1, text="Enter password:",font="arial 15 bold",bg="seagreen2").grid(row=1, column=0,padx=5,sticky='w')
        self.txt2 = Entry(self.f1, width=53)
        self.txt2.grid(row=1, column=1,pady=10,padx=10)
        
        Label(self.f1, text="Select role:",font="arial 15 bold",bg="seagreen2").grid(row=2, column=0, padx=5,sticky='w')
        self.cb1 = ttk.Combobox(self.f1, values=("Super Admin","Admin"),width=50,state="readonly")
        self.cb1.grid(row=2, column=1, pady=10,padx=10)

        self.bt1=Button(self.f1,text="Press to Insert",command=self.add,font="cambria 13 bold", fg="green")
        
        self.bt1.bind("<Return>",self.add)
        
        self.bt1.grid(row=3,column=1,pady=10)
        
        self.f1.pack()

        self.root.mainloop()

    def add(self,event=None):
        self.email=self.txt1.get()
        self.password=self.txt2.get()
        self.role=self.cb1.get()
        #print(self.password)

        alpha=re.compile("[a-zA-Z]")
        num=re.compile("[0-9]")
        spc= re.compile('[@_!#$%^&*()<>?/\|}{~:+.;,"\'-]')
 

        conn=connection.Connect()
        # conn = connect(host="127.0.0.1", user="root", passsword="", database="smartparkingsystem")
        cr=conn.cursor()
        if self.email=="" or self.password=="" or self.role=="":
            showerror("", " All fields required ")

        elif self.email.count('@')!=1 or self.email.count('.')<1:
            showwarning("Warning","Please enter a valid Email")

        elif alpha.search(self.password)==None or num.search(self.password)==None or spc.search(self.password)==None:
            showwarning("Warning","Password must contains \nAlphabet + Numbers + SpecialCharacter ")

        else:
            q=f"select * from admin where email='{self.email}'"
            cr.execute(q)
            result=cr.fetchone()
            if result==None:
                q=f"insert into admin values('{self.email}','{self.password}','{self.role}')"
                cr.execute(q)
                conn.commit()
                showinfo("","User added successfully")
            else:
                showerror("","User already exist")


#obj=main()