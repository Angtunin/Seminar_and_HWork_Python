"""
Задача 21
Напишите программу, которая определит позицию второго вхождения
строки в списке либо сообщит, что её нет.
Пример:
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1
"""


# Первый вариант
# def find_str(my_list, str_a):
#     count = 0
#     for i in range(len(my_list)):
#         if my_list[i] == str_a:
#             count += 1
#             pos = i
#             if count == 2:
#                 return pos
#     return -1
#
# print(find_str(["qwe", "asd", "zxc", "qwe", "ertqwe"], "qwe"))

# Второй вариант
def find_str1(my_list, str_a, pos_count=2): # pos_count=2 параметр по умолчанию, если его не указывать считаетс с 2
    count = 0
    for i, item in enumerate(my_list):
        if item == str_a:
            count += 1
            if count == pos_count:
                return i
    return -1


print(find_str1(["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], "йцу"))
