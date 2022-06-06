from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import connection


class main:
    # print("View Price")

    def __init__(self):
        self.root = Tk()
        self.root.state("zoomed")
        self.root.title("View Issued Monthly Pass")
        self.root.config(bg="royalblue")

        Label(self.root, text="View Issued Monthly Pass ", font="rockwell 38 bold underline", fg="red", bg="orange", relief=SUNKEN,
              bd=6).pack(pady=10, ipadx=10)

        self.font2 = "arial 10 bold"
        # creating Frame for search
        self.f0 = Frame(self.root, bg="royal blue")
        Label(self.f0, text="Search By", font=self.font2).grid(row=0, column=0, padx=5)

        self.search_type = ("Id", "VehicleId", "PassId")
        self.f0txt1 = ttk.Combobox(self.f0, values=self.search_type, state="readonly", font=self.font2)
        self.f0txt1.grid(row=0, column=1, padx=5)

        Label(self.f0, text="Enter Value:", font=self.font2).grid(row=0, column=2, padx=5)

        self.f0txt2 = Entry(self.f0, font=self.font2)
        self.f0txt2.grid(row=0, column=4, padx=5)

        Button(self.f0, text="Search", width=10, font=self.font2, fg="green", bg="yellow",
               command=self.viewPriceSearch).grid(row=0, column=5, padx=5, pady=10)
        Button(self.f0, text="ShowAll", width=10, font=self.font2, fg="green", bg="green yellow",
               command=self.getValues).grid(row=0, column=6, padx=5, pady=10)

        self.f0.option_add('*TCombobox*Listbox.font', self.font2)
        self.f0.pack(pady=10)

        self.f1 = Frame(self.root)

        style = ttk.Style(self.root)
        style.theme_use("winnative")  # setting a theme

        style.configure("Treeview", background="hotpink", rowheight=25, fieldbackground="hotpink",
                        foreground="black")  # modify color of treeview

        style.map('Treeview', background=[('selected', 'darkorchid1')])  # modify color of selected items in treeview

        style.configure("Treeview.Heading", font='rockwell 14 bold italic')  # Modify the font of the headings
        style.configure("Treeview", highlightthickness=0, font='times 12')  # Modify the font of the body

        scroll_y = Scrollbar(self.f1, orient=VERTICAL)

        col = ('id', 'vehicleid', 'passid','dateofissue','dateofexpiry','type')
        self.obj = ttk.Treeview(self.f1, columns=col, yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.obj.yview)

        for i in col:
            self.obj.heading(i, text=i.capitalize(),anchor="w")
        self.obj["show"] = "headings"

        # self.obj.column("#1", anchor="center")
        # self.obj.column("#2", anchor="center")
        # self.obj.column("#3", anchor="center", width=150)


        self.getValues()
        self.obj.pack()
        self.f1.pack()

        self.root.mainloop()

    def getValues(self):
        conn = connection.Connect()
        cur = conn.cursor()
        q = "Select * from issue_monthly_pass"
        cur.execute(q)
        result = cur.fetchall()
        self.obj.delete(*self.obj.get_children())
        count = 0
        for row in result:
            self.obj.insert("", index=count, values=row)
            count += 1
        self.f0txt1.set("")
        self.f0txt2.delete(0, END)

    def viewPriceSearch(self):
        conn = connection.Connect()
        cur = conn.cursor()

        if self.f0txt1.get() == self.search_type[0]:
            q = f"Select * from issue_monthly_pass where id={self.f0txt2.get()}"

        elif self.f0txt1.get() == self.search_type[1]:
            q = f"Select * from issue_monthly_pass where vehicleid={self.f0txt2.get()}"

        elif self.f0txt1.get() == self.search_type[2]:
            q = f"Select * from issue_monthly_pass where passid={self.f0txt2.get()}"

        cur.execute(q)
        result = cur.fetchall()
        self.obj.delete(*self.obj.get_children())

        count = 0
        for row in result:
            self.obj.insert("", index=count, values=row)
            count += 1
        self.r1.destroy()
# main()