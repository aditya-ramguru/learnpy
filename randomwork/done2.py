largest=None
smallest=None
while True:
    num=input("Enter a number:")
    if num=="done":
        break

    try:
        fval=int(num)
    except:
        print("Invalid input")
        continue

    if largest is None or largest<fval:
       largest=fval


    if smallest is None or smallest>fval:
       smallest=fval
       


print("Maximum is",largest)
print("Minimum is",smallest)
