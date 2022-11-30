"""
Задача 43.
Дана последовательность чисел. Получить список уникальных элементов заданной последовательности. Пример:
[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

def get_unique(lst):
    pass

test_data = [
    [[1, 1, 2], [2]],
    [[1, 2, 3, 5, 1, 5, 3, 10], [2, 10]]
]
for nums, exp in test_data:
    assert get_unique(nums) == exp
    assert get_unique_func(nums) == exp
"""
test_list = [1, 2, 3, 5, 1, 5, 3, 10]
uniques = list(set(test_list))

one_and_only = []
for member in uniques:
    counter = 0
    for tst in test_list:
        if member == tst:
            counter += 1
            if counter > 2:
                break
    if counter == 1:
        one_and_only.append(member)

print(one_and_only)