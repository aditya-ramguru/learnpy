# n = int(input())
# arr = map(int, input().split())
# new = list(set(arr))
# new.sort(reverse = True)
# print(new[1])
def swap_case(s):
    new = ''
    for i in range(len(s)):
        if s[i].isupper():
            new = new + s[i].lower()
        elif s[i].islower():
            new = new + s[i].upper()
        else:
            new = new + s[i]
    return new

def count_substring(string,sub_string):
    count = 0
    if sub_string in string:
        count +=1
    return count
s = 'ABCDCDC'
ss ='CDC'
print(count_substring(s,ss))




