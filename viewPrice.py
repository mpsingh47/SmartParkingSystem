from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import re
import connection


class main:
    #print("View Price")

    def __init__(self):
        self.root = Tk()
        self.root.state("zoomed")
        self.root.title("View Price")
        self.root.config(bg="royalblue")

        Label(self.root, text="View Price", font="rockwell 38 bold underline",fg="red",bg="orange",relief=SUNKEN,bd=6).pack(pady=10,ipadx=10)

        self.font2="arial 10 bold"
        #creating Frame for search
        self.f0 = Frame(self.root,bg="royal blue")
        Label(self.f0, text="Search By", font=self.font2).grid(row=0,column=0,padx=5)
        
        self.search_type = ("Id","VehicleType","Description")
        self.f0txt1 = ttk.Combobox(self.f0,values=self.search_type,state="readonly" ,font=self.font2)
        self.f0txt1.grid(row=0,column=1,padx=5)

        Label(self.f0, text="Enter Value:", font=self.font2).grid(row=0,column=2,padx=5)

        self.f0txt2 = Entry(self.f0,font=self.font2)
        self.f0txt2.grid(row=0,column=4,padx=5)

        Button(self.f0, text="Search" ,width=10, font=self.font2,fg="green",bg="yellow",command=self.viewPriceSearch).grid(row=0,column=5,padx=5,pady=10)
        Button(self.f0, text="ShowAll" ,width=10, font=self.font2,fg="green",bg="green yellow",command=self.getValues).grid(row=0,column=6,padx=5,pady=10)

        self.f0.option_add('*TCombobox*Listbox.font', self.font2)
        self.f0.pack(pady=10)

        self.f1 = Frame(self.root)
        
        style = ttk.Style(self.root)
        style.theme_use("winnative")#setting a theme

        style.configure("Treeview", background="hotpink", rowheight=25, fieldbackground="hotpink", foreground="black")#modify color of treeview

        style.map('Treeview',background=[('selected','darkorchid1')])#modify color of selected items in treeview
        
        style.configure("Treeview.Heading", font='rockwell 14 bold italic') # Modify the font of the headings
        style.configure("Treeview", highlightthickness=0, font='times 12') # Modify the font of the body

        scroll_y=Scrollbar(self.f1,orient=VERTICAL)

        col = ('id', 'vehicletype','price','description')
        self.obj = ttk.Treeview(self.f1, columns=col, yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.obj.yview)

        for i in col:
            self.obj.heading(i, text=i.capitalize())
        self.obj["show"] = "headings"

        self.obj.column("#1",anchor="center")
        self.obj.column("#2",anchor="center")
        self.obj.column("#3",anchor="center",width=150)
        self.obj.column("#4",anchor="center",width=250)

        self.getValues()
        self.obj.bind('<Double-1>', self.onDoubleClick)
        self.obj.pack()
        self.f1.pack()

        self.root.mainloop()
    

    def getValues(self):
        conn = connection.Connect()
        cur = conn.cursor()
        q = "Select * from parking_charge"
        cur.execute(q)
        result = cur.fetchall()
        self.obj.delete(*self.obj.get_children())
        count = 0
        for row in result:
            self.obj.insert("", index=count, values=row)
            count += 1
        self.f0txt1.set("")    
        self.f0txt2.delete(0,END)

    def viewPriceSearch(self):
        conn = connection.Connect()
        cur = conn.cursor()

        if self.f0txt1.get()==self.search_type[0]:
            q=f"Select * from parking_charge where id={self.f0txt2.get()}"

        elif self.f0txt1.get()==self.search_type[1]:
            q = f"Select * from parking_charge where vehicletype like ('%{self.f0txt2.get()}%')"

        elif self.f0txt1.get()==self.search_type[2]:
            q = f"Select * from parking_charge where description like ('%{self.f0txt2.get()}%')"

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
        q = f"select vehicletype from parking_charge where id='{self.items[0]}'"
        cr.execute(q)
        result = cr.fetchone()

        self.r1 = Toplevel()
        self.r1.title('Update Price')
        self.r1.geometry("600x550+0+0")
        self.r1.config(bg="green3")

        Label(self.r1, text="Update Price", font="rockwell 25 bold underline",fg="chocolate2",bg="green").pack(fill=X,pady=15)

        Label(self.r1, text="Id",font=self.font2).pack()
        self.txt1 = Entry(self.r1, width=50,font=self.font2)
        self.txt1.insert(0,self.items[0])
        self.txt1.config(state="readonly")
        self.txt1.pack(pady=5)

        Label(self.r1, text="Vehicle Type:",font=self.font2).pack()
        self.vtypes=("Two Wheeler","Three Wheeler","Four Wheeler","Six Wheeler")
        
        self.txt2 = ttk.Combobox(self.r1,values=self.vtypes,state="readonly" ,font=self.font2,width=47)
        self.root.option_add('*TCombobox*Listbox.font', self.font2)

        self.txt2.current(self.vtypes.index(self.items[1]))
        self.txt2.pack(pady=5)

        Label(self.r1, text="Price",font=self.font2).pack()
        self.txt3 =Entry(self.r1, width=50,font=self.font2)
        self.txt3.insert(0,self.items[2])
        self.txt3.pack(pady=5)

        Label(self.r1, text="Description",font=self.font2).pack()
        self.txt4 =Entry(self.r1, width=50,font=self.font2)
        self.txt4.insert(0,self.items[3])
        self.txt4.pack(pady=5)


        Button(self.r1, text="Update",width=10, font=self.font2,fg="green",command=self.updatePrice).pack(pady=5)
        Button(self.r1, text="Delete", width=10,font=self.font2,fg="green",command=self.deletePrice).pack(pady=5)
        Button(self.r1, text="Exit", width=10,font=self.font2,fg="red",command=lambda: self.r1.destroy()).pack(pady=5)

        self.r1.option_add('*TCombobox*Listbox.font', self.font2)
        self.r1.mainloop()

    def updatePrice(self):
        vid = self.txt1.get()
        vtype = self.txt2.get()
        pr = self.txt3.get()
        des = self.txt4.get()

        alpha=re.compile("[a-zA-Z]") #using import re

        conn = connection.Connect()
        cur = conn.cursor()
        if vtype == "" or pr == "" or des == "":
            showerror("Error", " All fields required ",parent=self.r1)
        elif vtype== self.items[1] and pr == str(self.items[2]) and des == self.items[3]:
            showwarning("Warning", "Nothing To Update!",parent=self.r1)
        elif alpha.search(pr)!=None:
            showerror("Error", "Please Enter a Valid Price (in numbers)",parent=self.r1)
        else:

            q = f"update parking_charge set vehicletype='{vtype}',price={pr},description='{des}' where id={vid}"
            cur.execute(q)
            conn.commit()
            self.getValues()
            showinfo("Success","Price Updated Successfully!",parent=self.r1)
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
            showinfo("","Price Deleted Successfully!",parent=self.r1)
            self.r1.destroy()


# main()