# from tkinter import *
# from tkinter import ttk
# class main:
#     def __init__(self):
#         self.root=Tk()
#         Label(self.root,text="hello",font="times 10",fg="red",bg="blue").pack()
#         self.root.mainloop()

# main()


# import tkinter as tk
# from tkinter import ttk 

# tkwindow = tk.Tk()
# v=['a','b','c']
# cbox = ttk.Combobox(tkwindow, values=v, state='readonly')
# cbox.grid(column=0, row=0)

# def p(*args):
#     #print(event)
#     if cbox.get()==v[0]:
#         print("a")
#     elif cbox.get()=='b':
#         print("b")
#     elif cbox.get()=='c':
#         print("c")

# cbox.bind("<<ComboboxSelected>>", p)

# tkwindow.mainloop()

from datetime import *
d=datetime.now().strftime("%B %d, %Y")
print(d)
print(type(d))