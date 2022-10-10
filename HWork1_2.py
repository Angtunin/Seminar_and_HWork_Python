"""
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""

# print(not (x or y or z) == (not x and not y and not z))
r = range(0, 2)
for x in r:
    for y in r:
        for z in r:
            print(f'not ({bool(x)} or {bool(y)} or {bool(z)}) == not {bool(x)} and not {bool(y)} and not {bool(z)}:', end=" ")
            print(not (bool(x) or bool(y) or bool(z)) == (not bool(x) and not bool(y) and not bool(z)))
