fhand = open('foo.txt', 'r+')
line = input('enter line you want to insert: ')
line_no = int(input('insert at line: '))
lines = fhand.readlines()
lines.insert(line_no-1, f'{line}\n')
fhand.close()

fhand1 = open('foo.txt', 'w')
fhand1.writelines(lines)
fhand1.close()

fhand2 = open('foo.txt', 'r')
content=fhand2.read()
print(content)




