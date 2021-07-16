"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
try:
    NUMBER_1 = int(input('Введите первое число: '))
    NUMBER_2 = int(input('Введите второе число: '))
    NUMBER_3 = int(input('Введите третье число: '))

    if NUMBER_1 == NUMBER_2 == NUMBER_3:
        print("Введены одинаковые числа")

    if NUMBER_2 < NUMBER_1 < NUMBER_3 or NUMBER_3 < NUMBER_1 < NUMBER_2:
        print(f"Среднее число: {NUMBER_1}")
    elif NUMBER_1 < NUMBER_2 < NUMBER_3 or NUMBER_3 < NUMBER_2 < NUMBER_1:
        print(f"Среднее число: {NUMBER_2}")
    else:
        print(f"Среднее число: {NUMBER_3}")

except ValueError:
    print('Введите число')