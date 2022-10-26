"""
Задача 13
Напишите программу, в которой пользователь будет задавать две строки,
а программа - определять количество вхождений одной строки в другой.
Пример:
"hello or world", "or" -> 2
"""
str_a = "hello or world"
str_b = "ld"
count = 0
for i in range(0, len(str_a) + 1):
    if str_a[i:i + len(str_b) - 1] == str_b:
        count += 1
print(count)
