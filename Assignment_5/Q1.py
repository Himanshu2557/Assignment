from tkinter import *
cal=Tk()
cal.geometry("350x275")
cal.title(" GST CALCULATOR")

def click(event):
    x=cal.focus_get()
    global originalprice,netprice
    mytext=event.widget.cget("text")
    if mytext =="=":
            try:
                oprice=eval(originalpriceEntry.get())
                nprice=eval(netpriceEntry.get())
                if nprice>oprice:
                    GSTrate.set(((nprice-oprice)*100)/oprice)
                    originalpriceEntry.update()
                    netpriceEntry.update()
                    GSTrateEntry.update()
                else:
                    GSTrate.set("ERROR (Net price<Original price)")
            except Exception as e:
                GSTrate.set("ERROR")
                GSTrateEntry.update()

    elif mytext == "C":
        originalprice.set("")
        netprice.set("")
        GSTrate.set("")
        originalpriceEntry.update()
        netpriceEntry.update()
        GSTrateEntry.update()
    else:
        originalprice.set(originalprice.get()+mytext)
        originalpriceEntry.update()



originalprice=StringVar()
netprice=StringVar()
GSTrate=StringVar()

originalpriceEntry=Entry(cal,textvar=originalprice,font="lucida 18 bold",justify=RIGHT,bg="powder blue",fg="black")
netpriceEntry=Entry(cal,textvar=netprice,font="lucida 18 bold",justify=RIGHT,bg="powder blue",fg="black")
GSTrateEntry=Entry(cal,textvar=GSTrate,font="lucida 18 bold",state=DISABLED,justify=RIGHT)

originalpriceEntry.grid(row=0,column=1,columnspan=3)
netpriceEntry.grid(row=1,column=1,columnspan=3)
GSTrateEntry.grid(row=2,column=1,columnspan=3)

netpriceEntry.config(borderwidth=1)
GSTrateEntry.config(borderwidth=1)
originalpriceEntry.config(borderwidth=1)

l1=Label(cal,text="ORIGINAL PRICE",font="helvetica 10")
l1.grid(row=0,column=0)
l2=Label(cal,text="NET PRICE",font="helvetica 10")
l2.grid(row=1,column=0)
l3=Label(cal,text="GST RATE",font="helvetica 10")
l3.grid(row=2,column=0)


#Buttons
b1=Button(cal,text="1",font="lucida 18 bold",relief=SUNKEN,activeforeground="red",border=0)
b1.grid(row=3,column=0,sticky=NSEW,ipady=3)
b1.bind("<Button-1>",click)
b2=Button(cal,text="2",font="lucida 18 bold",relief=SUNKEN,activeforeground="red",border=0)
b2.grid(row=3,column=1,sticky=NSEW,ipady=3)
b2.bind("<Button-1>",click)
b3=Button(cal,text="3",font="lucida 18 bold",relief=SUNKEN,activeforeground="red",border=0)
b3.grid(row=3,column=2,sticky=NSEW,ipady=3)
b3.bind("<Button-1>",click)
b4=Button(cal,text="+",font="lucida 18 bold",relief=SUNKEN,activeforeground="red",border=0)
b4.grid(row=3,column=3,sticky=NSEW,ipady=3)
b4.bind("<Button-1>",click)
b5=Button(cal,text="4",font="lucida 18 bold",relief=SUNKEN,activeforeground="red",border=0)
b5.grid(row=4,column=0,sticky=NSEW,ipady=3)
b5.bind("<Button-1>",click)
b6=Button(cal,text="5",font="lucida 18 bold",relief=SUNKEN,activeforeground="red",border=0)
b6.grid(row=4,column=1,sticky=NSEW,ipady=3)
b6.bind("<Button-1>",click)
b7=Button(cal,text="6",font="lucida 18 bold",relief=SUNKEN,activeforeground="red",border=0)
b7.grid(row=4,column=2,sticky=NSEW,ipady=3)
b7.bind("<Button-1>",click)
b8=Button(cal,text="-",font="lucida 18 bold",relief=SUNKEN,activeforeground="red",border=0)
b8.grid(row=4,column=3,sticky=NSEW,ipady=5)
b8.bind("<Button-1>",click)
b9=Button(cal,text="7",font="lucida 18 bold",relief=SUNKEN,activeforeground="red",border=0)
b9.grid(row=5,column=0,sticky=NSEW,ipady=3)
b9.bind("<Button-1>",click)
b10=Button(cal,text="8",font="lucida 18 bold",relief=SUNKEN,activeforeground="red",border=0)
b10.grid(row=5,column=1,sticky=NSEW,ipady=3)
b10.bind("<Button-1>",click)
b11=Button(cal,text="9",font="lucida 18 bold",relief=SUNKEN,activeforeground="red",border=0)
b11.grid(row=5,column=2,sticky=NSEW,ipady=3)
b11.bind("<Button-1>",click)
b12=Button(cal,text="*",font="lucida 18 bold",relief=SUNKEN,activeforeground="red",border=0)
b12.grid(row=5,column=3,sticky=NSEW,ipady=3)
b12.bind("<Button-1>",click)
b13=Button(cal,text="C",font="lucida 18 bold",relief=SUNKEN,activeforeground="red",border=0)
b13.grid(row=6,column=0,sticky=NSEW,ipady=3)
b13.bind("<Button-1>",click)
b14=Button(cal,text="0",font="lucida 18 bold",relief=SUNKEN,activeforeground="red",border=0)
b14.grid(row=6,column=1,sticky=NSEW,ipady=3)
b14.bind("<Button-1>",click) 
b15=Button(cal,text=".",font="lucida 18 bold",relief=SUNKEN,activeforeground="red",border=0)
b15.grid(row=6,column=2,sticky=NSEW,ipady=3)
b15.bind("<Button-1>",click)
b16=Button(cal,text="/",font="lucida 18 bold",relief=SUNKEN,activeforeground="red",border=0)
b16.grid(row=6,column=3,sticky=NSEW,ipady=3)
b16.bind("<Button-1>",click)
b17=Button(cal,text="=",font="lucida 18 bold",relief=SUNKEN,activeforeground="red",border=0)
b17.grid(row=7,column=0,sticky=NSEW,ipady=3,columnspan=4)
b17.bind("<Button-1>",click)


cal.mainloop()






