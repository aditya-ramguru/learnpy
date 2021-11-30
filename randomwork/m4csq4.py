no_of_tuples = int(input("enter number: "))
dictionary = {}
for i in range(no_of_tuples):
    no_of_items = int(input('enter no of items: '))
    title = input("title: ")
    d1 = {}
    val = 0
    for i in range((no_of_items-1)//2):
        key = input('key: ')
        d1[key] = int(input('val: '))
        val += d1[key]
    dictionary[title] = val
l1 = []
for k,v in dictionary.items():
    l1.append((k,v))

print(tuple(l1))

