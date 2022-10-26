"""
Задача 12
Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
Пример:
Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
"""

n = int(input('n: '))



# for i in range(n):
#     print(f'{i + 1}: {3 * (i + 1) + 1}, ', end='')

def dict_range(n):
    print(f'n = {n}:', end=" ")
    result = {}
    for i in range(n):
        result[i + 1] = 3 * (i + 1) + 1
    return result


print(dict_range(n))

