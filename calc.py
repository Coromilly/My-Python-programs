def calculator():
    """
    Арифметический калькулятор. Позволяет производить простейшие арифметические действия с целыми числами, как положительными, так и отрицательными, используя только знаки '+' и '-'.
    """
	
    print('Введите целое натуральное число а: ')
    a = int(input())
    print('Введите целое натуральное число b: ')
    b = int(input())
    print('Введите арифметическую операцию ("+", "-", "*", "/") для чисел: ')
    operation = str(input())
    def addition():
        print('Сумма чисел {0} и {1} = {2}'.format(a, b, a + b))
    def subtraction():
        i, j = a, b
        if j < 0:
            while j < 0:
                i += 1
                j = j + 1
        else:
            while j > 0:
                i -= 1
                j = j - 1
        print('Разность чисел {0} и {1} = {2}'.format(a, b, i))
    def multiplication():
        """
        Умножение числа 'a' на число 'b' не используя знак '*'.
        """
        mult = 0
        i, j = a, b
        if j < 0:
            while j < 0:
                mult -= i
                j = j + 1
        else:
            while j > 0:
                mult += i
                j = j - 1
        print('Произведение чисел {0} и {1} = {2}'.format(a, b, mult))
    def division():
        div = 0
        rest = 0
        i, j = a, b
        if b == 0:
            raise ZeroDivisionError
        if (i > 0 and j > 0) or (i < 0 and j < 0):
            while abs (i) - abs (j) >= 0:
                div += 1
                i -= j
            else:
                rest = i
        elif i > 0 and j < 0:
            while i + j >= 0:
                div -= 1
                i += j
            else:
                rest = i
        else:
            while i + j <= 0:
                div -= 1
                i += j
            else:
                rest = i
        print('{0} разделить на {1} = {2}, остаток {3}'.format(a, b, div, rest))
    if operation == '+':
        addition()
    elif operation == '-':
        subtraction()
    elif operation == '*':
        multiplication()
    else:
        division()

