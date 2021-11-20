# def donuts(count):
#   if count>10:
#     return('Number of donuts: many')
#   else:
#       return('NUmber of donuts:'+str(count))
# print(donuts(5))
# print(donuts(60))
#
# def both_ends(s):
#   if len(s)<2:
#     return('')
#   else:
#     x=s[:1]
#     y=s[-2:-1]
#     return(x+y)
# print(both_ends('spring'))
# print(both_ends('s'))
# print(both_ends('aditya'))

# def fix_start(s):
#   front=s[:1]
#   back = s[1:]
#   x = back.replace(front,'*')
#   print(front+x)
# fix_start('babble')

# def mix_up(a, b):
#   afin = b[:2] + a[2:]
#   bfin= a[:2] + b[2:]
#   print('afin','bfin')
# mix_up('dog','dinner')