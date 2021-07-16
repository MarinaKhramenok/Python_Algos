"""
Задание_1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

Подсказка: используйте вложенный цикл

Пример:
В диапазоне 2-99: 49 чисел кратны 2
В диапазоне 2-99: 33 чисел кратны 3
В диапазоне 2-99: 24 чисел кратны 4
В диапазоне 2-99: 19 чисел кратны 5
В диапазоне 2-99: 16 чисел кратны 6
В диапазоне 2-99: 14 чисел кратны 7
В диапазоне 2-99: 12 чисел кратны 8
В диапазоне 2-99: 11 чисел кратны 9
"""
from memory_profiler import profile


@profile
def task_1():
    for i in range(2,10):
        result = [j for j in range(2, 100) if j % i == 0]
        print(f'В диапазоне 2-99: {len(result)} чисел кратны {i}')


@profile
def task_2():
    lst_1 = list(range(2, 100))
    lst_2 = list(range(2, 10))
    for el in lst_2:
        numb = 0
        for i in lst_1:
            if i % el == 0:
                numb += 1
        print(f"В диапазоне 2-99: {numb} чисел кратны {el}")


task_1()
task_2()