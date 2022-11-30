"""
Задача 36.
Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
Порядок элементов менять нельзя.
Пример:
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7]


test_data = [
[[1, 5, 2, 3, 4, 6, 1, 7], [1, 5, 6, 7]],
[[1, 2, 3, 4, 6, 1, 7], [1, 2, 3, 4, 6, 7]]
]

for nums, exp in test_data:
assert inc_sequence(nums) == exp

[1, 5, 6, 7]
[1, 2, 3, 4, 6, 7]
"""
list_data = [1, 5, 2, 3, 4, 6, 1, 7]


def increasing_list(n):
    in_list = []
    in_list.append(n[0])
    num = n[0]
    for i in n:
        if i > num:
            in_list.append(i)
            num = i
    return in_list

print(increasing_list(list_data))

def increasing_list1(n):
    in_list = n[:1]
    for i in n[1:]:
        if i > in_list[-1]:
            in_list.append(i)
    return in_list

print(increasing_list1(list_data))