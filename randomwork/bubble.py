#bubble sort
def bubble(x):
    ind = len(x)-1
    for i in range(ind):
        for j in range(ind-i):
            if x[j]>x[j+1]:
                temp = x[j]
                x[j]=x[j+1]
                x[j+1]=temp
    return x



#selection sort
def selection(x):
    for i in range(len(x)):
        min = i
        for j in range(i+1,len(x)):
            if x[min]>x[j]:
                min =j
        if min != i:
            x[i],x[min]=x[min],x[i]
    return x
print(selection([23,45,43,32,34]))



#insertion sort
def insertion(x):
    for i in range(1,len(x)):
        while x[i-1]>x[i] and i>0:
            x[i-1],x[i] = x[i],x[i-1]
            i = i-1

    return x

print(insertion([2,5,4,3,34,56,343,23,45,2,3,5,32,12]))



















