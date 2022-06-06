from tkinter import *
from tkinter import ttk 
from tkinter.messagebox import *
from datetime import *
import connection

class main:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("600x550+0+0")
        self.root.title("Add Issue Monthly Pass")
        self.root.config(bg="orange2")
        Label(self.root, text="Issuing Monthly Pass", font="rockwell 35 bold underline",fg="green",bg="seagreen2").pack(fill=X,pady=30)

        self.f1 = Frame(self.root,bg="orange2")

        font1="arial 15 bold"
        font2="arial 10 bold"
        
        # Label(self.f1, text="Enter id:", font=font1).grid(row=0, column=0, padx=5, sticky='w')
        # self.txt1 = Entry(self.f1, width=50)
        # self.txt1.grid(row=0, column=1, pady=10)

        #selecting vehicle type
        
        Label(self.f1, text="Enter Vehicle Id:", font=font1,bg="seagreen2").grid(row=1, column=0, padx=5, sticky='w')
        self.txt1 = Entry(self.f1,font=font2, width=50,textvariable=20)
        self.txt1.grid(row=1, column=1, padx=5,pady=15)
        
        Label(self.f1, text="Select Vehicle Type:", font=font1,bg="seagreen2").grid(row=2, column=0,padx=5, sticky='w')
        self.passvehicletypes=("Two Wheeler","Three Wheeler","Four Wheeler","Six Wheeler")
        
        self.txt2 = ttk.Combobox(self.f1,values=self.passvehicletypes,state="readonly" ,font=font2,width=47)
        self.txt2.bind("<<ComboboxSelected>>",self.autoIdSelection)
        self.txt2.grid(row=2, column=1, padx=5,pady=15)
        
        
        Label(self.f1, text="Date of Issue:", font=font1,bg="seagreen2").grid(row=3, column=0, padx=5, sticky='w')
        self.txt3= Entry(self.f1 ,font=font2, width=50)
        self.txt3.insert(0,datetime.now().strftime("%B %d, %Y"))
        self.txt3.config(state="disabled")
        self.txt3.grid(row=3, column=1, padx=5,pady=15)

        Label(self.f1, text="Date of Expiry:", font=font1,bg="seagreen2").grid(row=4, column=0, padx=5, sticky='w')
        self.txt4= Entry(self.f1 ,font=font2, width=50)
        self.txt4.insert(0,(datetime.now()+timedelta(days=30)).strftime("%B %d, %Y"))
        self.txt4.config(state="disabled")
        self.txt4.grid(row=4, column=1, padx=5,pady=15)

        Label(self.f1, text="Select Type:", font=font1,bg="seagreen2").grid(row=5, column=0,padx=5, sticky='w')
        self.passtype=("Prepaid","Postpaid")
        
        self.txt5 = ttk.Combobox(self.f1,values=self.passtype,state="readonly" ,font=font2,width=47)
        self.txt5.grid(row=5, column=1, padx=5,pady=15)

        self.bt1 = Button(self.f1, text="Press to Add",font="cambria 13 bold",foreground="green", command=self.addIssueMonthlyPass)
        self.bt1.bind("<Return>", self.addIssueMonthlyPass)
        self.bt1.grid(row=7, column=1, pady=10)

        self.f1.pack()

        self.root.option_add('*TCombobox*Listbox.font', font2)
        self.root.mainloop()


    def addIssueMonthlyPass(self, event=None):
        #id auto inc
        vid = self.txt1.get()
        #self.passid
        doi=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        doe=(datetime.now()+timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S") 

        conn = connection.Connect()
        cr = conn.cursor()

        if vid == "" or self.txt2.get()=="" or doi == "" or doe== "" :
            showerror("Error", " All fields required ",parent=self.root)
        else:
            q=f"select vehicletype from vehicle_registration where id={vid}"
            cr.execute(q)
            result=cr.fetchone()
            if result==None:
                showerror("Error", " Your Id doesn't exist in Vehicle_Registration\nPlease Register your Vehicle",parent=self.root)
            elif self.txt2.get() != result[0]:
                showerror("Error", f" Please select Your Valid Vehicle Type\n (Id= { vid } have registration with VehicleType={result[0]}",parent=self.root)
            else:
                q = f"Insert into issue_monthly_pass values (NULL,{vid},{self.passid},'{doi}','{doe}')"
                print(q)
                cr.execute(q)
                conn.commit()
                showinfo("Success", "Price added successfully",parent=self.root)
                self.root.destroy()

    def autoIdSelection(self,event):
        conn=connection.Connect()
        cr=conn.cursor()

        q=f"select id from monthly_pass where vehicletype = '{self.txt2.get()}'"

        cr.execute(q)
        result=cr.fetchone()
        #print(result)
        self.passid=result[0]
        #print(type(self.passid))
        


        conn.commit()
        conn.close()



    
# main()