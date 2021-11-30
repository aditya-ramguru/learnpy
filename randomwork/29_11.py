import re
# val = input()
# if re.match('^[1-9][0-9]+$',val):
#     print('valid')
# else:
#     print('invalid')


# val2 = input()
# if re.match('^[aA][a-zA-z]+[b-sB-S]$',val2):
#     print('valid')
# else:
#     print('invalid')

# reg_no = input()
# if re.match('[1-9][0-9][A-Z]{3}[0-9]{4}$',reg_no):
#     print('valid')
# else:
#     print('invalid')

val = input()
val = val.split()

for i in val:
    if re.match('^[^sS].*[sS].*[^sS]$',i):
        print(i)
