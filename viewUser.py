from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import connection
import re

class main:        

    def __init__(self):
        #self.root=root
        self.root=Tk()
        self.root.state("zoomed")
        self.root.title("View User")
        self.root.config(bg="royalblue")
        Label(self.root,text="View User",font="rockwell 38 bold underline",fg="red",bg="orange",relief=SUNKEN,bd=6).pack(pady=10,ipadx=10)
        
        self.font2="arial 10 bold"
        self.f1=Frame(self.root)

        # style = ttk.Style(self.root)
        # style.theme_use("winnative")#setting a theme

        # style.configure("mystyle.Treeview", background="hotpink", rowheight=25, fieldbackground="hotpink", foreground="black")#modify color of treeview

        # style.map('mystyle.Treeview',background=[('selected','darkorchid1')])#modify color of selected items in treeview
        
        # style.configure("mystyle.Treeview.Heading", font='rockwell 14 bold italic') # Modify the font of the headings
        # style.configure("mystyle.Treeview", highlightthickness=0, font='times 12') # Modify the font of the body
        
        scroll_y=Scrollbar(self.f1,orient=VERTICAL)

        col=('Email','Role')
        self.obj= ttk.Treeview(self.f1,columns=col, yscrollcommand=scroll_y.set,style="mystyle.Treeview")

        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.obj.yview)

        for i in col:
            self.obj.heading(i, text=i.capitalize(),anchor="w")
        self.obj["show"]="headings"
        self.getValues()

        self.obj.bind('<Double-1>',self.onDoubleClick)
        self.obj.pack()
        self.f1.pack(pady=10)
        
        self.root.mainloop()

    def getValues(self):
        conn=connection.Connect()
        cur=conn.cursor()
        q="Select email, role from admin"
        cur.execute(q)
        result= cur.fetchall()
        #print(result)
        x=[]
        for row in result:
            x.append(list(row))
        for k in self.obj.get_children():
            self.obj.delete(k)
        #print(x)
        count=0
        for i in x:
            self.obj.insert("",index=count,values=i)
            count+=1

    def onDoubleClick(self,event):
        self.items=self.obj.item(self.obj.focus())["values"]
        print(self.items)
        conn=connection.Connect()
        cr=conn.cursor()
        q=f"select password from admin where email='{self.items[0]}'"
        cr.execute(q)
        result=cr.fetchone()

        self.r1=Toplevel()
        self.r1.title('Update Users')
        self.r1.geometry("500x500+0+0")
        self.r1.config(bg="green3")
        Label(self.r1,text="Update User",font="rockwell 30 bold ",fg="chocolate2",bg="green").pack(fill=X,pady=15)
        
        Label(self.r1,text="Email:",font=self.font2).pack()
        self.txt1= Entry(self.r1,width=50,font=self.font2)
        self.txt1.pack(pady=5)
        self.txt1.insert(0,self.items[0])
        self.txt1.config(state="disabled")

        Label(self.r1,text="Enter Password:",font=self.font2).pack()
        self.txt2= Entry(self.r1,width=50,font=self.font2)
        self.txt2.pack(pady=5)
        
        Label(self.r1,text="Select Role:",font=self.font2).pack()
        col=("Super Admin","Admin")
        current_role= col.index(self.items[1])
        
        self.txt3= ttk.Combobox(self.r1,width=47,values=col,font=self.font2)
        self.txt3.pack(pady=5)
        self.txt3.current(current_role)
        
        self.txt2.insert(0,result[0])

        Button(self.r1, text="Update",width=10, font=self.font2,fg="green",command=self.updateUser).pack(pady=10)
        Button(self.r1, text="Delete", width=10,font=self.font2,fg="green",command=self.deleteUser).pack(pady=10)
        Button(self.r1, text="Exit", width=10,font=self.font2,fg="red",command=lambda: self.r1.destroy()).pack(pady=10)

        self.r1.mainloop()

    def updateUser(self):
        self.email=self.txt1.get()
        self.password=self.txt2.get()
        self.role=self.txt3.get()

        alpha=re.compile("[a-zA-Z]")
        num=re.compile("[0-9]")
        sp_char= re.compile("[@_!#$%^&*()<>?/\|}{~:+.;,]")

        conn=connection.Connect()
        cur=conn.cursor()
        if self.password=="" or self.role=="":
            showerror("", " All fields required ")
        elif alpha.search(self.password)==None or num.search(self.password)==None or sp_char.search(self.password)==None:
            showwarning("Warning","Password must contains \nAlphabet + Numbers + SpecialCharacter ")
        else:

            q=f"update admin set password='{self.password}', role='{self.role}' where email='{self.email}'"
            cur.execute(q)
            conn.commit()
            self.getValues()
            self.r1.destroy()

    def deleteUser(self):
        self.email= self.txt1.get()
        ans=askyesno("Confirm",f"Do You Really Want to Delete the record of Email = '{self.email}' ?" , parent=self.r1)
        if ans:
            conn=connection.Connect()
            cur=conn.cursor()
            q=f"delete from admin where email ='{self.email}'"
            cur.execute(q)
            conn.commit()
            self.getValues()
            self.r1.destroy()


        self.r1.mainloop()


# main()