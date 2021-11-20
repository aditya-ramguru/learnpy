fhand=open("C:/Users/adity/Desktop/py4e/words.txt")
wd=dict()
for line in fhand:
    words=line.split()
    for word in words:
        if word not in wd:
            wd[word]=1
        else:
            wd[word]=wd[word]+1
print(wd)
    

