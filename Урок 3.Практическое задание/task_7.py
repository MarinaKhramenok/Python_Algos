"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Пример:
Исходный массив: [28, -86, 44, -37, -7, -52, -19, -3, -15, -73]
Наименьший элемент: -86, встречается в этом массиве 1 раз
Второй наименьший элемент: -73
"""
import random
import timeit
import cProfile


def min_1(A):
    MIN_1 = A[0]
    MIN_2 = A[0]
    for i in A:
        if i < MIN_1:
            MIN_2 = MIN_1
            MIN_1 = i
        elif i < MIN_2:
            MIN_2 = i
    return f'Наименьший элемент: {MIN_1}, Второй наименьший элемент: {MIN_2}'

def min_2(A):
    B = sorted(A)[:2]
    return f'Наименьший элемент: {B[0]}, Второй наименьший элемент: {B[1]}'

A = [random.randint(1, 5) for i in range(5)]
print(f'Массив: {A}')
print(min_1(A))
print(min_2(A))