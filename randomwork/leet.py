def reversewords(s):
    y=s.split()
    for i in range(len(y)-1,-1,-1):
        print(y[i],end=' ')


def reversestring(x):
    reverse=''
    for i in range(len(x)-1,-1,-1):
        reverse = reverse +x[i]
    return(reverse)





