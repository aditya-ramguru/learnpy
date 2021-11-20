fhand=open('mbox-short.txt')
count=0
for line in fhand:
    if line.startswith('From'):
        words=line.split()
        count=count+1
        print(words[1])

print('there were',count,'lines in the file with from as the first word')