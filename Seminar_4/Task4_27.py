"""
Задача 27
Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
В качестве символа-разделителя используйте пробел.
Пример
"12 346 62 34 9 25623 42 34" -> 25623, 9

test_data = [
["12 346 62 34 9 25623 42 34", [25623, 9]],
["7 346 1 34 9 6 42 -2 6", [346, -2]],
]

for nums, expected in test_data:
assert find_max_min(map(int, nums.split(" "))) == expected
"""


def min_max_str(my_str):
    my_list = list(map(int, my_str.split()))
    num_min = my_list[0]
    num_max = my_list[0]
    for i in my_list:
        if i > num_max:
            num_max = i
        elif i < num_min:
            num_min = i
    result = []
    result.append(num_max)
    result.append(num_min)
    return result


my_str = "12 346 62 34 9 25623 42 34"

print(f'{my_str} -> {min_max_str(my_str)}')


