"""
Задача 20
Задайте список. Напишите программу, которая определит,
присутствует ли в заданном списке строк некое число.
Пример:
["qwe", "asd", "12", "qwe", "2"], 2 -> True
["qwe", "asd", "qwe", "681"], 7 -> False
["qwe", "asd", "qwe", "0"], 0 -> True
"""
# list_c = ["qwe", "asd", "12", "qwe", "2"]
# n = 2
def find_nunber(n, list):

    for i in list:
        if i == n:
            return True
    return False

print(find_nunber(str(2), ["qwe", "asd", "12", "qwe", "2"]))