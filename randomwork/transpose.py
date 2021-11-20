r1=int(input("Enter number of rows for m1 "))
c1=int(input("enter number of colums for m1 "))
m1=[]
print('enter number row wise ')
for i in range(r1):
    a = []
    for j in range(c1):
        c = int(input('enter value '))
        a.append(c)
    m1.append(a)
for i in range(r1):
    print(m1[i],end='\n')
Rm=[]
for i in range(r1):
    m2=[]
    for j in range(c1):
        r = m1[j][i]
        m2.append(r)
    Rm.append(m2)
print(Rm)