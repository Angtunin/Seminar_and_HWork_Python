"""
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
"""
from random import randint

def input_progress(gamer):
    candys = int(input(f'{gamer}, введите число конфет от 1 до 28: '))
    while candys < 1 or candys > 28:
        candys = int(input(f'{gamer}, введите число конфет от 1 до 28: '))
    return candys

def output_progres(gamer, candys, candys_gamer, all_candys):
    print(f'Ход: {gamer}, взял: {candys}, стало: {candys_gamer}. Осталось {all_candys} конфет')

gamer1 = input('Введите имя первого игрока: ')
gamer2 = input('Введите имя второго игрока: ')
all_candys = int(input('Введите кол-во конфет: '))
turn = randint(0, 2)
if turn:
    print(f'Ход {gamer1}')
else:
    print(f'Ход {gamer2}')

candys_gamer1 = 0
candys_gamer2 = 0

while all_candys > 28:
    if turn:
        candys = input_progress(gamer1)
        candys_gamer1 += candys
        all_candys -= candys
        turn = False
        output_progres(gamer1, candys, candys_gamer1, all_candys)
    else:
        candys = input_progress(gamer2)
        candys_gamer2 += candys
        all_candys -= candys
        turn = True
        output_progres(gamer2, candys, candys_gamer2, all_candys)

if turn:
    print(f'Выйграл {gamer1}')
else:
    print(f'Выйграл {gamer2}')

