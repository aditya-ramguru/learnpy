def copy_print(file):
    fp = open('welcome.txt', 'w')
    lines = file.readlines()
    fp.writelines(lines)
    fp.close()
    fp=open('welcome.txt','r')
    print(fp.read(7))



file1 = open('foo.txt', 'r')
copy_print(file1)
file1.close()