"""
Задача 4.
Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

"""
a = int(input('a: '))

if (a % 5 or a % 10 or a % 15) and not a % 30 == 0:
    print('кратно')
else:
    print('не кратно')
