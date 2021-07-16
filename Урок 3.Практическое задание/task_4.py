"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
import random
from memory_profiler import profile


@profile
def fync():
    a = [random.randint(1, 5) for i in range(10000)]
    print(a)
    max_count = 0
    for i in a:
        if max_count < a.count(i):
            max_count = a.count(i)
            num = i
    print(f'Число {num} встречается {max_count} раз')


fync()