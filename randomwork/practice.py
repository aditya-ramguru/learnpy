# import re
# Q1 separate numbers in string
# string = input('Enter string: ')
# string_list = list(string)
# numbers = []
# letters=[]
# for each in string_list:
#     if re.match('[0-9]', each):
#         numbers.append(int(each))
#         print(each)
#     else:
#         letters.append(each)
#
#
# print(letters)
# print(numbers)

# Q2 starts with a or e
# val_list = []
# required = []
# for i in range(5):
#     val = input('enter val: ')
#     val_list.append(val)
#
# for item in val_list:
#     if re.match('^[aA]', item) or re.match('^[eE]', item):
#         required.append(item)
#     else:
#         continue
#
# print(val_list)
# print(required)

# Q3 find position of substring in string
# val = input('enter string: ')
# substring = input('Enter substring: ')
# index = 0
# while index < len(val):
#     val_string = val[index:]
#     if substring in val_string:
#         x = val_string.find(substring)
#         index = index + x
#         print(f'Yes {substring} is present in {val} at {index}.')
#         index = index + len(substring)
#     else:
#         continue

# Q4 higher lower game
# goal = random.randint(1, 100)
# guess = 0
# print('Guess the number you have 5 guesses based on your guess the computer will give you hints\n')
# while guess != goal:
#     guess = int(input('Enter number: '))
#     if guess < goal:
#         print('too low, Try again')
#     elif guess > goal:
#         print('too high, Try again')
# print('Well Done')
# print('See you later')

# Q5 leap year program
# year = int(input('enter year: '))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('leap year')
#         else:
#             print('not leap year')
#     else:
#         print('leap year')
# else:
#     print('not a leap year')

# Q6 sum of rows and column
# rows = int(input('enter number of rows: '))
# columns = int(input('enter number of columns: '))
# matrix = []
# for i in range(rows):
#     row = []
#     for j in range(columns):
#         num = random.randint(1, 10)
#         row.append(num)
#     matrix.append(row)
# print(matrix)
#
# x = 1
# for row in matrix:
#     row_sum = sum(row)
#     print(f'row {x} sum = {row_sum}')
#     x += 1
#
# no_of_columns = len(matrix[1])
# print(no_of_columns)
# y = 1
# for column in range(no_of_columns):
#     column_sum = 0
#     for row in range(len(matrix)):
#         column_sum += matrix[row][column]
#     print(f'column {y} sum = {column_sum}')
#     y += 1


# Q7 print all permutations of a given string or number
# Write your code below this line 👇
# s = input()
# x = 0
# for i in range(len(s)):
#     if s[i:i+5].isalnum():
#         x = 1
#         print('True')
#         break
# if x == 0:
#     print('False')
#
# x = 0
# for each in s:
#     if each.isalpha():
#         print('True')
#         x = 1
#         break
# if x == 0:
#     print('False')
#
# x = 0
# for each in s:
#     if each.isdigit():
#         print('True')
#         x = 1
#         break
# if x == 0:
#     print('False')
#
# x = 0
# for each in s:
#     if each.islower():
#         print('True')
#         x = 1
#         break
# if x == 0:
#     print('False')
#
# x = 0
# for each in s:
#     if each.isupper():
#         print('True')
#         x = 1
#         break
# if x == 0:
#     print('False')
# val = input().split()
# new_list = []
# for item in val:
#     print(item)
#     new_string = ''
#     for i in range(len(item)):
#         if item[i].isupper():
#             new_string += item[i].lower()
#         elif item[i].islower():
#             new_string += item[i].upper()
#     new_list.append(new_string)
# result = ' '.join(new_list)
# print(result)
# val = input()
# my_list = list(val)
# list_without_duplicates = list(set(val))
# if len(my_list) == len(list_without_duplicates):
#     print('GOOD')
# else:
#     print('BAD')
# import re
# val = input()
# d = {}
# names = re.findall('[A-Z]',val)
# age = re.findall('[0-9]+',val)

# no_people = int(input())
# available_tickets = int(input())
# d = {}
# age_list = []
# for i in range(no_people):
#     val = input().split(',')
#     token_num = val[0]
#     age = val[1]
#     d[age] = token_num
#     age_list.append(age)
# age_list.sort(reverse=True)
# token_list = []
# for i in range(available_tickets):
#     token_no = d[age_list[i]]
#     token_list.append(int(token_no))
# token_list.sort()
# print(tuple(token_list))


# (1,0),(0,1),(0,0)
#  parallelogram
# coordinates = input()
# new_string = ''
# for i in range(len(coordinates)):
#     if i > 0 and coordinates[i] == ',' and coordinates[i-1] == ')':
#         new_string += ' '
#     else:
#         new_string += coordinates[i]
# coor_list = new_string.split()
# x_coordinates = []
# y_coordinates = []
# cc_list = [ for item in coor_list]
# print(cc_list)
# for item in coor_list:
#     xcor = int(item[1])
#     x_coordinates.append(xcor)
#     ycor = int(item[3])
#     y_coordinates.append(ycor)
# dx = {}
# for x in x_coordinates:
#     dx[x] = dx.get(x, 0) + 1
#
# dy = {}
# for y in y_coordinates:
#     dy[y] = dy.get(y, 0) + 1
#
# for key in dx:
#     if dx[key] == 1:
#         required_xcor = key
#
# for key in dy:
#     if dy[key] == 1:
#         required_ycor = key
#
# print((required_xcor, required_ycor))


coor = input().split('),(')
r = ' '.join(coor)
r = r[1:-2]
coor2 = r.split()
print(coor2)











