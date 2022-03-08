from tkinter import *
from tkinter import messagebox

# Setting Enviroment
cal=Tk()
cal.geometry("350x175")
cal.title(" GST CALCULATOR")
cal.config(bg="#2C2F35")

def equal():
    global value
    # Checking if correct price values are entered
    if originalprice.get()=="0" or netprice.get()=="0" or originalprice.get()=="" or netprice.get()=="": # If price is zero or empty
        messagebox.showwarning("Invalid input!", "Enter Valid Input\n(Price Can't be zero)")
    elif int(originalprice.get())<0 or int(netprice.get())<0:  # If price is negative
        messagebox.showwarning("Invalid input!", "Enter Valid Input\n(Price Can't be negative)")
    elif int(originalprice.get())>int(netprice.get()):
        messagebox.showwarning("Invalid input!", "Enter Valid Input!\n(Original Price Cannot Be greater Than Net price)")
    else:  
        try:
            value=((int(netprice.get())-int(originalprice.get()))*100)/int(originalprice.get())
            GSTrate.set(value)
            GSTrateEntry.update()
        except Exception as e:
            messagebox.showerror("INVALID INPUT","Invalid Input!")  # If any other error in prices

# To clean entry boxes for new input
def clean():
    GSTrate.set("")
    originalprice.set("")
    netprice.set("")


# Variables
originalprice=StringVar()
netprice=StringVar()
GSTrate=StringVar()
# Entry Boxes
originalpriceEntry=Entry(cal,textvar=originalprice,font="lucida 18 bold",bg="powder blue",fg="black",relief=SUNKEN)
netpriceEntry=Entry(cal,textvar=netprice,font="lucida 18 bold",bg="powder blue",fg="black")
GSTrateEntry=Entry(cal,textvar=GSTrate,font="lucida 18 bold",state=DISABLED)
# Placing Entry Boxes
originalpriceEntry.grid(row=0,column=1,columnspan=3,pady=1)
netpriceEntry.grid(row=1,column=1,columnspan=3,pady=1)
GSTrateEntry.grid(row=2,column=1,columnspan=3,pady=1)
#Configuring entry boxes
netpriceEntry.config(borderwidth=3)
GSTrateEntry.config(borderwidth=3)
originalpriceEntry.config(borderwidth=3)

# Setting up labels
l1=Label(cal,text="ORIGINAL PRICE",font="helvetica 10")
l1.grid(row=0,column=0,padx=1)
l2=Label(cal,text="NET PRICE",font="helvetica 10")
l2.grid(row=1,column=0)
l3=Label(cal,text="GST RATE (%)",font="helvetica 10")
l3.grid(row=2,column=0)


#Buttons
ans=Button(cal,text="CALCULATE",font="lucida 18 bold",relief="raised",activeforeground="red",borderwidth=3,command=equal)
ans.grid(row=3,column=2,columnspan=2,pady=5,sticky=NSEW,padx=2)

clear=Button(cal,text="CLEAR",font="lucida 18 bold",relief="raised",activeforeground="red",borderwidth=3,command=clean)
clear.grid(row=3,column=0,columnspan=2,pady=5,sticky=NSEW,padx=2)

cal.mainloop()






