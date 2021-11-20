# #inverted pyramid of descending numbers
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(i,end='')
#     print('')
#
# #simple number triangle pattern
# for i in range(1,6):
#     for j in range(i):
#         print(i,end='')
#     print('')
# print('\n')
#
# #inverted pyramid of numbers
# rows = 5
# b=0
# for i in range(rows,0,-1):
#     b+=1
#     for j in range(1,i+1):
#         print(b,end='')
#     print('')
# print('\n')
#
# #half pyramid pattern of numbers
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='')
#     print('')
# print('\n')
#
# #inverted pyramid of same number
# rows = 5
# for i in range(rows,0,-1):
#     for j in range(i):
#         print(rows,end='')
#     print('')
# print('\n')
#
# #reverse pyramid of numbers
# rows = 5
# for i in range(1,rows+1):
#     for j in range(0,i):
#         print(i-j,end='')
#     print('')
# print('\n')
for i in range (5,0,-1):
    a=1
    for j in range(i,0,-1):
        print(a,1,end=' ')
        a+=1
    print('\n')


# # val = 7
# # for i in range(1,val+1):
# #     print(" "*(val-i)+'* '*i)