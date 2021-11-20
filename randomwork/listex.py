# fhand = open('romeo.txt')
# x= list()
# for line in fhand:
#     y = line.split()
#     for i in y:
#         if i not in x:
#             x.append(i)
#             x.sort()
#         else:
#              continue
# print(x)

# fhand = open('mbox.txt')
# count = 0
# for line in fhand:
#     if line.startswith('From '):
#         x = line.split()
#         count = count + 1
#         print(x[1:2])
#
#     else:
#         continue
# print('there were ',count,'staring from from in the file')


# y = list()
# while True:
#     num = input('enter a number: ')
#     if num =='done':
#         break
#     x= float(num)
    # y.append(x)



# print('maximum :',max(y))
# print('minimum :',min(y))

# counts = dict()
# fhand = open('words.txt')
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) +1
#         counts
#
# print(counts)

# counts = dict()
# x = list()
# fhand = open('mbox-short.txt')
# for line in fhand:
#     if line.startswith('From '):
#         words = line.split()
#         name = words[1]
#         dom = name.split('@')
#         ain = dom[1]
#         x.append(ain)
# for domain in x:
#     counts[domain] = counts.get(domain, 0)+1
# print(counts)
