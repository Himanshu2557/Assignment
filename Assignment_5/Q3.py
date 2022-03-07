from tkinter import *
cal=Tk()
cal.geometry("345x250")
cal.title("CALCULATOR")
# cal.config(bg="white")

def click(event):
    global exp,result
    mytext=event.widget.cget("text")
    if mytext =="=":
        if exp.get().isdigit():
            value=int(exp.get())
        else:
            try:
                value=eval(expressionEntry.get())
                result.set(value)
                expressionEntry.update()
                exp.set(result.get())
                resultEntry.update()
            except Exception as e:
                exp.set("ERROR")
                expressionEntry.update()
    elif mytext == "C":
        exp.set("")
        result.set("")
        expressionEntry.update()
    else:
        exp.set(exp.get()+mytext)
        expressionEntry.update()



exp=StringVar()
result=StringVar()
result.set("")
exp.set("")

expressionEntry=Entry(cal,textvar=exp,font="lucida 18 bold",justify=RIGHT,bg="powder blue",fg="black",bd=3)
resultEntry=Entry(cal,textvar=result,font="lucida 18 bold",state=DISABLED,justify=RIGHT,bd=1)
expressionEntry.grid(row=0,column=0,columnspan=4,ipadx=40)
resultEntry.grid(row=1,column=1,columnspan=3)

l2=Label(cal,text="RESULT",font="helvetica 13")
l2.grid(row=1,column=0)

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
b15=Button(cal,text="=",font="lucida 18 bold",relief=SUNKEN,activeforeground="red",border=0)
b15.grid(row=6,column=2,sticky=NSEW,ipady=3)
b15.bind("<Button-1>",click)
b16=Button(cal,text="/",font="lucida 18 bold",relief=SUNKEN,activeforeground="red",border=0)
b16.grid(row=6,column=3,sticky=NSEW,ipady=3)
b16.bind("<Button-1>",click)


cal.mainloop()