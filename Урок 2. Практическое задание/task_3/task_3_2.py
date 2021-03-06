"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
def recur(number, inverted_num=0):
    if number == 0:
        return inverted_num
    else:
        inverted_num = inverted_num * 10 + number % 10
        number = number // 10
        return recur(number, inverted_num)


try:
    NUMBER = int(input('Введите число: '))
    print(f'Перевернутое число: {recur(NUMBER)}')
except ValueError:
    print('Ошибка! Введите число')