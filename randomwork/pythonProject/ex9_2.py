fhand = open("C:/Users/adity/Desktop/py4e/mbox/mbox-short.txt")
day = dict()
for line in fhand:
    if not line.startswith('From') :
        continue
    else:
        word = line.split()
        if not len(word) < 3:
            x = word[2]
            day[x] = day.get(x, 0) + 1

print(day)
