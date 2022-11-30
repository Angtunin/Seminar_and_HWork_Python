"""
Задайте натуральное число N. Напишите программу,
которая составит список простых множителей числа N.
https://newtonov.ru/chemu-ravno-chislo-pi/
# https://wm-help.net/lib/b/book/2288537098/12
https://stackoverflow.com/questions/5811151/why-do-we-check-up-to-the-square-root-of-a-number-to-determine-if-the-number-is
"""


def input_num():
    n = input('Задайте натуральное число №: ')
    while not n.isdigit():
        n = input('Вы вели не число, введите число: ')
    return int(n)


def prime_factors(num):
    k = 11
    list_num = []
    while num > 1:
        if num % 2 == 0:
            num //= 2
            list_num.append(2)
        if num % 3 == 0:
            num //= 3
            list_num.append(3)
        if num % 5 == 0:
            num //= 5
            list_num.append(5)
        if num % 7 == 0:
            num //= 7
            list_num.append(7)
        for i in range(num + 1):
            if num % k == 0:
                num //= k
                list_num.append(k)
                break
        k += 1
    list_num.sort()
    return list_num

n = input_num()
print(f'простые множители {n} -> {prime_factors(n)}')

