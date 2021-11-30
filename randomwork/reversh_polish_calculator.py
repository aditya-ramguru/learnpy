# 5 1 2 / 4 * + 3 - = 4
val = input("enter")
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
            if item == '/':
                result = l2[pos-2]/l2[pos-1]
            elif item == '*':
                result = l2[pos-2]*l2[pos-1]
            elif item == '+':
                result = l2[pos-2]+l2[pos-1]
            else:                                                    # 5 1 2 / 4 * + 3 -
                result = l2[pos-2]-l2[pos-1]
            del l2[pos - 2:pos + 1]
            l2.insert(pos-2, result)
            break

print(int(l2[0]))









