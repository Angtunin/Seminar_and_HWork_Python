"""
Реализуйте алгоритм перемешивания списка.
"""
import random
n = int(input('n: '))
list_a = list(range(-n, n + 1))


def random_list(list_a, n):
   k = []
   i = 0
   while i < len(list_a):
      c = random.randint(0, n * 2)
      if c in k:
         continue
      else:
         k.append(c)
         i += 1
   random_list_a = list_a.copy()
   m = 0
   for j in k:
      random_list_a[m] = list_a[j]
      m += 1
   return random_list_a

print(f'{list_a} -> {random_list(list_a, n)}')

