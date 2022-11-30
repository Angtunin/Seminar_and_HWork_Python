"""
Задайте последовательность чисел. Напишите программу,
которая выведет список неповторяющихся элементов исходной последовательности.
"""
import random
# def input_num(text1, text2):
#     n = input(text1)
#     while not n.isdigit():
#         n = input(text2)
#     return int(n)
#
#
# n = input_num('Введите числа через пробел: начало, конец и количество членов последовательности: ', 'введите 3 числа')
# print(n)
list_num = []
for i in range(10):
    list_num.append(random.randint(-5, 5))

print(list_num)

def del_dublikat(list_n):
    list_del = set(list_n)
    return list(list_del)
print(del_dublikat(list_num))
