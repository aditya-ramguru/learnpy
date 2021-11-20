N = int(input())
l1 = []
for i in range(N):
    val = input()
    x = val.split()
    if val =='print':
        print(l1)
    if len(x) == 3:
        ind = int(x[1])
        chr = int(x[2])
        l1.insert(ind, chr)
    elif len(x) == 1:
        y = x[0]
        if y == 'sort':
            l1.sort()
        elif y == 'pop':
            l1.pop()
        elif y =='reverse':
            l1.reverse()
    elif len(x) == 2:
        y = x[0]
        chr = int(x[1])
        if y == 'remove':
            l1.remove(chr)
        elif y == 'append':
            l1.append(chr)