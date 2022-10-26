"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""
def fib_num(n):
    if n == 0: return n
    elif n == 1 or n == 2: return 1
    else:
        return fib_num(n - 1) + fib_num(n - 2)


def fib_list(num):
    f_list = []
    for i in range(n + 1):
        f_list.append(fib_num(i))
    return f_list

def niga_fib(my_list):
    niga_f = my_list[::-1]
    niga_fin = []
    if len(my_list) % 2 == 0:
        for i in range(len(my_list)):
            if i % 2 == 0:
                niga_fin.append(niga_f[i])
            else: niga_fin.append(-niga_f[i])
    else:
        for i in range(len(my_list)):
            if i % 2 == 0:
                niga_fin.append(-niga_f[i])
            else: niga_fin.append(niga_f[i])
    niga_fin += my_list[1:]
    return niga_fin

n = int(input('Введите число k: '))

print(f'для k = {n} список {niga_fib(fib_list(n))}')


