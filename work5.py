ls=[(0),(1),(2,'abc'),(3,'def'),(4,'ghi'),(5,'jkl'),(6,'mno'),(7,'pqrs'),(8,'tuv'),(9,'wxyz')]
def cesi(s):
    for i in range (2,len(ls)):
        if s in ls[i][1]:
            return ls[i][0]
s=input(">>")
s=s.lower()
s1=''
for i in s:
    if i.isalpha()==True:
        i=str(cesi(i))
    s1+=i
print(s1)

