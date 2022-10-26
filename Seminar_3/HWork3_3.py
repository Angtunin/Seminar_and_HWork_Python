"""
Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""


def find_min_max(my_list):
    num_min = my_list[0] - int(my_list[0])
    num_max = my_list[0] - int(my_list[0])
    for i in my_list:
        if i - int(i) != 1 and i - int(i) != 0:
            if i - int(i) > num_max:
                num_max = i - int(i)
            else:
                num_min = i - int(i)
    result = round(num_max - num_min, 2)
    return result

my_list = [1.1, 1.2, 3.1, 5, 10.01]

print(find_min_max(my_list))