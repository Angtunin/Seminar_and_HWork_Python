"""
Задача 28
Найдите корни квадратного уравнения Ax² + Bx + C = 0, где A ≠ 0 двумя способами:
1) с помощью математических формул нахождения корней квадратного уравнения
2) с помощью дополнительных библиотек Python

test_data = [
[[1, -3, 2], [1.0, 2.0]],
[[1, 2, 1], [-1, -1]],
[[2, 2, 1], []]
]
D = b**2 - 4*a*c
if D < 0: -> нет корней
for nums, expected in test_data:
assert quadratic_equation(*nums) == expected
"""
nums = input("Введите A, B, C через пробел: ")
nums = nums.split()

def calcs(nums):
    a = int(nums[0])
    b = int(nums[1])
    c = int(nums[2])
    discr = b ** 2 - 4 * a * c
    if discr < 0:
        return 'no roots'
    else:
        return (-b - discr ** 0.5) / (2 * a), (-b + discr ** 0.5) / (2 * a)

print(calcs(nums))
