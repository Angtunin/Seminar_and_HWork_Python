"""
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов
"""

def sum_list(data1, data2):
    sum_l = []
    for i in range(len(data1)):
        sum_l.append(int(data1[i]) + int(data2[i]))
    return sum_l
from HWork4_4 import print_poly

def read_text_file(file_txt):
    path = file_txt
    f = open(path, 'r')
    data = f.read() + ' '
    f.close()
    data = data.split()
    return data


data1 = read_text_file('file1.txt')
data2 = read_text_file('file2.txt')

print(data1)
print(data2)
print('='*100)


print(sum_list(data1, data2))

print(print_poly(sum_list(data1, data2)))