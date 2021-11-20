#print only the diagonal elements of matrix
r1=int(input("Enter number of rows for m1 "))
c1=int(input("enter number of columns for m1 "))
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
    a = []
    for j in range(c1):
        x=m1[i][j]
        if i == j:
            a.append(x)
        else:
            a.append('*')

    Rm.append(a)
for i in range(r1):
    print(Rm[i],end='\n')
