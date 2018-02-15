x=int(input("enter the year:"))
if(x%4==0):
    if(x%100==0):
        if(x%400==0):
            print("it is leap year")
        else:
            print("it is not leap year")
    else:
        print("it is leap year")
else:
    print("it is not leap year")
