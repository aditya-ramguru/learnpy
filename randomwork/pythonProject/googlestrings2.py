# def verbing(s):
#   if len(s)<3:
#     print(s)
#   else:
#     if s[-3:]=='ing':
#       print(s[:-3]+'ly')
#     else:
#       print(s+'ing')
#
# verbing('hail')
# verbing('do')
# verbing('swimming')

def front_back(a, b):
    x=int((len(a)/2))
    y=int((len(b)/2))
    if len(a)%2==0:
        afront = a[:x]
        aback = a[x:]
    elif len(a)%2!=0:
         afront = a[:x+1]
         aback = a[x:]
    if len(b)%2==0:
        bfront = b[:y]
        bback = b[y:]
    elif len(b)%2!=0:
        bfront = b[:y+1]
        bback = b[y:]
    print(afront + bfront + aback + bback)

front_back('kitten','donut')

def not_bad(s):
  n = s.find('not')
  b = s.find('bad')
  if n != -1 and b != -1 and b > n:
    s = s[:n] + 'good' + s[b+3:]
  print(s)