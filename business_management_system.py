'''
Python Project :
Stock Control
GUI with a storage database

by --------------
Akash Chakraborty ECE - 126
Neelakshi Talukdar ECE - 135

-----------------------------------------------------------------------------------------------------------------------
| This is a stock control system for a Wholesale trader, who supplies goods to a limited number of big retail sellers |
-----------------------------------------------------------------------------------------------------------------------

'''



import sqlite3
from tkinter import*
from tkinter import Tk, StringVar, ttk
import random
import datetime
from datetime import date
import time
import random


root = Tk() # thus just like in OOP , root has been declared as the object
root.geometry("1350x750+0+0")  # setting up the screen resolution
root.title("Stock Control System")
root.configure(background = "white")
root.iconbitmap("guiicon.ico")


TopFrame = Frame(root, width = 1350, height = 100, bd = 14, relief = 'raise')  # making a frame #the bd is for giviing the frame a 3-d effect
TopFrame.pack(side=TOP)  # placing the frame at the top


BottomFrame = Frame(root, width = 1350, height = 200, bd = 14, relief = 'raise') # making the bottom frame
BottomFrame.pack(side=BOTTOM)  # placing the frame at the bottom


LeftMidFrame = Frame(BottomFrame, width = 750, height = 1000, bd = 14, relief = 'raise')  # making a frame ## the bd is for giviing the frame a 3-d effect
LeftMidFrame.pack(side=LEFT)  # placing the frame at the left



RightMidFrame = Frame(BottomFrame, width = 600, height = 1000, bd = 14, relief = 'raise')  # making a frame ## the bd is for giviing the frame a 3-d effect
RightMidFrame.pack(side=RIGHT)  # placing the frame at the right

# now adding a label to the top frame
lblTitle = Label(TopFrame, font=('Times New Roman',40, 'bold'), text = "Apollo Arial Robotics.", bd = 10, width = 39, justify = 'center')
lblTitle.grid(row = 0, column = 0) # justify will actually place the text in the position specified, bd was not necessary

lblTitle = Label(TopFrame, font=('Times New Roman',10, 'bold'), text = "Factory Sales Department", bd = 10, width = 20, justify = 'center')
lblTitle.grid(row = 1, column = 0)

#=============================================================Variables====================================================================================

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = StringVar()
var9 = StringVar()
VAT = StringVar()  # variable for VAT combobox
Tax = StringVar() # variable for the TAX
Date1 = StringVar()
Date2 = StringVar()
Date3 = StringVar()
CustomerID = StringVar()
OrderID = StringVar()
tax = IntVar()
total1 = IntVar()
subtotal1 = IntVar()
Time = StringVar()
noof = IntVar()



var1.set("0")
var2.set("")
var3.set("")
var4.set("")
var5.set("0")  # this variable has been set for customerIDcombobox
var6.set("")
var7.set("")
var8.set("")
var9.set("")
VAT.set("")
Tax.set("0")
CustomerID.set("")
tax.set(0)
total1.set(0)
subtotal1.set(0)
noof.set(0)

OrderID.set(''.join(random.choice('012345678ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')for i in range(10))) # giving a random unique ID
                  

Date1.set(time.strftime("%d-%m-%y"))  # this will act as the order date and warranty valid from date

Time.set(time.strftime(" %H:%M:%S"))

def Product():
    if (var1.get()== "PID001"):      # var1 for product ID
        var2.set("Eagle")            # var2 for product name
        var3.set("5000 rpm motors")  # var3 for product description
        var4.set(5000)               # var4 for Stock level
        var5.set(20)                 # var5 discount 
        var6.set(4500)                # var6 cost per unit
        var9.set("2 years")
        if(VAT.get() == "YES"):
           tax.set(15)
        else:
            tax.set(0)
           
           
        
    elif (var1.get()== "PID002"):
        var2.set("Main Frame")
        var3.set("Drone Body(H.D)")
        var4.set(200)
        var5.set(30)
        var6.set(3890)
        var9.set("1 year")
        if(VAT.get() == "YES"):
            tax.set(15)
        else:
            tax.set(0)    
    elif (var1.get()== "PID003"):
        var2.set("Wings X")
        var3.set("propeller clockwise")
        var4.set(346)
        var5.set(50)
        var6.set(5000)
        var9.set("1 year")
        if(VAT.get() == "YES"):
            tax.set(15)
        else:
            tax.set(0)
    elif (var1.get()== "PID004"):
        var2.set("Wings-C")
        var3.set("propellor anticlockwise")
        var4.set(346)
        var5.set(50)
        var6.set(4000)
        var9.set("2 years")
        if(VAT.get() == "YES"):
            tax.set(15)
        else:
            tax.set(0)
    elif (var1.get()== "PID005"):
        var2.set("Compass-X")
        var3.set("Gyro-Sensors")
        var4.set(346)
        var5.set(50)
        var6.set(6000)
        var9.set("1 year")
        if(VAT.get() == "YES"):
            tax.set(15)
        else:
            tax.set(0)
    elif (var1.get()== "PID006"):
        var2.set("Power-X")
        var3.set("Battery set")
        var4.set(346)
        var5.set(50)
        var6.set(800)
        var9.set("NONE")
        if(VAT.get() == "YES"):
            tax.set(15)
        else:
            tax.set(0)
    elif (var1.get()== "PID007"):
        var2.set("Connect")
        var3.set("Wire and screw Set")
        var4.set(346)
        var5.set(50)
        var6.set(500)
        var9.set("NONE")
        if(VAT.get() == "YES"):
            tax.set(15)
    elif (var1.get()== "PID008"):
        var2.set("ESC")
        var3.set("Electronic Speed Control")
        var4.set(346)
        var5.set(50)
        var6.set(7000)
        var9.set("2 years")
        if(VAT.get() == "YES"):
            tax.set(15)
        else:
            tax.set(0)
    elif (var1.get()== "PID009"):
        var2.set("FCB")
        var3.set("Flight Control Board")
        var4.set(346)
        var5.set(50)
        var6.set(8000)
        var9.set("2 years")
        if(VAT.get() == "YES"):
            tax.set(15)
        else:
            tax.set(0)
    elif (var1.get()== "PID010"):
        var2.set("Via")
        var3.set("Radio transmitter and receiver")
        var4.set(346)
        var5.set(50)
        var6.set(750)
        var9.set("2 years")
        if(VAT.get() == "YES"):
            tax.set(15)
        else:
            tax.set(0)
    elif (var1.get()== "PID011"):
        var2.set("Flash")
        var3.set("6000 rpm motors")
        var4.set(346)
        var5.set(50)
        var6.set(4000)
        var9.set("1 year")
        if(VAT.get() == "YES"):
            tax.set(15)
        else:
            tax.set(0)

#=============================================================Prodcut Details=======================================================================

lblProductID = Label(LeftMidFrame, font=('Times New Roman',16, 'bold'), text = "Product ID", bd = 10, width = 20, anchor = 'w') # anchor anchors the name to the specified direction, in this case west(w)
lblProductID.grid(row = 0, column = 0)

# creating a combobox for product ID

cmbProductID = ttk.Combobox(LeftMidFrame, textvariable = var1, state = 'readonly', font=('Times New Roman',16, 'bold'), width = 20)
cmbProductID['value'] = ('','PID001','PID002','PID003','PID004','PID005','PID006','PID007','PID008','PID009','PID010','PID011')
cmbProductID.current(0)
cmbProductID.grid(row = 0, column = 1)

lblProductName1 = Label(LeftMidFrame, font=('Times New Roman',16, 'bold'), text = "Product Name", bd = 10, width = 20, anchor = 'w')
lblProductName1.grid(row = 1, column = 0)
lblProductName2 = Label(LeftMidFrame, font=('Times New Roman',16, 'bold'), textvariable = var2, bd = 10, width = 17, relief = 'sunken')
lblProductName2.grid(row = 1, column = 1)

lblDescription1 = Label(LeftMidFrame, font=('Times New Roman',16, 'bold'), text = "Description", bd = 10, width = 20, anchor = 'w')
lblDescription1.grid(row = 2, column = 0)
lblDescription2 = Label(LeftMidFrame, font=('Times New Roman',16, 'bold'), textvariable = var3, bd = 10, width = 17, relief = 'sunken')
lblDescription2.grid(row = 2, column = 1)

lblStockLevel1 = Label(LeftMidFrame, font=('Times New Roman',16, 'bold'), text = "Stock Level", bd = 10, width = 20, anchor = 'w')
lblStockLevel1.grid(row = 3, column = 0)
lblStockLevel2 = Label(LeftMidFrame, font=('Times New Roman',16, 'bold'), textvariable = var4, bd = 10, width = 17, relief = 'sunken')
lblStockLevel2.grid(row = 3, column = 1)


lblReorderDate1 = Label(LeftMidFrame, font=('Times New Roman',16, 'bold'), text = "Recorder Date", bd = 10, width = 20, anchor = 'w')
lblReorderDate1.grid(row = 8, column = 0)
lblReorderDate2 = Label(LeftMidFrame, font=('Times New Roman',16, 'bold'), textvariable = Date1, bd = 10, width = 17, relief = 'sunken')
lblReorderDate2.grid(row = 8 , column = 1)

lblDiscount1 = Label(LeftMidFrame, font=('Times New Roman',16, 'bold'), text = "Discount", bd = 10, width = 20, anchor = 'w')
lblDiscount1.grid(row = 9, column = 0)
lblDiscount2 = Label(LeftMidFrame, font=('Times New Roman',16, 'bold'), textvariable = var5, bd = 10, width = 17, relief = 'sunken')
lblDiscount2.grid(row = 9 , column = 1)

lblCostPerUnit1 = Label(LeftMidFrame, font=('Times New Roman',16, 'bold'), text = "Cost Per Unit", bd = 10, width = 20, anchor = 'w')
lblCostPerUnit1.grid(row = 10, column = 0)
lblCostPerUnit2 = Label(LeftMidFrame, font=('Times New Roman',16, 'bold'), textvariable = var6, bd = 10, width = 17, relief = 'sunken')
lblCostPerUnit2.grid(row = 10, column = 1)


#================================================================Right Mid Frame=====================================================================


lblValidFrom1 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), text = "Warranty time", bd = 10, width = 10, anchor = 'w')
lblValidFrom1.grid(row = 0, column = 0)
lblValidFrom2 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), textvariable = var9, bd = 10, width = 10, relief = 'sunken')
lblValidFrom2.grid(row = 0, column = 1)


lblOrderTime = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), text = "Order Time", bd = 10, width = 10, anchor = 'w')
lblOrderTime.grid(row = 0, column = 2)
lblOrderTime2 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), textvariable =Time, bd = 10, width = 10, relief = 'sunken')
lblOrderTime2.grid(row = 0, column = 3)


lblOderID1 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), text = "Order ID", bd = 10, width = 10, anchor = 'w')
lblOderID1.grid(row = 1, column = 0)
lblOderID2 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), textvariable = OrderID, bd = 10, width = 15, relief = 'sunken')
lblOderID2.grid(row = 1, column = 1)


# we will not do the combo box for Order ID as it will be input by the admin  or will be automtically given by the machine


lblDateOrdered1 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), text = "Date", bd = 10, width =3, anchor = 'w')
lblDateOrdered1.grid(row = 1, column = 2)
lblDateOrdered2 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), textvariable = Date1, bd = 10, width = 9, relief = 'sunken',anchor = 'w')
lblDateOrdered2.grid(row = 1, column = 3)


lblCustomerID1 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), text = "CustomerID", bd = 10, width = 10, anchor = 'w')
lblCustomerID1.grid(row = 2, column = 0)


# customer id combobox


cmbCustomerID2 = ttk.Combobox(RightMidFrame, textvariable = CustomerID, state = 'readonly', font=('Times New Roman',16, 'bold'), width = 12)
cmbCustomerID2['value'] = ('','CID0079','CID0080','CID0081','CID0082','CID0083','CID0084','CID0085','CID0086','CID0087','CID0088','CID0089','CID0090','CID0091','CID0092','CID0093','CID0094','CID0095','CID0096','CID0097','CID0098','CID0099','CID0100','CID0101')
cmbCustomerID2.current(0)
cmbCustomerID2.grid(row = 2, column = 1)


lblNoOfItemsOrdered1 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), text = "No. Of Items", bd = 10, width = 10, anchor = 'w')
lblNoOfItemsOrdered1.grid(row = 2, column = 2)
txtNoOfItemsOrdered2 = Entry(RightMidFrame, font=('Times New Roman',16, 'bold'), textvariable = noof, bd = 10, width = 10)
txtNoOfItemsOrdered2.grid(row = 2, column = 3)


lblFirstName1 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), text = "First Name", bd = 10, width = 10, anchor = 'w')
lblFirstName1.grid(row = 3, column = 0)
txtFirstName2 = Entry(RightMidFrame, font=('Times New Roman',16, 'bold'), textvariable = StringVar(), bd = 10, width = 20)
txtFirstName2.grid(row = 3, column = 1)


lblItemOrdered1 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), text = "Item Ordered", bd = 10, width = 10, anchor = 'w')
lblItemOrdered1.grid(row = 3, column = 2)
lblItemOrdered2 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), textvariable = var1, bd = 10, width = 10 , relief = 'sunken')
lblItemOrdered2.grid(row = 3, column = 3)


lblSurname1 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), text = "Surname", bd = 10, width = 10, anchor = 'w')
lblSurname1.grid(row = 4, column = 0)
txtSurname2 = Entry(RightMidFrame, font=('Times New Roman',16, 'bold'),textvariable = StringVar(), bd = 10, width = 20)
txtSurname2.grid(row = 4, column = 1)


lblPaymentMethod1 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), text = "Payment Method", bd = 10, width = 12, anchor = 'w')
lblPaymentMethod1.grid(row = 4, column = 2)


#payment method combobox

cmbPaymentMethod2 = ttk.Combobox(RightMidFrame, textvariable = var8, state = 'readonly', font=('Times New Roman',16, 'bold'), width = 11)
cmbPaymentMethod2['value'] = ('','Cash','Master Card','Visa','Rupay','PayPal','Paytm','BHIM','Tez')
cmbPaymentMethod2.current(0)
cmbPaymentMethod2.grid(row = 4, column = 3)



lblAddress1 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), text = "Address", bd = 10, width = 10, anchor = 'w')
lblAddress1.grid(row = 5, column = 0)
txtAddress2 = Entry(RightMidFrame, font=('Times New Roman',16, 'bold'),textvariable = StringVar(), bd = 10, width = 45)
txtAddress2.grid(row = 5, column = 1, columnspan = 4)

lblAccountType1 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), text = "Account Type", bd = 10, width = 10, anchor = 'w')
lblAccountType1.grid(row = 7, column = 0)

# account type combobox

cmbAccountType2 = ttk.Combobox(RightMidFrame, textvariable = var7, state = 'readonly', font=('Times New Roman',16, 'bold'), width = 10)
cmbAccountType2['value'] = ('','Debit Card','Credit Card','Cash')
cmbAccountType2.current(0)
cmbAccountType2.grid(row = 7, column = 1)



lblVAT1 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), text = "VAT", bd = 10, width = 5, anchor = 'w')
lblVAT1.grid(row = 7, column = 2)

# VAT combobox

cmbVAT2 = ttk.Combobox(RightMidFrame, textvariable = VAT, state = 'readonly', font=('Times New Roman',16, 'bold'), width = 5)
cmbVAT2['value'] = ('','YES','NO')
cmbVAT2.current(0)
cmbVAT2.grid(row = 7, column = 3)


lblTax1 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), text = "Tax", bd = 10, width = 10, anchor = 'w')
lblTax1.grid(row = 8, column = 0)
lblTax2 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), textvariable = tax, bd = 10, width = 10, relief = 'sunken')
lblTax2.grid(row = 8, column = 1)


lblSubTotal1 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), text = "Sub Total", bd = 10, width = 10, anchor = 'w')
lblSubTotal1.grid(row = 8, column = 2)
lblSubTotal2 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), textvariable = subtotal1, bd = 10, width = 10, relief = 'sunken')
lblSubTotal2.grid(row = 8, column = 3)


lblTotal1 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), text = "Total", bd = 10, width = 10, anchor = 'w')
lblTotal1.grid(row = 9, column = 0)
lblTotal2 = Label(RightMidFrame, font=('Times New Roman',16, 'bold'), textvariable = total1, bd = 10, width = 10, relief = 'sunken')
lblTotal2.grid(row = 9, column = 1)


#==============================================================Making Buttons===========================================================================

def subTot():
    a = noof.get()
    b = var6.get()
    subtotal1.set(a*b)
   
ButtonSubTotal = Button(RightMidFrame, font=('Times New Roman',20, 'bold'), text = "Sub Total", command = subTot, bd = 5, width = 10)
ButtonSubTotal.grid(row = 10, column = 0)

def grandTotal():
    if (VAT.get()== "YES"):
        i = subtotal1.get()
        j = (15/100)*i
        total1.set(i+j)
        
    else:
        k = subtotal1.get()
        total1.set(k)

ButtonTotal = Button(RightMidFrame, font=('Times New Roman',20, 'bold'), text = "Total", command = grandTotal,bd = 5, width = 10)
ButtonTotal.grid(row = 10, column = 1)

Exit = Button(RightMidFrame, font=('Times New Roman',20, 'bold'), text = "Exit", bd = 5, width = 10, activebackground='white', command = quit)
Exit.grid(row = 10, column = 3)

def Reset_all():
    cmbProductID.set('')
    txtFirstName2.delete(0,'end')
    txtSurname2.delete(0,'end')
    txtAddress2.delete(0,'end')
    noof.set(0)
    cmbPaymentMethod2.set('')
    cmbVAT2.set('')
    cmbAccountType2.set('')
    cmbCustomerID2.set('')
    var2.set('')
    var3.set('')
    var4.set('')               
    var5.set('')                  
    var6.set('')
    var9.set('')
    total1.set(0)
    subtotal1.set(0)
    tax.set(0)
    OrderID.set(''.join(random.choice('012345678ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')for i in range(10)))
    Date1.set(time.strftime("%d-%m-%y"))
    Time.set(time.strftime(" %H:%M:%S"))
    

Reset = Button(LeftMidFrame, font=('Times New Roman',20, 'bold'), text = "Reset", bd = 5, width = 9, command = Reset_all)
Reset.grid(row = 12, column = 0)

ProductInfo = Button(LeftMidFrame, font=('Times New Roman',20, 'bold'), text = "Product Info", bd = 5, width = 15, command = Product)
ProductInfo.grid(row=11, column = 0)


#===============================================================DataBase========================================================================================


def data_base():
    conn = sqlite3.connect('Sales_Record.db')
    c = conn.cursor()
    
    def create_table():
        c.execute('CREATE TABLE IF NOT EXISTS salesRecord(Customer_ID TEXT, Name TEXT, Surname TEXT, Address TEXT, Order_ID TEXT, Order_Time REAL, Order_Date TEXT, no_of_items REAL, Item TEXT, Warranty_Time TEXT, Payment_Method TEXT,Sub_Total REAL, Tax REAL, Total REAL)')

    def data_entry():
        Customer_ID = CustomerID.get()
        Name = txtFirstName2.get()
        Surname = txtSurname2.get()
        Address = txtAddress2.get()
        Order_ID = OrderID.get()
        Order_Time = Time.get()
        Order_Date = Date1.get()
        no_of_items = noof.get()
        Item = var1.get()
        Warranty_Time = var9.get()
        Payment_Method = var8.get()
        Sub_Total = subtotal1.get()
        Tax = tax.get()
        Total = total1.get()
        c.execute("INSERT INTO salesRecord(Customer_ID, Name, Surname, Address, Order_ID, Order_Time, Order_Date, no_of_items, Item, Warranty_Time, Payment_Method,Sub_Total, Tax, Total) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(Customer_ID, Name, Surname, Address, Order_ID,Order_Time, Order_Date, no_of_items, Item, Warranty_Time, Payment_Method, Sub_Total, Tax, Total))
        conn.commit()

    create_table()
    data_entry()
    c.close()
    conn.close()

ButtonRecordData = Button(RightMidFrame, font=('Times New Roman',20, 'bold'), text = "Record Data", command = data_base, bd = 5, width = 10)
ButtonRecordData.grid(row = 10, column = 2)




#=========================================================================================================================================================================================================================================================================================================================================================================================#
 















root.mainloop()

print("Exit")





