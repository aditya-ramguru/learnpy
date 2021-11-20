uwl=list()
fname=input('Enter file name:')
fhand=open(fname)
for line in fhand:
    x=line.split()
    for words in x:
        if words in uwl:
            continue
        else:
            uwl.append(words)

uwl.sort()
print(uwl)
