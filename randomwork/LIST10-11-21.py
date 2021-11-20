l1=[]
l2=[]
print("enter 'done' to finish entering values")
while True:
    val = input("enter word: ")
    if val == 'done':
        break
    l1.append(val)
for i in l1:
    if 'tion' in i:
        l2.append(i)
print(l2)