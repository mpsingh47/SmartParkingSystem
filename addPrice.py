from tkinter import *
from tkinter import ttk 
from tkinter.messagebox import *
import connection

class main:
    #print("Add Price")
    def __init__(self):
        self.root = Tk()
        self.root.geometry("600x550+0+0")
        self.root.title("Add Price")
        self.root.config(bg="orange2")
        Label(self.root, text="Adding the Price", font="rockwell 35 bold underline",fg="green",bg="seagreen2").pack(fill=X,pady=30)

        self.f1 = Frame(self.root,bg="orange2")

        font1="arial 15 bold"
        font2="arial 10 bold"
        
        # Label(self.f1, text="Enter id:", font=font1).grid(row=0, column=0, padx=5, sticky='w')
        # self.txt1 = Entry(self.f1, width=50)
        # self.txt1.grid(row=0, column=1, pady=10)

        #selecting vehicle type
        Label(self.f1, text="Select Vehicle Type:", font=font1,bg="seagreen2").grid(row=1, column=0,padx=5, sticky='w')
        
        self.vtypes=("Two Wheeler","Three Wheeler","Four Wheeler","Six Wheeler")
        
        self.txt2 = ttk.Combobox(self.f1,values=self.vtypes,state="readonly" ,font=font2,width=47)
        self.root.option_add('*TCombobox*Listbox.font', font2)
        self.txt2.current(0)
        self.txt2.bind("<<ComboboxSelected>>",self.autoPriceSelection)
        self.txt2.grid(row=1, column=1, padx=5,pady=15)
        
        
        Label(self.f1, text="Ticket Price (Rs.):", font=font1,bg="seagreen2").grid(row=2, column=0, padx=5, sticky='w')
        self.txt3 = Entry(self.f1,font=font2, width=50,textvariable=20)
        self.txt3.insert(0,20)
        self.txt3.config(state="readonly")
        self.txt3.grid(row=2, column=1, padx=5,pady=15)

        Label(self.f1, text="Enter Description:", font=font1,bg="seagreen2").grid(row=3, column=0, padx=5, sticky='w')
        self.txt4= Entry(self.f1 ,font=font2, width=50)
        self.txt4.grid(row=3, column=1, padx=5,pady=15)

        self.bt1 = Button(self.f1, text="Press to Add",font="cambria 13 bold",foreground="green", command=self.addPrice)
        self.bt1.bind("<Return>", self.addPrice)
        self.bt1.grid(row=4, column=1, pady=10)

        self.f1.pack()

        self.root.mainloop()


    def addPrice(self, event=None):
        #self.id = self.txt1.get()
        vtype = self.txt2.get()
        pr = self.txt3.get()
        des = self.txt4.get()

        

        conn = connection.Connect()
        cr = conn.cursor()
        if vtype == "" or pr == "" or des== "" :
            showerror("", " All fields required ",parent=self.root)
        else:
            q = f"Insert into parking_charge values (NULL,'{vtype}',{pr},'{des}')"
            print(q)
            cr.execute(q)
            conn.commit()
            showinfo("Success", "Price added successfully",parent=self.root)
            self.root.destroy()

    def autoPriceSelection(self,event):
        vt=self.txt2.get()
        self.txt3.config(state="normal")
        self.txt3.delete(0,END)
        
        if vt==self.vtypes[0]:                
            self.txt3.insert(0,20)
        elif vt==self.vtypes[1]:
            self.txt3.insert(0,30)
        elif vt==self.vtypes[2]:
            self.txt3.insert(0,50)
        elif vt==self.vtypes[3]:
            self.txt3.insert(0,100)
        else:
            showerror("","Select Proper Vehicle Type")
        self.txt3.config(state="readonly")

    
# main()