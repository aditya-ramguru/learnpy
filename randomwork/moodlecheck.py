# i = 1
# n = int(input("enter stair height"))
# while i<=n:
#     print("#"*i)
#     i = i+1
#
# n = int(input("enter height"))
# for i in range(1,n+1):
#     print('#'*i)


# num = str(input("enter number pair :"))
# spc = num.find(" ")
# a = num[0:spc]
# b = num[spc+1:]
# # b = int(input("enter 2nd number"))
# print(b," ",a)

# ftemp = float(input("Enter fahrenheit temperature"))
# ftoc = lambda f:(f-32)*(5/9)
# a = ftoc(ftemp)
# print("celsius temperature is ",format(a,'.2f'))

# intval = int(input("enter value :"))
# strval = str(intval)
# print(strval)

# val = int(input("enter value"))
# print(bin(val))
# print(oct(val))
# print(hex(val))


# a = complex(input())
# b = complex(input())
# c = a+b
# print(c)
# print("real part is",int(c.real))
# print("imaginary part is",int(c.imag))

#
# nofrm = int(input("enter number of farms "))
# i = 0
# litsum = 0
# while i < nofrm:
#     milk = str(input("enter amount of milk in litres and ml "))
#     milkval = milk.split()
#     lit = int(milkval[0])+(int(milkval[2])/1000)
#     litsum+=lit
#     i = i+1
# total = litsum
# mltot = (total - int(total))*1000
# print("total amount of milk from",nofrm,"farms is",int(total),"litres", round(mltot),"ml")


# intvl = int(input("enter integer value "))
# introman={1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C'}
# b = intvl%10
# a = intvl//10
# if a>=1 and a<4:
#     tens = introman[10]*a
# elif a ==4:
#     tens = introman[10]+introman[50]
# elif a>=5 and a<9:
#     tens = introman[50]+(introman[10]*(a-5))
# elif a ==9:
#     tens = introman[10]+introman[100]
# else:
#     tens =''
# if b>=1 and b<4:
#     ones = introman[1]*b
# elif b==4:
#     ones = introman[1]+introman[5]
# elif b>=5 and b<9:
#     ones = introman[5]+ (introman[1]*(b-5))
# else:
#     ones = introman[1]+introman[10]

# print("roman numeral is ",tens+ones)

# n = int(input("Enter number of rows: "))
# i = 0
# for i in range(1,n+1):                         #pascals triangle
#     print(' '*(n-i+1)+'# ' *(i))

# val = input("enter number or string ")
# a = len(val)                         #reverse string
# for i in range(a-1,-1,-1):
#     print(val[i],end="")

# val = int(input("enter number "))
# for i in range(1,val+1):
#     for j in range(i):                      #reverse pyramid of numbers
#         print(i-j,end="")
#     print('\n')

# val = int(input("number "))
# for i in range(val,-1,-1):             #inverted half pyramid number pattern
#     for j in range(i+1):
#         print(j,end='')
#     print('\n')

# cunumb = 1                                       #pyramid of natural number less than 10
# stop = 2
# for i in range(1,4):
#     for j in range(1,stop):
#         print(cunumb,end='')
#         cunumb+=1
#     print('\n')
#     stop+=2

# val = 5
# stop = 2
# for i in range(1,val+1):
#     for j in range(1,stop):
#         print(j,end='')
#         if j ==i:
#             print(i-j+1,end='')
#     stop+=1
#     print('\n')

# str = input("enter number")
# intval = int(str)
# rev=''
# a = len(str)
# for i in range(a-1,-1,-1):
#     rev = rev + str[i]
# print(int(rev))
