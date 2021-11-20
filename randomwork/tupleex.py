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
x = 'ahjfuelradhkfueradsfhkjrgbeukrufhdkjssjcjhfealkhfakjfuerh'
z=dict()
def split(word):
    return list(word)
y = split(x)
for i in y:
    z[i] = z.get(i,0)+1
print(sorted([(v,k)for k,v in z.items()],reverse=True))
d = list()
for (k,v) in z.items():
    d.append((v,k))
d.sort(reverse=True)
l=list()
for(v,k) in d:
    l.append((k,v))
print(l)
