def longest(a1, a2):
    string = ''
    l1 = list(a1)
    l2 = list(a2)
    for item in l1:
        if item not in l2:
            string += item
    return string

print(longest("aretheyhere", "yestheyarehere"))




