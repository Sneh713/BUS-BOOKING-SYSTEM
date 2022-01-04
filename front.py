from bus import BusBooking
from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
bb=BusBooking()
root.title("SINGH BUS SERVICE")
root.geometry("500x500")
tmsg.showinfo("NOTE","Without LOGIN , you can not book seat")
  
def login():
    top=Toplevel()
    top.geometry("400x300")
    top.title("LOGIN")
    def insert_user():
        try:
            bb.insert_user(userid.get(),name.get(),phone.get(),address.get(),email.get(),password.get())
        except Exception as e:
            print(e)
            
   
    Label(top,text=" LOGIN PAGE",pady=5,font="comicsansms 13 bold").grid(row=0,column=3)
    userid=Label(top,text="USER ID").grid(row=1,column=2)
    name=Label(top,text="NAME").grid(row=2,column=2)
    phone=Label(top,text="PHONE").grid(row=3,column=2)
    add=Label(top,text="ADDRESS").grid(row=4,column=2)
    email=Label(top,text="EMAIL").grid(row=5,column=2)
    password=Label(top,text="PASSWORD").grid(row=6,column=2)
    userid=StringVar()
    name=StringVar()
    phone=StringVar()
    address=StringVar()
    email=StringVar()
    password=StringVar()
    useridentry=Entry(top,textvariable=userid).grid(row=1,column=3)
    nameentry=Entry(top,textvariable=name).grid(row=2,column=3)
    phoneentry=Entry(top,textvariable=phone).grid(row=3,column=3)
    addentry=Entry(top,textvariable=address).grid(row=4,column=3)
    emailentry=Entry(top,textvariable=email).grid(row=5,column=3)
    passwordenttry=Entry(top,textvariable=password).grid(row=6,column=3)
    Button(top,text="submit",command=insert_user).grid(row=7,column=3)
def book_seat():
    top1=Toplevel()
    top1.geometry("300x300")
    top1.title("BOOK SEAT")
    def insert_seat():
        bb.insert_ticket(tid.get(),payment.get(),userid.get())
            
     
    Label(top1,text=" BOOK SEAT",pady=5,font="comicsansms 13 bold").grid(row=0,column=3)
    ticketid=Label(top1,text="TICKET ID").grid(row=1,column=2)
    payment=Label(top1,text="PAYMENT").grid(row=2,column=2)
    userid=Label(top1,text="USER ID ").grid(row=3,column=2)
   
    tid=StringVar()
    payment=StringVar()
    userid=StringVar()
    
    useridentry=Entry(top1,textvariable=tid).grid(row=1,column=3)
    nameentry=Entry(top1,textvariable=payment).grid(row=2,column=3)
    phoneentry=Entry(top1,textvariable=userid).grid(row=3,column=3)
    
    Button(top1,text="submit",command=insert_seat).grid(row=4,column=3)
def food():
    bb.food_menu()
def orderfood():
    def insert_food():
        bb.insert_food(food.get(),foodid.get(),payment.get(),userid.get())
    
            
        
        
    top1=Toplevel()
    top1.geometry("400x300")
    top1.title("ORDER FOOD")
    Label(top1,text=" ORDER FOOD",pady=5,font="comicsansms 13 bold").grid(row=0,column=3)
   
    foodid=Label(top1,text="FOOD ID").grid(row=1,column=2)
    food=Label(top1,text="FOOD").grid(row=2,column=2)
                                           
    payment=Label(top1,text="PAYMENT").grid(row=3,column=2)
    userid=Label(top1,text="USER ID ").grid(row=4,column=2)
    
   
    food=StringVar()
    foodid=StringVar()
    payment=StringVar()
    userid=StringVar()
    
    foodentry=Entry(top1,textvariable=food).grid(row=2,column=3)
    foodidentry=Entry(top1,textvariable=foodid).grid(row=1,column=3)
    entry=Entry(top1,textvariable=payment).grid(row=3,column=3)
    useridentry=Entry(top1,textvariable=userid).grid(row=4,column=3)
    
    Button(top1,text="submit",command=insert_food).grid(row=5,column=3)

def cancel():
    top1=Toplevel()
    def cancal_booking():
        try:
            bb.cancel(userid.get())
            tmsg.showinfo("THANKS","Thanks for coming and welcome for future ")
        except Exception as e:
            print(e)
        
        
    top1.geometry("400x300")
    top1.title("CANCEL")
    Label(top1,text="CANCEL BOOKING",pady=5,font="comicsansms 13 bold").grid(row=0,column=3)
   
    USERID=Label(top1,text="USER ID ").grid(row=1,column=2)
    userid=StringVar()
    useridentry=Entry(top1,textvariable=userid).grid(row=1,column=3)
    Button(top1,text="submit",command=cancal_booking).grid(row=2,column=3)
def cheak():
    top1=Toplevel()
    def cancal_booking():
        try:
            bb.cheak(userid.get(),choice.get())
        except Exception as e:
            print(e)
        
        
    top1.geometry("400x300")
    top1.title("CHEAK")
    tmsg.showinfo("CHOICE","press  1 for user  detils \npress 2 for seat details \npress 3 for food details")
    Label(top1,text="CHEAK DETAILS",pady=5,font="comicsansms 13 bold").grid(row=0,column=3)
   
    USERID=Label(top1,text="USER ID ").grid(row=1,column=2)
    choice=Label(top1,text="CHOICE ").grid(row=2,column=2)
    
    userid=StringVar()
    choice=StringVar()
    useridentry=Entry(top1,textvariable=userid).grid(row=1,column=3)
    choiceentry=Entry(top1,textvariable=choice).grid(row=2,column=3)
    Button(top1,text="submit",command=cancal_booking).grid(row=3,column=3)

    

    
    
    


f0 = Frame(root, width=400, height=70,bg="red")
Label(f0, text="SINGH BUS SERVICE", font="lucida 25 bold").pack()
f0.pack()
f1 = Frame(root, width=400, height=195, pady=14)
Label(f1, text=" HOME  ", font="lucida 15 bold").pack()
Button(f1,text="     LOGIN     ",command=login).pack(pady=10)

Button(f1,text=" SEAT BOOK ",command=book_seat).pack(pady=10)

Button(f1,text="FOOD MENU",command=food).pack(pady=10)

Button(f1,text="ORDER FOOD",command=orderfood).pack(pady=10)
Button(f1,text="CHEAK DETAILS",command=cheak).pack(pady=10)

Button(f1,text="   CANCAL     ",command=cancel).pack(pady=10)

f1.pack()
f2 = Frame(root, width=400, height=195, pady=14, padx=22)
Label(f2, text="BY", font="lucida 18 bold").pack()
Label(f2, text="191B262 SNEH SINGH", font="lucida 20 bold").pack()

f2.pack()


root.mainloop()
