import random

list_numbers = []
for i in range(7):
    list_numbers.append(random.randint(1, 100))
print(list_numbers)
index_required = []
for i in range(len(list_numbers)):
    if i >= 1:
        left = [list_numbers[x] for x in range(i)]
        print(left)
        left_sum = sum(left)

        right = [list_numbers[x] for x in range(i+1, len(list_numbers))]
        print(right)
        right_sum = sum(right)

        if left_sum == right_sum:
            index_required.append(i)

print(index_required)