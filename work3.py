s=input(">>")
q=0
if len(s)>=8 and s.isalnum()==True :
    for i in s:
        if i.isdigit()==True:
            q+=1
        if q==2:
            print("Valid SSN")
            break
    if q<2:
        print("Invalid SSN")
else:
    print("Invalid SSN")
