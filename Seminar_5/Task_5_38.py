"""
Задача 38.
Напишите программу, удаляющую из текста все слова, содержащие "абв".


test_data = [
[["привет абв как абвышные дела?", "абв"], "привет как дела?"]
]
for args, exp in test_data:
assert remove_substr(*args) == exp
#assert remove_substr_func(*args) == exp
"""

test_data = "привет абв как абвышные дела?"


replace_text = 'абв'
# list = [wd for wd in test_data.split() if replace_text not in wd]
# print(f'{" ".join(list)}')

# test_list = test_data.split()
# res_data = []
# for i in test_list:
# if remove_set not in i:
# res_data.append(i)
#
# print(' '.join(res_data))
test_list = test_data.split()
list_1 = filter(lambda word: not "абв" in word, test_list)
print(" ".join(list_1))