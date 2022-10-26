"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""

def num_binary(num):
    result = []
    while 1 + num != 1:
        result.append(str(num - (int(num / 2)) * 2))
        num = int(num / 2)
    return result


def revers_bin(my_list):
    bin_list = my_list[::-1]
    bin_num = ''.join(bin_list)
    bin_num = int(bin_num)
    return bin_num

n = int(input('Введите число n: '))
print(f'{n} -> {revers_bin(num_binary(n))}')

