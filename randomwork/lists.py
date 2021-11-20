nlist=list()
index=0
while True:
    try:
        inp=input('Enter a number:')
        if inp=='done': break
        value=int(inp)
        nlist.append(value)
        index=index+1
        i=int(index)

    except:
        print("please enter a number!")
        continue

def chop(x):
    del x[i-1]
    del x[0]
    return(None)

def middle(x):
    print(x[1:i-1])

middle(nlist)
chop(nlist)
print (nlist)
