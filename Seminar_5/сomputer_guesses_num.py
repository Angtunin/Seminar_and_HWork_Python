"""
1. В этой игре человек загадывает число, а компьютер пытается его угадать.
В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги.
Компьютер начинает его отгадывать предлагая игроку варианты чисел.
Если компьютер угадал число, игрок выбирает “победа”.
Если компьютер назвал число меньше загаданного,
игрок должен выбрать “загаданное число больше”.
Если компьютер назвал число больше,
игрок должен выбрать “загаданное число меньше”.
Игра продолжается до тех пор пока компьютер не отгадает число.
"""
number = int(input('Загадайте (введите) число от 1 до 100: '))
numbers = range(1, 101)
#print(list(numbers))
random_number = int(100 / 2)
random_range = 50

while random_number != number:
    random_range = int(random_range / 2)
    if number > random_number:
        print('Число меньше загаданного')
        random_number = random_number + random_range
        print(random_range)
        if random_range <= 2:
            while random_number != number:
                random_number += 1

        #print(random_number)
    elif number < random_number:
        print('Число больше загаданного')
        random_number = random_number - random_range
        print(random_range)
        if random_range <= 2:
            while random_number != number:
                random_number -= 1

        #print(random_number)
else:
    print('Число угадано ', random_number)

