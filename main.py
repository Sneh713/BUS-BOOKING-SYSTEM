from bus import BusBooking
def main():
    bb=BusBooking()
    while True:
        print("****************** WELCOME IN SINGH  BUS SERVICE************")
        print()
        print("NOTE:")
        print("without login you can not do anything like seat book and order food")
        print()
        print("press 1  for login ")
        print("press 2 for book seat ")
        print("press 3 for food menu ")
        print("press 4 for order food")
        print("press 5 for cheak detils of user, seat , food")
        print("press 6 for cancel ")
        print("press 7 for exit")
        print()
        print()
        try:
            choice=int(input("enter your choice  "))
            if choice==1:
                uid=int(input("enter your id     "))
                name=input("enter your name  ")
                phone=input("enter your phone number   ")
                email=input("enter your email    ")
                address=input("enter your address      ")
                password=input("enter your password      ")
                bb.insert_user(uid,name,phone,email,address,password)
            elif choice==2:
                tid=input("enter your ticket id ")
                payment=input("enter payment according to your seat prefrance")
                uid=int(input("enter your user id "))
                bb.insert_ticket(tid,payment,uid)
            elif choice==3:
                bb.food_menu()
            elif choice==4:
                food=input("enter your food ")
                fid=int(input("enter your food id "))
                payment=int(input("enter paymnet  of your food"))
                uid=int(input("enter your user id "))
                bb.insert_food(food,fid,payment,uid)
            elif choice==5:
                uid=int(input("enter your user id "))
                choice=int(input("enter your choice"))
                bb.cheak(uid,choice)
                           
                
            elif choice==6:
                uid=int(input(" enter your user id     "))
                bb.cancel(uid)
            elif choice==7:
                print()
                print("****************thankyou for coming here*****************")
                print()
                break
            else:
                print("     invalid   input    ")
        except Exception as e:
            print(e)
            print(" enter vaild input")
            


main()
