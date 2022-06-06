from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import re

import connection

class main:
    #print("View Registration")

    def __init__(self):
        self.root = Tk()
        self.root.state("zoomed")
        self.root.title("View Registration")
        self.root.config(bg="royal blue")

        Label(self.root, text="View Vehicle Registration", font="rockwell 38 bold underline",fg="red1",bg="orange",relief=SUNKEN,bd=6).pack(pady=10,ipadx=10)

        self.font2="arial 10 bold"
        #creating frame for search
        self.f0 = Frame(self.root,bg="royal blue")
        Label(self.f0, text="Search By", font=self.font2).grid(row=0,column=0,padx=5)
        
        self.search_type = ("Id","VehicleNumber","VehicleType","OwnerName")
        self.f0txt1 = ttk.Combobox(self.f0,values=self.search_type,state="readonly" ,font=self.font2)
        self.f0txt1.grid(row=0,column=1,padx=5)

        Label(self.f0, text="Enter Value:", font=self.font2).grid(row=0,column=2,padx=5)

        self.f0txt2 = Entry(self.f0,font=self.font2)
        self.f0txt2.grid(row=0,column=4,padx=5)

        Button(self.f0, text="Search" ,width=10, font=self.font2,fg="green",bg="yellow",command=self.viewRegistrationSearch).grid(row=0,column=5,padx=5,pady=10)
        Button(self.f0, text="ShowAll" ,width=10, font=self.font2,fg="green",bg="green yellow",command=self.getValues).grid(row=0,column=6,padx=5,pady=10)

        self.f0.option_add('*TCombobox*Listbox.font', self.font2)
        self.f0.pack()

        self.f1 = Frame(self.root,relief=RIDGE,bd=4)

        style = ttk.Style(self.root)
        style.theme_use("winnative")#setting a theme

        style.configure("mystyle.Treeview", background="hotpink", rowheight=25, fieldbackground="hotpink", foreground="black")#modify color of treeview

        style.map('mystyle.Treeview',background=[('selected','darkorchid1')])#modify color of selected items in treeview
        
        style.configure("mystyle.Treeview.Heading", font='rockwell 14 bold italic') # Modify the font of the headings
        style.configure("mystyle.Treeview", highlightthickness=0, font='times 12') # Modify the font of the body

        scroll_x=Scrollbar(self.f1,orient=HORIZONTAL)
        scroll_y=Scrollbar(self.f1,orient=VERTICAL)
        
        col = ('id','vehicleNumber', 'vehicleType','ownerName','designation','address','mobile','email','gender')
        self.obj = ttk.Treeview(self.f1, columns=col,xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set,style='mystyle.Treeview')

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.obj.xview)
        scroll_y.config(command=self.obj.yview)

        for i in col:
            self.obj.heading(i, text=i.capitalize(),anchor="w")
        self.obj["show"] = "headings"
        
        self.obj.column("id",width=100)
        self.obj.column("vehicleNumber",width=150)
        self.obj.column("vehicleType",width=120)
        self.obj.column("ownerName",width=150)
        self.obj.column("mobile",width=100)
        self.obj.column("gender",width=100)

        self.getValues()
        self.obj.bind('<Double-1>', self.onDoubleClick)
        self.obj.pack(fill=BOTH,expand=1)
        self.f1.place(x=10,y=150,width=1350,height=500)
        #self.f1.pack()
        self.root.mainloop()
    

    def getValues(self):
        conn = connection.Connect()
        cur = conn.cursor()
        q = "Select * from vehicle_registration"
        cur.execute(q)
        result = cur.fetchall()
        self.obj.delete(*self.obj.get_children())
        count = 0
        for row in result:
            self.obj.insert("", index=count, values=row)
            count += 1
        self.f0txt1.set("")    
        self.f0txt2.delete(0,END)
    
    def viewRegistrationSearch(self):
        conn = connection.Connect()
        cur = conn.cursor()

        if self.f0txt1.get()==self.search_type[0]:
            q=f"Select * from vehicle_registration where id={self.f0txt2.get()}"

        elif self.f0txt1.get()==self.search_type[1]:
            q = f"Select * from vehicle_registration where vehiclenumber like ('%{self.f0txt2.get()}%')"

        elif self.f0txt1.get()==self.search_type[2]:
            q = f"Select * from vehicle_registration where vehicletype like ('%{self.f0txt2.get()}%')"

        elif self.f0txt1.get()==self.search_type[3]:
            q = f"Select * from vehicle_registration where ownername like ('%{self.f0txt2.get()}%')"

        cur.execute(q)
        result = cur.fetchall()
        self.obj.delete(*self.obj.get_children())
        
        count = 0
        for row in result:
            self.obj.insert("", index=count, values=row)
            count += 1

    
    def onDoubleClick(self, event):
        self.items = self.obj.item(self.obj.focus())["values"]
        #print(self.items)
        conn = connection.Connect()
        cr = conn.cursor()
        q = f"select * from vehicle_registration where id={self.items[0]}"
        cr.execute(q)
        result = cr.fetchone()
        #print(result)

        self.r1 = Toplevel()

        self.r1.title('Update Registration')
        self.r1.geometry("600x680+0+0")
        self.r1.config(bg="green3")
        
        Label(self.r1, text="Update Registration", font="rockwell 30 bold ",fg="chocolate2",bg="green").pack(fill=X,pady=15)

        Label(self.r1, text="Id:",font=self.font2).pack()
        self.txt1 = Entry(self.r1, width=50,font=self.font2)
        self.txt1.insert(0,self.items[0])
        self.txt1.config(state="disabled")
        self.txt1.pack(pady=5)

        Label(self.r1, text="Vehicle Number:",font=self.font2).pack()
        self.txt2 = Entry(self.r1, width=50,font=self.font2)
        self.txt2.insert(0,self.items[1])
        self.txt2.config(state="disabled")
        self.txt2.pack(pady=5)

        Label(self.r1, text="Vehicle Type:",font=self.font2).pack()
        self.vtypes=("Two Wheeler","Three Wheeler","Four Wheeler","Six Wheeler")
        self.txt3 = ttk.Combobox(self.r1,values=self.vtypes,state="readonly" ,font=self.font2,width=47)
        self.txt3.current(self.vtypes.index(self.items[2]))
        self.txt3.config(state="disabled")
        self.txt3.pack(pady=5)

        Label(self.r1, text="Owner Name:",font=self.font2).pack()
        self.txt4 =Entry(self.r1, width=50,font=self.font2)
        self.txt4.insert(0,self.items[3])
        self.txt4.pack(pady=5)

        Label(self.r1, text="Designation:",font=self.font2).pack()
        self.desg=("Administration Staff","Parking Staff","Janitors Staff","Customer","Other")
        self.txt5 = ttk.Combobox(self.r1, values=self.desg, state="readonly", font=self.font2, width=47)
        self.txt5.current(self.desg.index(self.items[4]))
        self.txt5.pack(pady=5)

        Label(self.r1, text="Address:",font=self.font2).pack()
        self.txt6 =Entry(self.r1, width=50,font=self.font2)
        self.txt6.insert(0,self.items[5])
        self.txt6.pack(pady=5)

        Label(self.r1, text="Mobile:",font=self.font2).pack()
        self.txt7 =Entry(self.r1, width=50,font=self.font2)
        self.txt7.insert(0,self.items[6])
        self.txt7.pack(pady=5)

        Label(self.r1, text="Email:",font=self.font2).pack()
        self.txt8 =Entry(self.r1, width=50,font=self.font2)
        self.txt8.insert(0,self.items[7])
        self.txt8.pack(pady=5)

        Label(self.r1, text="Gender:",font=self.font2).pack()
        self.gen=("Male","Female","Other")
        self.txt9 = ttk.Combobox(self.r1, values=self.gen, state="readonly", font=self.font2, width=47)
        self.txt9.current(self.gen.index(self.items[8]))
        self.txt9.pack(pady=5)

        Button(self.r1, text="Update",width=10, font=self.font2,fg="green",command=self.updatePrice).pack(pady=5)
        Button(self.r1, text="Delete", width=10,font=self.font2,fg="green",command=self.deletePrice).pack(pady=5)
        Button(self.r1, text="Exit", width=10,font=self.font2,fg="red",command=lambda: self.r1.destroy()).pack(pady=5)

        self.r1.option_add('*TCombobox*Listbox.font', self.font2)
        self.r1.mainloop()

    def updatePrice(self):
        vid = self.txt1.get()
        vnum= self.txt2.get()
        vtype = self.txt3.get()
        oname= self.txt4.get()
        desg= self.txt5.get()
        addr= self.txt6.get()
        mob= self.txt7.get()
        em= self.txt8.get()
        gen= self.txt9.get()

        alpha=re.compile("[a-zA-Z]")
        spc= re.compile('[@_!#$%^&*()<>?/\|}{~:+.;,"\'-]')

        conn = connection.Connect()
        cur = conn.cursor()
        # for i in self.items:
        #     print(i , type(i))
        # print(type(vid),type(vnum),type(vtype),type(oname),type(desg),type(addr),type(mob),type(em),type(gen))

        if oname == "" or desg== "" or addr=="" or mob=="" or em=="" or gen=="":
            showerror("Error", " All fields required ",parent=self.r1)

        elif len(mob)!=10 or alpha.search(mob)!=None or spc.search(mob)!=None:
            showerror("Error", " Please Enter a Correct 10-Digit Number!",parent=self.r1)

        elif oname == self.items[3] and desg== self.items[4] and addr==self.items[5] and mob==str(self.items[6]) and em==self.items[7] and gen==self.items[8]:
            showwarning("Warning", " Nothing To Update!",parent=self.r1)
            # print(self.items)
            # print(vid,vnum,vtype,oname,desg,addr,mob,em,gen)

        else:

            q = f"update vehicle_registration set ownername='{oname}',designation='{desg}',address='{addr}',mobile='{mob}',email='{em}',gender='{gen}' where id={vid}"
            cur.execute(q)
            conn.commit()
            self.getValues()
            showinfo("Success","Vehicle Registration Updated Successfully!",parent=self.r1)
            self.r1.destroy()

    def deletePrice(self):
        self.id= self.txt1.get()
        ans=askyesno("Confirm",f"Do You Really Want to Delete the record of ID = '{self.id}' ?" , parent=self.r1)
        if ans:
            conn = connection.Connect()
            cur = conn.cursor()
            q = f"delete from parking_charge where id ={self.id}"
            cur.execute(q)
            conn.commit()
            self.getValues()
            showinfo("","Vehicle Registration Deleted Successfully!",parent=self.r1)
            self.r1.destroy()


# main()