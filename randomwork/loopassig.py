# val = input('enter sentence: ')
# a = len(val)
# result=''
# for i in range(1,a,2):
#     result+=val[i]
# print(result)


# val=int(input('enter height'))
# for i in range(1,val+1):
#     for j in range(i):
#         print(i,end='')
#     print('')

# import time

# start = time.time()
# a = int(input(''))
# b= int(input(''))
# oddsum = 0
# evesum=0
# for i in range(a,b,2):
#     oddsum+=i
# for i in range(a+1,b+1,2):
#     evesum+=i
# print(oddsum)
# print(evesum)
# end = time.time()
# print(end - start,'time taken')



a=int(input(''))
b=int(input(''))
oddsum=0
evensum=0
for i in range(a, b+1):
    if i%2==0:
        evensum+=i
    else:
        oddsum+=i
print(evensum)
print(oddsum)
