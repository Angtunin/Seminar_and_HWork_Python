"""
Вычислить число c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
при d = 0.0000000001 π = 3.1415926535
"""

def input_num():
    n = input('Задайте точность от 1 до 10: ')
    while not n.isdigit():
        n = input('Вы вели не число, введите число от 1 до 10: ')
    return int(n)


def pi_calculation(d):
    a = 2
    b = 0
    pi = 3
    i = 0
    while abs(b - pi) > 10 **(-d-3):
        b = pi
        pi += (4 / (a * (a + 1) * (a + 2))) - (4 / ((a + 2) * (a + 3) * (a + 4)))
        a += 4
        i += 1
    pi = pi * (10 ** d)
    pi = pi // 1
    return pi * (10 ** (-d))

d = input_num()
print(pi_calculation(d))
