from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import re
import connection


class main:
    # print("Add Price")
    def __init__(self):
        self.root = Tk()
        self.root.geometry("700x550-20-50")
        self.root.title("Add Registration")
        self.root.config(bg="orange2")
        Label(self.root, text="Vehicle Registration Form",  font="rockwell 30 bold underline",fg="green",bg="seagreen2").pack(fill=X,pady=20)

        self.f1 = Frame(self.root,bg="orange2")

        font1 = "arial 15 bold"
        font2 = "arial 11 bold"

        # Label(self.f1, text="Enter id:", font=font1).grid(row=0, column=0, padx=5, sticky='w')
        # self.txt1 = Entry(self.f1, width=50)
        # self.txt1.grid(row=0, column=1, pady=10)

        Label(self.f1, text="Enter Vehicle Number:", font=font1,bg="seagreen2").grid(row=0, column=0, padx=10, sticky='w')
        self.txt1 = Entry(self.f1, width=50,font=font2)
        self.txt1.grid(row=0, column=1, pady=10)

        # selecting vehicle type
        Label(self.f1, text="Select Vehicle Type :", font=font1,bg="seagreen2").grid(row=1, column=0, padx=10, sticky='w')

        self.vtypes = ("Two Wheeler", "Three Wheeler", "Four Wheeler", "Six Wheeler")

        self.txt2 = ttk.Combobox(self.f1, values=self.vtypes, state="readonly", font=font2, width=47)
        self.txt2.current(0)
        self.txt2.grid(row=1, column=1, pady=10)

        Label(self.f1, text="Owner Name:", font=font1,bg="seagreen2").grid(row=2, column=0, padx=10, sticky='w')
        self.txt3 = Entry(self.f1, font=font2, width=50)
        # self.txt3.insert(0, 20)
        # self.txt3.config(state="readonly")
        self.txt3.grid(row=2, column=1, pady=10)

        self.desg=("Administration Staff","Parking Staff","Janitors Staff","Customer","Other")
        Label(self.f1, text="Designation:", font=font1,bg="seagreen2").grid(row=3, column=0, padx=10, sticky='w')
        self.txt4 = ttk.Combobox(self.f1, values=self.desg, state="readonly", font=font2, width=47)
        self.txt4.current(3)
        self.txt4.grid(row=3, column=1, pady=10)

        Label(self.f1, text="Address:", font=font1,bg="seagreen2").grid(row=4, column=0, padx=10, sticky='w')
        self.txt5 = Entry(self.f1, font=font2, width=50)
        self.txt5.grid(row=4, column=1, pady=10)

        Label(self.f1, text="Mobile:", font=font1,bg="seagreen2").grid(row=5, column=0, padx=10, sticky='w')
        self.txt6 = Entry(self.f1, font=font2, width=50)
        self.txt6.grid(row=5, column=1, pady=10)

        Label(self.f1, text="Email:", font=font1,bg="seagreen2").grid(row=6, column=0, padx=10, sticky='w')
        self.txt7 = Entry(self.f1, font=font2, width=50)
        self.txt7.grid(row=6, column=1, pady=10)

        Label(self.f1, text="Gender:", font=font1,bg="seagreen2").grid(row=7, column=0, padx=10, sticky='w')
        self.gen=("Male","Female","Other")
        self.txt8 = ttk.Combobox(self.f1, values=self.gen, state="readonly", font=font2, width=47)
        self.txt8.grid(row=7, column=1, pady=10)

        self.bt1 = Button(self.f1, text="Press to Add", font="cambria 13 bold", foreground="green",
                          command=self.addVehicleRegistration)
        self.bt1.bind("<Return>", self.addVehicleRegistration)
        self.bt1.grid(row=8, column=1, pady=10)

        self.f1.pack()

        self.root.option_add('*TCombobox*Listbox.font', font2)
        self.root.mainloop()

    def addVehicleRegistration(self, event=None):
        # self.id = self.txt1.get()
        self.vno =  self.txt1.get()
        self.vtype = self.txt2.get()
        self.oname = self.txt3.get()
        self.des = self.txt4.get()
        self.address = self.txt5.get()
        self.mob = self.txt6.get()
        self.email = self.txt7.get()
        self.gender = self.txt8.get()

        alpha=re.compile("[a-zA-Z]")
        spc= re.compile('[@_!#$%^&*()<>?/\|}{~:+.;,"\'-]')

        conn = connection.Connect()
        cr = conn.cursor()

        q=f"select vehiclenumber from vehicle_registration"
        cr.execute(q)
        res=cr.fetchall()
        #print(res)

        if self.vno == "" or self.vtype == "" or self.oname == "" or self.des == "" or self.address == "" or self.mob == "" or self.email == "" or self.gender == "":
            showerror("Error", " All fields required ",parent=self.root)
        elif len(self.mob)!=10 or alpha.search(self.mob)!=None or spc.search(self.mob)!=None:
            showerror("Error", " Please Enter a Correct 10-Digit Number!",parent=self.root)
        elif any([self.vno in i for i in res ]):
            q=f"select id from vehicle_registration where vehiclenumber='{self.vno}'"
            cr.execute(q)
            vid=cr.fetchone()
            showerror("Error",f"The Vehicle Number: {self.vno} is already Registered\nYour Registered Vehicle ID is '{vid[0]}'")
        else:
            q = f"Insert into vehicle_registration values (NULL,'{self.vno}','{self.vtype}','{self.oname}','{self.des}','{self.address}','{self.mob}','{self.email}','{self.gender}')"
            #print(q)
            cr.execute(q)
            conn.commit()
            showinfo("Success", "Vehicle Registered Successfully!",parent=self.root)
            self.root.destroy()

# main()