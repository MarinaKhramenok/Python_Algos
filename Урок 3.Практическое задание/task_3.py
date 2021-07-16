"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

Пример:
В данном массиве чисел максимальное число   88 стоит на
0 позиции, а минимальное число  -49 стоит на    6 позиции
Заменяем их
[88, 26, 41, 75, 23, 52, -49, 60, 69, -18]
В данном массиве чисел максимальное число   88 стоит на
6 позиции, а минимальное число  -49 стоит на    0 позиции
[-49, 26, 41, 75, 23, 52, 88, 60, 69, -18]
"""
import random
from memory_profiler import profile


@profile
def fync():
    a = [random.randint(-20, 20) for i in range(10)]
    print(f'Массив №1: {a}')
    max_num = a[0]
    min_num = a[0]
    for i in a:
        if i > max_num:
            max_num = i
        elif i < min_num:
            min_num = i
    min_ind = a.index(min_num)
    max_ind = a.index(max_num)
    a[min_ind], a[max_ind] = a[max_ind], a[min_ind]
    print(f'Максимальное число: {max_num}, минимальное число: {min_num}\n'
          f'Меняем числа местами')
    print(f'Массив №2: {a}')


fync()
