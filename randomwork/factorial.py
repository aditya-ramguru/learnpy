#q3
#W.P.P to print factorial of a number
f = input("enter number ")
a = int(f)
factorial =1
if a == 0:
    factorial = 1
    print("factorial of",f,"is",factorial)
elif a>=1 :
    factorial = 1
    for i in range(a,0,-1):
        factorial = factorial*i
    print("factorial of",f,"is",factorial)
else:
    print("invalid input")




