

no_of_list = 2
len_list = 5
database = []
d1 = {}
for i in range(no_of_list):
    val = input().split(' ')
    print(val)
    int_val = int(val[2])
    val[2] = int_val
    float_val = float(val[4])
    val[4] = float_val
    database.append(val)

index_of_key = int(input())
for rows in database:
    d1[rows[index_of_key]] = rows

search_key = input()
print(d1[search_key])
# no_of_list = int(input())
# len_list = int(input())
# list_of_val = []
# database = {}
#
# for i in range(no_of_list):
#     val = input().split(' ')
#     first_name = val[0].strip('"')
#     last_name = val[1].strip('"')
#     key = int(val[2])
#     marks = float(val[-1])
#     grade = val[3].strip('"')
#     val[0] = first_name
#     val[1] = last_name
#     val[2]= key
#     val[-1] = marks
#     val[3] = grade
#
#     list_of_val.append(val)
#
# print(list_of_val)
# index_of_key = int(input())
#
# for rows in list_of_val:
#     database[rows[index_of_key]] = rows
#
# search_key = int(input())
# print(database[search_key])
#
#      "John" "smith" 1234 "B+" 10.03
#      "Rockey" "Jr" 6789 "A+" 40.03
#      'John' 'smith' 1234 'B+' 10.03
#      'Rockey' 'Jr' 6789 'A+' 40.03
# “John”  “smith”  1234  “B+”  10.03