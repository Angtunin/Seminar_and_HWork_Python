"""
Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

def sum_pos_list(my_list):

    sum = 0
    for i, item in enumerate(my_list):
        if i % 2 != 0:
            sum += item
    return sum

my_list = [2, 3, 5, 9, 3]

print(sum_pos_list(my_list))
