from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import datetime 

import connection


class main:
    def __init__(self,vnum):
        self.root = Toplevel()
        self.root.geometry("600x550+600+50")
        self.root.title("Demo Form")
        self.root.config(bg="indianred")
        Label(self.root, text="Vehicle Form", font="rockwell 35 bold underline", fg="green",
              bg="seagreen2").pack(fill=X, pady=30)

        self.f1 = Frame(self.root,bg="indianred")

        Label(self.f1, text="Vehicle Number:", font="cambria 15 bold", bg="seagreen2").grid(row=0,column=0,padx=10,pady=10,sticky='w')
        self.txt1 = Entry(self.f1, font="cambria 13 bold", width=30, textvariable=20)
        self.txt1.insert(0,vnum)
        self.txt1.grid(row=0,column=1,padx=10, pady=10,sticky='w')

        self.bt1 = Button(self.f1, text="Search", font="cambria 13 bold", foreground="green",command=self.formChecking)
        self.bt1.grid(row=0,column=2,padx=5,pady=5)

        Label(self.f1, text="Vehicle Id:", font="cambria 15 bold", bg="seagreen2").grid(row=1, column=0, padx=10,
                                                                                            pady=10,sticky='w')
        self.txt2 = Entry(self.f1, font="cambria 13 bold", width=30)
        self.txt2.config(state="readonly")
        self.txt2.grid(row=1, column=1, padx=10, pady=10,sticky='w')

        Label(self.f1, text="Date:", font="cambria 15 bold", bg="seagreen2").grid(row=2, column=0, padx=10,
                                                                                        pady=10,sticky='w')
        self.txt3 = Entry(self.f1, font="cambria 13 bold", width=30)
        self.txt3.config(state="readonly")
        self.txt3.grid(row=2, column=1, padx=10, pady=10,sticky='w')

        Label(self.f1, text="Time:", font="cambria 15 bold", bg="seagreen2").grid(row=3, column=0, padx=10,
                                                                                        pady=10,sticky='w')
        self.txt4 = Entry(self.f1, font="cambria 13 bold", width=30)
        self.txt4.config(state="readonly")
        self.txt4.grid(row=3, column=1, padx=10, pady=10,sticky='w')

        Label(self.f1, text="Vehicle Type:", font="cambria 15 bold", bg="seagreen2").grid(row=4, column=0, padx=10,
                                                                                        pady=10,sticky='w')
        self.txt5 = Entry(self.f1, font="cambria 13 bold", width=30)
        self.txt5.config(state="readonly")
        self.txt5.grid(row=4, column=1, padx=10, pady=10,sticky='w')

        Label(self.f1, text="Fare:", font="cambria 15 bold", bg="seagreen2").grid(row=5, column=0, padx=10,
                                                                                        pady=10,sticky='w')
        self.txt6 = Entry(self.f1, font="cambria 13 bold", width=30)
        self.txt6.config(state="readonly")
        self.txt6.grid(row=5, column=1, padx=10, pady=10,sticky='w')

        self.bt2 = Button(self.f1, text="Submit the Form", font="cambria 13 bold", foreground="green",
                          command=self.formSubmit)
        self.bt2.grid(row=6, column=1, padx=5, pady=5)



        self.f1.pack(padx=10,pady=15)


        self.root.mainloop()


    def formChecking(self):
        if  self.txt2.get()=="" and self.txt3.get()=="" and self.txt4.get()=="" and self.txt5.get()=="" and self.txt6.get()=="" :
            self.vno = self.txt1.get()
            print(self.vno)



            conn = connection.Connect()
            cur = conn.cursor()

            q=f"select id,vehicletype from vehicle_registration where vehiclenumber = '{self.vno}'"
            cur.execute(q)
            result = cur.fetchone()
            print(result)
            if result==None:
                ans= askyesno("Vehicle Not Registered","Your vehicle is not registered \n\nPlease Register the Vehicle\n\nDo you want to Register?",parent=self.root)
                if ans:
                    import addVehicleRegistration
                    addVehicleRegistration.main()
            else:
                self.txt2.config(state="normal")
                self.txt3.config(state="normal")
                self.txt4.config(state="normal")
                self.txt5.config(state="normal")
                self.txt6.config(state="normal")

                self.txt2.insert(0, result[0])
                self.txt3.insert(0, datetime.datetime.now().strftime("%B %d, %Y"))
                self.txt4.insert(0, datetime.datetime.now().strftime("%H:%M:%S"))
                self.txt5.insert(0,result[1])

                self.txt2.config(state="readonly")
                self.txt3.config(state="readonly")
                self.txt4.config(state="readonly")
                self.txt5.config(state="readonly")

                q = f"select id from issue_monthly_pass where vehicleid = {result[0]}"
                cur.execute(q)
                result2 = cur.fetchone()
                print("R@+",result2)
                if result2 == None:
                    vtypes=("Two Wheeler","Three Wheeler","Four Wheeler","Six Wheeler")
                    ourtype= result[1]
                    if ourtype==vtypes[0]:
                        self.txt6.insert(0, "20")
                    elif ourtype==vtypes[1]:
                        self.txt6.insert(0, "30")
                    elif ourtype==vtypes[2]:
                        self.txt6.insert(0, "50")
                    elif ourtype==vtypes[3]:
                        self.txt6.insert(0, "100")
                    else:
                        showerror("Error", "Unsupported Vehicle Type Found")

                else:
                    self.txt6.insert(0, "Monthly Pass")


    def formSubmit(self):
        self.vno = self.txt1.get()
        self.vid = self.txt2.get()
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.time = datetime.datetime.now().strftime("%H:%M:%S")
        self.vtype = self.txt5.get()
        self.fare = self.txt6.get()

        conn = connection.Connect()
        cur = conn.cursor()

        if self.vno=="" or self.vid=="" or self.date=="" or self.time=="" or self.fare==""  :
            showerror("Error","All fields are required",parent=self.root)
        elif self.fare=="Monthly Pass":
            q=f"insert into entry values(NULL,{self.vid},'{self.date}','{self.time}','Monthly Pass')"
            cur.execute(q)
            conn.commit()
            showinfo("Success","Form Submitted Successfully",parent=self.root)
            self.root.destroy()
        else:
            q=f"insert into entry values(NULL,{self.vid},'{self.date}','{self.time}','Cash')"
            cur.execute(q)
            conn.commit()
            
            q=f"insert into transaction values(NULL,{self.vid},'{self.date}','{self.time}',{float(self.fare)})"
            cur.execute(q)
            conn.commit()


            showinfo("Success","Form Submitted Successfully",parent=self.root)
            self.root.destroy()

# main("PB02AA9988")