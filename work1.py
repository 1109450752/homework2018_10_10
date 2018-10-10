a=input(">>")
if len(a)==11:
    if a[0:3].isdigit()==True and a[3]=='-'and a[4:6].isdigit()==True and a[6]=='-'and a[7:11].isdigit()==True :
        print("Valid SSN")
    else:
        print("Invalid SSN")
else:
    print("Invalid SSN")