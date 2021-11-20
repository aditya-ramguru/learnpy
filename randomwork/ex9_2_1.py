fhand = open("C:/Users/adity/Desktop/py4e/mbox/mbox-short.txt")
day = dict()
for line in fhand:
    if not line.startswith('From'):
        continue
    else:
        word = line.split()
        if len(word) > 2:
            x = word[1]
            y = x.split('@')
            z = y[1]
            day[z] = day.get(z, 0) + 1

print(day)
