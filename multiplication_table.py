def multiplication_table():
    """
    Программа выводит фрагмент таблицы умножения для всех чисел отрезка [a;b] на все числа отрезка [c;d].
    """
    a=int(input('Введите число а: '))
    b=int(input('Введите число b: '))
    c=int(input('Введите число c: '))
    d=int(input('Введите число d: '))
    for j in range(c, d+1):
        print ('\t', end=str(j))
    print('',end='\n')
    for i in range(a,b+1):
        print (i, end='\t')
        for j in range(c,d+1):
            print (i*j, end='\t')
        print('',end='\n')

multiplication_table()