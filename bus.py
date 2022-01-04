import mysql.connector as connector
class BusBooking:
    def __init__(self):
        self.con=connector.connect(host="localhost",port="3306",user="root",password="sneh@singh111",database="busbooking")
        print(self.con)
        query='create table if not exists user(uid int primary key,uname varchar(200),phone varchar(12),email varchar(200),address varchar(100),password varchar(100))'
        query1='create table if not exists ticket(tid int primary key ,tno int ,payment varchar(10),uid int, foreign key (uid) references user(uid))'
        query2='create table if not exists food(food varchar(200),fid int primary key,payment varchar(5),uid int ,foreign key (uid) references user(uid))'
        query3='create table if not exists food_menu(fid int primary key ,food_name varchar(50),payment varchar(10))'
        cur=self.con.cursor()
        cur.execute(query)
        cur.execute(query1)
        cur.execute(query2)
        cur.execute(query3)
        print("created")
    def insert_user(self,usid ,name,phone, email,address,password):
        query="insert into user(uid,uname,phone,email,address,password) values({},'{}','{}','{}','{}','{}')".format(usid,name,phone,email,address,password)
        #print("sneh")
        #print(query)
        cur=self.con.cursor()
        #print("sneh1")
        #print(cur)
        cur.execute(query)
        #print("sneh3")
        self.con.commit()
        print("sneh ")
    def insert_ticket(self,tsid,payment,uid):
        seat=int(payment)
        #print(seat)
        if seat<100:
            seat="C"
        elif seat>100:
            seat="A"
        else :
            seat="B"
        #print(seat)
        
        tsno=10
        query="insert into ticket(tid,tno,payment,uid,seat_type) values({},{},'{}',{},'{}')".format(tsid,tsno,payment,uid,seat)
        #print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("sneh")
    def insert_food(self,food,fsid,payment,uid):
        query="insert into food(food,fid,payment,uid) values('{}',{},'{}',{})".format(food,fsid,payment,uid)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("sneh ")
    def cancel(self,uid):
        
        query1="delete from ticket where uid={}".format(uid)
        cur=self.con.cursor()
        cur.execute(query1)
        self.con.commit()
        query2="delete from food where uid={}".format(uid)
        cur=self.con.cursor()
        cur.execute(query2)
        self.con.commit()
        query="delete from user where uid={}".format(uid)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("sneh")
    def food_menu(self):
        query="select * from food_menu"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print()
            print(" Food ID :",row[0])
            print(" Food Name:",row[1])
            print(" Paayment :",row[2])
            print()
    def cheak(self,uid,ch):
        #print("press  1 for user  detils \npress 2 for seat details \npress 3 for food details")
        
        
        try:
            #choice=int(input(" press 1/2/3    "))
            choice=int(ch)
            if choice==1:
                query="select * from user where uid={}".format(uid)
                cur=self.con.cursor()
                cur.execute(query)
                for row in cur:
                    print()
                    print("your id :",row[0])
                    print("Name :",row[1])
                    print("Phone:", row[2])
                    print("Email:",row[3])
                    print("Address:",row[4])
                    print()
            elif choice==2:
                query="select * from ticket where uid={}".format(uid)
                cur=self.con.cursor()
                cur.execute(query)
                for row in cur:
                    print()
                    print("Your id :",row[0])
                    print("seat number:",row[1])
                    print("payment  :",row[2],".Rs")
                    print("seat type:",row[4])
                    print()
            elif choice==3:
                query="select * from food where uid={}".format(uid)
                cur=self.con.cursor()
                cur.execute(query)
                for row in cur:
                    print()
                    print("your id :" , row[1])
                    print("food:",row[0])
                    print("payment :",row[3],".Rs")
                    print()
            else:
                print("invalid input")
        except Exception as e:
            print(e)
                
            
        
#ticket=BusBooking()
#ticket.insert_user(102,"Sneh Singh","9340575521","sing8@gmail.com","JP rewa","snehsingh111")

#ticket.insert_ticket(1002,108, 1002)
#ticket.insert_food("samosa",102,"15",102)
#ticket.insert_food("jalebi",1002,"30",1001)
#ticket.cheak(1001,1)
#ticket.cancel(102)
#ticket.food_menu()



