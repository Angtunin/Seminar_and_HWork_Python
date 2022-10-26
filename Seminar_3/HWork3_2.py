"""
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""
def sum_par(my_list):
    sum = []
    item = 0
    for i in range(len(my_list) // 2 + len(my_list) % 2):
        sum.append(my_list[i] * my_list[-i - 1])
    return sum

my_list = [2, 3, 4, 5, 6]
print(sum_par(my_list))

