#MATRIX 1
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
#MATRIX 2
r2=int(input("Enter number of rows for m2 "))
c2=int(input("enter number of colums for m2 "))
m2=[]
for i in range(r2):
    a = []
    for j in range(c2):
        c = int(input('enter value '))
        a.append(c)
    m2.append(a)
#RESULT
if c1 == r2:
    Rm=[]
    for i in range(r1):
        m3=[]
        for k in range(c2):
            x=0
            for j in range(c1):
                r = m1[i][j]*m2[j][k]
                x+=r
            m3.append(x)
        Rm.append(m3)
    print(m1)
    print(m2)
    print('\n','resultant matrix')
    print(Rm)
else:
    print("multiplication not possible")

