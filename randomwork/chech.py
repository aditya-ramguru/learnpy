largest=None
smallest=None
while True:
    num=input("Enter a number:")
    if num=="done":
        break

    try:
        fval=int(num)
    except:
        print("Invalid input")
        continue

    if largest is None or largest<fval:
       largest=fval


    if smallest is None or smallest>fval:
       smallest=fval



print("Maximum is",largest)
print("Minimum is",smallest)

name = input("enter you name")
print("welcome", name)
cel = input(" Enter celsius temperature",)
cel = float(cel)
far = ((9/5)*cel)+32
print("in fahrenheight temperature is", far)


str = input("enter a string")
length = len(str)
index = 0
for i in str:
    while length > index:
        print(str[length - 1])
        length = length - 1
        continue
    if length == index:
        print("done")
        break


total = 0
count = 0
average = 0
while True:
    num = input(" enter a number : ")
    try:
        if num == 'done':
            break
        x = float(num)
        total = total + x
        count = count +1
        average = total/count
        continue


    except:
        print(" invalid input")

print(total, count, average)

maximum = None
minimum = None
while True:
    num = input("enter a number: ")
    try:

        if num =='done':
            break
        num = int(num)
        if maximum is None or num>maximum:
            maximum = num

        if minimum is None or minimum>num:
            minimum = num
            continue





    except:
        print("invalid input")
        continue

print(maximum, minimum)

fname = input("enter file name: ")
count = 0
average = 0
total = 0
try:
    fhand = open(fname)
    for line in fhand:
        if not line.startswith('X-DSPAM-Confidence:'):
            continue
        else:
            atpos = line.find(":")
            num = float(line[atpos+1:])
            count = count + 1
            total = total + num
            average = total/count
            continue
    print("average spam confidence :", average)
except:
    if fname == "na na boo boo":
        print("you've been punked")
    else:
        print('file',fname,'not found')

def middle(numlist):
    x = numlist[1:len(numlist)-1]
    print(x)

x = list()
x.append(36)
y = [24 ,35 ,64 ,73]
x.extend(y)
middle(x)


                                                             # getting double value
  bigword = None
bigcount = None
for k,v in counts.items():
    if bigcount is None or v>bigcount:
        bigword = k
        bigcount = v
# print(counts)
# print(bigword,':',bigcount)

# counts = dict()
# lst = list()
# lst3 = list()
# fhand = open('mbox.txt')
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

# chocolate bob
# total = 15
# # cost = 3
# # choc = total/cost
# # cwrap = choc
# # wrap = 2
# # while





