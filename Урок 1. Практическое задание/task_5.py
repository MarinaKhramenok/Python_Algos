"""
Задание 5.
Пользователь вводит две буквы. Определить,
на каких местах алфавита они стоят, и сколько между ними находится букв.

Подсказка:
Вводим маленькие латинские буквы.
Обратите внимание, что ввести можно по алфавиту, например, a,z
а можно наоборот - z,a
В обоих случаях программа должна вывести корректный результат.
В обоих случаях он 24, но никак не -24
"""
A = ord(input('Введите первую букву: '))
B = ord(input('Введите вторую букву: '))

if A == B:
    print('Введены одинаковые буквы ')

A = A - ord('a') + 1
B = B - ord('a') + 1

print(f'Позиции: {A} и {B}')
print(f'Между буквами символов: {abs(A - B) - 1}')
