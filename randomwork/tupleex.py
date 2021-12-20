# counts = dict()
# lst = list()
# lst3 = list()
# fhand = open('mbox-short.txt')
# for line in fhand :
#     if line.startswith('From '):
#         words = line.split()
#         email = words[1]
#         lst.append(email)
#
# for word in lst:
#     counts[word] = counts.get(word,0) + 1
# print(counts)
#
# for (k,v) in counts.items():
#     lst3.append((v,k))
#
# lst3.sort(reverse=True)
# for v,k in lst3:
#     print(k,v)

# hlst= list()
# counts=dict()
# fhand = open('mbox-short.txt')
# for line in fhand:
#     if line.startswith("From "):
#         words = line.split()
#         time = words[5]
#         tim = time.split(':')
#         hours = tim[0]
#         hlst.append(hours)
#
# for hour in hlst:
#     counts[hour]= counts.get(hours,0) +1
# lst = list()
# for k,v in counts.items():
#     lst.append((k,v))
#
# lst.sort()
# for k,v in lst:
#     print(k,' ',v)
#
#
# x = 'ahjfuelradhkfueradsfhkjrgbeukrufhdkjssjcjhfealkhfakjfuerh'
# z=dict()
# def split(word):
#     return list(word)
# y = split(x)
# for i in y:
#     z[i] = z.get(i,0)+1
# print(sorted([(v,k)for k,v in z.items()],reverse=True))
# d = list()
# for (k,v) in z.items():
#     d.append((v,k))
# d.sort(reverse=True)
# l=list()
# for(v,k) in d:
#     l.append((k,v))
# print(l)
# total = {}
# lowest = 100
# lowest2 = None
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     total[name] = score
#     if score < lowest:
#         lowest2 = lowest
#         lowest = score
#     elif lowest2 == None or lowest2 > score:
#         lowest2 = score
# new_list = []
# for key in total:
#     if total[key] == lowest2:
#         new_list.append(key)
# new_list.sort()
# for item in new_list:
#     print(item, end=' ')
# if __name__ == '__main__':
#     s = input()
#     s_list = list(s)
#     d = {}
#     for i in s_list:
#         d[i] = d.get(i, 0) + 1
#     s_list = (sorted([(v, k) for k, v in d.items()], reverse=True))
#     for i in range(len(s_list)-1):
#         if s_list[i][0] == s_list[i + 1][0]:
#             chr1 = s_list[i][1]
#             chr2 = s_list[i + 1][1]
#             if ord(chr2) < ord(chr1):
#                 s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
#     for i in range(3):
#         print(s_list[i][1], s_list[i][0])

# test_cases = int(input())
# for i in range(test_cases):
#     val = input().split()
#     a = val[0]
#     b = val[1]
#     try:
#         result = int(a)/int(b)
#     except ZeroDivisionError:
#         print('Error Code: integer division or modulo by zero')
#     except ValueError:
#         print(f"Error Code: invalid literal for int() with base 10: '{b}'")
#     else:
#         print(int(result))
from itertools import permutations
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    #i = [[i for i in range(x+1)],[j for j in range(y+1)]]
    l1 = ([(i,j,k) for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n])




