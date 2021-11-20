# sal = float(input(""))
# if sal > 100000:
#     tax = 0.04*sal
# elif 1000000>=sal>500000:
#     tax = 0.02*sal
# else:
#     tax = 0
# print(tax)

# k= int(input(''))
# if k <=10:
#     price = 15*k
# elif 10<k<=100:
#     price= (15*10)+(8*(k-10))
# else:
#     price = 15*10+(8*(k-10))+(6*(k-100))
# print(price)

m = float(input())
c = input().upper()
if len(c)==0:
    print("Enter appropriate marks")
elif m >=80:
    if c == 'T':
        fm = m+(0.08*m)
    else:
        fm = m +(0.06*m)
    print(fm)
elif 80>m>=60:
    if c == 'T':
        fm = m+(0.06*m)
    else:
        fm = m +(0.04*m)
    print(fm)
elif 60>m>=40:
    if c == 'T':
        fm = m+(0.04*m)
    else:
        fm = m +(0.02*m)
    print(fm)
elif 40>m:
      fm = m
      print(fm)

# val = (input("enter value"))
# num = int(val)
# x = list(val)
# sum = 0
# for i in range(0,len(x)):
#     sum+=int(x[i])
# if sum>=10:
#     y = list(str(sum))
#     sum=0
#     for i in range(0,len(y)):
#         sum+=int(y[i])
# print(sum)

# def factorial(x):
#     fact = 1
#     for i in range(x,0,-1):
#         fact = fact*i
#     return fact
# y = input()
# n = int(y)
# if n%2==0:
#     for i in range(0,n+1):
#         if i % 2 ==0:
#             print(i,' ',factorial(i))
# else:
#     for i in range(0,n+1):
#         if i % 2 != 0:
#             print(i,' ',factorial(i))








