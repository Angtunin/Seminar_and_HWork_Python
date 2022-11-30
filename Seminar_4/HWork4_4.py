"""
Задана натуральная степень k. Сформировать случайным образом список
коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
import random

def print_poly(poly):
    for i in range(len(poly)):
        print(poly[i], end="")
        if i == 0:
            print('x^', i + 2, end="", sep="")
        if i == 1:
            print('x', end="", sep="")
        if i != len(poly) - 1:
            print(' + ', end="")
    return ' = 0'
def random_factor(n):
    list_num = []
    for i in range(n):
        list_num.append(random.randint(1, 101))
    return list_num

def input_num():
    n = input('Задайте число от 1 до 3: ')
    while not n.isdigit():
        n = input('Вы вели не число, введите число от 1 до 3: ')
    return int(n)

# num = input_num()
#
# k = random_factor(num)

def print_factor(k):
    data = open('file2.txt', 'w')
    for i in range(len(k)):
        data.writelines(str(k[i]) + ' ')
    data.close()

print(k)

print(print_poly(k))
print_factor(k)