import operator
def countletters(s,a):
    q=0
    for i in range (len(s)):
        if a == s[i]:
            q+=1
    return q
s=input(">>")
s1=''
s2=''
for i in s:
    if i not in s1:
        s1+=i
for i in s1:
    ls=str(("\"{}\":{}".format(i,countletters(s,i))))
    s2=s2+ls+','
s2="'{"+s2[0:len(s2)-1]+"}'"
s3=eval(eval(s2))
#s3=str(s3)
s4=sorted(s3.items(),key= lambda x:x[1])
#s4=sorted(s3.items(),key=operator.itemgetter(1))
s5=dict(s4)
print(s2,type(s2))
print(s3,type(s3))
print(s4,type(s4))
print(s5,type(s5))
