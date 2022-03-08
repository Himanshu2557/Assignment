from tkinter import *
from tkinter import messagebox
win=Tk()
Label_1=Label(win,text='GST Tax Finder Calculator',bg='red',font=('Algerian',20))
Label_1.pack()
Label_2=Label(win,text='Enter Orignal Cost(+ Rational no.) : ',font=('Arial black',10))
Label_2.place(x=15,y=60)
Entry_1=Entry(win,width='20')
Entry_1.place(x=270,y=60)
Label_3=Label(win,text='Enter Net Price(+ Rational no.) : ',font=('Arial black',10))
Label_3.place(x=35,y=100)
Entry_2=Entry(win,width='20')
Entry_2.place(x=270,y=100)
Label_4=Label(win,text='GST (in %) : ',font=('Arial black',10))
Label_4.place(x=175,y=140)
def myclick():
    global Answer
    if(Entry_1.get()=='' or Entry_2.get()=='' or float(Entry_1.get())<0 or float(Entry_2.get())<0):
        messagebox.showwarning("Invalid input", "Enter all valid inputs (Can't zero or negative)")
        return
    Net_price=float(Entry_2.get())
    Orignal_cost=float(Entry_1.get())
    if(Orignal_cost==0):
        messagebox.showwarning("Invalid Original Cost", "Can't Zero or negative")
        return
    GST=(Net_price-Orignal_cost)*100/Orignal_cost
    if(GST<0):
        messagebox.showinfo("Invalid GST", "GST can't be in negative")
        return
    Answer=Label(win,text=str(GST))
    Answer.place(x=270,y=140)
    Answer_but['state']=DISABLED
    New_but['state']=NORMAL
def newinput():
    Answer_but['state']=NORMAL
    New_but['state']=DISABLED
    Answer.destroy()
Answer_but=Button(win,text='Calculate GST',font=('Arial black',10),bg='blue',command=myclick,activebackground='yellow',activeforeground='red')
Answer_but.place(x=220,y=180)
New_but=Button(win,text='New Input',font=('Arial black',10),bg='red',command=newinput,activebackground='yellow',activeforeground='red')
New_but.place(x=120,y=180)
New_but['state']=DISABLED
win.mainloop()