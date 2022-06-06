from tkinter import *
from tkinter import ttk 
from tkinter.messagebox import *
from PIL import Image,ImageTk
import datetime
from itertools import count, cycle


import addUser
import viewUser
import changeAdminPass
import addPrice
import viewPrice
import addMonthlyPass
import viewMonthlyPass
import addVehicleRegistration
import viewVehicleRegistration
import addIssueMonthlyPass
import viewIssueMonthlyPass
import fileDemo



class main:
        
    def __init__(self, email):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('Welcome to Dashboard')

        self.root_menu = Menu(self.root)
        self.root.config(menu=self.root_menu,bg="navy")
        
        #Profile menu
        self.profileMenu = Menu(self.root_menu, tearoff=0,font='helvetica 11 bold',fg='royalblue3',activebackground='blue',bg="mediumorchid1")
        self.root_menu.add_cascade(label='Profile', menu=self.profileMenu)
        
        #commands of Profile menu
        self.profileMenu.add_command(label='Change Password', command=lambda: changeAdminPass.changePass(email=email))
        self.profileMenu.add_command(label='Contact Us', command=lambda: showinfo("Contact Us","You can contact us on Following Platforms:\n\nEmail: manpreetsinghnangli@gmail.com\nContact No.:7986779359\nLinkedIn: @pythonSquad"))
        self.profileMenu.add_separator()
        self.profileMenu.add_command(label='Exit',command=lambda: self.root.destroy())

        #user management menu
        self.userMenu = Menu(self.root_menu, tearoff=0,font='helvetica 11 bold',fg='royalblue3',activebackground='blue',bg="mediumorchid1")
        self.root_menu.add_cascade(label='User Management', menu=self.userMenu)
        #commands of user management 
        self.userMenu.add_command(label='Add the User', command=lambda: addUser.main())
        self.userMenu.add_command(label='View the User', command=lambda: viewUser.main())

        
        #Price menu
        self.priceMenu = Menu(self.root_menu, tearoff=0,font='helvetica 11 bold',fg='royalblue3',activebackground='blue',bg="mediumorchid1")
        self.root_menu.add_cascade(label='Price', menu=self.priceMenu)
        
        #commands of Price menu
        self.priceMenu.add_command(label='Add the Price', command=lambda: addPrice.main())
        self.priceMenu.add_command(label='View the Price',command=lambda: viewPrice.main())

        #monthlyPass menu
        self.monthlyPassMenu = Menu(self.root_menu, tearoff=0,font='helvetica 11 bold',fg='royalblue3',activebackground='blue',bg="mediumorchid1")
        self.root_menu.add_cascade(label='Monthly Pass', menu=self.monthlyPassMenu)
        
        #commands of monthlyPass menu
        self.monthlyPassMenu.add_command(label='Add Monthly Pass', command=lambda: addMonthlyPass.main())
        self.monthlyPassMenu.add_command(label='View Monthly Passes',command=lambda: viewMonthlyPass.main())

        #vehicleRegistration menu
        self.vehicleRegistrationMenu = Menu(self.root_menu, tearoff=0,
        font='helvetica 11 bold',fg='royalblue3',activebackground='blue',bg="mediumorchid1")
        self.root_menu.add_cascade(label='Vehicle Registration', menu=self.vehicleRegistrationMenu)
        
        #commands of vehicleRegistration menu
        self.vehicleRegistrationMenu.add_command(label='Add Vehicle Registration', command=lambda: addVehicleRegistration.main())
        self.vehicleRegistrationMenu.add_command(label='View Vehicle Registrations',command=lambda: viewVehicleRegistration.main())

        #issueMonthlyPass menu
        self.issueMonthlyPassMenu = Menu(self.root_menu, tearoff=0,
        font='helvetica 11 bold',fg='royalblue3',activebackground='blue',bg="mediumorchid1")
        self.root_menu.add_cascade(label='Issue Monthly Pass', menu=self.issueMonthlyPassMenu)
        
        #commands of issueMonthlyPass menu
        self.issueMonthlyPassMenu.add_command(label='Add Issue Monthly Pass', command=lambda: addIssueMonthlyPass.main())
        self.issueMonthlyPassMenu.add_command(label='View Issued Monthly Passes',command=lambda: viewIssueMonthlyPass.main())

        # Detection menu
        self.detectionMenu = Menu(self.root_menu, tearoff=0,
                                         font='helvetica 11 bold', fg='royalblue3', activebackground='blue',
                                         bg="mediumorchid1")
        self.root_menu.add_cascade(label='Detection', menu=self.detectionMenu)

        # commands of vehicleRegistration menu
        self.detectionMenu.add_command(label='Video Capture')
        self.detectionMenu.add_command(label='Select files',
                                              command=lambda: fileDemo.main())
        #select files-->fileDemo-->plateDemo-->demoForm

        img_dash=ImageTk.PhotoImage(file="dashboard2.png")
        Label(self.root, image=img_dash ,bg="navy",relief=GROOVE,bd=6).grid(row=0,column=1,padx=110)
        #, font=('times', 30 ,'bold' ,'underline'),fg="red1",bg="navy"

        date=datetime.date.today()
        
        self.date_lbl=Label(self.root, text=f"Date : {date.strftime('%d-%b-%Y  ,  %A')}" , font=('cambria', 16 ),fg="yellow",bg="navy")
        self.date_lbl.grid(row=0,column=0,padx=10,pady=4,sticky="n")
        
        self.time_lbl=Label(self.root , font=('cambria', 16 ),fg="yellow",bg="navy")
        self.time_lbl.grid(row=0,column=2,padx=40,pady=4,sticky="n")
        self.tick()

        self.gif_lbl=Label(self.root)
        self.gif_lbl.grid(row=1,column=1,pady=50)
        self.load("cargiphy4.gif")

        self.root.mainloop()
    
    def tick(self):
        time=datetime.datetime.now().strftime("%I:%M:%S %p")
        self.time_lbl.config(text=f"Time : {time}")
        self.time_lbl.after(1000,self.tick)

    """
    A Label that displays images, and plays them if they are gifs
    im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
            #print("delay=",self.delay)
        except:
            self.delay = 100

        if len(frames) == 1:
            self.gif_lbl.config(image=next(self.frames))
        else:
            self.next_frame()

    # def unload(self):
    #     self.gif_lbl.config(image=None)
    #     self.frames = None

    def next_frame(self):
        if self.frames:
            self.gif_lbl.config(image=next(self.frames))
            self.gif_lbl.after(self.delay, self.next_frame)


    # def file(self):
    #     from fileDemo import main
    #     root=Toplevel()
    #     obj=main(root)
    #     root.mainloop()



# main('m@gmail.com')