def computepay(h, r):
    x=float(h)*float(r)
    return x

h = float(input("Enter Hours:"))
r=float(input("Enter Rate:"))

if h>40:
    pay=40*r+((h-40)*r*1.5)
    print("Pay",pay)

else:
    f=computepay(h,r)
    print("Pay",f)
  
