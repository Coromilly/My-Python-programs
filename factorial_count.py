print('Введите число n: ')
n = int(input())
def factorial(n):
    """
    Вычисление факториала числа n.
    """
    assert n>=0, 'Факториал не считаю'
    if n == 0:
        return 1
    return factorial(n - 1) * n

print('Факториал числа {0} равен {1}'.format(n, factorial(n)))