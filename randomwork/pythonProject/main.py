txt='but soft what light inn yonder window breaks'
words = txt.split()
t=list()
for word in words:
    t.append((len(word), word))

t.sort()

res = list()
for length, word in t:
    res.append(word)

print(t)
print(res)
str.split("@")