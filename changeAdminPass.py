from tkinter import *
from tkinter import ttk 
from tkinter.messagebox import *
import connection


class changePass:

    def __init__(self, email):
        self.root = Tk()
        self.root.geometry('650x550+0+0')
        self.root.title('Change Password')
        self.root.config(bg='firebrick')

        Label(self.root, text='Change Password', font='rockwell 35 bold underline',fg="green",bg="seagreen2").pack(fill=X,pady=20)
        
        self.f1 = Frame(self.root,bg="firebrick")
        
        Label(self.f1, text='Email:',font="arial 15 bold",bg="seagreen2").grid(row=0, column=0,padx=15,pady=10,sticky="w")
        self.txt1 = Entry(self.f1, width=40,font="arial 11 bold")
        self.txt1.insert(0, email)
        self.txt1.config(state='readonly')
        self.txt1.grid(row=0,column=1,pady=10)
        
        Label(self.f1, text='Enter Old Password:',font="arial 15 bold",bg="seagreen2").grid(row=1, column=0,padx=15,pady=10,sticky="w")
        self.txt2 = Entry(self.f1, width=40,show='*',font="arial 11 bold")
        self.txt2.grid(row=1,column=1,pady=10)
        
        Label(self.f1, text='Enter New Password:',font="arial 15 bold",bg="seagreen2").grid(row=2, column=0,padx=15,pady=10,sticky="w")
        self.txt3 = Entry(self.f1, width=40,show='*',font="arial 11 bold")
        self.txt3.grid(row=2,column=1,pady=10)
        
        
        Button(self.f1, text='Submit', width=15, command=self.changeAdminPass,font="cambria 13 bold", fg="green").grid(row=3,column=1,pady=20)
        
        self.f1.pack()
        self.root.mainloop()

    def changeAdminPass(self):
        self.email = self.txt1.get()
        self.oldPass = self.txt2.get()
        self.newPass = self.txt3.get()
        # print(self.password,self.email)
        conn = connection.Connect()
        cr = conn.cursor()
        if self.newPass == '' and self.oldPass == '':
            showerror('Error','Please Enter the data')
        else:
            q = 'select * from admin where email="{}" and password="{}"'.format(self.email, self.oldPass)
            cr.execute(q)
            result = cr.fetchone()
            if result == None:
                showerror('Error','Invalid Old Password')
            else:
                q = 'update admin set password="{}" where email="{}"'.format(self.newPass,self.email)
                cr.execute(q)
                conn.commit()
                showinfo('Success', 'Password Changed Successfully')
                self.root.destroy()

    
# changePass(email='m@.')