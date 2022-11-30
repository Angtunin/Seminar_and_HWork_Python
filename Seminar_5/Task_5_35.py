"""
 Задача 35.
В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

test_data = [
["3 4 5 6 7 9 10 11 12", 8],
["3 4 6 7 8 9 10 11 12", 5],
["1 3", 2]
]

for sequence, exp in test_data:
find_missing(sequence) == exp
# find_missing_func(sequence) == exp
"""
list_data = [1, 3, 4, 5, 6, 7, 8]

def num_find(list_d):
    for i in range(list_d[0], list_d[-1]):
        if list_d[i] - 1 != list_d[i - 1]:
            num = list_d[i - 1] + 1
            print(num)
            break
    return num

num_find(list_data)
list_d = [1, 2, 3, 4, 5, 7, 8]
index = list(filter(lambda i: list_d[i] - 1 != list_d[i - 1], range(1, len(list_d))))[0]
print(list_d[index] - 1)