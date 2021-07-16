"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""
try:
    A = int(input('a = '))
    B = int(input('b = '))
    C = int(input('c = '))

    if A == B == C:
        print('Равносторонний треугольник')

    elif A != B and A != C and B != C:
        print('Разносторонний треугольник')

    elif A + B <= C or A + C <= B or B + C <= A:
        print('Треугольник не существует')

    else:
        print('Равнобедренный треугольник')

except ValueError:
    print('Введите число')
