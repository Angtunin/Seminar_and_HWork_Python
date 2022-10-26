"""
Задача 13
Напишите программу, в которой пользователь будет задавать две строки,
а программа - определять количество вхождений одной строки в другой.
Пример:
"hello or world", "or" -> 2
"""
str_a = "hello or world"
str_b = "rl"
count = 0
i = 0
while i < len(str_a) - 1:
    if str_b == str_a[i] + str_a[i + 1] :
        count += 1
    i += 1
print(count)