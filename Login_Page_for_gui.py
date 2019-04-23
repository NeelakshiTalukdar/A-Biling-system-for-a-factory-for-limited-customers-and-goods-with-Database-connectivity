'''
Python Business Login Page

It will open the main Gui Page when we enter
the correct credentials

by-----------------

Neelakshi Talukdar ECE-135
Akash Chakraborty ECE -126


'''






import os

from PIL import ImageTk, Image


import tkinter
from tkinter import*
from tkinter import Tk, StringVar, ttk
import tkinter.messagebox

root= Tk()
root.geometry("1350x750+0+0")
root.title("Admin Login")
root.configure(background = "white")
root.iconbitmap("rooticon.ico")

TopFrame=Frame(root, width=1350, height=200, bd=20, relief= 'raise')
TopFrame.pack(side=TOP)

BottomFrame=Frame(root, width=1350, height=100, bd=20, relief= 'sunken')
BottomFrame.pack(side=BOTTOM)

ImageFrame=Frame(root, width= 450, height= 300, bd=14,relief='raise')
ImageFrame.pack(side=LEFT)

USFrame=Frame(root, width=450, height=300,bd=10,relief='sunken')
USFrame.pack(side=LEFT)


NameFrame=Frame(root,width=450,height=300,bd=14,relief='raise')
NameFrame.pack(side=LEFT)

lblTitle=Label(TopFrame, font=('Times New Roman',50,'bold'),text="Administrator Log-In",bd=15,width=30,justify='center')
lblTitle.grid(row=0,column=0)

lblAddress=Label(BottomFrame, font=('Times New Roman', 20),text="Apollo Arial Robotics",bd=10,width=30,justify='center')
lblAddress.grid(row=0,column=0)

lblAddress=Label(BottomFrame, font=('Times New Roman', 10),text="IT Lab AC2",bd=10,width=30,justify='center')
lblAddress.grid(row=1,column=0)

lblAddress=Label(BottomFrame, font=('Times New Roman', 10),text="Contact: 9876543210 / 7297857398",bd=10,width=30,justify='center')
lblAddress.grid(row=2,column=0)

#=====================================================================Variables=================================================================================

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = IntVar()
var5 = IntVar()


var1.set("")
var2.set("")
var3.set("")
var4.set("")
var5.set("")


img = PhotoImage(file = "U46_PNG-101320-380x380.png")

img2 = PhotoImage(file = "white.png")

#======================================================================MainBody======================================================================


Username=Label(USFrame, font=('Franklin Gothic Book', 22, "bold"),text="User Name :",bd=10,width=19, relief = "raise")
Username.grid(row=0,column=0)
UserName = ttk.Combobox(USFrame, textvariable = var1, state = 'readonly', font=('Times New Roman',16, 'bold'), width = 11)
UserName['value'] = (' ','Neelakshi','Akash')
UserName.current(0)
UserName.grid(row = 0, column = 1)


lblPassword=Label(USFrame, font=('Franklin Gothic Book',22, "bold"),text="Password :",bd=10,width=19, relief = "raise")
lblPassword.grid(row=2,column=0)
txtPassword=Entry(USFrame, font=('Times New Roman', 16), show = "*", textvariable = StringVar(), bd=10,width=12)
txtPassword.grid(row=2,column=1)

imageLabel = Label(ImageFrame, image = img)
imageLabel.grid(row = 0, column = 0)

image2Label = Label(NameFrame, image = img2)
image2Label.grid(row=0, column = 0)



#======================================================================Buttons=========================================================================


def my_callback():
    command= ("E:\\Akash\\Python_project\\business_management_system.py")
    #var2 = txtPassword.get()
    if(txtPassword.get() == "admin123"):
        os.system(command)
    else:
        
        tkinter.messagebox.showinfo('ERROR!','You entered a Wrong password!')

        
Login=Button(USFrame, font=('Times New Roman', 16, 'bold'),text="Log In",command = my_callback, bd=5,width=10)
Login.grid(row=5,column=1)


#======================================================================================================================================================

root.mainloop()
