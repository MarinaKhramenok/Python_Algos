"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа

Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6)  и максимальным (88) элементами: 234
"""
import random
from memory_profiler import profile


@profile
def fync():
    a = [random.randint(1, 10) for i in range(10)]
    print(f'Массив: {a}')
    min_index = 0
    max_index = 0
    step = 1
    common_sum = 0

    for i in a:
        if a[min_index] > i:
            min_index = a.index(i)
        elif a[max_index] < i:
            max_index = a.index(i)

    if max_index - min_index < 0:
        step = -1

    for i in a[min_index + step:max_index:step]:
        common_sum += i

    print(
        f"Сумма элементов между минимальным ({a[min_index]})",
        f" и максимальным ({a[max_index]}) элементами: {common_sum}"
    )


fync()
