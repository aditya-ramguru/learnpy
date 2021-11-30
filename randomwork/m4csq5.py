# no_of_students = int(input('students: '))
# d = {}
# for i in range(no_of_students):
#     no_of_subjects = int(input('subjects: '))
#     for each in range(no_of_subjects):
#         subject_name = input('name: ')
#         subject_marks = int(input('marks: '))
#         if subject_name not in d:
#             d[subject_name] = 0
#         if subject_marks < 50:
#             d[subject_name] += 1
#
# total_failures = 0
# for key in d:
#     print(key)
#     print(d[key])
#     total_failures += d[key]
# print(total_failures)

#q1
len_list = int(input())
numbers = input()
list_numbers_str = numbers.split(' ')
list_numbers = []
index_required = []
for i in list_numbers_str:
    list_numbers.append(int(i))

for i in range(len_list):
    if i > 0:
        left = [list_numbers[x] for x in range(i)]
        left_sum = sum(left)

        right = [list_numbers[x] for x in range(i + 1, len_list)]
        right_sum = sum(right)

        if left_sum == right_sum:
            index_required.append(i)

if len(index_required) == 0:
    print(0)

else:
    print(index_required[0])

#q2
len_of_index = int(input())
val = input()
l1 = val.split(' ')
l2 = []
for item in l1:
    try:
        l2.append(int(item))
    except:
        l2.append(item)

while len(l2) > 1:
    for item in l2:
        if type(item) == str:
            pos = l2.index(item)
            n1 = l2[pos - 2]
            n2 = l2[pos - 1]

            if item == '/':
                result = n1 / n2
            elif item == '*':
                result = n1 * n2
            elif item == '+':
                result = n1 + n2
            else:
                result = n1 - n2

            del l2[pos - 2:pos + 1]
            l2.insert(pos - 2, result)
            break

print(int(l2[0]))

#q3
no_of_list = int(input())
len_list = int(input())
list_of_val = []
database = {}

for i in range(no_of_list):
    val = input().split('  ')
    int_val = int(val[2])
    val[2] = int_val
    float_val = float(val[-1])
    val[-1] = float_val
    list_of_val.append(val)

index_of_key = int(input())

for rows in list_of_val:
    database[rows[index_of_key]] = rows

search_key = int(input())
print(database[search_key])

#q4
no_of_tuples = int(input())
dictionary = {}
for i in range(no_of_tuples):
    no_of_items = int(input())
    title = input()
    d1 = {}
    val = 0
    for i in range((no_of_items-1)//2):
        key = input()
        d1[key] = int(input())
        val += d1[key]
    dictionary[title] = val

l1 = []
for k,v in dictionary.items():
    l1.append((k,v))

print(tuple(l1))