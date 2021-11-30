# file = open('my_file.txt')
# contents = file.read()
# print(contents)
# file.close()

with open('abcd', mode ='w') as file:
    file.write('\nnew text.')
