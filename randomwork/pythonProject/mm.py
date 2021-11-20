nlist=list()
while True:
    try:
        num=input('Enter a number:')
        if num=='done':break
        x=float(num)
        nlist.append(x)

    except:
        print('not a number')
        continue

a=max(nlist)
b=min(nlist)
print('maximum:',a)
print('minimum:',b)
