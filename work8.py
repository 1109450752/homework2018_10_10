s = "978013213080"
s1=[]
for i in s:
    i=int(i)
    s1.append(i)
q=10-(s1[0]+3*s1[1]+s1[2]+3*s1[3]+s1[4]+3*s1[5]+s1[6]+3*s1[7]+s1[8]+3*s1[9]+s1[10]+3*s1[11])%10
if q==10:
    q=0
for i in s1:
    print(i,end='')
print(q)
