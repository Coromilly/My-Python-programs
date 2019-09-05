def least_common():
    """
    Программа вычисляет наименьшее общее кратное (НОК) чисел a и b.
    НОК - наименьшее число, на которое делятся a и b без остатка.
    """


    a = int(input('Введите число а: '))
    b = int(input('Введите число b: '))
    d = 0
    while d <= a * b:
        if d % a == 0 and d % b == 0 and d != 0:
            print(d)
            d = a * b + 1
        d += 1

least_common()
