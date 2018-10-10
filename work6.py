#s=input(">>")
s="waddawd"
def reserve(s):
    s1=''
    for i in range (len(s)-1,-1,-1):
        s1=s1+str(s[i])
    #print(s1)
    return s1
print(reserve(s))