from tkinter import *
from tkinter import ttk 
from tkinter import messagebox 
from PIL import ImageTk,Image
from tkinter import filedialog

import cv2

class main:
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("550x400+0+40")
        self.root.title("Select Image")
        self.root.config(bg="cyan")
        
        self.file = Label(self.root, text='Choose the Image of Number Plate',font=("gabriola", 25,"bold"),bg="blue").pack(fill=X,pady=10)

        img = Image.open("imagesicon.png")
        self.photo=ImageTk.PhotoImage(img)
        
        self.l1=Label(self.root,image=self.photo,relief=RIDGE,bd=10,bg="cyan")
        self.l1.pack(pady=30)

        self.click=ImageTk.PhotoImage(file="clickhere2.png")
        self.file_button = Button(self.root, image=self.click,bg="cyan", command=self.chooseFile)
        
        self.file_button.pack(pady=10)
        self.root.mainloop()

    def chooseFile(self):
        self.filename = filedialog.askopenfilename(initialdir="/vs_GUI/smart_parking_system", title="Select file", filetypes=((('jpg', '*.jpg'), ("png", "*.png"), ('jpeg', '*.jpeg'))))
        if len(self.filename) != 0 :
            #self.img = cv2.imread(self.filename)
            #self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            #self.file_button.config(text=self.filename)
            import plateDemo2
            plateDemo2.main(self.filename)
        else:
            messagebox.showinfo("info", "Image is Not Selected")
            self.root.destroy()


# obj_fileDemo=main()